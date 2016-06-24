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


import itertools
#recibe una lista de oraciones y regresa los word_couples

def word_couples_moens(lista):
    word_couples = []
    regexp = "[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+"
    
    
    for oracion in lista:
        tokens = nltk.regexp_tokenize(oracion, regexp)
        print len(tokens)
        pairs = list(itertools.permutations(tokens, 2))
        for pair in pairs:
            word_couples.append(pair[0]+"~"+pair[1])
        
    return word_couples





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

# recibe lista de lemas  y regresa arreglo con los 5 elemetos

def maracadores_florou(monograms_solo_lemas):
    
    
    #valores para tiempos
    dm= [0,0,0,0,0]
    dm_nom= ["justificacion","explicacion","deduccion","refutacion","condicional"]
    
    
    # buscar palabras claves
    #dm= [0,0,0,0,0]
    #dm_nom= ["justificacion","explicacion","deduccion","refutacion","condicional"]
    
    markers_count=[]
    
    #lematizar con freeling antes
    
    
    lemas_string= " ".join(monograms_solo_lemas)
  
    #caracteristicas enriquecidas traducidas directamente
    pc_justificacion=["(porque)","(como)","(la razón ser)","(el motivo ser)", "(deber a)","(a causa de)","(razón de que)", "(motivo de que)" ]
    pc_explicacion=["(en otro palabra)","(de otro modo)", "(decir de otro modo)","(la razón ser)","(el motivo ser)", "(deber a)","(a causa de)","(razón de que)", "(motivo de que)", "(por este razón)", "(por este motivo)", "(por ese razón)", "(por ello)", "(por ejemplo)"]
    pc_deduccion=["(a consecuencia de)","(demostrar que)","(probar que)", "(establecer que)", "(concluir que)", "(deducir que)", "(inferir que)", "(implicar que)" , "(de acuerdo a el anterior)"]
    pc_refutacion=["(sin embargo)","(a pesar de)","(a menos)"]
    pc_condicional=["(suponer que)","(aunque)","(si)", "(en caso de)","(si y solo si)" ]
    
    for pc in pc_justificacion:
        dm[0]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)                                   #imprime el arreglo con todas las instancias de la palabra clave
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )       # agregar a un  la palabra clave y las veces que se repite
    
    for pc in pc_explicacion:
        dm[1]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )
    
    for pc in pc_deduccion:
        dm[2]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )
            
    for pc in pc_refutacion:
        dm[3]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )
            
    for pc in pc_condicional:
        dm[4]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)   
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )
    
    return dm
    
    #fin buscar palabras claves
    
    
    
def maracadores_florou_enriquecidos(monograms_solo_lemas):
                
    #valores para tiempos
    dm= [0,0,0,0,0]
    dm_nom= ["justificacion","explicacion","deduccion","refutacion","condicional"]
    
    
    # buscar palabras claves
    #dm= [0,0,0,0,0]
    #dm_nom= ["justificacion","explicacion","deduccion","refutacion","condicional"]
    
    markers_count=[]
    
    #lematizar con freeling antes
    
    
    lemas_string= " ".join(monograms_solo_lemas)
    
    #caracteristicas enriquecidas
    pc_justificacion=["a causa de","a el fin y a el cabo","a el fin y a el postre","a fin de cuenta","como","como mostrar","como ser indicar por","con decir te","dar que","de acuerdo con","de hecho","deber a","deber se a","después de todo","el anterior porque","el motivo ser","el razón ser","el razón ser que","en tanto que","en vista de que","gracia a","motivo de que","no en vano","poner que ser consecuencia de","por causa de","por cuanto","por todo ello","porque","pues","puesto que","razón de que","se poder deducir de","se poder derivar de","se seguir de","ser que","ver que","ya que"]
    pc_explicacion=["a causa de","a fin de cuenta","así","de otro modo","deber a","decir de otro modo","el motivo ser","en concreto","en definitivo","en otro palabra","en particular","el razón ser","motivo de que","poner","poner por caso","por ejemplo","por ello","por ese razón","por este motivo","por este razón","razón de que","uno ejemplo","uno poner"]
    pc_deduccion=["a consecuencia de","a el fin y a el cabo","ante el anterior","así","así pues","así que","como conclusión","como consecuencia","como resultado","concluir que","conclusión","consecuentemente","consiguientemente","correspondientemente","de acuerdo a el anterior","de ahí que","de este forma","de manera que","de tal forma","de tal manera","deducir que demostrar que","el cual apuntar a el conclusión de que","el cual implicar que","el cual mostrar que","el cual nos permitir inferir que","el cual probar que","el cual significar que","en conclusión","en consecuencia","en definitivo","en fin","en resumen","en resumir cuenta","en sí","en síntesis","en suma","en tal caso","entonces","establecer que","finalmente","implicar que","inferir que","llegar a el","llegar a el conclusión","para","para concluir","para terminar","poder inferir que","por consiguiente","por el que","por el tanto","por ello","por ende","por ese","por este razón","por tanto","por último","probar que","que","resumir","se desprender","se desprender de","se seguir que","ser por ese que"]
    pc_refutacion=["a el contrario","a menos","a pesar de","a pesar de todo","ahora","antes bien","aun así","aunque","bien a el contrario","de cualquiera modo","de todo modo","después de todo","empero","en cambio","ese sí","mas","más aun","más bien","muy a el contrario","no obstante","no parecer","pero","pero sin embargo","pesar a","por contra","por el contrario","pues","si bien","sin embargo","sino","sólo que"]
    pc_condicional=["según","con tal que","a condición de que","a menos que","con que","suponer que","aunque","si","en caso de","si y solo si"]
    
 
    for pc in pc_justificacion:
        dm[0]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)                                   #imprime el arreglo con todas las instancias de la palabra clave
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )       # agregar a un  la palabra clave y las veces que se repite
    
    for pc in pc_explicacion:
        dm[1]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )
    
    for pc in pc_deduccion:
        dm[2]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )
            
    for pc in pc_refutacion:
        dm[3]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )
            
    for pc in pc_condicional:
        dm[4]+=len(re.findall(pc, lemas_string))
        if (re.findall(pc, lemas_string)):
            #print re.findall(pc, lemas_string)   
            markers_count.append( pc+" "+str(len(re.findall(pc, lemas_string))) )
    
    return dm
    
    #fin buscar palabras claves
    

def verbos_florou(monograms_solo_tags):

    #valores para tiempos
    tiempos = ["P","S","I","C","F","0"]
    tiempos_nom= ["Presente","Pasado","Imperfecto","Condicional","Futuro","No_tiene"]
    
    
    #P    Presente
    #S    Pasado
    #I    Imperfecto
    #C    Condicional
    #F     Futuro
    rel=[0,0,0,0,0,0] #arreglo para tiempos y modos
    rel_cuenta=[0,0,0,0,0,0] #  arreglo con cuenta de tiempos y modos
    total_verbos=0
    
    
    modo= ["P","G","I","S","M","N"]
    modo_nom= ["Participio","Gerundio","Indicativo","Subjuntivo","Imperativo","Infinitivo"]

    #P     Participio
    #G     Gerundio
    #I     Indicativo
    #S     Subjuntivo
    #M     Imperativo
    #N    Infinitivo
    rel2=[0,0,0,0,0,0] #arreglo para tiempos y modos
    rel_cuenta2=[0,0,0,0,0,0] #  arreglo con cuenta de tiempos y modos
    
    #fin valores modo
    # posibles combinaciones 
    
    
    
    combinaciones_mt=['P0', 'G0', 'IP', 'IS', 'SP', 'II', 'SI', 'M0', 'N0', 'IC', 'IF']
    combinaciones_mt_conteo=[0,0,0,0,0,0,0,0,0,0,0]
    rcm_mt=[0,0,0,0,0,0,0,0,0,0,0]
    total_terminos=0
    
    monograms=[]           #almacena las POS tags
    monograms_lemas=[]     #almacena tags y lemas
    monograms_solo_lemas=[]     #almacena lemas de todo el texto
    texto_completo="" 
    monograms_mt=[]    #almacena modo y tiempo
    
    #list1=( linea.split() for linea in open(namefile) )
    
    
    verbo_aux_haber=0
    verbo_haber=0
      
        
    for word in monograms_solo_tags:
        if len(word)>2:          
            if re.match("V.+",word):
                #print word[2] # word[2] tag
                monograms.append(word) #agrega verbo a la lista
                #monograms_lemas.append(word[1]+" "+word[2])
                monograms_mt.append(word[2]+word[3]) #arreglo de modo y tiempos
                i=tiempos.index(word[3]) #encontrar donde esta el elememnto "P" en la lista
                rel_cuenta[i]+=1
                i=modo.index(word[2]) #encontrar donde esta el elememnto en la lista
                rel_cuenta2[i]+=1
                total_verbos+=1   # cuenta de verbos
                
                combinacion_temp= word[2]+word[3] #la combinacion de modo y tiempo a buscar
                i=combinaciones_mt.index(combinacion_temp)
                combinaciones_mt_conteo[i]+=1
                
#                 if verbo_aux_haber == 1:
#                     verbo_aux_haber=0
#                     print word[1]+" "+word[2]
#                 
#                 if re.match("VA.+",word) and word=="haber":
#                     verbo_aux_haber=1
#                     verbo_haber+=1
#                     print word[1]+" "+word[2]
#                 
                
    # se obtiene de freeling
    
    #encontrar frecuencia relativa de tiempos
    for i in range(len(rel)):
        if rel_cuenta[i]>0:
            rel[i]=rel_cuenta[i]/total_verbos #tiempos
        
    for i in range(len(rel2)):
        if rel_cuenta2[i]>0:
            rel2[i]=rel_cuenta2[i]/total_verbos #modos
    
    for i in range(len(combinaciones_mt_conteo)):
        if combinaciones_mt_conteo[i]>0:
            rcm_mt[i]=combinaciones_mt_conteo[i]/total_verbos
            
    bin_mt = [0,0,0,0,0,0] #tiempos 
    bin2_mt = [0,0,0,0,0,0] #modos
    
    for i in range(len(rel)): #tiempos 
        if rel_cuenta[i]>0:
            bin_mt[i]=1
        
    for i in range(len(rel2)): #modos
        if rel_cuenta2[i]>0:
            bin2_mt[i]=1
            
    
            
    #fin de frecuencias
    
    # tiempo, modo y combinacion mas frecuente
    
    tiempo_mf= tiempos[rel.index(max(rel))]
    #print "tiempo mas frecuente:"+str(tiempo_mf)
    
    modo_mf= modo[rel2.index(max(rel2))]
    #print "modo mas frecuente:"+str(modo_mf)
    
    comb_mf= combinaciones_mt[rcm_mt.index(max(rcm_mt))]
    #print "combinacion mas frecuente:"+str(comb_mf)
    
    
    
  #  markers_count=[]
    
    
    
    #tiempo y modos
#     freq_mono_tm = freq_lema_ngrams(monograms_mt,monograms_lemas)
#     texto_mt=""
#     texto_mt_freq=""
#     for elemento in freq_mono_tm:
#             texto_mt+= ', '.join(map(str,elemento))
#             texto_mt+= "\n"
#             texto_mt_freq+=  str(elemento[0])+ " "
#             texto_mt_freq+=  str(elemento[1])+ " "
#             texto_mt_freq+=  str(elemento[2])+ " "
#             texto_mt_freq+="\n"
    
    
    
    #Presentar resultados de extraccion -------
   # print ""
    
    #print namefile
    #print ' '.join(list_presenta)
    
#     print ""
#     print texto_completo
#     print ""
    
    #print texto1
    #print set(monograms)
    #print len(set(monograms))
    
   # print "modo y tiempo"
   
    #print set(monograms_mt)
    #print len(set(monograms_mt))
    
    #print texto_mt_freq
    
    
    #imprimir vector de caracteristicas
    #tiempos_nom[tiempos.index(tiempo_mf)] 
    
    modo_nom[modo.index(comb_mf[0])],tiempos_nom[tiempos.index(comb_mf[1])] 
    
    
    #imprime vector de parrafo           
    #print tiempos_nom, "\n",modo_nom,"\n", combinaciones_mt,"\n", tiempos, modo,"\n","tiempo:",tiempos_nom[tiempos.index(tiempo_mf)], "- modo:",modo_nom[modo.index(modo_mf)], "- combinación:",modo_nom[modo.index(comb_mf[0])],tiempos_nom[tiempos.index(comb_mf[1])] 
    #print rel,"\n", rel2,"\n", rcm_mt, "\n",bin_mt, bin2_mt,"\n", tiempo_mf, modo_mf, comb_mf
#     
    
    vector=[]
    vector+=rel+rel2+rcm_mt+bin_mt+bin2_mt
    vector.append(tiempos.index(tiempo_mf))
    vector.append(modo.index(modo_mf))
    vector.append(combinaciones_mt.index(comb_mf))
    
    
#      "Rel_t Rel_m  RCm  bin_t  bin_m   ,tiempo_mf,modo_mf,comb_mf"


#tiempos_nom= ["Presente(P)","Pasado(S)","Imperfecto(I)","Condicional(C)","Futuro(F)","No_tiene(0)"]
#modo_nom= ["Participio(P)","Gerundio(G)","Indicativo(I)","Subjuntivo(S)","Imperativo(M)","Infinitivo(N)"]
# combinaciones_mt=['P0', 'G0', 'IP', 'IS', 'SP', 'II', 'SI', 'M0', 'N0', 'IC', 'IF']

    
#     print ""
#     print vector
#     print ""
    
#     for palabra in markers_count:
#             print palabra
#             
#     print ""
    
    return vector



#   
# prueba = ["VSIF3P0","VMIS1P0","VMM03P0","VMIC1P0"]
#   
# salida = verbos_florou(prueba)
#   
# print salida

