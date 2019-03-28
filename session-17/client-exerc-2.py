import http.client
import json
import termcolor

PORT = 8004
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
person = json.loads(data1)

print("CONTENT: ")


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

