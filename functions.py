from string import punctuation
from random import sample
from calendar import monthrange

from graphics import contenido


def decimalTobin(x):
  return(f"{x} en binario es {bin(x)}")
def tiketsCost(ages):
  if ages <= 2:
    return("Costo de ticket : 0")
  elif ages in range(3,13):
    return("Costo de ticket : 14000")
  elif ages in range(13,62):
    return("Costo de ticket : 25000")
  else:
    return("Costo de ticket : 18000")


def yearToAnimal(x):
  mono = []
  año=0
  for i in range (0,x+1):
    año+=12
    mono.append(año)
    
  if  mono.count(x) == 0:
    return("no")
  

def isFibonacci(n):
  
  fib = []
  a = 0
  b = 1

  for i in range(10000):
    c = a + b
    a = b
    b = c
    fib.append(c)
    
  if fib.count(n)==0:
    return(f"{n} No es un número de Fibonacci")
  else:
    return(f"{n} Si es un número de Fibonacci")





def shapeType(x):
  if x == 3:
    return("triángulo")
  elif x == 4:
    return("cuadrilátero")
  elif x == 5:
    return("pentágono")
  elif x == 6:
    return("hexágono")
  elif x == 7:
    return("heptágono")
  elif x == 8:
    return("octágono")
  elif x == 9:
    return("eneágono")
  elif x == 10:
    return("decágono")
  else:
    return("None")

def isStrongPassword(password):
 
  if len(password)>=8:
    if any([i.isdigit() for i in password]):
      if any([i.islower() for i in password]):
        if any([i.isupper() for i in password]):
          if any([True if i in punctuation else False for i in password]):
            print(f"La contraseña {password} = True(es segura)")
            return True

  return(f"La contraseña {password} = False(No es segura)")
  
  


  

def median(a,b,c):
  lista = []
  lista.append(a)
  lista.append(b)
  lista.append(c)
  lista.sort()
  return(f"la mediana es : {lista[1]}")

def randomPassword(size):
  password = ""
  ascii = []
  for i in range(33,127):
    ascii.append(chr(i))  
  password = "".join(sample(ascii,size))
  return(f"La contraseña aleatoria de 9 caracteres es : {password}") 






def daysInMonth(year,month):
  return (f"Cantidad de días: {monthrange(year,month)[1]}")
  





def Main():
  decimalTobin(5)
  tiketsCost(62)
  isFibonacci(53453)
  shapeType(5)
  isStrongPassword("A123-")
  median(18,6,4)
  print(randomPassword(9))
  daysInMonth(2003,12)
  contenido(randomPassword(9))
  



