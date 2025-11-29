


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Give me name and phone please."
    return inner



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


@input_error
def add_contact(arguments, contacts):
    """
    Функція створює новий запис у словник contacts:
    name(key): phone(value).

    Якщо передана неправильна команда, повертається "Error: please provide name and phone."
    Якщо все передано правильно, повертається "Contact added." і запис додається в словник. 

    """
    name = arguments[0]
    phone = arguments[1]
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(arguments, contacts):
    """
    Функція оновлює новий запис у словнику contacts:
    name(key): phone(value).

    Якщо передана неправильна команда, повертається "Error: please provide name and phone."
    Якщо за вказаним іменем name не знайдено запису в словнику, повертається "Contact not found."

    Якщо все передано правильно, повертається "Contact updated." і запис оновлюється в словнику.

    
    """
    name = arguments[0]
    phone = arguments[1]
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(arguments, contacts):
    """
    Функція повертає номер телефону за іменем (повертає value по вказаному key).

    Якщо передана неправильна команда, повертається "Error: please provide a name."
    Якщо за вказаним іменем name не знайдено запису в словнику, повертається "Contact not found."

    Якщо все передано правильно, повертається номер телефону, який відповідає вказаному імені.

    """
    name = arguments[0]
    return contacts[name]

@input_error
def show_all(contacts):

    """
    Функція повертає всі контакти (пари name:phone) зі словника contacts.

    Якщо записів немає, повертається "The contact book is empty."
    
    """
    if not contacts:
        return "The contact book is empty."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


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
            print(add_contact(arguments, contacts))

        elif command == "change":
            print(change_contact(arguments, contacts))

        elif command == "phone":
            print(show_phone(arguments, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()