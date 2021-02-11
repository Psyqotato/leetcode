class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m1, n1, mid = len(nums1), len(nums2), int((len(nums1) + len(nums2))/2)
        nums3 = []
        while (len(nums3) <= mid):
            if len(nums1) == 0:nums3 = nums3 + nums2[:(mid-len(nums3)+1)]
            elif len(nums2) == 0:nums3 = nums3 + nums1[:(mid-len(nums3))+1]
            else:
                m, n = len(nums1)-1, len(nums2)-1
                if nums1[0] > nums2[0]:
                    while nums2[n] > nums1[0]: n = int(n/2)
                    nums3 = nums3 + nums2[:n+1]
                    nums2 = nums2[n+1:]
                else:
                    while nums1[m] > nums2[0]: m = int(m/2)
                    nums3 = nums3 + nums1[:m+1]
                    nums1 = nums1[m+1:]            
        if (m1 + n1) % 2 == 0:return((nums3[mid-1] + nums3[mid])/2)
        else:return(nums3[mid])