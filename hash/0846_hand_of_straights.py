from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: list, W: int) -> bool:
        '''
        1: 1
        2: 2
        3: 2
        4: 1
        6: 1
        7: 1
        8: 1
        
        [1 2 3] [2 3 4] [6 7 8]
        '''
        card_cnt = defaultdict(int)
        for card in hand:
            card_cnt[card] += 1
            
        sorted_cards = sorted(card_cnt.keys())
        
        for card in sorted_cards:
            if card_cnt[card] == 0:
                continue
            else:
                # straight starts from here
                straight_num = card_cnt[card]
                for c in range(card, card + W):
                    if card_cnt[c] < straight_num:
                        return False
                    else:
                        card_cnt[c] -= straight_num
                
        return True