import sys
import time

class CustomPrint:
    def __init__(self, text):
        self.text = text

    def custom_print(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()