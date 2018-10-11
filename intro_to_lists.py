my_list=[1,2,3]

new_list=["hello", 100, 23.2]

print(len(my_list))
# prints 3 since there are 3 things in my list

print(new_list)
# prints out new_list and shows that we have can have different data types
# all in the same list

print(new_list[1])
# prints out 100 since thats is the second value in my list AKA indexing

print(new_list[0:3])
print(new_list[0:])
# both print out the entire list AKA slicing

# we can also concatinate lists
list_2=[4,5,6]
print(my_list+list_2)
