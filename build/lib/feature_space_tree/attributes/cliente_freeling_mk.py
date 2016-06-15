#!/usr/local/bin/python
# coding: utf-8


import re, string
import nltk
from sys import stderr, version
import socket
import sys

# Codigo de Mike apoyado en pynlpl
#regresar lemas, tags , tuplas (texto , lema, tag)

#uso con regexp que separa

#regexp = "[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+-*[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[.]+|[/,$?:;!()&%#=+{}*~.]+"

#linex = "Mary año tiene un borrego acasffss.  es una causa perdida. Los niños juegan."
#line = " Los niños juegan. La propuesta se distingue por incorporar la representación de la experiencia en el modelo del estudiante. Generalmente, las aplicaciones afines se concentran en representar el conocimiento adquirido por el estudiante GRUNDY (Rich, 1979), sus atributos personales Smex Web (Albrecht et al., 2000), conductas observadas ELM-PE (Brusilovsky, 1995b), distorsiones en el aprendizaje Modelos de Diagnóstico (Brown y Burton, 1978) y el conocimiento de enseñanza ADAPS (Brusilovsky y Cooper, 1999). En cambio, en el presente trabajo los atributos de la experiencia forman parte del propio modelo del estudiante. Como resultado, se obtiene una representación más rica del fenómeno de estudio, puesto que se consideran a dos protagonistas: el emisor y el receptor del conocimiento que se transmite y adquiere."
#words, postags, lemmas, tuplas = POS_freeling(linex, regexp)
#print tuplas


def u(s, encoding = 'utf-8', errors='strict'):
    #ensure s is properly unicode.. wrapper for python 2.6/2.7,
    if version < '3':
        #ensure the object is unicode
        if isinstance(s, unicode):
            return s
        else:
            return unicode(s, encoding,errors=errors)
    else:
        #will work on byte arrays
        if isinstance(s, str):
            return s
        else:
            return str(s,encoding,errors=errors)

def b(s):
    #ensure s is bytestring
    if version < '3':
        #ensure the object is unicode
        if isinstance(s, str):
            return s
        else:
            return s.encode('utf-8')
    else:
        #will work on byte arrays
        if isinstance(s, bytes):
            return s
        else:
            return s.encode('utf-8')
        
 
def POS_freeling(texto, regexp):
 
    #preprocesado para pasar una lista con las palabras
    # se podria pasar despues del posfilter ya que ahi se tienen las palabras en 
    # una lista
    host = "localhost"
    port = 50005
    debug=True
    
    tokens = nltk.regexp_tokenize(texto, regexp)
    texto_s= " ".join(tokens) 
    sourcewords_s = texto_s
    sourcewords = tokens
    
    encoding='utf-8'
    timeout=120.0
    host = "localhost"
    
    port = 50005
    BUFSIZE = 10240
    socketx = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socketx.settimeout(timeout)
    socketx.connect( (host,int(port)) )
    socketx.sendall('RESET_STATS\0')
    
    
    r = socketx.recv(BUFSIZE)
    if not r.strip('\0') == 'FL-SERVER-READY':
        raise Exception("Server not ready")
#     else:
#         print "server listo"
    
    #se toma lista separada por espacios
    
    
    socketx.sendall( b(sourcewords_s) +'\n\0') #funciona con str no con UTF ojo
    #print "Sent:",line2s,file=sys.stderr
    
    debug = False
    results = []
    done = False
    while not done:    
        data = b""
        while not data:
            buffer = socketx.recv(BUFSIZE)
            #print("Buffer: ["+repr(buffer)+"]")
            #print buffer
            if buffer[-1] == '\0':
                data += buffer[:-1]
                done = True
                break
            else:
                data += buffer
        
        
        #print data
        
        data = u(data,encoding) #combierte a utf-8
        #if debug: print("Received:",data) 
    
        for i, line in enumerate(data.strip(' \t\0\r\n').split('\n')):
            if not line.strip():
                done = True
                break
            else:
                cols = line.split(" ")
                subwords = cols[0].lower().split("_")
                if len(cols) > 2: #this seems a bit odd?
                    for word in subwords: #split multiword expressions
                        results.append( (word, cols[1], cols[2], i, len(subwords) > 1 ) ) #word, lemma, pos, index, multiword?
        
    
    #print results
    if debug: print("Received:",results) 
    
    
    words = []
    postags = []
    lemmas = []
    for fields in results:
        word, lemma,pos = fields[:3]
        words.append(word)
        postags.append(pos)
        lemmas.append(lemma)
    
    
    #print lemmas,"\n", postags,"\n" , words
    
    return words, postags, lemmas, results
    
    #---------------------------------------------------------
    
    #words = line.strip().split(' ') # se debe pasar como lista o separado por espacios

# se lo puedo pasar por lineas o simplemente una cadena separada por espacios 
# recibe o lista o texto simplemente separado por espacios o bien como lista 

# 3 opciones

#uso de freeling para lemas y tags

# # 
# regexp = "[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+-*[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[.]+|[/,$?:;!()&%#=+{}*~.]+"
#  
# linex = "Mary año tiene un borrego acasffss.  es una causa perdida. Los niños juegan."
# line = " Los niños juegan. La propuesta se distingue por incorporar la representación de la experiencia en el modelo del estudiante. Generalmente, las aplicaciones afines se concentran en representar el conocimiento adquirido por el estudiante GRUNDY (Rich, 1979), sus atributos personales Smex Web (Albrecht et al., 2000), conductas observadas ELM-PE (Brusilovsky, 1995b), distorsiones en el aprendizaje Modelos de Diagnóstico (Brown y Burton, 1978) y el conocimiento de enseñanza ADAPS (Brusilovsky y Cooper, 1999). En cambio, en el presente trabajo los atributos de la experiencia forman parte del propio modelo del estudiante. Como resultado, se obtiene una representación más rica del fenómeno de estudio, puesto que se consideran a dos protagonistas: el emisor y el receptor del conocimiento que se transmite y adquiere."
# words, postags, lemmas, tuplas = POS_freeling(linex, regexp)
# 
# print tuplas
# 
# #parte de POS
# sufix_tag = []
# for i in range(len(postags)):
#     print postags[i]
#     if len(postags[i])>4:
#         sufix_tag.append(postags[i][0:4])
#     else:
#         sufix_tag.append(postags[i])
#         
# print sufix_tag






