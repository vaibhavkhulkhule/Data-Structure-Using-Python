# Python Program To Create A Stack Class That Can  Perform Some Important Operations

'''
Function Name    :  Create Stack Class 
Function Date    :  1 Oct 2020
Function Author  :  Prasad Dangare
Input            :  ----
Output           :  ----
'''

class Stack:
    def __init__(self):
        self.st = []
        
    def isempty(self):
        return self.st == []
    
    def push(self, element):
        self.st.append(element)
    
    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop()
        
    def peep(self):
        n = len(self.st)
        return self.st[n-1]
    
    def search(self, element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.st.index(element)
                return len(self.st)-n
            except ValueError:
                return -2
            
    def display(self):
        return self.st