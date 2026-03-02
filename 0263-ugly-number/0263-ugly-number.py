class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 5 or n == 3 or n == 2 or n == 1:
            return True
        if n % 5 == 0:
            return self.isUgly(n / 5)
        elif n % 3 == 0:
            return self.isUgly(n / 3)
        elif n % 2 == 0:
            return self.isUgly(n / 2)
        else:
            return False
