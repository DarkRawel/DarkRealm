# utils

import time

def slow(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()