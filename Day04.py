# Part 1 --- Answer 1873

# set inputs
a = 136760
b = 595730
z = 0 # the output
# print(a)

# want to loop through all numbers and then check it at the end if it meets the criteria
for i in range(136760,595730):
    x = 0 # setting x to count up and determine if the number meets rule 1 by determining if x = 5
    y = 0 # setting y to count up and determine if the number meets rule 2 by determining if y = 1
    for a in range (0,5):
        number = str(i)
        if number[a] <= number[a+1]:
            #print('hurray')
            #print(number[a], number[a+1])
            x += 1
            #print(b)
            if x == 5:
                # print(i)
                for b in range (0,5):
                    if number[b] == number[b+1]:
                        y += 1
                        if y == 1:
                            #print(i)
                            z += 1
print(z)


# part 2
'''new rule mean that if there are more than 2 of the same digits next to eachother, they don't count 
(e.g. 111123 shows 4 1's in a row, thus doesn't count, but 111122 does work because it still has 2 2's)'''

# set inputs
a = 136760
b = 595730
c = 0 # the output
# print(a)

# want to loop through all numbers and then check it at the end if it meets the criteria
for i in range(136760,595730):
    x = 0 # setting x to count up and determine if the number meets rule 1 by determining if x = 5
    y = 0 # setting y to count up and determine if the number meets rule 2 by determining if y = 1
    for a in range (0,5):
        number = str(i)
        if number[a] <= number[a+1]:
            #print('hurray')
            #print(number[a], number[a+1])
            x += 1
            #print(b)
            if x == 5:
                # print(i)
                for b in range (0,5):
                    if number[b] == number[b+1]:
                        y += 1
                        if y == 1:
                            #print(i)
                            c += 1
print(c)