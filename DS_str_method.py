'''
Description      :  Data Structure Using String Method 
Function Date    :  07 Feb 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

# This is a string object

name = 'prasad'

if name.startswith('pra'):
    print ('Yes, the string starts with "pra"')

if 'a' in name:
    print ('Yes, it contains the string "a"')

if name.find('sad') != -1:
    print ('Yes, it contains the string "sad"')

delimiter = '_*_'
mylist = ['USA', 'Russia', 'India', 'UAE']
print (delimiter.join(mylist))