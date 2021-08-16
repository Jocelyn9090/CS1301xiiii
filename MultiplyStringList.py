#Write a function called multiply_strings. Multiply
#strings should have one parameter, a list of strings.
#It should return a modified list according to the
#following changes:
#
# - Every string stored at an even index should be
#   doubled.
# - Every string stored at an index that is a multiple
#   of 3 should be tripled.
# - Every other string should remain unchanged.
#
#These changes should "stack": the string stored at index
#6 should be duplicated six times (2 * 3).
#
#Then, return the new list. You may assume that 0 is a
#multiple of 2 and 3.
#
#Hint: To do this, you need to modify the values of the
#list using their indices, e.g. a_list[1]. If you're not
#using their indices, your answer won't work!


#Write your function here!

def multiply_strings(test):
    if len(test) > 0:
        test[0] *= 6
        for i in range(1, len(test)):
            k = 1
            if i % 2 == 0:
                k *= 2
            if i % 3 == 0:
                k *= 3
            test[i] *= k
    return test

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#['AAAAAA', 'B', 'CC', 'DDD', 'EE', 'F', 'GGGGGG']
test_list = ["A", "B", "C", "D", "E", "F", "G"]
print(multiply_strings(test_list))




sample answer

def multiply_strings(a_list):
    
    #So, we need to go through each item in the list.
    #However, we're going to need to modify each item. That
    #means we need to modify them by their index. If we use
    #a for-each loop like for item in a_list, then the
    #change we make will only apply to the variable item:
    #it won't carry over to the list itself.
    #
    #So, we need a for loop over the range:
    
    for i in range(0, len(a_list)):
        
        #Note that this is a place where zero-indexing helps
        #keeps things simpler: we go from 0 to the length of
        #the list. The length of the list is one greater than
        #the index of the last item because of zero-indexing,
        #and the for loop stops one item short of the length
        #of the list. So, this simple loop covers all the
        #items.
        #
        #Next, we need to look at the index. First, if it's
        #even, we multiply it by two:
        
        if i % 2 == 0:
            a_list[i] *= 2
            
        #Then, if it's a multiple of 3, we multiply it by
        #3:
        
        if i % 3 == 0:
            a_list[i] *= 3
        
        #Notice we're not using elif here because the problem
        #said these effects should 'stack': if we used elif,
        #only one could ever run.
        
    #Then, finally, we return the result. Notice again that
    #this return is *outside* the loop: we only want to return
    #once all these changes are made and the loop is done
    #running:
    
    return a_list


test_list = ["A", "B", "C", "D", "E", "F", "G"]
print(multiply_strings(test_list))


