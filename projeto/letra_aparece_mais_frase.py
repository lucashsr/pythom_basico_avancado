frase = "agora ou nunca"

frase = frase.replace(" ", "")

i = 0 

aux = 0
aux_letra = ''

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_apareceu = frase.count(letra_atual)

    print(letra_atual, quantas_vezes_apareceu)


    if (quantas_vezes_apareceu > aux): aux = quantas_vezes_apareceu
    if (quantas_vezes_apareceu == aux): aux_letra = letra_atual

    i+=1

print(f'A letra que mais apareceu foi a letra "{aux_letra}", {aux} vezes')