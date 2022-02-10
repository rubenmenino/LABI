import socket
import random
import json
import hashlib
from Crypto.Cipher import AES
import base64
import csv

def clothes(t, w, h):

	# t -> TEMPERATURA
	# w -> VENTO
	# h -> HUMIDADE
	
	if h > 75:
		print("Leve chapéu de chuva para o exterior")
	
	if t >= 20:
		print("Sinta-se à vontade para usar t-shirt e/ou calções. ")
		if w > 20:
			print("Vento forte! Leve um casaco.")
	elif t < 20 and t > 13:
		print("Aconselhável a utilização de duas camadas de roupa. ")
		if w > 20:
			print("Vento forte! Leve um casaco.")
	else:
		print("Aconselhável o uso de pelo menos 3 camadas de roupa. ")
		if w > 20:
			print("Vento forte! Leve um casaco. ")
	
	print(" ")
	
def connect():
	
	# CRIAÇÃO DO SOCKET
	tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_s.bind( ("0.0.0.0", 0))
	tcp_s.connect( ("xcoa.av.it.pt", 8080))
	
	return tcp_s
	
def get_x_token(server):
    
	a = (int)(random.random()*10)
	p = 6029856719847159731460134756013
	g = 29384717641
    
    # ENVIAR AO SERVIDOR O COMANDO 'CONNECT'
	server.send(("CONNECT " + str(pow(g,a,p)) + "," +str(p) + "," + str(g) +"\n").encode("utf-8"))
	
	data = server.recv(4098)
	data = data.decode("utf-8")
	data = json.loads(data)
	
	# RECEBER O TOKEN (VEM NO FORMATO JSON)
	token = data["TOKEN"]
	
	# CÁLCULO DE 'X', USANDO 'B' DO SERVIDOR
	b = data["B"]
	X = pow(b,a,p)
	X = str(X).encode("utf-8")
	MD5 = hashlib.md5()
	MD5.update(X)
	X = MD5.hexdigest()
	X = X[0:16]
	
	return X, token

def encode(data, key):
	
	cipher = AES.new(key)
	
	# CORRIGIR O TAMANHO DO ULTIMO BLOCO
	lastBlockLen = len(data) % cipher.block_size
	if (lastBlockLen != cipher.block_size):
		p = cipher.block_size - len(data)
		data = data + chr(p)*p
	# ENCRIPTAR
	data = cipher.encrypt(data)
	# CODIFICAR
	data = base64.b64encode(data)+"\n".encode("utf-8")
	
	return data
	
def get_data(server, key):
	
	cipher = AES.new(key)
	
	data = server.recv(4098)
	
	# DESCODIFICAR
	data = base64.b64decode(data)
	# DESENCRIPTAR
	data = cipher.decrypt(data)
	
	p = data[len(data)-1]
	data = data[0:len(data)-p]
	
	return data

def main():

	# CONECTAR AO SERVIDOR
	server = connect()
	
	print("CONNECTED!")
	
	# OBTER O TOKEN E 'X' ENVIADOS PELO SERVIDOR
	X, token = get_x_token(server)
	
	data = ("READ " + str(token))
	data = encode(data, X)
	
	# ENVIAR O COMANDO 'READ' + 'TOKEN'
	server.send(data)

	print("SENT")
	
	# ABRIR O FICHEIRO
	weatherfile = open("weather.csv", 'w')
	writer = csv.DictWriter(weatherfile, fieldnames = ['TEMPERATURE', 'WIND', 'HUMIDITY'], delimiter = ';')
	writer.writeheader()

	# CONTADOR 'i'
	i = 0; 
	
	while i<6:
		try:
			json_data = get_data(server, X)
			json_decode = json_data.decode('utf-8')
			print(json_decode)
			dados = json.loads(json_decode)
			if len(dados)==3 :	
				t = dados["TEMPERATURE"]
				w = dados["WIND"]
				h = dados["HUMIDITY"]
				clothes(t, w, h)
			writer.writerow(dados)
			i = i + 1
		except:
			continue
	
	# FECHAR O FICHEIRO
	weatherfile.close()
	
	# FECHAR A LIGAÇÃO AO SERVIDOR
	server.close()
    
main()
