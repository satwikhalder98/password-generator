import random
from random import shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
a=int(input("enter number of letters you want in the password"))
b=int(input("enter number of symbols you want in the password"))
c=int(input("enter the number of numbers you want in the password"))
password=""
for i in range(1,a+1):
    v=random.choice(letters)
    password=password+v

for  i in range(1,b+1):
    w=random.choice(numbers)
    password=password+w

for i in range (1,c+1):
    x=random.choice(symbols)
    password=password+x
     
l = list(password)
random.shuffle(l)
y = ''.join(l)
print(f"your new password is {y}")


    
