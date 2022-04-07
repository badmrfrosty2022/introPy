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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Eduardo')

    # chamar a função de calculo da area do retângulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A área do retangulo é de {resultado} m²')

    # chamar a função de calculo da area do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de {resultado} m²')

    # chamar a função de calculo da área do triangulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f'A área do triangulo é de {resultado} m²')

    # executar uma contagem progressiva
    contagem_progressiva(11)

    # exibir o nome do candidato varias vezes
    apoiar_candidato('Bolsonaro 2022', 100)

    #brincar de plim
    brincar_de_plim(100)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
