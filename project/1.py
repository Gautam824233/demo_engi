print("C")
print('c')
print("5")
print("2.3")
print('25.35')
print("\t 12")
print("\n mh")
#separation
print("hello","world",sep="+")
print("hello","world", sep="+", end="\n")
print("hello")
print("hello","world",sep="+",end="\t")
print("hello")
print("def end=\n")
#replication
print('hello'*5)
#comment
#concanitation
print("hello"+"world")
print("python. session&day2")
str1="python"
str2="session"
str3="day2"
print(str1,'.',end="\t")
print(str2,'&',end =" ")
print(str3)
print("kumar\'s laptop")
print("Gautam Sinha  "*5)
a='hello'
b=5
c=5.5
print(type(a))
print(type(b))
print(type(c))
#print same thing
print('c:\docs\\notation')
print(r'c:\docs\notation')
#for loop
#execute block of code with fixesd number of time,range,string, iterated over,etc
Height=float(input("Enter the Your Height in CM: "))
Weight=float(input("Enter yore weight in kg: "))
Height=Height/100
BMI=Weight/(Height*Height)
print(BMI)
if(BMI>=0):   
    if(BMI<=16):
        print("You are Very Under Weight")
    elif(BMI<=25.5):
        print("You are Under Weight")
    elif(BMI<=30):
        print("You are Healthy")
    else:
        print("Enter Correct Values")

#email Slice
username=str(input("Enter Your User Name: "))
domain=str(input("Enter Your Domain Name: "))
print(username)
print(domain)
email=username+domain
print(email)

email=input("Enter Your Email : ").strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
print(" your User Name is {username}")
print("Your Domail Name Is :")