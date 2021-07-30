from math import *
s=10
while s>1:
  try:
    sqr="square"
    sqt="square root"
    print("please type which operation you want to perform. square or square root?")
		
	    
    opr=str(input())
		
    if opr==sqr:
	  try:
	     print("Type the number ")
	     num=int(input())
	     num1=num*num
	     print('square of %f is %f'%(num,num1)
 
	   except:
	     print("error! please type number.")
     elif opr==sqt:
	    try:
	       print("Type the number ")
	       num2=int(input(""))
	       num3=sqrt(num2)
	       print("square root of %d is %d"%(num2,num3)
	     except:
	       print("error")
  except:
    print("error")
