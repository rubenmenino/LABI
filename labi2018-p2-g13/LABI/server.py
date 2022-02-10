#!python
#encoding:utf8
import os
import wave
import cherrypy
from database import *
cherrypy.config.update({'server.socket_port': 10013,})

# The absolute path to this file's base directory:
baseDir = os.path.dirname(os.path.abspath(__file__))

# Dict with the this app's configuration:
config = {
	"/": { "tools.staticdir.root": baseDir },
	"/img": { "tools.staticdir.on" : True,
			  "tools.staticdir.dir" : "img" },
	"/sounds": {	"tools.staticdir.on" : True,
					"tools.staticdir.dir" : "sounds" },
	"/javascript":   { "tools.staticdir.on": True,
					   "tools.staticdir.dir": "javascript" },
	"/css":  { "tools.staticdir.on": True,
			 "tools.staticdir.dir": "css" },
	"/pages": { "tools.staticdir.on": True,
			 "tools.staticdir.dir": "pages" },
	"/samples": { "tools.staticdir.on": True,
			 "tools.staticdir.dir": "samples" },
	"/audio": { "tools.staticdir.on": True,
			 "tools.staticdir.dir": "audio" },
}

class Root:
	# This class atribute contains the HTML text of the main page:
	indexHTML = """<!doctype html>
<html lang="pt">
	
	<head>
		<title>Trabalho</title>
		<!--Icon-->
		<link rel="icon" href="../img/nota.ico">
		
		<!-- Required meta tags -->
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		
		<!-- Bootstrap CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
		<link rel="stylesheet" href="../css/estilo.css">
		<link rel="stylesheet" href="../css/tabela.css">
		<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">

		
		<!-- Optional JavaScript -->
		<!-- jQuery first, then Popper.js, then Bootstrap JS -->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
		<script type="text/javascript" src="../javascript/navbar.js"></script>
		<script type="text/javascript" src="/javascript/js_functions.js"></script>
		
	</head>

<!--Menu Principal-->
	<body onload="navbar()">

		<section class="cover-1 text-center">
			<nav class="navbar navbar fixed-top navbar-expand-lg navbar-dark navbar-custom">
				<div class="container">
					<img src="../img/notas.png" width="30" height="30" class="d-inline-block align-top"/>
					<a class="navbar-brand" href="/index"> &nbsp;  Música</a>
					<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
						<span class="navbar-toggler-icon"></span>
					</button>
					<div class="collapse navbar-collapse pull-xs-right justify-content-end" id="navbarSupportedContent" >
						<ul class="navbar-nav mt-2 mt-md-0">
							<li class="nav-item active">
								<a class="nav-link" href="/pages/lista.html">Listar Músicas</a>
							</li>
							<li class="nav-item dropdown">
								<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
								  Excerto de sons
								</a>
								<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
								  <a class="dropdown-item" href="#">1</a>
								  <a class="dropdown-item" href="#">2</a>
								  <a class="dropdown-item" href="#">3</a>
								   <a class="dropdown-item" href="#">4</a>
								</div>
							</li>
							</li>
							<li class="nav-item">
								<a class="scroll nav-link" href="/pages/tabela.html">Composiçao de músicas</a>
							</li>
							<li class="nav-item">
								<a class="nav-link" href="/pages/sobrenos.html">Sobre Nós</a>
							</li>
						</ul>
					</div>
				</div>
			</nav>
		</section>
<!--Fim Menu-->
<br>
<br>
<br>
<!--1ªSection-->
		<section class="cover-1 text-center">
			<div class="cover-container pb-5">
				<div class="cover-inner container">
					<h1 class="ti"><strong>Make your own song</strong></h1>
					<h2 class="lead">Bem vindo ao nosso site.</h2>
					
				</div>
			</div>
		</section>

	</body>
	</html>
"""

	@cherrypy.expose
	def like(self, id):
		upvote(str(id))
		return "Thank you for your vote!"
			
	
	@cherrypy.expose
	def dislike(self, id):
		downvote(str(id))
		return "Thank you for your vote!"
		
	@cherrypy.expose
	def index(self):
		return Root.indexHTML

	#tabela de musicas em formato json
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listMusics(self):
		return get_musics() 
		
	@cherrypy.expose
	def upload(self, myFile):
		fo = open(os.getcwd()+ "/sounds/" + myFile.filename, "wb")
		while True:
			data = myFile.file.read(8192)
			if not data:
				break
			fo.write(data)
		fo.close()
		addSoundBlock(myFile.filename)
		raise cherrypy.HTTPRedirect("/pages/lista.html")
		
def addSoundBlock(file_name):
	with open(os.path.dirname(os.path.abspath(__file__))+"/pages/lista.html", "r") as in_file:
		buf = in_file.readlines()
		
	with open(os.path.dirname(os.path.abspath(__file__))+"/pages/lista.html", "w") as out_file:
		for line in buf:
			if line == """			<!--add-->\n""":
				line = """			<div>
				<h3>"""+file_name[:-4]+"""</h3>
                
                <button class="button_like" type="button" class="btn btn-default btn-sm pull-right" onclick="upVote("""+file_name[:-4]+""")">

                  <i class="fas fa-thumbs-up"></i>

                </button>

                <button class="button_dislike" type="button" class="btn btn-default btn-sm pull-right" onclick="downVote("""+file_name[:-4]+""")">

                  <i class="fas fa-thumbs-down"></i>

                </button>
                <audio class="reproduzir" controls>
					<source src="../sounds/"""+file_name+"""" type="audio/wav">
					Erro.
                </audio>
			</div> 
			
			<br>
			
			<!--add-->\n"""
			out_file.write(line)
			
	fname = os.getcwd()+"/sounds/"+file_name
	f = wave.open(fname,'r')
	frames = f.getnframes()
	rate = f.getframerate()
	duration = frames / float(rate)
	duration = round(duration)
	f.close()
	
	addMusic(file_name[:-4], duration)
	
	


cherrypy.quickstart(Root(), "/", config)

