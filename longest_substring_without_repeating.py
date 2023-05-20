class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str_length = 0
        for i in range(len(s)):
            for j in range(len(s)):
                sub_str = s[i:(len(s)-j)] 
                if len(sub_str) == len(set(sub_str)):
                    if len(set(sub_str)) > sub_str_length:
                        sub_str_length = len(set(sub_str))
        
        return sub_str_length

f = Solution()
print(f.lengthOfLongestSubstring("pwwkew"))
