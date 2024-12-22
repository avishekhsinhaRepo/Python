def user_choice():
    is_invalid_choice = True
    while is_invalid_choice:
        choice = input("Enter your choice (1-10): ")
        if choice.isdigit() and 1 <= int(choice) <= 10:
            is_invalid_choice = False
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


print(user_choice())