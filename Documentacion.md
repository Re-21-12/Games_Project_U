Documentacion Externa: Primer Proyecto
========
## **Proyecto desarrollado por:**
### Victor Alfredo Macario Enriquez 7690-22-5042
### Jefferson Ramiro Lopez Ramirez 7690-21-1522
### Roberto Antonio Ramírez Gómez 7690-22-12700
***
##  Triples de pitagoras: Python
- Primero importaremos una libreria llamada <mark>COLORAMA</mark>:
  ~~~
    from  colorama import init,Fore,Back,Style
    import colorama  
    ~~~
    Ademas de inicializar sus funcionalidades con la palabra *Init()*:
    ~~~
    Init()
    ~~~
    ***
- Seguido a los pasos anteriorss debemos declarar nuestras variables a utilizar:
  ~~~
  contador = 0;
  ~~~
  Esta variable seguira el proceso que a continucacion se explicara, agregando una valor por cada vuelta en los tres ciclos for, donde de esta manera nos dira en que intento se resolvio el triple de pitagoras.

- Para realizar la demostracion de fuerza bruta,  usaremos tres ciclos for anidados para  demostrar los triples de piitagoras, donde ***l1***, ***l2***  y ***h***  se iteraran hasta llegar a 500:
    ~~~
    for l1 in range(1,500):
        for l2 in range(1,500):
            for h in range(1,500):
    ~~~
    De esta manera cada uno de los ciclos for debera llegar desde el valor 1 hasta su limite 500.

- Para demostrar que existe un triple de pitagoras en una de las iteraciones de los 3 ciclos for anidados usaremos una sentencia **If**:
    ~~~
    if l1*l1 + l2*l2 == h*h:
    ~~~
    Donde utilizando la ecucacion ***l<sup>2</sup> * l<sup>2</sup> = h<sup>2</sup>*** que nos dice que la suma de los catetos al cuadrado debera ser igual a la hipotenusa, quien es el lado mas grande. 

- Si la anterior sentencia se cumple por demostracion de la cantidad de intentos, agregaremos con la variable anteriormente llamada **contador**, un contador que agregue +1 a su valor por cada intento realizado de manera correcta:
   ~~~
   contador += 1;
   ~~~

- Si la anterior sentencia no es correcta entonces, pasara de esta manera:
    ~~~
    else:
        pass
    ~~~
- Por ultimo para obtener la cantidad de intentos acertados realizamos una diferencia de esta manera:
   ~~~
   dif = contador - 500;
   ~~~
### Codigo Fuente
~~~
'''
Triples de pitagoras
'''
from  colorama import init,Fore,Back,Style
import colorama
init()
colorama.init(autoreset = True)
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
name = input(Fore.BLACK + Style.BRIGHT + Back.WHITE + 'Buen dia por favor ingrese su nombre ->')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

print(Fore.MAGENTA + Style.BRIGHT + Back.WHITE + 'Bienvenid@', Fore.RED + Style.BRIGHT + Back.WHITE + name)
for i in range(6+1):
    void=6-i
    print( Fore.YELLOW + Style.BRIGHT + ' '*void+'#'*i)

print(Fore.MAGENTA + Style.BRIGHT + ' A continucacion se mostrara un ejemplo de fuerza bruta computacional con triples de pitagoras en: ', '[','500',']', 'intentos')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

contador = 0;
# evaluar de rango 1 hasta 500 cero h = 0  es 0 no hay h
for l1 in range(1,500):#para l1 1 en rango 0 hasta 500-1
    for l2 in range(1 , 500):#para l2 en rango de l1+1 hasta limite
        for h in range(1, 500):#para h en rango l2+1 o l1+1+1 hasta limite + 1
                
                 if l1*l1 + l2*l2 == h*h:
                    contador += 1;
                    print( Fore.RED + Style.DIM + 'El cateto adyacente es:', Fore.BLACK + Style.BRIGHT + '[',l1, Fore.BLACK + Style.BRIGHT + ']', Fore.RED + Style.NORMAL +'El cateto opuesto es:', Fore.BLACK + Style.BRIGHT + '[',l2, Fore.BLACK + Style.BRIGHT + ']',Fore.RED + Style.BRIGHT+ 'Donde su hipotenusa es:', Fore.BLACK + Style.BRIGHT + '[',h, Fore.BLACK + Style.BRIGHT+ ']',Fore.MAGENTA + Style.BRIGHT+ 'Registrado en intento numero',Fore.BLACK + Style.BRIGHT + '{',contador, Fore.BLACK + Style.BRIGHT + '}')
                 else:
                    pass
                
                
dif = contador - 500;
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print(Fore.MAGENTA + Style.DIM + Back.WHITE + 'En un rango de-> ','500 intentos' , Fore.RED + Style.BRIGHT + Back.WHITE +'contiene-> ',dif, Fore.BLUE + Style.BRIGHT + Back.WHITE +'triples de pitagoras')
print(Fore.MAGENTA + Style.DIM + Back.WHITE + 'Ten un lindo dia: ', Fore.RED + Style.BRIGHT + Back.WHITE + name)
for i in range(6+1):
   print(Fore.YELLOW + Style.BRIGHT + '^' * i)
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
~~~
### Video
[Triple de pitagoras: Python](https://youtu.be/rdc-HpfA9bw)
***

# ***Documentacion Externa : Primer Proyecto, Triple De Pitagoras en C++***


 *Primero debemos de agregar nuestras librerias a utilizar las cuales serian:*
 
 * **Iostream**
 
 * **windows.h**

*Seguido de esto agregados la estrucruta basica de c++*

![Esta es una imagen de ejemplo ](https://image.slidesharecdn.com/estructurabsicadeunprogramaendevc-140605195118-phpapp02/85/estructura-bsica-de-un-programa-en-c-2-320.jpg?cb=1402013714)

**De la siguiente manera empezamos con nuestro programa el cual requiere triple de pitagoras**

*Declaramos nuestras variables*

* hipote
* cateA
* cateO

**Utilizando la estructura de control for** 

*Requerimos utilizar un for triplemente anidado para nuestro programa, dichas variables estarian declaradas dentro del for*

## Ejemplo
***

### *for (int hipote = 1; hipote <=500; hipote++)*

*De esta manera cada ciclo debe iterar hasta 500,cada ciclo for debe de cumplir con su funcion la cual seria que empieza con dicho valor de 1 hasta 500*

**Este metodo seria un ejemplo de la computacion de fuerza bruta**

#### Seguido de este proceso para comprobar un triple de pitagoras utilizamos dicha formula**

*(A²+B²=C²)*

## Ejemplo
****

###  *if(cateA*cateA + cateO*cateO == hipote**hipote)

*Utilizamos un if para comprobar si  la suma de dichos catetos al ² son iguales ala Hipotenusa ya que la hipotenusa posee el valor mas grande  A²+B²==C²*

*si esta condicion se cumple obtendremos nuestras tiples de pitagoras.* 
### Codigo fuente
~~~
#include <iostream>

using namespace std;
 
int main(){
   
  cout<< " ********** "<<endl;
  cout<<" TRIPLE DE PITAGORAS "<<endl;
  cout<< " ********** "<<endl;
  cout<<" "<<endl;
  cout << " ** cate.A ** fila1 * " <<endl;
  cout<<" "<<endl;
  cout << " ** cate.O ** fila2 * " <<endl;
  cout<<" "<<endl;
  cout << " ** Hipote ** fila3 * " <<endl;
  cout<<" "<<endl;
  cout << " ** Resul **  fila4 * "<< endl;

  for (int hipote = 1; hipote*hipote <= 500; hipote++) {
    for(int cateA = 1; cateA < hipote; cateA++)
      for(int cateO = 1; cateO < hipote; cateO++)  
        if (hipote*hipote == cateA*cateA + cateO*cateO)

          cout << "(" << cateA << "," << cateO  <<","  << hipote<<")="<<hipote*hipote<<endl;
  
  }
  
  return 0;
}
~~~
### Video
[Triple de pitagoras: C++](https://youtu.be/SmiuiDtsB7I)

**Referencias bibliograficas de apoyo**
1. [Referencia euclides: triples pitagoricos](https://euclides.org/triples-pitagoricos/)
2. [Wikipedia: Terna pitagorica](https://es.wikipedia.org/wiki/Terna_pitag%C3%B3rica)
***

##  Ahorcado: C++

## ***¿Que es el juego del ahorcado?***
*El ahorcado es un juego de adivinazas, en el cual el jugador 1 piensa una palabra o frase y el jugador 2 debera adivinar, El jugador 1 indica por medio de guiones (-) la cantidad de letras que tiene la palabra o frase. El jugador 2 debera ir diciendo letra por letra hasta adivinar la palabra o frase, pero unicamente tiene 6 vidas.*

## **PASO 1**
## Librerias para que nuestro programa funcione

        iostream

        cstdlib

        string.h

        ctime

        windows.h

Agregamos la funcion **define color SetConsoleTextAttribute** para darle color a las letras.

Ademas agregamos el comando using namespace std; para poder ver resultados en pantalla.

## **PASO 2**
Dentro de la funcion principal **int main** declaramos las variables a utilizar:

 Nota: A algunas variables les asignamos valor.

 | TIPO | VARIABLE      | VALOR |
 | ---- | :------:      | :---: |
 | INT  |  i,j          |       |
 | INT  |  opcion       |       |
 | INT  |  longitud     |       |
 | INT  |  espacios     |       |
 | INT  |  puntos       |  12   |
 | INT  |  aciertos     |   0   |
 | INT  |  vidas        |   0   |
 | char |  letra        |       |
 | char |  PalabraOculta|       |

Ademas declaramos un **Array** de tipo **char** con 10 palabras, el cual funcionara como base de datos para generar una palabra aleatoria.

Con la función **rand** generamos una palabra aleatoria desde el array.

Con la función **strlen** tomamos el tamaño de letras de la palabra generada aleatoriamente.

Con estructura de control **for** y la variable **i** sustituimos cada una de las letras de la palabra aleatoria por **guiones(-)**.

## **PASO 3**

Con la estructura de control **do while** desarrollamos lo necesario para que nuestro programa funcione y cumpla con los lineamientos solicitados. Dentro de esta estructura tambien utilizamos las estructuras de control **for** e **if**

Agregamos la funcion system("cls") para que nos limpie la pantalla durante el juego.

Indicamos en pantalla una pista extra la cual es: **ADIVINA EL LENGUAJE DE PROGRAMACION**

Indicamos el numero de vidas con las que cuenta el jugados, VIDAS = 6

Indicamos el número de puntos con los que cuenta el jugado, PUNTOS = 12

Con la estructura de control **for** imprimimos en pantalla el número de guiones equivalente a la cantidad de letras de la palabra generada aleatoriamente.

Con un ciclo **if** verificamos si el jugador perdio la partida y le indicamos cual era la palabra a adivinar

Iniciamos la variable **espacios** y le asignamos valor **0**, y verificamos que si dentro de la palabra aun existe un espacio(-) y si lo existe eso significa que aun no has adivinado la palabra.

Con un ciclo **if** verificamos que si no hay espacios en la palabra es porque ha sido adivinada y le indicamos al jugador que ha ganado y lo felicitamos.

Solicitamos al usuario que ingrese una letra mayuscula. 

Con una estructrua de control **For** comprobamos que si la letra ingresada corresponde a la palabra y reemplaza el guion por la letra.

Con un ciclo **if** realizamos el proceso para que los puntos se resten en menos 2 por cata vida perdida.

Finalizamos el **while** con vidas=7



### Codigo fuente
~~~
#include <iostream>
#include <cstdlib>
#include <string.h>
#include <ctime>
#include <windows.h>
#define color SetConsoleTextAttribute

using namespace std;

int main(){
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	int i,j;
	int opcion;
	int longitud;
	int espacios;
	int puntos = 12; 
	int aciertos = 0;
	int vidas = 0;
	char letra;
	char lenguajes[20][25] = {"PYTHON", "C++", "OBJETIVEC", "JAVA","JAVASCRIPT", "PHP", "SWIFT","HTML", "MATLAB", "TYPESCRIPT"};
	
	srand(time(NULL));
	opcion = rand() % 10; //Se genera palabra aleaotria 
	longitud = strlen(lenguajes[opcion]); //tamaño de la palabra 
	char PalabraOculta[longitud];
	for(i=0; i < longitud; i++){//Proceso para cambiar las letras de la palabra por guiones
		PalabraOculta[i] = '-';
	}
	do{
		aciertos = 0;
		system("cls");
		color(hConsole, 14);
		cout<<"    .:.:.:.:.:.:.:.:.:.:.:.:.:.:.:"<<endl<<endl;
		cout<<"          JUEGO EL AHORCADO"<<endl<<endl;
		cout<<"    .:.:.:.:.:.:.:.:.:.:.:.:.:.:.:"<<endl<<endl<<endl;
		color(hConsole, 3);
		cout<<"   ADIVINA EL LENGUAJE DE PROGRAMACION"<<endl<<endl;
		color(hConsole, 2);
		cout<<"   VIDAS: "<<6-vidas<<endl;
		cout<<"   PUNTOS: "<<puntos<<endl;
		
		cout<<"\n\n\n";
		for(i=0; i < longitud; i++){
			color(hConsole, 4);
			cout<<"   "<<PalabraOculta[i];
		}

		if (vidas == 6){
			color(hConsole, 11);
			cout<<"\n\n           PERDISTE :("<<endl<<endl;
			cout<<"   EL LENGUAJE DE PROGRAMACION ERA: "<<lenguajes[opcion]<<endl<<endl<<endl;
			color(hConsole, 7);
			system("pause");
			return 0;	
		}
		
		espacios=0;//Proceso que comprueba si has adivinado la palabra
	
		for (i = 0; i < longitud; i++){
			if (PalabraOculta[i] == '-')//Si en la palabra aun existe un guion es porque aun no has adivinado la palabra
				espacios++;
		}
			
		if (espacios == 0){
			color(hConsole, 6);
			cout<<endl<<endl<<"      ADIVINASTE!!"<<endl<<endl;
			cout<<"  FELICIDADES HAS GANADO  :)"<<endl<<endl<<endl;
			color(hConsole, 7);
			system("pause");
			return 0;
		}
		
		color(hConsole, 3);
		cout<<"\n\n\n   ESCRIBE UNA LETRA MAYUSCULA: ";
		cin>>letra;
			  
		for (j = 0; j < longitud; j++){           //Comprueba se la letra ingresada existe en la palabra y replaza el guion por la letra.
			if (letra == lenguajes[opcion][j]){
				PalabraOculta[j] = letra;
				aciertos++;
			}	
		}	
		if (aciertos == 0){
			vidas++;	
			puntos -= 2;//Se restan 2 puntos por cada vida perdida
		}
				
	}while(vidas != 7);
	
}
~~~
### Video
[Ahorcado:C++](https://youtu.be/mvG1udP0xQo)
***
##  Ahorcado: Python
 
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
 Por ultimo seria validar con la condicion *if*
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

### Codigo Fuente
~~~
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

~~~
### Video
[Ahorcado: Python](https://www.youtube.com/watch?v=pahuZ3zNNn0&ab_channel=VictorMacario)
***

