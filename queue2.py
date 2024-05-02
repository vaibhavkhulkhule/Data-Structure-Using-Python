# Python Program To Perform Some Operations On A Queue

'''
Function Name    :  Perform Some Operations On A Queue
Function Date    :  1 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

from queue1 import Queue

q = Queue() # Create Empty Queue Object

# Display Menu

choice = 0
while choice < 4:
    print('\n QUEUE OPERATIONS')
    print('1 Add Elements')
    print('2 Delete Elements')
    print('3 Search For Elements')
    print('4 Exit')
    choice = int(input('Your Choice : '))
    
    # Perform A Task Depending On User Choice
    
    if choice == 1:
        element = float(input('\n Enter Element : '))
        q.add(element)
        
    elif choice == 2:
        element = q.delete()
        if element == -1:
            print('\n The Queue Is Empty')
        else:
            print('Removed Element = ', element)
            
    elif choice == 3:
        element = float(input('\n Enter Element : '))
        pos = q.search(element)
        if pos == -1:
            print('\n The Queue Is Empty')
        elif pos == -2:
            print('\n Element Not Found In The Queue')
        else:
            print('Element Found At Position : ', pos)
            
    else:
        break
    
    # Display the contents of queue object
    
    print('Queue = ', q.display())
            