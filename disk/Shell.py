import os


def handle_shell_command():
    while True:
        command = input("\n# ")
        if command == "ls":
            files_and_directories = os.listdir("/")
            _counter = 0
            for item in files_and_directories:
                print(item, end="    ")
                _counter += 1
                if _counter == 9:
                    print("\n")
                    _counter = 0
