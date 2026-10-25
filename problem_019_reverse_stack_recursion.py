def push_at_bottom(stk, elem):
    if len(stk) == 0:
        stk.append(elem)
        return
    top_val = stk.pop()
    push_at_bottom(stk, elem)
    stk.append(top_val)

def invert_stack(stk):
    if len(stk) == 0:
        return
    current_top = stk.pop()
    invert_stack(stk)
    push_at_bottom(stk, current_top)

stack_data = [1, 2, 3, 4]
invert_stack(stack_data)
print(stack_data)
