import json
import termcolor

#Has to be exactly like this
#in the file i click copy path
#go to the web a paste it

f = open("person.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person = json.load(f)

length = len(person['users'])
print()
print('Total people in the database', length)
for a, human in enumerate(person['users']):
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(human['Firstname'], human['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(human['age'])

# Get the phoneNumber list
    phoneNumbers = human['phoneNumber']

    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])