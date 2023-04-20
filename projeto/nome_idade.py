def exibir_formulario(nome, idade):
    return(f'seu nome é: {nome}\n'
           f'sua idade é: {idade}\n'
           f'seu nome invertido é {nome[::-1]}\n'
           f'{contem_espaco(nome)}\n'
           f'seu nome contem {len(nome.replace(" ",""))} letras\n'
           f'a primeira letra do seu nome é {nome[0]}\n'
           f'a ultima letra do seu nome é {nome[-1]}\n')

def contem_espaco(nome):
    if " " in nome: return "seu nome contem espaco"
    else: return "seu nome nao contem espaco"


nome = input("Informe seu nome: ")
idade = int(input("informe sua idade: "))

if nome and idade:
    print(exibir_formulario(nome, idade))
else:
    print("desculpe voce deixou campos vazios" )