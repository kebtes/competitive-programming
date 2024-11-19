# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        output, prefix = [], ""
        start_idx = 0

        for char in searchWord:
            prefix += char

            start = bisect.bisect_left(products, prefix)

            search_results = []
            for i in range(start, min(len(products), start + 3)):
                if products[i].startswith(prefix):
                    search_results.append(products[i])
                else:
                    break

            output.append(search_results)

        return output
