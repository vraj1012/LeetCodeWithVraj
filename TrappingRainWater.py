# 42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        # Base condition
        if not height:
            return 0
        n = len(height)
        # Taking 2 arrays LtoR and RtoL
        l_r = [0] * n
        r_l = [0] * n

        # Initial values in both arrays
        l_r[0] = height[0]
        r_l[n-1] = height[n-1]
        total_water = 0

        # Iterating for LtoR array starting from 2nd element
        for i in range(1, n): 
            l_r[i] = max(height[i],l_r[i-1])
        
        for j in range(n-2, -1, -1):
            r_l[j] = max(height[j], r_l[j+1])

        for i in range(n):
            # Take min value between LtoR and RtoL and subtract it from orginal height array
            total_water += (min(l_r[i],r_l[i]) - height[i])

        return total_water
        