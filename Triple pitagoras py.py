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
