def merge(nums1, m, nums2, n):
  for i in range(n):
    nums1.remove(0)
    nums1.append(nums2[i])
  nums1.sort()


