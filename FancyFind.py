#Write a function called fancy_find. fancy_find should have
#two parameters: search_within and search_for.
#
#fancy_find should check if search_for is found within the
#string search_within. If it is, it should print the message
#"[search_for] found at index [index]!", with [search_for]
#and [index] replaced by the value of search_for and the
#index at which it is found. If search_for is not found
#within search_within, it should print, "[search_for] was
#not found within [search_within]!", again with the values
#of search_for and search_within.
#
#For example:
#
#  fancy_find("ABCDEF", "DEF") -> "DEF found at index 3!"
#  fancy_find("ABCDEF", "GHI") -> "GHI was not found within ABCDEF!"


#Add your function here!
def fancy_find(search_within,search_for):
    s = search_within.find(search_for)
    if search_within.find(search_for) >= 0:
        return("{} found at index {}!".format(search_for,s))
    else:
        return("{} was not found within {}!".format(search_for,search_within))


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#DEF found at index 3!
#GHI was not found within ABCDEF!

print(fancy_find("ABCDEF", "DEF"))
print(fancy_find("ABCDEF", "GHI"))



sample answer



def fancy_find(search_within, search_for):
    
    #Now, there are two ways we could do this. We could use
    #the in operator to check if search_for is within
    #search_within, and if it is, then find its index.
    #
    #However, the find() method will return -1 if search_for
    #is not found in search_within anyway, and that's all
    #we need for our conditional. So, first we use the
    #find() method and save the index:
    
    index = search_within.find(search_for)
    
    #If search_for was found, that means index will be a
    #positive number. So, if it's a number greater than or
    #equal to 0...
    
    if index >= 0:
        
        #...then we return that the string was found! Because
        #index is an integer, we need to convert it to a
        #string to concatenate it with the other strings:
        
        return search_for + " found at index " + str(index) + "!"
    
    else:
        
        #If index wasn't greater than or equal to 0, then that
        #means search_for was not found in search_within. So,
        #we return that message instead:
        
        return search_for + " was not found within " + search_within + "!"



print(fancy_find("ABCDEF", "DEF"))
print(fancy_find("ABCDEF", "GHI"))
