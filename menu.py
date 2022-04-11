# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Oi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def calcular_area_do_retangulo(largura,comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura,comprimento):
    return largura * comprimento / 2

def contagem_progressiva(fim):
    for numero in range(fim): # repetir o bloco de zero até o fim
        print(numero)         # exibir o número

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        # contador = numero + 1
        # print(f'{contador} - {nome}')

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1,'-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM')
        else:
            print('{:0>3}'.format(numero))

def sair():
    print('Obrigado e Volte Sempre')

#def exibir_menu(resposta):
#    opcao = {
#        1: print_hi('Eduardo'),
#       2: calcular_area_do_retangulo(8, 9),
#        3: calcular_area_do_quadrado(7),
#        4: calcular_area_do_triangulo(5, 4),
#        5: contagem_progressiva(10),
#        6: apoiar_candidato('Bolsonaro', 10),
#        7: brincar_de_plim(20),
#        8: sair()
#    }
#    return opcao.get(escolha, 'Opção Inválida')

# Estrutura de identificação / execução do script
if __name__ == '__main__':

    resposta = "C"

    while resposta.upper() != 'Z':
        print('#######################################')
        print('#                                     #')
        print('#     M E N U   D E   O P Ç Õ E S     #')
        print('#                                     #')
        print('#    1 - Olá Mundo                    #')
        print('#    2 - Área do Retangulo            #')
        print('#    3 - Área do Quadrado             #')
        print('#    4 - Área do Triangulo            #')
        print('#    5 - Contagem Progressiva         #')
        print('#    6 - Apoiar Candidato             #')
        print('#    7 - Brincar de Plim              #')
        print('#                                     #')
        print('#    Z - Sair                         #')
        print('#                                     #')
        print('#######################################')


        resposta = input("Escolha a sua opção ")
        print(f'A sua escolha foi: {resposta}')
        #exibir_menu(resposta)

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Eduardo')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(8,7)
                print(f'A área do retangulo é de {resultado} m²')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(6)
                print(f'A área do quadrado é de {resultado} m²')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(5,8)
                print(f'A área do triângulo é de {resultado} m²')
            elif resposta == '5':
                contagem_progressiva(10)
            elif resposta == '6':
                apoiar_candidato('Bolsonaro 2002',10)
            elif resposta == '7':
                brincar_de_plim(7)
            else:
                print('Vc digitou uma opção inválida. Escolha uma opção de 1 a 7')


    print('Você escolheu sair. Volte Sempre')


