import random
import sys
import time
from disk.responses import *
from disk.the_bruh_dictionary import *
from disk.python_codes import *
from disk.chatgpt_dictionary import *
from disk.commands import *  # Assuming you have a file containing your commands
from disk.print_delay import print_with_delay as print_with_delay
from disk.converter import handle_converter_command

# Function to evaluate a mathematical expression
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except (SyntaxError, ValueError) as e:
        if str(e) == "SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers":
            result = str(result)[1:]
            return result
        elif "division by zero" in str(e):
            return "∞"


# Function to handle the "/converter" command


# Main chat loop
print("Hello! I'm your chatbot. Type 'bye' to end the conversation.")
response = None
while True:
    user_input = input("You: ")
    if user_input == '':
        print("WARNING<!>request rejected:no user entered")

    if user_input.lower() == 'bye':
        print_with_delay("Goodbye!")
        break

    # Check for specific commands
    if user_input.lower() == "/converter":
        handle_converter_command()
        continue  # Skip the rest of the loop to avoid further processing

    # Check if the user input is a mathematical expression
    if any(op in user_input for op in "+-*/"):
        response = evaluate_expression(user_input)
    else:
        response = responses.get(user_input.lower())
        if response == "EX3mple)(*&^%":
            response = random.choice(python_codes)
        elif response == "*&^%$#@*&^%$#the bruh dictionary":
            response = random.choice(the_bruh_dictionary)
        elif response == "@$#^$#%&$^$#&#$&#%$chatgpt":
            response = random.choice(gpt_dictionary)

    # Check for specific questions
    if "what is the value of" in user_input.lower():
        expression = user_input.lower().replace("what is the value of", "").strip()
        response = evaluate_expression(expression)
    elif "what is" in user_input.lower():
        expression = user_input.lower().replace("what is", "").strip()
        response = evaluate_expression(expression)
    if response is not None:
        print_with_delay(response, delay=0.006)
