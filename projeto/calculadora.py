
while True:

    x = input("digite um numero: ")
    operador = input("digite um operador: ")
    y = input("digite outro numero: ")

    flag = None
    try: 
        x = float(x)
        y = float(y)
        flag = True
    except:
        flag = None

    if flag is None: print("um ou ambos numeros digitados são invalidos")

    operadores_permitidos = '-+/*'

    if operador not in operadores_permitidos:
        print("operador invalido")
        continue

    if len(operador) > 1:
        print("digite apenas um operador")
        continue

    if operador == "+": print(x + y)
    elif operador == "-": print(x - y) 
    elif operador == "*": print(x * y) 
    else: print(x / y) 
  

    sair = input("deseja sair? [s]im: ").lower().startswith('s')
    if sair is True: break


