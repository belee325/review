# python3
import sys


def InverseBWT(bwt):
    # write your code here
    idx_dict = {'A': -1, 'G': -1, 'T': -1, 'C': -1, '$': -1}
    bwt_occ = []
    for char in bwt:
        if idx_dict[char] == -1:
            bwt_occ.append((char, 1))
            idx_dict[char] = 1
        else:
            idx_dict[char] += 1
            bwt_occ.append((char, idx_dict[char]))
    char_count = {'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in bwt:
        char_count[char] += 1
    #first = sorted(bwt)
    idx_dict['$'] = 0
    if char_count['A']!=0:
        idx_dict['A'] = 1
    if char_count['C']!=0:
        idx_dict['C'] = char_count['A']+1
    if char_count['G'] != 0:
        idx_dict['G'] = char_count['A'] + char_count['C'] + 1
    if char_count['T'] != 0:
        idx_dict['T'] = char_count['A'] + char_count['C']  + char_count['G']+ 1
    ret = ""
    i = 0
    idx = 0
    while i < len(bwt):
        curr = bwt_occ[idx]
        ret = ret + curr[0]
        idx = idx_dict[curr[0]] + (curr[1] - 1)
        i += 1
    ret = ret[::-1]
    ret = ret[1:] + '$'
    return ret


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
