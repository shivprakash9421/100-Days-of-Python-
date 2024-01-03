# BREAK & COUNTINUE STATEMENTS

for x in range(15):
    print("7 x ",x,"=",7*(x))
    if (x==10):
        break 

for x in range(12):
    if (x==10):
        print("skip the itration")
        continue
    print("5 x ",x,"=",5*(x)) 

x=0
while (x<100):        # we can also write while True 
    print(x)
    x=x+1
    if(x%15 == 0):
        break



for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("done")
print("Thank you")


#DO-WHILE LOOP IN PYTHON

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
    




    