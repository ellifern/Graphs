class Stack:

  def __init__(self, size):
    self.stack_array = [None] * size
    self.top_pointer = -1

  def push(self, new_item):
    if self.top_pointer == len(self.stack_array):
      print("Stack is full=", self.top_pointer, "values.")
    else:
      self.top_pointer += 1
      self.stack_array[self.top_pointer] = new_item


  def pop(self):
    stack_array.pop(self.top_pointer)