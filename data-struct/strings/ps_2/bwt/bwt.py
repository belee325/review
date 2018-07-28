# python3
import sys

def BWT(text):
    if len(text) == 0:
        return ""
    rotations = []
    rotations.append(text)
    for i in range(len(text)):
        rotations.append(rotations[i][-1]+rotations[i][0:len(text)-1])
    rotations = rotations[1:]
    rotations=sorted(rotations)
    ret_str = ""
    for i in range(len(text)):
        ret_str = ret_str + rotations[i][-1]
    return ret_str

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))