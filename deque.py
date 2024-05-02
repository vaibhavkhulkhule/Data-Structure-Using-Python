# Python Program To Create And Use Deque

'''
Function Name    :  Create And Use Deque Operations
Function Date    :  1 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

from collections import deque

d = deque() # Create An Empty Deque

choice = 0
while choice < 7:
    print('\n DEQUE OPERATIONS')
    print('1 Add Elements At Front')
    print('2 Remove Element At Front')
    print('3 Add Element At Rear')
    print('4 Remove Element At Rear')
    print('5 Remove Element In The Middle')
    print('6 Search For Elements')
    print('7 Exit')
    choice = int(input('\n Your Choice : '))
    
    # Perform A Task Depending On User Choice 
    
    if choice == 1:
        element = input('\n Enter Elements : ')
        d.appendleft(element)
        
    elif choice == 2:
        if len(d) == 0:
            print('Deque Is Empty')
        else:
            d.popleft()
            
    elif choice == 3:
        element = input('\n Enter Element : ')
        d.append(element)
        
    elif choice == 4:
        if len(d) == 0:
            print('Deque Is Empty')
        else:
            d.pop()
            
    elif choice == 5:
        element = input('\n Enter Element : ')
        try:
            d.remove(element)
        except ValueError:
            print('Element Not Found')
            
    elif choice == 6:
        element = input('\n Enter Element : ')
        c = d.count(element)
        print('No Of Times The Element Found : ', c)
    else:
        break
    
    # Display The Deque Element Using For Loop
    
    print('Deque = ', end = '')
    for i in d:
        print(i , ' ', end = '') 
        print() # Move Cursor To Next Line