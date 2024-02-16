from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)

        for cpdomain in cpdomains:
            visit, domain = cpdomain.split()
            subdomains = domain.split(".")
            
            for i in range(len(subdomains)):
                sub = ".".join(subdomains[i:])
                domains[sub] += int(visit)
            
        output = [str(count) + " " + sub for sub, count in domains.items()]
        return output

            
        