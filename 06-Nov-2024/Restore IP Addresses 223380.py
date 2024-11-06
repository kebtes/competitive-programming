# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []

        def func(idx = 0, n_int = 0, ip = []):
            if n_int == 4 and idx == len(s):
                output.append(".".join(ip[:]))
    
            for i in range(idx + 1, min(idx + 4, len(s) + 1)):
                segment = s[idx: i]
    
                if segment and (segment == "0" or (segment[0] != "0" and 0 <= int(segment) <= 255)):
                    ip.append(segment)
                    func(i, n_int + 1, ip)
                    ip.pop()
    
        func()
        return output