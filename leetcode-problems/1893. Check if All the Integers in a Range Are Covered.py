class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right+1):
            is_in_range = False

            for rng in ranges:
                l,e = rng[0], rng[1]
                if num in range(l,e+1):
                    is_in_range = True

            if not is_in_range:
                return False

        return True