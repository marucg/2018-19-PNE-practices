# Example of reading a file located
# in our local filesystem

NAME = 'mynotes.txt'

#Open file

#Creating an OBJECT -myfile-
myfile = open(NAME, 'r')
print('File opended: ', myfile)
# other way to call it - print('File opened: {}'.format(myfile.name)
contents = myfile.read()
print('The file contents are: ', contents)
# 'The file contents are: {}'.format(contents)

myfile.close()