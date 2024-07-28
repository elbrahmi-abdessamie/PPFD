# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)
llst =[1,2,1,3]
myit = iter(llst)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# print('The filtered letters are:')
# for s in filtered:
#     print(s)
