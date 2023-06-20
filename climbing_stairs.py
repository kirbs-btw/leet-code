""" imma complete this after vacation """

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        for i in range(n/2):



    def binomial(self, n, k):
        return (self.faculty(n) / (self.faculty(k) * self.faculty(n-k)))

    def faculty(self, n):
        f = 1
        for i in range(n):
            f = f * (i+1) 

        return f