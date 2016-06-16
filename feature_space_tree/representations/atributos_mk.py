# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:33:02 2015

@author: miguel
"""


import re


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
    
    
