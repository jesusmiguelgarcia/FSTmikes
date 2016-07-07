# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:33:02 2015

@author: miguel
"""


from __future__ import division
import re
from nltk.probability import FreqDist
from operator import itemgetter
from decimal import *
import nltk
import itertools



#recibe una lista de oraciones y regresa los word_couples

def word_couples_moens(lista):
    word_couples = []
    regexp = "[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+"
    
    
    for oracion in lista:
        tokens = nltk.regexp_tokenize(oracion, regexp)
        #print len(tokens)
        pairs = list(itertools.permutations(tokens, 2))
        for pair in pairs:
            word_couples.append(pair[0]+"~"+pair[1])
        
    return word_couples

#comenta el dr aurelio incluir la puntuacion a los pares de palabras
def word_couple_con_puntuacion(lista):
    word_couples = []
    regexp = "[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+-*[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[.]+|[/,$?:;!()&%#=+{}*~.]+|[0-9]+"
    
    for oracion in lista:
        tokens = nltk.regexp_tokenize(oracion, regexp)
        #print len(tokens)
        pairs = list(itertools.permutations(tokens, 2))
        for pair in pairs:
            word_couples.append(pair[0]+"~"+pair[1])
        
    return word_couples


#word_couple_con_puntuacion_pares_minusculas

def word_couple_con_puntuacion_pares_minusculas(lista):
    word_couples = []
    
    
    regexp = "[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+-*[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[.]+|[/,$?:;!()&%#=+{}*~.]+|[0-9]+"
    
    for oracion in lista:
        
        #oracion = str(oracion)
        #oracion = oracion.to_lower
        #print oracion
        
        
        tokens = nltk.regexp_tokenize(oracion.lower(), regexp)
        #print len(tokens)
        
#         tokens_lower = []
#         for i in range(len(tokens)):
#             palabra = str(tokens[i])
#             tokens_lower.append(palabra.to_lower() )          
            
        
        pairs = list(itertools.permutations(tokens, 2))
        for pair in pairs:
            word_couples.append(pair[0]+"~"+pair[1])
        
    return word_couples



#recibe un texto asi que le tendre que hacer join a lo que me manda el programa de pastor
#rivisar como eliminar los saltos de linea
def busca_oraciones_texto_sin_formato_moens(texto):
    texto = texto.replace("\n", " ")
    #arregloTexto = texto.split(".")
      #segmentado para oraciones en español
    spanish_tokenizer = nltk.data.load("tokenizers/punkt/spanish.pickle")
    oraciones_spanish= spanish_tokenizer.tokenize(texto) # .decode('utf8')
    #print "oraciones"
    #print len(oraciones_spanish)
    #print oraciones_spanish
      
    return oraciones_spanish

# buscar logitud de oracion


#def logitud_oracion(texto):
    #segmentar
    #dividir en tokens
    

# logitud promedio de oraciones
#recibe lista de oraciones
def longitud_promedio_oraciones_moens(lista):
    regexp = "[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[.]+|[/,$?:;!()&%#=+{}*~.]+"
    total = 0
    num_oraciones = 0
    tokens = 0
    for oracion in lista:
        tokens = nltk.regexp_tokenize(oracion, regexp)
        total += len(tokens)
        #print len(tokens)        
        #total += len(oracion.split())
        num_oraciones += 1
    promedio = total / num_oraciones
    return promedio


def longitud_promedio_palabras_moens(lista):
    regexp = "[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+"
    total_palabras_en_oraciones = 0
    num_oraciones = 0
    tokens = 0
    promedio_longitud_palabras_oraciones = []
    for oracion in lista:
        total_palabras_oracion = 0
        num_palabras_oracion = 0
        tokens = nltk.regexp_tokenize(oracion, regexp)
        total_palabras_en_oraciones += len(tokens)
        for palabra in tokens:
            total_palabras_oracion += len(palabra)
            num_palabras_oracion += 1
            #print palabra
            #print len(palabra)
        if total_palabras_oracion > 0:
            promedio_longitud_palabras_oraciones.append(total_palabras_oracion/num_palabras_oracion)
        else:
            print oracion
        #print len(tokens)
        #total += len(oracion.split())
        num_oraciones += 1
    #promedio = total_palabras_en_oraciones / num_oraciones
    #print promedio_longitud_palabras_oraciones
    suma_promedios=0
    num_promedios = 0
    for promedios in promedio_longitud_palabras_oraciones:
        suma_promedios += promedios
        num_promedios += 1
    promedio = suma_promedios/num_promedios
        
    #promedio = sum(promedio_longitud_palabras_oraciones)/float(len(promedio_longitud_palabras_oraciones))    
    return promedio


#recibe texto y regresa numero de marcadores de puntuacion
def numero_puntuacion_moens(texto):
    regexp = "[/,$?:;!()&%#=+{}*~.]+"
    tokens = nltk.regexp_tokenize(texto, regexp)
    total = len(tokens)
    print len(tokens)    
    print tokens    
    return total



#funcion frecuencias y lemas
#obtener frecuencia
def freq_lema_ngrams(list_monograms,list_lemas):
    fdist1 = FreqDist(list_monograms)
    #fdist2 = FreqDist(list_lemas)
    vocabulary1 = fdist1.keys()  #valores distintos
    frec_grams=[];
    for tag in vocabulary1:
        temp1=[]
        for i in range(len(list_monograms)):
            if(list_monograms[i] == tag):
                temp1.append(list_lemas[i])
        temp2=set(temp1)                 
        
        frec_grams.append([tag, fdist1[tag], fdist1.freq(tag),'-'.join(temp2)])
    frec_grams_sort= sorted(frec_grams, key=itemgetter(1), reverse=True)
    return frec_grams_sort
    
#fin funcion

