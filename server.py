"""
запускаемый процесс веб-сервера
"""

from service.logger import Logger
from service.tabl_maker import TablMaker

import beaker.middleware
from bottle import run, app, hook, route, post, static_file, template, \
	request, response


@route('/<filename:re:.*\.css>')
def stylesheets(filename):
	"""
	выдача статики типа css
	"""
	return static_file(filename, root='css')

@route('/<filename:re:.*\.png>')
def outputimage(filename):
	"""
	здесь выдается результат сборки табулатуры
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
	Logger.clear()
	session_id = request.get_cookie('beaker.session.id')
	if session_id is None:
		Logger.log('no session from your side')
		return template('index', output=session_id, log_records=Logger.get(), 
			name='', typer='', code='')
	
	name  = request.forms.get('name')  or ''
	typer = request.forms.get('typer') or ''
	code  = request.forms.get('code')  or ''
	
	request.session['name']  = name
	request.session['typer'] = typer
	request.session['code']  = code
	lines = map(lambda x: x.strip(), code.split("\n"))
	TablMaker.process(lines, name, 'output/' + session_id + '.png')
	return template('index', output=session_id, log_records=Logger.get(), 
		name=name, typer=typer, code=code)

@route('/')
def index():
	Logger.clear()
	session_id = request.get_cookie('beaker.session.id')
	name  = request.session['name']  if 'name'  in request.session else ''
	typer = request.session['typer'] if 'typer' in request.session else ''
	code  = request.session['code']  if 'code'  in request.session else ''
	return template('index', output=session_id, log_records=Logger.get(), 
		name=name, typer=typer, code=code)


session_opts = {
		'session.type'    : 'file',
		'session_data_dir': './session/',
		'session.auto'    : True,
	}
app = beaker.middleware.SessionMiddleware(app(), session_opts)
run(app=app, host='localhost', port=8080, reloader=True)
