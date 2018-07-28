# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False
    
def process_input(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char == '(' or char == '[' or char == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(char,i))

        if char == ')' or char == ']' or char == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) ==0:
                print(i+1)
                return
            last_open = opening_brackets_stack.pop()
            if (last_open.bracket_type == '(' and char !=')') or (last_open.bracket_type == '[' and char !=']') or (last_open.bracket_type == '{' and char !='}'):
                print(i+1)
                return
    # Printing answer, write your code here
    if len(opening_brackets_stack) ==0:
        print("Success")
    else:
        print(opening_brackets_stack.pop().position+1)
    return
if __name__ == "__main__":
    text = sys.stdin.read()
    process_input(text)