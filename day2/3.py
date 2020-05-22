i=0
j=6
for row in range(7):
    for col in range(7):
        if col==i or col==j:
            print('*',end="")
        else:
             print("  ",end="")
    print("\n")
    i=i+1
    j=j-1
