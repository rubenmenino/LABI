# encoding=utf-8
import wave
import json
import math
from math import sin, pi

rate = 44100

# sem efeito
def efeito_null(info, sounds):
    
	for sound in sounds:
		info += sound['samples']
		
	return info

# efeito eco
def efeito_eco(info, sounds):
	
	info = efeito_null(info, sounds)
	
	# aumenta o tempo do som de modo a não cortar o eco
	for i in range(0, rate/2):
		info.append(0)
	
	
	for i in range (0, len(info)):
		if i > rate/10:
			info[i] += 0.5 * info[i-rate/10] # delay de 0.1 segundos
		
		if i > rate/5:
			info[i] += 0.2 * info[i-rate/5]	# delay de 0.2 segundos

	return info

# efeito tremer
def efeito_tremer(info, sounds):
	
	info = efeito_null(info, sounds)
	
	for i in range (0, len(info)):
		info[i] += 0.3 * sin(2.0 * pi * 20 * i / rate) * info[i];

	return info

# efeito distorção
def efeito_distort(info, sounds):
	
	info = efeito_null(info, sounds)
	
	for i in range (0, len(info)):
		info[i] = pow(info[i], 2)

	return info


def create_wav_file(name, sounds, efeito='none'):
	
	wv = wave.open(name, 'w')
	wv.setparams((1, 2, rate, 0, 'NONE', 'not compressed'))

	info = []
	
	if efeito == 'eco':
		info = efeito_eco(info, sounds)
	
	elif efeito == 'tremer':
		info = efeito_tremer(info, sounds)
	
	elif efeito == 'distortion':
		info = efeito_distort(info, sounds)
	
	else:
		info = efeito_null(info, sounds)
		
	info = normalize(info)	# não sei se funciona, retirado de guião
	wvData = ''
	for x in info:
		wvData += pack('h', x)
	wv.writeframes(wvData)
	wv.close()
