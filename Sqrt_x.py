class Solution(object):
    def mySqrt(self, x):
        
        for i in range(x):
            if (i * i) > x:
                return (i - 1)
