class Solution:
    def pivotInteger(self, n: int) -> int:
        list_original = list(range(1, n + 1))
        list1 = []
        list2 = []

        def sumLists(a: list):
            sum = 0
            for item in a:
                sum = sum + item
            return sum

        for i in list_original:
            list1 = list_original[:i]
            list2 = list_original[i - 1 :]
            print(sumLists(list1), sumLists((list2)))
            if sumLists(list1) == sumLists(list2):
                return i

        return -1