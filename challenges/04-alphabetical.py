# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sort_string(string):
    new_string = ('').join(sorted(string))
    return new_string

print(sort_string("hello"))
print(sort_string("supercalifragilisticexpialidocious"))