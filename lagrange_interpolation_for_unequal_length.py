#Interpolation for Unequal Interval length
#Lagrange's Interpolation Method

#Input
a=[]
s=""
loop=0
print("Enter x and y value in format x y separated by space and E to exit")
while(s!="E"):
    print(loop," ",end="")
    s=input()
    if(s=="E"):
        continue
    loop+=1
    ta=[float(item) for item in s.split()]
    a.append(ta)
    ta=[]
print("Enter x whose y has to be calculated")
x=float(input())  #x corresponding y that we need to find


#Main calculation
y=float(0)
for i in range (len(a)):
    mulx=float(1)
    muly=float(1)
    for j in range (len(a)):
        if(i==j):
            mulx=mulx*a[j][1]
            continue
        mulx=mulx*(x-a[j][0])
        muly=muly*(a[i][0]-a[j][0])
    y=y+(mulx/muly)
print("y = ",y)

#Example Question
#[[5,12],[6,13],[9,14],[11,16]]
#10

#Deeptimaan Banerjee
