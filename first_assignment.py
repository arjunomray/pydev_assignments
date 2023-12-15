'''First Assignment'''

def create_task():
    print("\nTask Created\n")

def edit_task(s:str):
    print(f"\nEditing task : {s}\n")

def desc_task(s:str):
    print(f"\nThis is the task about: {s}\n")

def remove_task(s:str):
    print(f"\nDeleting this task: {s}\n")

while True:
    print("What do you wanna do:")
    choice = int(input("\n1.Create\n2.Edit\n3.Describe\n4.Delete\n5.Exit\n\n"))

    if choice == 1:
        create_task()
        continue

    elif choice == 2:
        edit_task("My task")
        continue

    elif choice == 3:
        desc_task("My task")
        continue

    elif choice == 4:
        remove_task("My task")
        continue
    elif choice == 5:
        print("Thanks you using, bye :)")
        break

    else:
        print("Enter valid input:")



