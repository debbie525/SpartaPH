''''
Descending Order

Your task is to make a function that can take any non-negative integer 
as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.


'''
#def descending(mynum):
num = input('Please enter an integer:')
print(num)

num_list = []
for item in num:
    num_list.append(int(item))
print(num_list)
descend=sorted(num_list, reverse=True)
print(descend)


for item in descend:
    print(item)


