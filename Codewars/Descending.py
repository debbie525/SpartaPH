''''
Descending Order

Your task is to make a function that can take any non-negative integer 
as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.


'''
#def descending(mynum):
num = input('Please enter an integer:')
print('Your number is: ' + num)

num_list = []
for item in num:
    num_list.append(int(item))
#print(num_list)
descend_list=sorted(num_list, reverse=True)

#print(descend_list)

final_output = ''
for item in descend_list:
    final_output += str(item)
print ('Sorted in Descending Order: ' + final_output)



