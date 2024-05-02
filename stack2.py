# Python Program To Perform Various Operations On A Stack Using Stack Class

'''
Function Name    :  Perform Various Operations On A Stack Using Stack Class
Function Date    :  1 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

from stack import Stack

# Create Empty Stack Object

s = Stack()

# Display Menu

choice = 0
while choice < 5:
    print('\n STACK OPERATIONS')
    print('1 Push Element')
    print('2 Pop Element')
    print('3 Peep Element')
    print('4 Search For Element')
    print('5 Exit')
    choice = int(input('\n Your Choice : '))
    
    # Perform A Task Depending On User Choice
    
    if choice == 1:
        element = int(input('\n Enter Element : '))
        s.push(element)
        
    elif choice == 2:
        element = s.pop()
        if element == -1:
            print('\n The Stack Is Empty')
        else:
            print('\n Popped Element = ', element)
            
    elif choice == 3:
        element = s.peep()
        print('Topmost Element = ', element)
        
    elif choice == 4:
        element = int(input('\n Enter Element : '))
        pos = s.search(element)
        if pos == -1:
            print('\n The Stack Is Empty')
        elif pos == -2:
            print('\n Element Not Found In The Stack')
        else:
            print('Element Found At Position : ', pos)
            
    else:
        break
    
    # Display The Contents Of Stack Object
    
    print('Stack = ', s.display())
    