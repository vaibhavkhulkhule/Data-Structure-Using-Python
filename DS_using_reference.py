'''
Description      :  Data Structure Using Reference 
Function Date    :  07 Feb 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

print ('\n Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

mylist = shoplist # mylist is just another name pointing to the same object!

del shoplist[0] # I purchased the first item, so I remove it from the list

print ('\n shoplist is', shoplist)
print (' mylist is', mylist)

# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object

print ('\n Copy by making a full slice')

mylist = shoplist[:] # Make a copy by doing a full slice

del mylist[0] # Remove first item

print ('\n shoplist is', shoplist)
print (' mylist is', mylist)

# Notice that now the two lists are different

print("\n")