def parse_input(user_input):
    """
    Функція перетворює інформація від користувача (input) на список elements.
    Потім розділяє його на команду та аргументи.
    
    Аргументи:
    user_input - інформація від користувача.

    Повертає:
    cmd, arguments - відповідно команда та аргументи; перший та всі наступні елементи списку elements.

    """
    elements = user_input.split()
    cmd = elements[0].strip().lower()   
    arguments = elements[1:]             
    return cmd, arguments

def add_contact(arguments, contacts):
    name=arguments[0]
    phone=arguments[1]
    contacts[name]=phone
    return "Contact added."

def change_contact(arguments, contacts):
    name=arguments[0]
    phone=arguments[1]
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone(arguments, contacts):
    name=arguments[0]
    if name not in contacts:
        return "Contact not found."
    phone=contacts[name]
    return phone

def show_all(contacts):
    all_contacts=[]
    for name, phone in contacts.items():
        all_contacts.append(f"{name}: {phone}")
    return "\n".join(all_contacts)
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, arguments = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(arguments) < 2:
                print("Error: please provide name and phone.")
                continue
            print(add_contact(arguments, contacts))

        elif command == "change":
            if len(arguments) < 2:
                print("Error: please provide name and phone.")
                continue
            print(change_contact(arguments, contacts))

        elif command == "phone":
            if len(arguments) < 1:
                print("Error: please provide a name.")
                continue
            print(show_phone(arguments, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
