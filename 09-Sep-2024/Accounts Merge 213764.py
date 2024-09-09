# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = defaultdict(list)
        parents = defaultdict(str)
        rank = defaultdict(int)

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])

            return parents[node]
        
        def union(node_1, node_2):
            parent_X = find(node_1)
            parent_Y = find(node_2)

            if parent_X != parent_Y:
                if rank[parent_Y] > rank[parent_X]:
                    parents[parent_X] = parent_Y
                elif rank[parent_Y] < rank[parent_X]:
                    parents[parent_Y] = parent_X
                else:
                    parents[parent_X] = parent_Y
                    rank[parent_X] += 1

        for acc in accounts:
            name = acc[0]
            first_acc = acc[1]
            
            for email in acc[1:]:
                email_to_name[email] = name
                if email not in parents:
                    parents[email] = email

                union(email, first_acc)

        merged_accounts = defaultdict(list)
        for email in parents:
            root = find(email)
            merged_accounts[root].append(email)
        
        output = []
        for root, emails in merged_accounts.items():
            output.append([email_to_name[root]] + sorted(emails))

        return output
