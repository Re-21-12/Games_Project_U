'''
'''
from random import randint
from  colorama import init,Fore,Back,Style
import colorama
init()
colorama.init(autoreset = True)#resetea el color en cada linea
nombre = input('Ingresa tu nombre')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print('Bienvenido: ', nombre)
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
mipalabra = ''  # mipalabra vacia para ingresar
vida = 6
palabra = {1: 'C++', 2: 'C', 3: 'Python', 4: "Carbon", 5: "GO", 6: "Javascript", 7: "Java", 8: "Editor de Codigo", 9: "Compilador", 10: "Sintaxis", 11: "Recursividad", 12: "Funcion", 13: "For", 14: "While", 15: "Do while", 16: "In", 17: "Not in", 18: "And", 19: "Or", 20: "Range", 21: "Plus", 22: "Minus", 23: "Codigo", 24: "If", 25: "Else", 26: "Condicionales", 27: "Compilar", 28: "Codear", 29: "Random", 30: "break", 31: "Variable", 32: "Constante", 33: "Operador", 34: "Iteracion", 35: "Iterar", 36: "Asignar", 37: "Archivo", 38: "Documento", 39: "Organizacion", 40: "Programacion", 41: "Sobreescribir", 42: "Importar", 43: "Exportar", 44: "Probar", 45: "Estructura de codigo", 46: "Reescribir", 47: "Guardar", 48: "Desarrollar", 49: "Investgiar", 50: "Fuerza bruta",
           51: "String", 52: "Bool", 53: "Integer", 54: "Tupla", 55: "Lista", 56: "Diccionario", 57: "Padre", 58: "Hijo", 59: "Diagrama", 60: "Analizar", 61: "array", 62: "Matriz", 63: "Vector", 64: "Pitagoras", 65: "Pi", 66: "Grado", 67: "Grados", 68: "Heredar", 69: "Mutar", 70: "Solucionar", 71: "Proveer", 72: "Identacion", 73: "Combinacion", 74: "Permutacion", 75: "Gramatica", 76: "Ortografia", 77: "Suma", 78: "Resta", 79: "Multiplicacion", 80: "Division", 81: "Potencia", 82: "Raiz", 83: "Sistema", 84: "Ecuacion", 85: "Recta", 86: "Vector", 87: "Ttypescript", 88: "React", 89: "Angular", 90: "Vue", 91: "Bootstrap", 92: "Framework", 93: "Documentacion", 94: "Interna", 95: "Externa", 96: "POO", 97: "Palabras", 98: "Letra", 99: "Numero", 100: "Compilador"}
r = randint(1, 100)  # Indica donde se debe almacenar el numero aleatorio
while vida > 0:  # Hacer todo mientras que vida sea mayor a 0
    error = 0  # Inicializa error
    for letra in palabra[r]:
        if letra in mipalabra:
            print(letra, end='')  # END AGREGA UN ESPACIO AL FINAL
        else:
            print(Fore.BLUE + Style.BRIGHT + '_', end='')
            error += 1  # Agrega un error
    if error == 0:
        print(Fore.RED + Style.BRIGHT +  'Felicidades has ganado!',vida)
        break  # Rompe el ciclo

    miletra = input(Fore.RED + Style.BRIGHT + 'Ingresa una letra: ')
    mipalabra += miletra
    if miletra not in palabra[r]:  # Not in == no se encuentra
        print( Fore.RED + Style.BRIGHT  + 'Te equivocaste, vuelve a intentarlo',vida)
        print('Posees: ', +vida, 'vidas')
        vida -= 1
    if vida == 0:
        print(Fore.YELLOW + Style.BRIGHT +'Has perdido, mejor suerte a la proxima: ', nombre)
else:
    print(Fore.YELLOW + Style.BRIGHT + 'gracias por participar', nombre)
    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
