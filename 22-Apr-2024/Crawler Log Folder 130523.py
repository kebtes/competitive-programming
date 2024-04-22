# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for call in logs:
            c, _ = call.split("/")

            if c == "..":
                if stack: 
                    stack.pop()
            
            elif c == ".":
                continue
            else:
                stack.append(c)

        return len(stack) 