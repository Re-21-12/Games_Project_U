 
 *Primero  importamos la libreria randint*
 ~~~
 from random import randint
 ~~~
  ***from random import randint***

*Esta libreria nos sirve para generar la palabrar a adividar dentro del juego*

*Seguido pedimos al usuario ingresar su nombre*
~~~
nombre=input('Ingresa tu nombre')

print('Bienvenido: ', nombre)
~~~
*Continuamos con los pasos*
~~~
mipalabra=" " (palabra vacia para ingresar)

vida = 6 contamos con un limite de 6 vidas
~~~
*Utilizamos la variable palabra la cual contiene las palabras a adivinar*
~~~
palabra = { 1: 'Hola',2: 'Adios', 3:'Como estas'}

r = randint (1,3) (Genera cualquiera de las palabras al azar)
~~~
*Utilizamos un ciclo while para que siempre que las vidas sean mayores que 0 imprima una letra hasta ganar o perder*
~~~
while vida > 0: 

    error = 0
    for letra in palabra[r]:
        if letra in mipalabra:
            print(letra,end=' ') ( endl= ""nos agrega un espacio al final)
        else:
            print(' _',end='')
            error+=1
    if error == 0:
        print('Felicidades has ganado!')
        break (con el break se termina dicho ciclo)
~~~
*De la siguiente manera pedimos al usuario que adivine una letra*
~~~
 miletra = input('Adivina una letra: ')

 mipalabra+=miletra** *(a mipalabra la cual esta vacia se le va agregando o sumando mi letra ingresada)
~~~
 *Por ultimo seria validar con la condicion *if*
~~~
  if miletra not in palabra[r]:
  
        print('Te equivocaste, vuelve a intentarlo')
        print('Posees: ', +vida, 'vidas')
        vida-=1
    if vida == 0:
        print('Has perdido, mejor suerte a la proxima: ',nombre)
*else:
    print('gracias por participar')*
~~~ 

