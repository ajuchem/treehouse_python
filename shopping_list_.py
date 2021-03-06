import os

# make a list to hold onto our items
shopping_list = []

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def show_help():
	clear_screen()
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to delete an item from your list.
""")

def show_list():
	clear_screen()
    # print out the list
    print("Here is your list:")

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1
    print("-"*10)

def remove_from_list():
	show_list()
	# remove item from list
	what_to_remove = input("What would you like to remove?\n> ")
	try:
		shopping_list.remove(what_to_remove)
	except ValueError:
		pass
	show_list()


def add_to_list(new_item):
	show_list()
    # add new items to list
    shopping_list.append(new_item)
    print("Added! List now has {} items.".format(len(shopping_list)))

show_help()

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
    	remove_from_list()
    else:
    	add_to_list(new_item)

show_list()
