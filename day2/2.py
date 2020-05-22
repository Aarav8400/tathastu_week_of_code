# fibonacci series upto nth number------------------------

num=int(input('enter a number upto what you want\n'))
a=0       
b=1
count=2
if num==0:
    print('for n=0 it is ',a)
elif num<0:
    print('please enter a positive number')
elif num==1:
    print('for n=1 it is ',a)
else:
    print(a,b, end=",")
    while count<num:
        c=a+b
        print(c,end=",")
        a,b=b,c
        count = count+1
