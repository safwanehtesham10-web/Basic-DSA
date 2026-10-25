def validate_parentheses(expression):
    stk = []
    mapping = {')': '(', '}': '{', ']': '['}
    for bracket in expression:
        if bracket in mapping.values():
            stk.append(bracket)
        elif bracket in mapping:
            if not stk or stk.pop() != mapping[bracket]:
                return False
    return not stk

print(validate_parentheses("{[()]}"))
