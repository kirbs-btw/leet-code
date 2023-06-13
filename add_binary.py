class Solution(object):
    def addBinary(self, a, b):
        # convert to real deca 

        numa = self.convert_to_dec(a)
        numb = self.convert_to_dec(b)


        return "{0:b}".format((numa+numb))

    
    def convert_to_dec(self, a):
        n = 0
        for i, j in enumerate(a[::-1]):
            if j == "1":
                n += 2**i

        return n
