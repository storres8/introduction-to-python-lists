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
# prints out a new list [1,2,3,4,5,6]
# concatination is non-mutatable. We still have the old variables saved as how
# they origionally were

# we can also mutate lists simply by indexing the value we want to change
list_3=[2,4,6]
list_3[0]=1
print(list_3)
# origionally the first index was a 2, but now it's 1 becuase we changed the
# value inside of the list
# we directly MUTATED the list

# We can also add to the end of the list through the .append() method
list_4=[1,2,5]
list_4.append(6)
print(list_4)
# prints [1, 2, 5, 6] since we MUTATED the list by appending 6 to the end

list_5=["hello", "world"]
list_5.pop()
print(list_5)
# prints ['hello']
# .pop() method removes the last item in the list
# .pop() can also take an argument of the index of the item you wish to remove

list_6=["removed", "this", "word"]
list_6.pop(1)
print(list_6)
# prints ['removed', 'word'] because we specified to removes the second index


list_7=[1,6,8,3,4]
list_7.sort()
print(list_7)
# prints the sorted list [1, 3, 4, 6, 8]
# .sort() OCCURS IN-LINE and has a return value of nothing
# meaning its automatucally saved to the original varaible that you used

list_8=[9,8,7,6,5]
list_8.reverse()
print(list_8)
# prints [5, 6, 7, 8, 9]
