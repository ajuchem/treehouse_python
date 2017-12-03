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
""")

def show_list():
	clear_screen()
    # print out the list
    print("Here is your list:")
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to list
    shopping_list.append(new_item)
    print("Added! List now has {} items.".format(len(shopping_list)))
    show_list()

show_help()

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()
