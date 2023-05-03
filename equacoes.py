opcao = 1
while opcao:
    print (" <------->  equação do primeiro grau <-------> ")
    a =  float(input("Declarar um valor para A !:"))
    b =  float(input("Declarar um valor para B !:"))
    c =  float(input("Declarar um valor para C !:"))
    print (" <------->    -   <--------->   -    <-------> ")

    if a > 0:
        crecente_ou_mão = ("A função é crecente!:")
    else:
        crecente_ou_mão = ("A função não é crecente!:")


    delta = b**2 - 4*a*c

    x1 = (-b+(delta**0.5))/(2*a)
    x2 = (-b-(delta**0.5))/(2*a)


    print(f"O delta é {delta}")
    print(crecente_ou_mão)
    print(f'O valor de x1 e {x1:.2f}')
    print(f'O valor de x2 e {x2:.2f}')

    opcao = input("Deseja testa outrar função? [s/n]:")
    if opcao == "s":
        opcao = 1
    elif opcao == "n":
        print('Obrigado por usar o nosso programa :)')
        opcao = 0
