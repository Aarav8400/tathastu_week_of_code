# run scored by each player

p1=int(input('run scored by p1 on 60 ball\n'))
p2=int(input('run scored by p2 on 60 ball\n'))
p3=int(input('run scored by p3 on 60 ball\n'))
ball=60
# strike_rate of each player

print('strikerate of player 1 is',p1/ball*100)
print('strikerate of player 2 is',p2/ball*100)
print('strikerate of player 3 is',p3/ball*100)

# run scored by each if they played for 60 balls more

print('run scored by player 1 is',p1*2)
print('run scored by player 2 is',p2*2)
print('run scored by player 3 is',p3*2)

# max no of sixes could have by hit by each player is

print('maximum no of 6 could have hit by player 1 is',p1//6)
print('maximum no of 6 could have hit by player 2 is',p2//6)
print('maximum no of 6 could have hit by player 3 is',p3//6)
