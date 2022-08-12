from collections import Counter

def intersect(nums1, nums2):
    a = Counter(nums1)
    b = Counter(nums2)
    result = a & b
    return list(result.elements())


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))