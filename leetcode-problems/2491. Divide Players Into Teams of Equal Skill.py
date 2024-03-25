class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        output = 0
        skill.sort()

        s = skill[0] + skill[-1]

        for i in range(len(skill)//2):
            if skill[i] + skill[-i-1] != s:
                return -1

            output += skill[i] * skill[-i-1]

        return output
