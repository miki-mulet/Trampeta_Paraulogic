# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 2021

@author: mmulet

Petita trampa pel joc Paraulògic. Impossible trobar la base de dades del DIEC,
així que utilitzo una llista de paraules de Softcatalà, on no estan classificades.
El resultat, per tant, dona moltes més paraules de les acceptades al joc, però pot ser d'ajuda!
"""


import unicodedata

#----- Canviar les lletres del dia!!

# keyLetter = input('Introdueix la lletra central: ')
# sixLetters = input('Introdueix les lletres restants en qualsevol ordre: ')
keyLetter = 'o' #Lletra central
sixLetters = 'aesmzr' #Lletres restants, l'ordre és indiferent

#-----


def diccionari():
    '''
    Output: LLista amb totes les parules de la base de dades de Softcatala sense 'ç'.
    
    '''
    dicc = []
    diccionari = open('catalan.txt', 'r', encoding = 'utf-8') #cataleg de paraules de softcatala, n'hi ha mes del compte
    for line in diccionari:
        inner_list = [elt.strip() for elt in line.split('/')]
        dicc.append(inner_list)
        
    diccionari = []
    
    for d in dicc:
        if 'ç' not in d[0]:
            diccionari.append(d[0])
    return diccionari

def normalitzaDiccionari(diccionari):
    '''
    Input: diccionari = LLista amb totes les parules de la base de dades de Softcatala sense 'ç'.
    Output: diccionari normalitzat; sense accents, majúscules ni dieresis.

    '''
    
    for i in range(len(diccionari)):
        nfkd_form = unicodedata.normalize('NFKD', diccionari[i])
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        diccionari[i] = only_ascii.decode('utf-8').lower()
    return diccionari

def createSolution(alfabetCheck, diccionari):
    '''
    Input:
        alfabetCheck = totes les lletres del alfabet excepte les acceptades pel joc.
        diccionari = Llista amb les parules normalitzades de Softcatalà.
    Output:
        Llista amb totes les paraules que compleixen les condicions de Paraulògic.

    '''

    for l in allKeyLetters:
        alfabetCheck = alfabetCheck.replace(l,'')
        
    result = []
    
    for paraula in diccionari:
        if keyLetter in paraula and len(paraula) > 2:
            for lletra in paraula:
                if lletra in alfabetCheck:
                    paraulaCorrecta = False
            if paraulaCorrecta:
                result.append(paraula)
            paraulaCorrecta = True
    return result

def tuti(result, allKeyLetters):
    '''
    Input:
        result = Llista amb totes les paraules que compleixen les condicions de Paraulògic.
        allKeyLetters = str amb totes les lletres acceptaded pel joc.
    Output:
        llista amb tots els tutis trobats

    '''
    tutis = []
    for paraula in result:
        tuti = True
        for lletra in allKeyLetters:
            if lletra not in paraula:
                tuti = False
        if tuti == True:
            tutis.append(paraula)
    return tutis

diccionari = diccionari()
diccionari = normalitzaDiccionari(diccionari)
allKeyLetters = keyLetter + sixLetters
alfabetCat = 'abcdefghijklmnopqrstuvwxyz'
alfabetCheck = alfabetCat

result = list(dict.fromkeys(createSolution(alfabetCheck, diccionari)))  
    
print('---Tuti/s: ')
print(tuti(result, allKeyLetters))
print('---Totes les solucions: ')
print(result)
    


