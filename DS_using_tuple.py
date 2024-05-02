'''
Description      :  Data Structure Using Tuple 
Function Date    :  06 Feb 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

zoo = ('Python', 'Elephant', 'Penguin') # Animals Of Old Zoo
print ('Number Of Animals In The Zoo Is', len(zoo)) # All Animals In New Zoo

new_zoo = 'Monkey', 'Camel', zoo # Animals Of New Zoo
print ('Number Of Cages In New Zoo Is', len (new_zoo) ) 
print ('All Animals In New Zoo Are', new_zoo)
print ('Animals Brought From Old Zoo Is', new_zoo [2] )
print ('Last Animal Brought From Old Zoo is', new_zoo [2] [2] ) # From Last Zoo
print ('Number Of Animals In New Zoo Is', \
    len(new_zoo) - 1 + len(new_zoo [2] ))