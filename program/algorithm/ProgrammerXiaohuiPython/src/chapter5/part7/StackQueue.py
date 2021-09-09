class StackQueue:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def en_queue(self, element):
        self.stackA.append(element)

    def de_queue(self):
        if len(self.stackB) == 0:
            if len(self.stackA) == 0:
                raise Exception("栈已经空了 !")
            self.transfer()
        return self.stackB.pop()

    def transfer(self):
        while len(self.stackA) > 0:
            self.stackB.append(self.stackA.pop())


stack_queue = StackQueue()
stack_queue.en_queue(1)
stack_queue.en_queue(2)
stack_queue.en_queue(3)
print(stack_queue.de_queue())
print(stack_queue.de_queue())
stack_queue.en_queue(4)
print(stack_queue.de_queue())
print(stack_queue.de_queue())

