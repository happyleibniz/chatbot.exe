import time


def print_with_delay(text, delay=0.0001):
    for char in str(text):
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
