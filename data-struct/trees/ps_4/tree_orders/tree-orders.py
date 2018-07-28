# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        left = self.left.copy()
        right=self.right.copy()
        stack =[]
        # we want to keep indices in the stack
        stack.append(0)
        curr = stack[-1]
        while len(stack) >0:
            #when we have left child push current onto stack
            if left[curr] != -1:
                hold = left[curr]
                left[curr] = -1
                curr = hold
                stack.append(curr)
            elif left[curr] == -1:
                #there is no more left child
                self.result.append(self.key[curr])
                stack.pop()
                # need to check if we have right
                if right[curr]!= -1:
                    hold = right[curr]
                    right[curr] =-1
                    curr = hold
                    stack.append(curr)
                else:
                    if len(stack)>0:
                        curr = stack[-1]
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def preOrder(self):
        self.result = []
        left = self.left.copy()
        right=self.right.copy()
        stack =[]
        # we want to keep indices in the stack
        stack.append(0)
        curr = stack[-1]
        self.result.append(self.key[curr])
        while len(stack) >0:
            #when we have left child push current onto stack
            if left[curr] != -1:
                hold = left[curr]
                left[curr] = -1
                curr = hold
                stack.append(curr)
                self.result.append(self.key[curr])
            elif left[curr] == -1:
                stack.pop()
                # need to check if we have right
                if right[curr]!= -1:
                    hold = right[curr]
                    right[curr] =-1
                    curr = hold
                    stack.append(curr)
                    self.result.append(self.key[curr])
                else:
                    if len(stack)>0:
                        curr = stack[-1]
        return self.result

    def postOrder(self):
        self.result = []
        stack =[]
        left = self.left.copy()
        right=self.right.copy()
        # we want to keep indices in the stack
        stack.append(0)
        curr = stack[-1]
        while len(stack) >0:
            #when we have left child push current onto stack
            if left[curr] != -1:
                hold = left[curr]
                left[curr] = -1
                curr = hold
                stack.append(curr)
            elif left[curr] == -1:
                # need to check if we have right
                if right[curr]!= -1:
                    hold = right[curr]
                    right[curr] = -1
                    curr = hold
                    stack.append(curr)
                else:
                    self.result.append(self.key[curr])
                    stack.pop()
                    if len(stack)>0:
                        curr = stack[-1]
        return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
