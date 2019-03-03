from stack import Stack


def check_brackets(text) -> bool:
    stack = Stack()
    for c in text:
        if c == '(':
            stack.push(c)
        elif c == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


s1 = "(())()()(((())))"
s2 = "(()"
print(check_brackets(s1))
print(check_brackets(s2))
