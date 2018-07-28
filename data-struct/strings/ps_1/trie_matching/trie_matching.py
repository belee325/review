# python3
import sys

class Node:
    def __init__(self, value):
        self.next = []
        self.value =value
    def get_next_values(self):
        res=[]
        for child in self.next:
            res.append(child.value)
        return res

    def add_node(self,Node):
        self.next.append(Node)

    def get_next_node(self, value):
        for child in self.next:
            if child.value == value:
                return child
def get_match_helper(text, trie):
    input_text = text
    res = []
    idx = 0
    while(len(input_text)>0):
        loc = get_match(input_text,trie,idx)
        if loc != -1:
            res.append(loc)
        input_text = input_text[1:]
        idx +=1
    return res

def get_match(text, trie, start_idx):
    idx = 0
    v = trie
    while idx < len(text):
        symbol = text[idx]
        if symbol in v.get_next_values():
            v = v.get_next_node(symbol)
            idx +=1
        elif not symbol in v.get_next_values():
            return -1
        if len(v.next) ==0:
            return start_idx
    #edge case
    if symbol == v.value and len(v.next)==0:
        return start_idx
    else:
        return -1

def solve(text, n, patterns):
    root = Node(None)
    for pattern in patterns:
        curr_node = root
        for char in pattern:
            if char in curr_node.get_next_values():
                curr_node = curr_node.get_next_node(char)
            else:
                new_node = Node(char)
                curr_node.next.append(new_node)
                curr_node = new_node
    result = get_match_helper(text, root)
    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
