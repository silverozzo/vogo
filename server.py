"""
запускаемый процесс веб-сервера
"""

from service.logger import Logger
from service.tabl_maker import TablMaker
from service.library import Library

import beaker.middleware
from bottle import run, app, hook, route, post, static_file, template, \
	request, response


@route('/<filename:re:.*\.css>')
def stylesheets(filename):
	"""
	выдача статики типа css
	"""
	return static_file(filename, root='css')


@route('/output/<filename:re:.*\.png>')
def outputimage(filename):
	"""
	здесь выдается картинко-результат сборки табулатуры
	"""
	return static_file(filename, root='output')


@hook('before_request')
def setup_request():
	"""
	здесь устанавливается сессия перед обработкой запроса
	"""
	request.session = request.environ['beaker.session']


@post('/')
def tablprocess():
	"""
	здесь собсно обрабатывается запрос на генерацию табулатуры из кода
	"""
	Logger.clear()
	session_id = request.get_cookie('beaker.session.id')
	if session_id is None:
		Logger.log('no session from your side')
		return template('index', output=session_id, log_records=Logger.get(), 
			name='', typer='', code='')
	
	name  = request.forms.get('name')  or ''
	typer = request.forms.get('typer') or ''
	code  = request.forms.get('code')  or ''
	share = request.forms.get('share') or ''
	
	request.session['name']  = name
	request.session['typer'] = typer
	request.session['code']  = code
	request.session['share'] = share
	lines = map(lambda x: x.strip(), code.split("\n"))
	TablMaker.process(lines, name, 'output/' + session_id + '.png')
	if share == 'on':
		lib = Library()
		lib.add_tabl(typer, name, code, session_id)
	
	return template('index', output=session_id, log_records=Logger.get(), 
		name=name, typer=typer, code=code, share=share)


@route('/helping_images/<filename>')
def helper_image(filename):
	"""
	здесь выдаются картинки к странице помощи
	"""
	return static_file(filename, root='views/helping_images')


@route('/help')
def helper():
	"""
	здесь выдается страница помощи
	"""
	return template('help')


@route('/library')
def library():
	"""
	здесь выдается библиотека расшаренных табулатур
	"""
	return template('library')


@route('/')
def index():
	"""
	здесь выдается основная страница с формой заполнения кода для табулатуры
	"""
	Logger.clear()
	session_id = request.get_cookie('beaker.session.id')
	name  = request.session['name']  if 'name'  in request.session else ''
	typer = request.session['typer'] if 'typer' in request.session else ''
	code  = request.session['code']  if 'code'  in request.session else ''
	share = request.session['share'] if 'share' in request.session else ''
	return template('index', output=session_id, log_records=Logger.get(), 
		name=name, typer=typer, code=code, share=share)


session_opts = {
		'session.type'    : 'file',
		'session_data_dir': './session/',
		'session.auto'    : True,
	}
app = beaker.middleware.SessionMiddleware(app(), session_opts)
run(app=app, host='localhost', port=8080, reloader=True)
