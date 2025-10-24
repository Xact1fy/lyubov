import os

def hidden_function():
    os.system('dir < hidden.txt')

    with open("hidden.txt", "w") as file:

        hidden_code = file.write("you found the hidden code! 😁😁😁")
