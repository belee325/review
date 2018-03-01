# Uses python3
import sys
import math

def fast_count_segments(starts, ends, points):
    count = [0] * len(points)
    temp =[]
    for x,y in zip(starts,ends):
        temp.append((x,'l'))
        temp.append((y,'r'))
    for p in points:
        temp.append((p,'p'))
    print(temp)
    temp.sort(key = lambda tup:(tup[0],tup[1]))
    print(temp)
    counter = 0
    for pt in temp:
        if pt[1]=='l':
            counter +=1
        elif pt[1]=='p':
            count[points.index(pt[0])] = counter
            points[points.index(pt[0])] = math.nan
        else:
            counter -= 1
            counter = max(0,counter)
    return count

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
