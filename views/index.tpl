<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link href="favicon.ico" rel="shortcut icon">
  <link rel="stylesheet" href="style.css">
  <title>vogo type</title>  
  <!--[if lt IE 9]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
</head>

<body>
  <div class="container">

    <header class="header clearfix">
      <div class="logo">.vogo</div>

      <nav class="menu_main">
        <ul>
          <li class="active">type</li>
          <li><a href="/help">help</a></li>
          <li><a href="#">library</a></li>
        </ul>
      </nav>
    </header>


    <div class="info">
      
      <article class="article clearfix">
        
        <div class="clearfix"></div>

        <div class="col_66">
          <form action="#" method="post" class="form">
            <h2>tabl form</h2>

            <p class="col_50">
              <label for="name">name:</label><br/>
              <input type="text" name="name" id="name" value="{{name}}" />
            </p>
            <p class="col_50">
              <label for="typer">typer:</label><br/>
              <input type="text" name="typer" id="typer" value="{{typer}}" />
            </p>
            <div class="clearfix"></div>
            
            <p>
              <label for="textarea">code:</label><br/>
              <textarea cols="60" rows="10" name="code" id="textarea" wrap="off">{{code}}</textarea>
            </p>
            
            <p class="col_50">
                <input type="submit" name="tabl" class="button" value="submit"/>
            </p>
            
            <p class="col_50">
              <label for="checkbox"><input type="checkbox" name="share" id="checkbox" />&nbsp;share</label><br/>
            </p>
            
          </form>
        </div>
        
        <div class="col_33">
          <h2>fast help</h2>
          
          <h3>usage</h3>
          <ul>
             <li>enter name of the tabl</li>
             <li>enter code</li>
             <li>press "submit"</li>
          </ul>
          
          <h3>possibilities</h3>
          <ul>
             <li>"share" &mdash; post to the ibrary</li>
             <li>"typer" &mdash; enter your name</li>
             <li>there is detail help</li>
             <li>there is console output for debug</li>
          </ul>
        </div>        

        <div class="clearfix"></div>
      </article>
      
      <br/><br/>
      
      <article class="article clearfix">
        <div class="col_66">
%from random import randint
%rando=randint(0, 1000)
          <img src="/output/{{output}}.png?{{rando}}"/>
        </div>
        
        <div class="col_33">
          <p class="message">
%for rec in log_records:
            <code>{{rec}}</code><br/>
%end
          </p>
        </div>
      </article>
      
    </div>
    
    <footer class="footer clearfix">
      <div class="copyright"><a href="http://www.python.org">python</a></div>
      <div class="copyright"><a href="http://www.imagemagick.org/">ImageMagick</a></div>
      <div class="copyright"><a href="http://pypi.python.org/pypi/Beaker">Beaker</a></div>
      <div class="copyright"><a href="http://bottlepy.org">Bottle</a></div>
      <div class="copyright"><a href="http://wand-py.org">Wand</a></div>
      <div class="copyright"><a href="http://simpliste.ru/">Simpliste</a></div>
    </footer>

  </div>
</body>
</html>