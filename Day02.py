import math

#part 1
'''
#parse txt file into a list
with open('input2.txt') as fp:
    myInput = fp.read()
    myList = myInput.split(",")
    myList = list(map(int, myList))
#print(myList)



#make initial data clean
myList[1] = 12
myList[2] = 2

#run solution
i = 0

while myList[i] != 99:
    print('**** START OF NEW LOOP ****')
    if myList[i] == 1:
        x = myList[i+1]
        y = myList[i+2]
        z = myList[i+3]
        print('i = ', i)
        print('value at index: ', myList[i])
        print('x: ', x ,'; y: ', y ,'; z: ', z)
        print('value at x: ', myList[x])
        print('value at y: ', myList[y])
        print('value at z: ', myList[z])
        a = myList[x] + myList[y]
        b = myList[z]
        print('a: ', a)
        print('b: ', b)
        myList.insert(b,a)
        b += 1
        print('new b: ', b)
        del myList[b] 
        print('updated list: ', myList)
        i += 4 
    elif myList[i] == 2:
        x = myList[i+1]
        y = myList[i+2]
        z = myList[i+3]
        print('i = ', i)
        print('value at index: ', myList[i])
        print('x: ', x ,'; y: ', y ,'; z: ', z)
        print('value at x: ', myList[x])
        print('value at y: ', myList[y])
        print('value at z: ', myList[z])
        a = myList[x] * myList[y]
        b = myList[z]
        print('a: ', a)
        print('b: ', b)
        myList.insert(b,a)
        b += 1
        print('new b: ', b)
        del myList[b] 
        print('updated list: ', myList)
        i += 4

print('Final list:')
print(myList)
print('Part 1 answer: ', myList[1])        
'''
## correct answer is 3790689, but it is showing up at index 1 not index 0....

#### why is the last instance not working???


#part 2

#parse txt file into a list
with open('input2.txt') as fp:
    myInput = fp.read()
    myList = myInput.split(",")
    myList = list(map(int, myList))
#make initial data clean
myList[1] = 12
myList[2] = 2

l = 19690720


for m in range(0, 100):
    for n in range(0, 100):
        with open('input2.txt') as fp:
            myInput = fp.read()
            myList = myInput.split(",")
            myList = list(map(int, myList))
        myList[1] = m
        myList[2] = n
        print(m,n)
#run solution
        i = 0
        while myList[i] != 99:
            
            if myList[i] == 1:
                x = myList[i+1]
                y = myList[i+2]
                z = myList[i+3]
                '''print('i = ', i)
                print('value at index: ', myList[i])
                print('x: ', x ,'; y: ', y ,'; z: ', z)
                print('value at x: ', myList[x])
                print('value at y: ', myList[y])
                print('value at z: ', myList[z])'''
                a = myList[x] + myList[y]
                b = myList[z]
                '''print('a: ', a)
                print('b: ', b)'''
                myList.insert(b,a)
                b += 1
                '''print('new b: ', b)'''
                del myList[b] 
                #print('updated list: ', myList)
                i += 4 
            elif myList[i] == 2:
                x = myList[i+1]
                y = myList[i+2]
                z = myList[i+3]
                #print('i = ', i)
                #print('value at index: ', myList[i])
                '''print('x: ', x ,'; y: ', y ,'; z: ', z)
                print('value at x: ', myList[x])
                print('value at y: ', myList[y])
                print('value at z: ', myList[z])'''
                a = myList[x] * myList[y]
                b = myList[z]
                '''print('a: ', a)
                print('b: ', b)'''
                myList.insert(b,a)
                b += 1
                '''print('new b: ', b)'''
                del myList[b] 
                '''print('updated list: ', myList)'''
                i += 4
                #print(l,myList[0])
            elif myList[i] != 1|2:
                print('Huston, we ran into a {} problem' .format(myList[i]))
                i += 4
        if myList[1] == l:
            print('Noun = ', m,'; Verb = ', n)
        #print(myList)

'''print('Final list:')
print(myList)
print('Part 1 answer: ', myList[0])    '''



# I am not sure what is going wrong with the program but it is puting an 8 in a operator index and if I skip it, then at 2,66 there is a out of range error