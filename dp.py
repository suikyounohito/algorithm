# -*- coding: utf-8 -*-

import sys
import pprint

DEBUG = False

class DP:
    "class Dynamic Programming"
    
    @classmethod
    def solve(cls, input, W):
        N = len(input)
        dp = [[0 for j in range(W + 1)] for i in range(N + 1)]
        
        for i in range(N):
            (w, v) = input[i]
            for j in range(W + 1):
                if (w > j):
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)
        
        if DEBUG:
            pprint.pprint(dp)
            
        return dp[N][W]

    
# main
if __name__ == "__main__":
    input = [(2, 3), (1, 2), (3, 4), (2, 2)]
    print DP.solve(input, 5)
