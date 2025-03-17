from heapq import heappop, heappush
class Stack:
  def __init__(self):
    self.stack = []
  def is_empty(self):
    return self.stack == []
  def push(self,item):
    self.stack.append(item)
  def pop(self):
    if self.is_empty():
      raise Exception('Stack is empty')
    return self.stack.pop()
class Queue:
    def __init__(self):
      self.queue = []
    def is_empty(self):
      return self.queue == []
    def enqueue(self,item):
      self.queue.append(item)
    def dequeue(self):
      if self.is_empty():
        raise Exception('Queue is empty')
      return self.queue.pop(0)
class PriorityQueue: # using heapq
    def __init__(self):
      self.queue = []
    def is_empty(self):
      return self.queue ==[]
    def enqueue(self,item,priority):
      heappush(self.queue,(priority,item))
    def dequeue(self):
      if self.is_empty():
        raise Exception('PriorityQueue is empty')
      return heappop(self.queue)