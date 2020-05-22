# checking number is even or odd..........................

num=int(input('enter a number to check even or odd'))
if num%2==0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

#  check palindrome........................

temp=num
nm=num
rev=0
while(num>0):
    dg=num%10
    rev=rev*10+dg
    num=num//10
if temp==rev:
    print(f'{temp} is palindrome')
else:
    print(f'{temp} is not a palindrome')


# check armstrong--------------------------------------------------------

sum=0
while temp>0:
    dg=temp%10
    sum=sum+dg**3
    temp=temp//10
if nm==sum:
    print(f'{nm} is armstrong')
else:
    print(f'{nm} is not an armstrong number')
