our_list = [] # create empty list


for i in range(0, 3): # set up loop to run 10 times
    number = int(input('Please enter a number: ')) # prompt user for number
    our_list.append(number) # append to our_list
 
print(max(our_list))