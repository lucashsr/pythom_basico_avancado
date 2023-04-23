"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os 

while True:

    palavra_secreta = "casa"
    letras_acertadas = ''
    count = 0

    while True:
        
        letra = input("digita uma letra: ")

        if len(letra) > 1:
            print("digite apenas uma letra")
            continue
        
        palavra_formatada = ''

        if letra in palavra_secreta: letras_acertadas += letra

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas: palavra_formatada += letra_secreta
            else: palavra_formatada += '*'

        print(palavra_formatada)

        count += 1

        if palavra_formatada == palavra_secreta: 
            os.system("cls")
            print(f"VOCE GANHOU!!! PARABENS!\n{count} TENTATIVAS\na palavra formada era: {palavra_secreta}")
            break




        
        
        
        
