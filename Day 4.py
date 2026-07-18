tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Task Add Karein")
    print("2. Sab Tasks Dekhein")
    print("3. Task Delete Karein")
    print("4. Exit")
    
    choice = input("Apna option chunein (1-4): ")
    
    if choice == "1":
        new_task = input("Naya task likhein: ")
        tasks.append(new_task)
        print(f"'{new_task}' add ho gaya!")
    
    elif choice == "2":
        if len(tasks) == 0:
            print("Abhi koi task nahi hai.")
        else:
            print("Aapke Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif choice == "3":
        task_num = int(input("Konsa task number delete karna hai? "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"'{removed}' delete ho gaya!")
        else:
            print("Galat number, dobara try karein.")
    
    elif choice == "4":
        print("Allah Hafiz! Program band ho raha hai.")
        break
    
    else:
        print("Galat option, 1-4 mein se chunein.")