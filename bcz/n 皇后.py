# -*- coding: utf-8 -*-
# __file__  : n 皇后.py
# __time__  : 2020/7/29 9:18 PM
from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        if m==0:
            return board
        n = len(board[0])
        if n==0:
            return board
        todo = True
        while todo:
            todo = False
            for i in range(m):
                for j in range(n-2):
                    if board[i][j]!=0 and abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]):
                        board[i][j] = board[i][j+1] = board[i][j+2] = -abs(board[i][j])
                        todo = True
            for j in range(n):
                for i in range(m-2):
                    if board[i][j]!=0 and abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]):
                        board[i][j] = board[i+1][j] = board[i+2][j] = -abs(board[i][j])
                        todo = True
            for j in range(n):
                wptr = m-1
                for i in range(m-1,-1,-1):
                    if board[i][j]>0:
                        board[wptr][j] = board[i][j]
                        wptr -= 1
                for i in range(0,wptr+1):
                    board[i][j] = 0
        return board


if __name__ == '__main__':
    Solution().candyCrush(6)

