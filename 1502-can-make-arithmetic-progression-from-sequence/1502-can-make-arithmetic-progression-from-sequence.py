class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        orderedArray = self.orderArray(arr)

        temp = 0
        for i in range(len(orderedArray)):
            if i != len(orderedArray) - 1:
                if i == 0:
                    temp = orderedArray[i + 1] - orderedArray[i]
                if orderedArray[i + 1] - orderedArray[i] != temp:
                    return False
        return True

    def orderArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        pivot = arr[int(len(arr) // 2)]
        left = []
        center = []
        right = []
        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            elif arr[i] == pivot:
              center.append(arr[i])

        return self.orderArray(left) + center + self.orderArray(right)
