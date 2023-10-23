def eh_prim(numero):
    for i in range(2, int(numero / 2) + 1):
        if numero % i == 0:
            return False
    return True


conjectura_falhou = True

numero1 = 1
while numero1 != 0:
    numero1 = int(input('Digite um numero: '))

    if numero1 == 0:
        print('Encerrando...')
        exit()
    elif numero1 <=2:
        print('O numero digitado é invalido, digite um numero superior ao 2!')
        numero1 += 1
    elif ((numero1 / 2)-(numero1//2)) != 0:
        print('Numero invalido, digite um numero par superior ao 2!')
        numero1 -= numero1
        numero1 += 1


    for i in range(numero1):
        for j in range(2, int(numero1 / 2) + 1):
            deu_certo = (eh_prim(j) and eh_prim(numero1 - j))
            if deu_certo:

                if (((numero1+1)/2)-((numero1+1)//2) != 0 ):
                    print(f'O número {numero1} pode ser a soma de {j}  e  {numero1 - j}')
                    numero1 += 1

#Diego Costa RM552648
#Lucas Minozzo RM553745
#Marcelo Galli RM553654