from string import punctuation
from random import sample
from calendar import monthrange


def decimalTobin(x):
  print(f"{x} en binario es {bin(x)}")
def tiketsCost(ages):
  if ages <= 2:
    print("Costo de ticket : 0")
  elif ages in range(3,13):
    print("Costo de ticket : 14000")
  elif ages in range(13,62):
    print("Costo de ticket : 25000")
  else:
    print("Costo de ticket : 18000")


def yearToAnimal(x):
  mono = []
  año=0
  for i in range (0,x+1):
    año+=12
    mono.append(año)
    
  if  mono.count(x) == 0:
    print("no")
  

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
    print(f"{n} No es un número de Fibonacci")
  else:
    print(f"{n} Si es un número de Fibonacci")





def shapeType(x):
  if x == 3:
    print("triángulo")
  elif x == 4:
    print("cuadrilátero")
  elif x == 5:
    print("pentágono")
  elif x == 6:
    print("hexágono")
  elif x == 7:
    print("heptágono")
  elif x == 8:
    print("octágono")
  elif x == 9:
    print("eneágono")
  elif x == 10:
    print("decágono")
  else:
    print("None")

def isStrongPassword(password):
 
  if len(password)>=8:
    if any([i.isdigit() for i in password]):
      if any([i.islower() for i in password]):
        if any([i.isupper() for i in password]):
          if any([True if i in punctuation else False for i in password]):
            print(f"La contraseña {password} = True(es segura)")
            return True

  print(f"La contraseña {password} = False(No es segura)")
  return False
  
  


  

def median(a,b,c):
  lista = []
  lista.append(a)
  lista.append(b)
  lista.append(c)
  lista.sort()
  print(f"la mediana es : {lista[1]}")
def randomPassword(size):
  password = ""
  ascii = []
  for i in range(33,127):
    ascii.append(chr(i))  
  password = "".join(sample(ascii,size))
  print(f"{password} Es la contraseña de {size} caracteres") 






def daysInMonth(year,month):
  print (f"Cantidad de días: {monthrange(year,month)[1]}")
  





def Main():
  decimalTobin(5)
  tiketsCost(62)
  isFibonacci(53453)
  shapeType(5)
  isStrongPassword("A123-")
  median(18,6,4)
  randomPassword(9)
  daysInMonth(2003,12)



