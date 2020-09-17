"""
--Check for balanced parentheses in an expression--
Given an expression string exp, write a program to examine whether the pairs and the orders of
“{“, “}”, “(“, “)”, “[“, “]” are correct in exp.
"""


def is_balanced(input_str):
    brackets_map = {"(": ")", "{": "}", "[": "]"}
    brackets_map_reversed = dict((value, key) for key, value in brackets_map.items())

    temp_stack_holder = []

    if len(input_str) % 2 != 0:
        # If input is of Odd length then straight away we know its unbalanced
        return False

    for char in input_str:

        if char in brackets_map.keys():
            temp_stack_holder.append(char)

        elif char in brackets_map.values():
            if temp_stack_holder and (brackets_map_reversed[char] == temp_stack_holder[-1]):
                temp_stack_holder.pop()

    return not temp_stack_holder


if __name__ == '__main__':

    balanced_inputs = ["()[]{}", "[]", "([]{})", "([{}])","[()]{}{[()()]()}"]
    unbalanced_inputs = ["][", "(])", "()[}]", "(", ")", "([{}]))"]

    for item in balanced_inputs:
        print(is_balanced(item))
    print('*' * 50)
    for item in unbalanced_inputs:
        print(is_balanced(item))
