# opens the file
readMe = open('my_file.txt', 'r')

# reads whole file as list
print(readMe.readlines())

# reads single line
print(readMe.readline())


# reads the file as it is 
# print(readMe.read())
readMe.close()