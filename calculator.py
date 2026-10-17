from pyfiglet import Figlet
f=Figlet(font='ogre')
print(f.renderText('Miller Calculator'))

operator=input("Enter your operator(+,*,-,/,% ):")
num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
if operator=="+":
    result=(num1+num2)
    print(result)
elif operator=="-":
    result=(num1-num2)
    print(result)
elif operator=="*":
    result=(num1*num2)
    print(result)
elif operator=="/":
    result=(num1/num2)
    print(round(result,3))
else:
    result=(num1%num2)
    print(round(result,3))