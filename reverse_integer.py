class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        f = str(x)[::-1]
        prefix = ""
        if str(x)[0] == "-":
            prefix = "-"
            f = f[0:(len(f)-1)]

        cut_zero = 0
        toggle = True
        for j, i in enumerate(f):
            print(i)
            if i != "0" and toggle:
                toggle = False
                cut_zero = j 
        return prefix + f[cut_zero::]

a = Solution()
print(a.reverse(-100203500))
