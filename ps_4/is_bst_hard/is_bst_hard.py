#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    stack = []
    res = []
    stack.append(0)
    curr = 0
    while len(stack) > 0:
        # has left child
        if tree[curr][1] != -1:
            hold = tree[curr][1]
            tree[curr][1] = -1
            # Check the ordering of the left child
            if tree[hold][0] >= tree[curr][0]:
                return False
            curr = hold
            stack.append(curr)
        elif tree[curr][1] == -1:
            #res.append(tree[curr][0])
            stack.pop()
            # has right child
            if tree[curr][2] != -1:
                hold = tree[curr][2]
                tree[curr][2] = -1
                #check ordering of right child
                if tree[hold][0] < tree[curr][0]:
                    return False
                curr = hold
                stack.append(curr)
            else:
                if len(stack) > 0:
                    curr = stack[-1]
    # print(res)
    #for i in range(len(res) - 1):
    #    if res[i] > res[i + 1]:
    #        return False
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if nodes == 0 or nodes == 1:
        print("CORRECT")
        return
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
