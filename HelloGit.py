# comment
print("Hello, World!")
a = 6 # variables
b = 5
print (a+b)

# how to make a list
myList = [1,2,3,4,3,2,1]

# how to stride
print(myList[0:6:2]) # from index 0 to 6, skip by 2

# strings are just lists
phrase = 'Catch the Dog'
phrase[2] # t
phrase[4] # h
phrase[-1:0:-3] #strides work backwards, -1 is right, 0 is middle, -3 is left

# how to access elements to a list
print(myList[1])

# how to write a function
def sumFunction(a,b):
	return a + b

# how to call a function
print(sumFunction(2,20))
x = 10
y = -10

# blocks of code
if(x==10):
	x = 5
elif(y==-10):
	y = 5
else:
	x = y - x
# loop
mylist = [1,3,8,412,43,2,20]

# lnegth of list
len(mylist)

# while
x = 0
while(x < 5):
          x += 1
          print ("x+ =" + str(x))

# for loop by index
for i in range(len(mylist)):
	print(mylist[i])

# for each loop
for val in mylist:
	print(val)

# dictionaries
lookup = {}
lookup['kc'] = 'chiefs'
lookup['ne'] = 'patriots'
