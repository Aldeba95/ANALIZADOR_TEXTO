def buscador_de_letras(texto, letra_1, letra_2, letra_3):

    lista_letras = [letra_1, letra_2, letra_3]

    # Contamos las letras que aparecen en el texto
    buscar_letra_1 = texto.count(lista_letras[0])
    buscar_letra_2 = texto.count(lista_letras[1])
    buscar_letra_3 = texto.count(lista_letras[2])

    print('-'*60)
    print('')
    print('BUSCADOR DE LETRAS')
    print(f'la letra "{lista_letras[0].upper()}" aparece {buscar_letra_1} veces')
    print(f'la letra "{lista_letras[1].upper()}" aparece {buscar_letra_2} veces')
    print(f'la letra "{lista_letras[2].upper()}" aparece {buscar_letra_3} veces')
    print('')
    print('-'*60)

def inicio_y_fin(texto):

    # Haciendo slicing para mostrar la primera  y última letra del texto
    inicio_texto = texto[0]
    fin_texto = texto[-1]
    
    print('')
    print('LETRA DE INICIO Y FIN DEL TEXTO')
    print(f'Su texto inicia con la letra "{inicio_texto.upper()}" y termina con la letra "{fin_texto.upper()}"')
    print('')
    print('-'*60)

def cantidad_de_palabras(texto):

    # Convertimos el texto a una lista y contamos sus atributos
    lista_texto = texto.split()
    palabras_texto = len(lista_texto)

    print('')
    print('CANTIDAD DE PALABRAS DEL TEXTO')
    print(f'El texto tiene "{palabras_texto}" palabras')
    print('')
    print('-'*60)

def texto_invertido(texto):

    palabras_texto = texto.split()
    palabras_texto.reverse()

    texto_reverso = ' '.join(palabras_texto)

    print('')
    print('TEXTO INVERTIDO')
    print(f'Tu texto al revés es: "{texto_reverso}"')
    print('')
    print('-'*60)

def coincidencia(texto, palabra_usuario):

    print('')
    print('BUSCANDO LA PALABRA EN EL TEXTO')

    if palabra_usuario in texto:  
        print(f'La palabra "{palabra_usuario.upper()}" se encuentra en el texto')
    else:
        print(f'La palabra "{palabra_usuario.upper()}" no se encuentra en el texto')



def main():
    
    # Texto que el usuario va a ingresar
    texto = input('Ingrese un texto a elección: ').lower()

    # Letras que el usuario quiere contar dentro del texto
    letra_1 = input('Ingrese la primera letra a buscar: ').lower()
    letra_2 = input('Ingrese la segunda letra a buscar: ').lower()
    letra_3 = input('Ingrese la tercera letra a buscar: ').lower()

    buscador_de_letras(texto, letra_1, letra_2, letra_3)
    inicio_y_fin(texto)
    cantidad_de_palabras(texto)
    texto_invertido(texto)
    

    palabra_usuario = input('Ingrese una palabra que desee buscar: ').lower()
    coincidencia(texto, palabra_usuario)

main()



    
