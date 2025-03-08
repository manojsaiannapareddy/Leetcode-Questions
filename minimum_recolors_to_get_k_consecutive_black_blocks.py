class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        a = k

        for i in range(len(blocks) - k + 1):
            black_count = blocks[i:i + k].count("B")
            a = min(a, k - black_count)

        return a