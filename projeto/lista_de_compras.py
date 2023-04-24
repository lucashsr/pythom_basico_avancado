import os

lista_compra = []

while True:
    opcao = input("selecione uma opção:\n(i)nserir (a)pagar (l)istar:").lower()
    
    if opcao[0] == "i":
        os.system("cls")
        produto = input("Informe o que deseja adicionar na lista de compras: ")
        lista_compra.append(produto)
    
    elif opcao[0] == "a":
        os.system("cls")
        indice_apagar = input('informe o indice do produto que deseja apagar: ')
        try: 
            indice_apagar = int(indice_apagar)
        except:
            ...

        if isinstance(indice_apagar, int) and indice_apagar < len(lista_compra): lista_compra.pop(indice_apagar)
        else: print("indice invalido")
    
    elif opcao[0] == "l":
        os.system("cls")
        for i, nome in enumerate(lista_compra): 
            print(i, nome)


