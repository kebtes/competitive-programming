class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        seen = set()
        doubles = set()

        for front, back in zip(fronts, backs):
            seen.add(front)
            seen.add(back)

            if front == back:
                doubles.add(front)

        return min(seen - doubles, default = 0)
        