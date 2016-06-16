# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:33:02 2015

@author: miguel
"""


from __future__ import division
import re
from nltk.probability import FreqDist
from operator import itemgetter


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

