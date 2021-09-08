'''
Count the number of digits

'''

number=input('Please input an integer:')
print('Your number is: ' + str(number))

num_list=[]
for item in number:
    num_list.append(item)
    #print(item)
#print(num_list)

count=len(num_list)
print(count)


