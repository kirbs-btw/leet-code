class Solution(object):
    def lengthOfLastWord(self, s):
        word_cach = ""
        switch = True
        for i in s[::-1]:
            if i == " " and switch:
                pass
            elif i == " " and not switch:
                break
            else:
                switch = False
                word_cach += i
        return len(word_cach)
