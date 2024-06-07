# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        distribution = [0] * k
        min_unfairness = float('inf')
        n = len(cookies)

        def func(idx):
            nonlocal distribution, min_unfairness

            if idx == n:
                min_unfairness = min(min_unfairness, max(distribution))
                return

            if min_unfairness <= max(distribution):
                return

            for i in range(k):
                distribution[i] += cookies[idx]
                func(idx + 1)
                distribution[i] -= cookies[idx]
        
        func(0)
        return min_unfairness