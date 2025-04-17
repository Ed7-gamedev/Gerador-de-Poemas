from teste import frases

rimas = []

assuntos = []

versos= []


def verAssunto(a):
    b = False
    
    if a in assuntos:
        b = True
    return b

def verRima(a):
    b = False
    
    if a in rimas:
        b = True
    return b


for frase in frases:
    if verAssunto(frase[1])  == False:
        assuntos.append(frase[1])
    if verRima(frase[2])  == False:
        rimas.append(frase[2])
    
    versos.append(frase[0] if frase[0] not in versos else None)
        
        
    rimas.sort()
    assuntos.sort()

print(len(versos))



    