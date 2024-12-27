#lab test (priogram 1:)
upper=0
lower=0
n=input('enter the string=')
for i in n:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
        
print('upper case count is:',upper)
print('lower case count is:',lower)
#(program 2:)
#Temperature Conversion
print("Enter 'c' to convert from Celsius to Fahrenheit")
print("Enter 'f' tp convert from Farenheit to Celsius")
choice=input("Enter Your Choice:")
if choice=='c':
    celsius=float(input("Enter temperature in celcius:"))
    farenheit=(celsius*9/5)+32
    print('%.2f Celcius is:%0.2f Farenheit'%(celsius,farenheit))
elif choice=='f':
    farenheit=float(input('Enter temperature in Frenheit:'))
    celsius=(farenheit-32)*5/9
    print('%.2f Farenheit is:%0.2f Celcius'%(farenheit,celsius))
else:
    print('Invalid input')
    print('the convertion completed')
    
