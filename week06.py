from queue import Queue

q = Queue()
q.put("Database")
q.put("Data Structure")
q.put("Java Script")
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
# print(q.size, q.front, q.rear)
# print(q.dequeue()) raise IndexError