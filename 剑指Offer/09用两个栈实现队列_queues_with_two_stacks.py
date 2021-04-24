# Implement two functions: appendTail and deleteHead
# Input：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# Output：[null,null,3,-1]

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

# Tip: Append stack1 to stack2 and then pop() when deleteHead.

class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2: return self.stack2.pop()
        
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2.pop()


