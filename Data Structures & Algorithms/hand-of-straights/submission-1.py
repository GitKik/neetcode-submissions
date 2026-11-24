class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = {}
        for v in set(hand) :
            d[v] = hand.count(v)
        if (len(hand) < groupSize) or (len(hand)%groupSize!=0):
            return False
        while d :
            min_key = min(d.keys())
            min_v = d[min_key]
            for i in range(groupSize):
                temp_key = min_key+i
                if temp_key not in d :
                    return False
                temp_v = d[temp_key]
                if temp_v-min_v < 0 :
                    return False
                if temp_v - min_v == 0 :
                    del d[temp_key]
                else :
                    d[temp_key] = temp_v - min_v
        return True 