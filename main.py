from art import logo
from replit import clear
print(logo)
def sum(first,second):
  return first+second
def sub(first,second):
  return first-second
def mul(first,second):
  return first*second
def div(first,second):
  return first/second
def cal():
  first=float(input("What is the first number ?: "))
  print("+")
  print("-")
  print("*")
  print("/")
  operation=input("Pick a operation:")
  second=float(input("What's the next number ?:"))
  if(operation=="+"):
    result=sum(first,second)
    print(f"{first} + {second} = {result}")
  elif(operation=="-"):
    result=sub(first,second)
    print(f"{first} - {second} = {result}")
  elif(operation=="*"):
    result=mul(first,second)
    print(f"{first} * {second} = {result}")
  elif(operation=="/"):
    result=div(first,second)
    print(f"{first} / {second} = {result}")
  newcal=True
  while newcal==True:
    new=input(f"Type 'y' to continue calculating with {result} ,or type 'n' to start a new calculation  ").lower()
    if(new=="y"):
      operation=input("Pick a operation:")
      third=float(input("What's the next number ?:"))
      if(operation=="+"):
        r1=sum(result,third)
        print(f"{result} + {third} = {r1}")
      elif(operation=="-"):
        r2=sub(result,third)
        print(f"{result} - {third} = {r2}")
      elif(operation=="*"):
        r3=mul(result,third)
        print(f"{result} * {third} = {r3}")
      elif(operation=="/"):
        r4=div(result,third)
        print(f"{result} / {third} = {r4}")
    else:
      clear()
      cal()
cal()