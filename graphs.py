class Stack:
  def __init__(self, ):
    self.stack = []

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    if len(self.stack) > 0:
        return self.stack.pop()
    else:
        return IndexError

  def get_size(self):
    return len(self.stack)
