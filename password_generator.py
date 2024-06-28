import random

letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
         "A","B","C","D","E","F","I","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","@","#","$","%","^","&","*","(",")","+","-","_","=","[","]","{","}","|",".",",","?","/","<",">"]
        
num_letters=int(input("enter the numbers of letters needed in your password:\n"))
if num_letters>0:
    print("the size is ok")
else:
    print("enter the numbers greater than 0")


num_numbers=int(input("enter the numbers of numbers needed in your password:\n"))
if num_numbers<=0:
    print("enter the numbers greater than 0")
else:
    print("the size is ok")
num_symbols=int(input("enter the numbers of symbols needed in your password:\n"))
if num_symbols<=0:
    print("enter the numbers greater than 0")
else:
    print("the size is ok")
password_list=[]

for i in range(0,num_letters+1):
    chr=(random.choice(letters))
    password_list+=chr

for i in range(0,num_numbers+1):
    chr=random.choice(numbers)
    password_list+=chr
for i in range(0,num_symbols+1):
    chr=(random.choice(symbols))
    password_list+=chr
random.shuffle(password_list)
password=""
for i in password_list:
    password+=i


if len(password)>=8:
    print("password length is ok")
    print(password)
else:
    print("password is too short hence try to enter the size of letters,numbers and symbols again")
    quit()






