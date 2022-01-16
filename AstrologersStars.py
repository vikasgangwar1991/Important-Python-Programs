#Pattern Programming
N=int(input("Enter no. of rows:"))
bool_var=bool(int(input("Enter 0 for false and 1 for true:")))
if bool_var==True:
   i=1
   while i<=N:
       j=1
       while j<=i:
           print('*',end="")
           j+=1
       i+=1
       print()
elif bool_var ==False :
    i=N
    while i>=1:
        j=1
        while j<=i:
            print("*",end=" ")
            j+=1
        i-=1
        print()




