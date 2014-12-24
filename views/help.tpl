<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link href="favicon.ico" rel="shortcut icon">
  <link rel="stylesheet" href="style.css">
  <title>vogo help</title>  
  <!--[if lt IE 9]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
</head>

<body>
  <div class="container">

    <header class="header clearfix">
      <div class="logo">.vogo</div>

      <nav class="menu_main">
        <ul>
          <li><a href="/">type</a></li>
          <li class="active">help</li>
          <li><a href="/library">library</a></li>
        </ul>
      </nav>
    </header>
    
    <div class="info">
      <article class="article clearfix">
      
        <div class="clearfix"></div>
        
        <div class="col_25">
          <h2>basics</h2>
          <li>use space for delimetering symbols</li>
          <li>each line is one stave</li>
          <li>use "/" for line concatination</li>
        </div>
      
        <div class="col_25">
          <h2>notes</h2>
          <img src="helping_images/simple_line.png"/><br/>
          <code>c d e f g a b</code><br/><br/>
          <img src="helping_images/simple_line_plus.png"/><br/>
          <code>c+ d+ e+ f+ g+ a+ b+</code><br/><br/>
        </div>
        
        <div class="col_25">
          <h2>durations</h2>
          <img src="helping_images/durations.png"/><br/>
          <code>f f. f2 f4 f8 f16 f32</code><br/><br/>
        </div>
        
        <div class="col_25">
          <h2>delimeters</h2>
          <img src="helping_images/delimeters_01.png"/><br/>
          <code>e f | e f |w e f ||</code><br/><br/>
          <img src="helping_images/delimeters_02.png"/><br/>
          <code>||: a b :||</code><br/><br/>
        </div>
        
        <div class="col_25">
          <h2>clefs</h2>
          <img src="helping_images/clefs.png"/><br/>
          <code>tr tr8 tr8- bc</code><br/><br/>
        </div>
        
        <div class="col_25">
          <h2>spaces</h2>
          <img src="helping_images/spaces.png"/><br/>
          <code>f g _ f g __ f g ___ f g</code><br/><br/>
        </div>
        
        <div class="col_25">
          <h2>tacts</h2>
          <img src="helping_images/tacts.png"/><br/>
          <code>t12 t34 t56 t78 t09 tc</code><br/><br/>
        </div>
        
        <div class="col_25">
          <h2>pauses</h2>
          <img src="helping_images/pauses.png"/><br/>
          <code>p04 p1 p2 p4 p8 p16</code><br/><br/>
        </div>
        
        <div class="col_25">
          <h2>knits</h2>
          <img src="helping_images/knits_simple.png"/><br/>
          <code>[ c8 c8 ] /<br/>
            [ [ d16 d16 ] ] /<br/>
            [ [ [ e32 e32 ] ] ]
          </code><br/><br/>
          <img src="helping_images/knits_combos.png"/><br/>
          <code>[ c8 [ d16 e16 ] ] /<br/>
            [ [ d16 ] c8 c8 ]
          </code><br/><br/>
          <img src="helping_images/knits_direction.png"/><br/>
          <code>[ d8+ d8+ ] /<br/>
            [!up d8+ d8+ ] /<br/>
            [ a8 a8 ] /<br/>
            [!down a8 a8 ]
          </code><br/><br/>
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