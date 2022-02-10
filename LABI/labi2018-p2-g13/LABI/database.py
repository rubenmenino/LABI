import sqlite3 as sql
import sys
import os
import wave
import time

def addMusic(ID, duration):
	insert = "INSERT INTO musicas (name, duration, date, uses, upvotes, downvotes) VALUES("
	executar = insert+str(ID)+","+str(duration)+","+time.strftime("%x")+","+"0,0,0);"
	
	database.execute(executar)
	database.commit()
	

def upvote(ID):
	executar ="SELECT upvotes FROM musicas WHERE name = " + str(ID)
	
	total = database.execute(executar)
	total = total.fetchone()
	total = total[0] +1
	
	executar ="UPDATE musicas SET upvotes = " + str(total) + " WHERE name = " + str(ID)
	
	database.execute(executar)
	database.commit()
	

def downvote(ID):
	executar ="SELECT downvotes FROM musicas WHERE name = " + str(ID)
	
	total = database.execute(executar)
	total = total.fetchone()
	total = total[0] + 1
	
	executar = "UPDATE musicas SET downvotes = " + str(total) + " WHERE name = " + str(ID)
	
	database.execute(executar)
	database.commit()
	
#mostrar tabela music
def get_musics():
	executar = "SELECT * FROM musicas"
	total = databaseb.execute(executar)
	rows = total.fetchall()
	x = []
	for row in rows:
		info = {"name":row[0],"id":row[1],"lenght":row[2],"uses":row[3],"upvotes":row[4],"downvotes":row[5]}
		x.append(info)
	return x


#Para a primeira abertura do servidor, onde ainda nao existe o ficheiro musicas.db criado
if not os.path.isfile("musicas.db"):
	if not os.path.isfile("create.txt"):
		print ("Ficheiro create.txt nao encontrado.")
		exit(1)
		
	database = sql.connect("musicas.db")
	
	readfile = open("create.txt", 'r')
	commands = ""
	for linha in readfile:
		commands += linha
		
	database.execute(commands)
	
	insert = "INSERT INTO musicas (name, duration, date, uses, upvotes, downvotes) VALUES("
		
	file_list = os.listdir(os.getcwd()+"/sounds")
	for song in file_list:
		name = song[:-4]
		
		fname = os.getcwd()+"/sounds/"+name+".wav"
		f = wave.open(fname,'r')
		frames = f.getnframes()
		rate = f.getframerate()
		duration = frames / float(rate)
		f.close()
		
		duration = round(duration)
		
		commands = insert+name+","+str(duration)+","+time.strftime("%x")+","+"0,0,0);"
		
		database.execute(commands)	
	
	database.commit()
	readfile.close()
	database.close()


database = sql.connect("musicas.db", check_same_thread=False)
