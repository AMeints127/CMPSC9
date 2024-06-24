class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
        # alters python list method, removes from top and returns the item

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
