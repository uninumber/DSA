def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    return print("Pushed: " + item)

def  pop(stack):
    if check_empty(stack):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
print("Popped item: " + pop(stack))
print("stack after popping an element:" + str(stack))

