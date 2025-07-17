fruit = "Mango"
       # flow  =   0  1  2  3  4
# reverse flow =  -5 -4 -3 -2 -1
mangoLen = len(fruit)
print(mangoLen) # 5
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5]) # if not assumed, assune it as [0:5]
print(fruit[0:-3]) # taken as from [0:2]
print(fruit[:len(fruit)-3]) # taken as from [0:2]
print(fruit[-1:len(fruit) - 3]) # taken as from [4,2]
#Rule of Slicing: Python tries to go from the start index up to (but not including) the end index by stepping forward one character at a time,but not backwards by default.
print(fruit[-3:-1]) # takes as [2:4]
print(fruit[-4:-2]) # taken as [1:3]

# Quick Quiz:
nm = "Harry"
# flow = 01234
# reverse flow = -5-4-3-2-1
print(nm[-4:-2])




