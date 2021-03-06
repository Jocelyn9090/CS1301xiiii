def string_length(text):
    
    #All we need to do here is return a tuple where the first
    #item is text, and the second is len(text). We could
    #store len(text) in a separate variable, or we can create
    #it right in the tuple definition:
    
    return (text, len(text))


print(string_length("Hello, world!"))
print(string_length("CS1301"))
print(string_length("Some people pronounce it 'toople'. Others pronounce it 'tuhple'. Either is correct."))



