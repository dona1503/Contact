#Python Program to create a repository of my classmate’s name and mobile number’s and search it out from the repository

# this function will contain the repository
def initial_repository():
    phone_book = [["K Yadav", 6206450948], ["Dona Dutta", 9832998537], ["Arghya Dutta", 6296912074], ["Anirban Roy", 1234567890],["Rohan Chakraborty", 9876543210], ["Esha Dey", 9832906230],["M Yadav", 6306350048], ["Dora Dutta", 9832199537], ["Arya Dutta", 9474192646], ["B Roy", 1234767890],["Rohini Chakraborty", 9866243210], ["E Dey", 9812904230]]

    return phone_book


# this function will print the menu
def menu():
    print("\nEnter 1 to search for a contact using name/number")
    print("Enter 2 to search multiple contact's number")
    print("Enter 3 to display all contacts")
    print("Enter 4 or any other number to exit")
    choice = int(input("\nPlease enter your choice: "))
    return choice


# this function will search for the contacts
def search(pb):
    choice = int(input("\nEnter search criteria\n\n1. Name\n2. Number\nPlease enter: "))

    temp = []
    check = -1

    if choice == 1:
	# This will execute for searches based on contact name
        query = str(input("\nPlease enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    elif choice == 2:
	# This will execute for searches based on contact number
        query = int(input("\nPlease enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
    else:
        print("\nInvalid search criteria")
        return -1
	# returning -1 indicates that the search was unsuccessful
	

    if check == -1:
        return -1
		# returning -1 indicates that the query did not exist in the directory
    else:
        display_all(temp)
        return check


# this function will extract numbers of multiple contacts
def multi_search(pb):
    temp = []

    f=int(input("\nPlease enter the number of contacts you want to search: "))
    # this will take the number of contacts needed for the "for loop"

    print("\nPlease enter the name of the contacts you wish to search")

    for j in range(f):    
        query = input(f"Contact {j+1} : ")

        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i][1])

    display_all(temp)
    

# this function will print the menu
def display_all(pb):
    for i in range(len(pb)):
        print(f"Contact {i+1} : {pb[i]}")
    print()


def thanks():
# A simple gesture of courtesy towards the user to enhance user experience
	print("********************************************************************\n")
	print("Thank you for using our application.")
	print("Please visit again!\n")
	print("********************************************************************")



# Main function code
print("....................................................................\n")
print("\t\t\tContact Repository\n\nHello dear user, welcome to our application")
print("You may now proceed to explore this repository\n")
print("....................................................................")
# This is solely meant for decoration purpose only.

ch=1
pb = initial_repository()
while ch in (1, 2, 3):
    ch = menu()
    if ch == 1:
        d = search(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 2:
        multi_search(pb)
    elif ch == 3:
        display_all(pb)
    else:
        thanks()
        break
