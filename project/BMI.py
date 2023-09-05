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