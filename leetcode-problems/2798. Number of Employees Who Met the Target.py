class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        employees = 0
        for hour in hours:
            if hour >= target:
                employees += 1
                
        return employees