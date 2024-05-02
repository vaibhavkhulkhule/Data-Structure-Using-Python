# Python Program To Create A Linked List And Perform Operations On The List

'''
Function Name    :  Create A Linked List And Perform Operations On The List
Function Date    :  1 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

# Create An Empty Linked List

Linkedlist = []

# Add Some String Type Elements In Linkedlist

Linkedlist.append("India")
Linkedlist.append("America")
Linkedlist.append("Japan")

# Display The List

print("\n The Existing List = ", Linkedlist)

# Display Menu

choice = 0
while choice < 5:
    print('LINKED LIST OPERATIONS')
    print('\n 1 ADD ELEMENTS')
    print('2 REMOVE ELEMENTS')
    print('3 REPLACE ELEMENTS')
    print('4 SEARCH FOR ELEMENTS')
    print('5 EXIT')
    choice = int(input('\n Your Choice : '))
    
    # Perform A Task Depending On User Choice
    
    if choice == 1:
        element = input('\n Enter Elements : ')
        pos = int(input('At What Position ? '))
        Linkedlist.insert(pos, element)
        
    elif choice == 2:
        try:
            element = input('\n Enter Elements : ')
            Linkedlist.remove(element)
        except ValueError:
            print('\n Element Not Found')
            
    elif choice == 3:
        element = input('\n Enter Elements : ')
        pos = int(input('At What Position ? '))
        Linkedlist.pop(pos)
        Linkedlist.insert(pos, element)
        
    elif choice == 4:
        element = input('\n Enter Elements : ')
        try:
            pos = Linkedlist.index(element)
            print('Element Found At Position : ', pos)
        except ValueError:
            print('\n Element Not Found')
    
    else:
        break
    
    # Display The List Elements
    
    print('List = ', Linkedlist)
    print("\n")    
    