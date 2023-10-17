records = {}


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Use help."
        except KeyError:
            return "Unknown rec_id. Try another or use help."
        except ValueError:
            return "Give me name and phone please"
    return inner


@user_error
def add_record(*args):
    rec_id = args[0].capitalize()
    rec_value = int(args[1])
    records[rec_id] = rec_value
    return f"Add record {rec_id = }, {rec_value = }"


@user_error
def change_record(*args):
    rec_id = args[0].capitalize()
    new_value = int(args[1])
    rec = records[rec_id]
    if rec:
        records[rec_id] = int(new_value)
        return f"Change record {rec_id = }, {new_value = }"


def hello():
    return "How can I help you?"

@user_error
def phone(*args):
    user_name = args[0].capitalize()
    if user_name in records:
        return records[user_name]
    else:
        return "Contact not found"


def show_all():
    if records:
        return "\n".join([f"{rec_id.capitalize()}: {rec_value}" for rec_id, rec_value in records.items()])


def exit_program():
    return "Good bye!"   
        

def unknown(*args):
    return "Unknown command. Try again."



COMMANDS = {add_record: "add",
            change_record: "change",
            show_all: "show all",
            hello: "hello",
            phone: "phone",
            exit_program: ["close", "exit", "good bye"]
            }


def parser(text: str):
    text = text.lower()
    for func, kw in COMMANDS.items():
        if isinstance(kw, list):
            for keyword in kw:
                if text == keyword:
                    return func, []
        else:
            if text.startswith(kw):
                return func, text[len(kw):].strip().split()
    return unknown, []


def main():
    while True:
        user_input = input(">>>")
        func, data = parser(user_input)
        result = func(*data)
        print(result)
        if result == "Good bye!":
            break
        
        
        
if __name__ == '__main__':
    main()