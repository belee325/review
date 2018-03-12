# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    #for i in range(len(self._data)):
    # for j in range(i + 1, len(self._data)):
    #    if self._data[i] > self._data[j]:
    #      self._swaps.append((i, j))
    #      self._data[i], self._data[j] = self._data[j], self._data[i]
    for i in reversed(range(0,len(self._data)//2)):
        while True:
            #left child = 2i + 1, right child = 2i +2
            min_idx = i
            left = 2*i+1
            right = left + 1
            if left < len(self._data) and self._data[min_idx] >= self._data[left]:
                min_idx = left 
            if right < len(self._data) and self._data[min_idx] >= self._data[right]: 
                min_idx = right
            if min_idx != i:
                self._data[i],self._data[min_idx] = self._data[min_idx],self._data[i]
                self._swaps.append((i,min_idx))
                i = min_idx
            else:
                break
    return
    
  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
