print ("""Enter 1 for Addition

         Enter 2 for Substraction

         Enter 3 for multiplication

         Enter 4 for division
  
         Enter 5 for modulodivision""")

ch=int(input("Enter ur choice"))

num1=int(input("Enter first number"))

num2=int(input("Enter second number"))
if ch==1:
    ans=num1+num2
    print ("The answer is:" ,ans)

elif ch==2:
    ans=num1-num2
    print ("The answer is:",ans)

elif ch==3:
    ans=num1*num2
    print ("The answer is:",ans)

elif ch==4:
    ans=num1/num2
    print ("The answer is:",ans)

elif ch==5:
    ans=num1%num2
    print ("The answer is:",ans)

else:

     print "Enter proper choice..."


