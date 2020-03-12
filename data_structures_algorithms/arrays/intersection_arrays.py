class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        for n in nums1:
            if n not in d1.keys():
                d1[n] = 0
            d1[n] += 1

        d2 = {}
        for n in nums2:
            if n not in d2.keys():
                d2[n] = 0
            d2[n] += 1

        output = []
        for k1 in d1.keys():
            for k2 in d2.keys():
                if k1 == k2:
                    if d1[k1] >= d2[k2]:
                        for i in range(d2[k2]):
                            output.append(k1)
                    else:
                        for i in range(d1[k1]):
                            output.append(k1)
        return output