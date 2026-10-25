class CustomMinStack:
    def __init__(self):
        self.items = []
        self.minima = []

    def push(self, val):
        self.items.append(val)
        if not self.minima or val <= self.minima[-1]:
            self.minima.append(val)

    def pop(self):
        if not self.items:
            return None
        removed = self.items.pop()
        if removed == self.minima[-1]:
            self.minima.pop()
        return removed

    def get_min(self):
        return self.minima[-1] if self.minima else None

stack_instance = CustomMinStack()
stack_instance.push(3)
stack_instance.push(5)
stack_instance.push(2)
print(stack_instance.get_min())
stack_instance.pop()
print(stack_instance.get_min())
