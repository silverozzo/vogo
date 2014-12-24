<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link href="favicon.ico" rel="shortcut icon">
  <link rel="stylesheet" href="style.css">
  <title>vogo library</title>  
  <!--[if lt IE 9]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
</head>

<body>
  <div class="container">

    <header class="header clearfix">
      <div class="logo">.vogo</div>

      <nav class="menu_main">
        <ul>
          <li><a href="/">type</a></li>
          <li><a href="/help">help</a></li>
          <li class="active">library</li>
        </ul>
      </nav>
    </header>

    <div class="info">
      <article class="article clearfix">
      
        <div class="clearfix"></div>
        
        <div class="col_100">
          <table class="table">
            <tr>
              <th>typer</th>
              <th>name</th>
              <th>code</th>
              <th>tabl</th>
            </tr>
            
%for rec in tabls:
            <tr>
              <td class="top">{{rec['typer']}}</td>
              <td class="top">{{rec['name']}}</td>
              <td class="top">
                <a id="show_id_{{rec['id']}}" 
                    onclick="document.getElementById('spoiler_id_{{rec['id']}}').style.display=''; document.getElementById('show_id_{{rec['id']}}').style.display='none';" 
                    class="link">
                  [show]
                </a>
                <span id="spoiler_id_{{rec['id']}}" style="display: none">
                  <a onclick="document.getElementById('spoiler_id_{{rec['id']}}').style.display='none'; document.getElementById('show_id_{{rec['id']}}').style.display='';" 
                      class="link">
                    [hide]
                  </a><br/>
                  <code>{{rec['code']}}</code>
                </span>
              </td>
              <td class="top">
                <a id="show_id_{{rec['id']}}_img" 
                    onclick="document.getElementById('spoiler_id_{{rec['id']}}_img').style.display=''; document.getElementById('show_id_{{rec['id']}}_img').style.display='none';" 
                    class="link">
                  [show]
                </a>
                <span id="spoiler_id_{{rec['id']}}_img" style="display: none">
                  <a onclick="document.getElementById('spoiler_id_{{rec['id']}}_img').style.display='none'; document.getElementById('show_id_{{rec['id']}}_img').style.display='';" 
                      class="link">
                    [hide]
                  </a><br/>
                  <img src="/library/{{rec['name']}}.png" />
                </span>
              </td>
            </tr>
%end
          </table>
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