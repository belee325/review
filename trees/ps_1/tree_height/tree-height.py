# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.dist =[-1]*self.n

        def compute_height(self):
            visited = {}
                # Replace this code with a faster implementation
            for i in range(0,self.n):
                curr = self.parent[i]
                if curr in visited or curr ==-1:
                    continue
                curr_height = 1
                while(curr!=-1):
                    if curr in visited:
                        self.dist[self.parent[i]] = curr_height + self.dist[curr] - 1
                        visited[self.parent[i]] = ''
                        break
                    curr = self.parent[curr]
                    curr_height+=1
                if curr == -1:
                    self.dist[self.parent[i]] = curr_height
                    visited[self.parent[i]] = ''
                #print(visited,self.dist)
            return max(self.dist)
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
