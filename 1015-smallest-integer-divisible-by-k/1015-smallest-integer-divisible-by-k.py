class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
      left = 0
      length = 0
      while length < k:
        length += 1
        left = (left * 10 + 1) % k
        if left == 0:
          return length
        
      return -1
      
        