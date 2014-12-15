<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link href="favicon.ico" rel="shortcut icon">
  <link rel="stylesheet" href="style.css">
  <title></title>  
  <!--[if lt IE 9]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
</head>

<body>
  <div class="container">

    <header class="header clearfix">
      <div class="logo">.vogo</div>

      <nav class="menu_main">
        <ul>
          <li class="active"><a href="#">Type</a></li>
          <li><a href="#">Help</a></li>
          <li><a href="#">Library</a></li>
        </ul>
      </nav>
    </header>


    <div class="info">
      
      <article class="article clearfix">
        
        <div class="clearfix"></div>

        <div class="col_66">
          <form action="#" method="post" class="form">
            <h2>Tabl form</h2>

            <p class="col_50">
              <label for="name">Name:</label><br/>
              <input type="text" name="name" id="name" value="{{name}}" />
            </p>
            <p class="col_50">
              <label for="typer">Typer:</label><br/>
              <input type="text" name="typer" id="typer" value="{{typer}}" />
            </p>
            <div class="clearfix"></div>
            
            <p>
              <label for="textarea">Code:</label><br/>
              <textarea cols="60" rows="10" name="code" id="textarea" wrap="off">{{code}}</textarea>
            </p>
            
            <p class="col_50">
                <input type="submit" name="tabl" class="button"/>
            </p>
            
            <p class="col_50">
              <label for="checkbox"><input type="checkbox" name="share" id="checkbox" />&nbsp;Share</label><br/>
            </p>
            
          </form>
        </div>
        
        <div class="col_33">
          <h2>Fast help</h2>
          
          <h3>How to use</h3>
          <ul>
             <li>type name of your table</li>
             <li>type your name as typesetter</li>
             <li>enter code content of your tabl</li>
             <li>you can set "Share"</li>
             <li>and press "Submit"</li>
          </ul>
        </div>        

        <div class="clearfix"></div>
      </article>
      
      <br/><br/>
      
      <article class="article clearfix">
        <div class="col_66">
%from random import randint
%rando=randint(0, 1000)
          <img src="{{output}}.png?{{rando}}"/>
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
      <div class="copyright">python</div>
      <div class="copyright">ImageMagick</div>
      <div class="copyright">Bottle</div>
      <div class="copyright">Wand</div>
      <div class="copyright">Simpliste</div>
    </footer>

  </div>
</body>
</html>