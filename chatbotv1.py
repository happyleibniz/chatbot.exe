import random
import sys
import time
from disk.responses import *
from disk.the_bruh_dictionary import *
from disk.python_codes import *
from disk.chatgpt_dictionary import *
from disk.Shell import *
from disk.commands import *  # Assuming you have a file containing your commands
from disk.print_delay import print_with_delay as print_with_delay
from disk.converter import handle_converter_command
from disk.essay_gpt import essay_gpt_dict


# Function to evaluate a mathematical expression
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError as e:
        return "∞"
    except SyntaxError as e:
        return str(expression)[1:]  # Use 'e' instead of 'result' and access the error message using 'str(e)'
    except SyntaxWarning as e:
        pass
    # ValueError,NameError,SyntaxWarning


# Main chat loop
print("Hello! I'm your chatbot. Type 'bye' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input == '':
        print("WARNING<!>request rejected:no user entered")
        continue  # Skip the rest of the loop if no user input
    if user_input.lower() == 'bye':
        print_with_delay("Goodbye!")
        break
    # Check for specific commands
    if user_input.lower() == "/converter":
        handle_converter_command()
        continue  # Skip the rest of the loop to avoid further processing
    elif user_input.lower() == "/shell":
        handle_shell_command()
        continue
    if "what is the value of" in user_input.lower():
        expression = user_input.lower().replace("what is the value of", "").strip()
        try:
            response = evaluate_expression(expression)
        except ZeroDivisionError:
            response = "∞"
    elif "what is" in user_input.lower():
        expression = user_input.lower().replace("what is", "").strip()
        try:
            response = evaluate_expression(expression)
        except ZeroDivisionError:
            response = "∞"
    elif any(op in user_input for op in "+-*/"):
        try:
            response = evaluate_expression(user_input)
        except ZeroDivisionError:
            response = "∞"
    else:
        response = responses.get(user_input.lower())
        if response == "EX3mple)(*&^%":
            response = random.choice(python_codes)
        elif response == "*&^%$#@*&^%$#the bruh dictionary":
            response = random.choice(the_bruh_dictionary)
        elif response == "@$#^$#%&$^$#&#$&#%$chatgpt":
            response = random.choice(gpt_dictionary)
        elif response == "jiof$#%@#$%@#$%@$%@#$%@#$":
            response = random.choice(essay_gpt_dict)
        elif response is None:
            print_with_delay("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIJust don't know what you're saYinG")
    if response is not None:
        print_with_delay(response, delay=0.006)
