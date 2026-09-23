class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # [5, 4, 3, 2, 5]
        # alice = 5, end
        # bob = 
        start, end = 0, len(piles) - 1
        alice, bob = 0, 0
        is_alice_turn = True
        while end > start:
            if piles[start] >= piles[end]:
                stone = piles[start]
                start += 1
            elif piles[start] < piles[end]:
                stone = piles[end]
                end -= 1
            if is_alice_turn:
                alice += stone
            else:
                bob += stone
        return alice > bob