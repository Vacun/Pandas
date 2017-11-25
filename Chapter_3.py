nested_tup = (4, 5), (1, 5, 7)

tup = tuple(['foo', [1, 2], True])

# even though the tuples are immutable, we can mutate the content of
# elements, if their are mutable on their on term

# for example, i can append another number to the second element of
# the tuple above, because it is a list and lists are mutable

tup[1].append(44)

print(tup)

# unpacking

a, b = 1, 2

# if I want to swap variable names, i can do the following

b, a = a, b

# a comman use of variable unpacking is iterating over sequences of
#  tuples or lists

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in seq:
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))

# "pluck" a few elements from the begining of the tuple

values = 1,2,3,4,5

a,b, *rest = values

#  OR better yet

a,b, *_ = values

# useful methos is .count()

a = (1,1,1,2,1,2,5,4,5,5,3,4,5)

a.count(3)


# LIST

# ADDING and REMOVING elements

b = 'foo','bar','baz'

b_list = list(b)

b_list[1] = 'peekaboo'

b_list.append('dwarf')

b_list.insert(1,'red')

# .insert is computationally expensive, if I need to add an item
# to both begining and the end of a list, i should look into 
# collections.deque, a double-ended queue, for this purpose.

# inverse operation of .insert is .pop which removes and returns an 
# element at a particular index

b_list.pop(2)

print(b_list)

print('dwarf' in b_list)

'dwarf' not in b_list,


# Concatinating and combining lists

x = [4, None, 'foo']
x.extend([7,8,(2,3)])
print(x)

# List concatination by addiyion is a comparatively expencive operations
# since a new list has to be created and the objects copied over.
# Use .extend(list) to append elements to an existing list.