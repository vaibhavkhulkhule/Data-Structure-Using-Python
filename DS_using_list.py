'''
Description      :  Data Structure Using List 
Function Date    :  06 Feb 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

# This is my shopping list

shoplist = [' Apple', ' Mango', ' Potato', ' Banana'] # We Create The List First

print ('I have', len(shoplist), 'Items To Purchase...') # Display Total Number Of Vegatables To Buy (4)
print ('\n These Items Are : '), # So Display It

for item in shoplist:
    print (item), # Here It Display

print ('\n I Have To Buy Rice...') # I Want To Buy One More Grocery

shoplist.append('rice') # Added Rice Last Of The Shoping List

print ('\n My Shopping List Is Now', shoplist) # Display The Shoping List
print ('\n I Will Sort My List Now...') # Sort The List By Name A-Z

shoplist.sort() # Here It's Short

print ('\n Sorted Shopping List Is', shoplist) # Then Again Display The Shorted Shoping List
print ('\n First Item I Will Buy Is ..', shoplist[0]) # So List Is Sorted So I Buy First Apple

olditem = shoplist[0]
del shoplist[0] # Cancel Apple From The Shoping List

print ('\n So I Bought ..', olditem) # I Got It (Apple)
print ('\n My Shopping List Is Now', shoplist) # Display The Remaining Shoping List For Buying