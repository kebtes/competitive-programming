class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings = {}
        
        for index, string in enumerate(list1):
            if string in list2:
                index_2 = list2.index(string)
                common_strings[string] = index + index_2
        
        if not common_strings:
            return []
        
        minimum = min(common_strings.values())
        
        return [string for string, index_sum in common_strings.items() if index_sum == minimum]