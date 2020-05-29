# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : 394.字符串解码.py
# __time__  : 2020/5/28 10:46 下午

class Solution:

    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)


if __name__ == '__main__':
    print(Solution().decodeString('"100[leetcode]"'))

