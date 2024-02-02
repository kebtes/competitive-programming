class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        merged = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j]) 
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        l = len(merged)

        if l % 2 == 0:
            n1 = merged[l // 2]
            n2 = merged[l // 2 - 1]
            return float((n1 + n2) / 2)
            
        else:
            return float(merged[l // 2])