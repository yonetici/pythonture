
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([aa for aa in a if aa < 5])


"""
A list comprehension behaves like this: [output] for [item] in [list] if [filter]

As you can see there are 4 components in its syntax:
output, item, list and filter.

In the case of Sachin's code [aa for aa in a if aa < 5]:

output = aa
item = aa
list = a
filter = aa < 5

What this means is that I'm outputting the variable 'aa' which refers to each item in the list (a).

Since 'aa' is set to refer to each item in list (a), the output will print the items in list (a). However, I also have a filter specified at the end of the code "if aa < 5".

This means that only the items in the list (referred to as aa) that are below 5 are printed out.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))

new_list = []

for i in a:
    if i < num:
        new_list.append(i)

print (new_list)


fruits = ["banana", "orange", "pinapple", "banana"]

print([object for object in fruits if object == "banana"])

#This would return "banana" 2 times, since there is a total of two objects called "banana" in the list "fruits".


number = int(input("Enter a number"))

def divisor():
    y = []
    x = range(number, 60)
    for item in x:
        if item % number == 0:
            y.append(item)
    print(y)
        
divisor()