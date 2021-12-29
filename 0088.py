class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_pin, nums2_pin, m1 = 0, 0, m
        while nums1_pin < m + n and nums2_pin < n and n != 0:
            if m1 == 0:
                for i in range(nums1_pin, m+n):
                    nums1[i] = nums2[nums2_pin]
                    nums2_pin += 1
                break
            if nums1[nums1_pin] > nums2[nums2_pin]:
                nums1.insert(nums1_pin,nums2[nums2_pin])
                nums2_pin += 1
                nums1_pin += 1          
            else:
                nums1_pin += 1
                m1 -= 1
        del nums1[m+n:m+n+n]