# -*- coding: utf-8 -*-
"""
Created on Fri May 17 08:05:21 2019

@author: HM
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_v=0
        l=0
        r=len(height)-1
        while r>l:
            v= min(height[r],height[l])*(r-l)
            if v>max_v :
                    max_v = v
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
            print(max_v)
        return max_v