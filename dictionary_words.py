"""# opens the file
readMe = open('my_file.txt', 'r')

# reads whole file as list
print(readMe.readlines())

# reads single line
print(readMe.readline())


# reads the file as it is 
# print(readMe.read())
readMe.close()

"""
# reading the file line by line using for loop
with open('my_file.txt', 'r') as my_file:
    count = - 1
    for line in my_file:
        count += 1
        print(line)
    count += 1
    print('\nThe number of counts: {}'.format(count))

# def file_len(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass
#     return i + 1

# print(file_len(my_file))
