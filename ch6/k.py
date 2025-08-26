a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
total_percent = (100)*(a+b+c)/300
if(total_percent>=40):

  print("pass")
elif(total_percent>=30):
  print("just pass")
else:
  print("fail")