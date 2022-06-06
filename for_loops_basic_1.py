# 1.
for i in range(0, 151):
    print(i)
#prints all integers from 0 to 150, inclusive

# 2.
for i in range(5, 1001, 5):
    print(i)
#prints all multiples of 5 from 5 to 1000, inclusive

# 3.
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
#prints all integers from 1 to 100, inclusive
#replacing multiples of 10 with "Coding Dojo" and just multiples of 5 with "Coding"

# 4.
sum = 0
for i in range(0, 500001):
    if i % 2 != 0:
        sum += i
print("The sum of the odds from 0 to 500,000 is", sum)
#prints the sum of all odd integers from 0 to 500000 by running all integers
#between 0 and 500001 through a conditional checking for odds
#a more efficient way to do this might be like below
#by starting at 1, you take out the conditional statements, and iterating by 2 takes half as long
sum = 0
for i in range(1, 500001, 2):
    sum += i
print("The sum of the odds from 0 to 500,000 is", sum)

# 5.
for i in range(2018, 0, -4):
    print(i)
#loop starts at 2018, goes down by 4 until it hits 0

# 6.
lowNum = 2
highNum = 9
mult = 3

if lowNum % mult != 0:
    for i in range (lowNum - (lowNum % mult) + mult, highNum + 1, mult):
        print(i)
else:
    for i in range(lowNum, highNum + 1, mult):
        print(i)
#prints all multiples of mult in the range from lowNum to highNum
#This works regardless of the values of mult, lowNum, and highNum