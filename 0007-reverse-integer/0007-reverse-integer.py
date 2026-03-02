class Solution:
    def reverse(self, x: int) -> int:
        result = str(x)
        if result[0] == "-":
          result = "-" + result[:0:-1]
        else:
          result = result[::-1]
        
        return int(result) if int(result).bit_length() < 32 else 0