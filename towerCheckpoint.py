import collections


class Stack:
    def __init__(self):
        self.deque = collections.deque()

    def push(self, item):
        self.deque.appendleft(item)

    def pop(self):
        return self.deque.popleft()

    def top(self):
        return self.deque[0]

    def len(self):
        return len(self.deque)

tower1 = ['red', 'white', 'blue']

tower2 = []

tower3 = []

def printTowers():
    
    print('tower 1',tower1)

    print('tower2',tower2)

    print('tower3',tower3, '\n')


stack = Stack()

print("here's the start. \n")

printTowers()

tower2.append(tower1[2:])
tower1.pop()

tower3.append(tower1[1:])
tower1.pop()

print("\n here's the set up after the first two moves: \n")

printTowers()

tower3.append(tower2[0:])
tower2.pop()

tower2.append(tower1[0:])
tower1.pop()

print("here's the set up after the next two moves: \n")

printTowers()

tower1.append(tower3[1:])
tower3.pop

tower2.append(tower3[0:])
tower3.clear()
tower1.clear()

print("here's the set up after the next three moves: \n")

printTowers()