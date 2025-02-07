class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        ascii_s1 = sum(ord(c) for c in s1)
        ascii_s2 = sum(ord(c) for c in s2)

        
        def lcs_ascii_sum(word1, word2):
            n, m = len(word1), len(word2)
            dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + ord(word1[i - 1])
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
            return dp[n][m]  

        
        ascii_lcs = lcs_ascii_sum(s1, s2)

        
        return (ascii_s1 + ascii_s2) - 2 * ascii_lcs
