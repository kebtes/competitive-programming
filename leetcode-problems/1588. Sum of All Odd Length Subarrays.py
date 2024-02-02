class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        window = 1
        l, r = 0, window
        arr_sum = 0

        while window <= len(arr):
            while r <= len(arr):
                arr_sum += sum(arr[l:r])
                l += 1
                r += 1
            
            window += 2
            l = 0
            r = window

        return arr_sum