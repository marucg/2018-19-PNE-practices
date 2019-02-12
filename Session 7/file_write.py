# Example of reading a file located (ALWAYS EXPLAIN WHAT I'M DOING IN THE FILE)
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

f = open(NAME, 'a')
# USE THE FUNCTION f.write(self, s) or just do it normal
f.write('\nWRITE IS A TEXT EXAMPLE FOR ADDING TO MY FILE')
f.close()
