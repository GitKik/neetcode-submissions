from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) :
            return ""
        if len(t) == len(s) :
            if sorted(s) == sorted(t):
                return s
            else :
                return ""
        retuned_str = ""
        is_valid_window = False 
        window_min = 0
        window_max = -1
        window_bound = len(s) - 1
        map_t = defaultdict(int)
        for st in t : 
            map_t[st] -=1

        while not is_valid_window :
            # If the whole word is the window
            print(window_max)
            print(map_t)

            if window_max == window_bound:
                return retuned_str
            window_max += 1 
            new_str = s[window_max]
            if new_str in map_t:
                map_t[new_str] +=1
            is_valid_window = True
            # Count if all occurences of each cara is accounted for 
            for count_ in map_t.values():
                if count_ < 0 :
                    is_valid_window = False
            print(is_valid_window)
        
        
        retuned_str = s[window_min:window_max+1]
        cara_to_check = set()
        cara_to_remove = set()
        while window_max < len(s):
            new_str = s[window_min]
            if new_str in map_t:
                map_t[new_str] -=1
                if map_t[new_str] < 0:
                    cara_to_check.add(s[window_min])
            is_valid_window = True
            print(map_t)
            for cara in cara_to_check:
                if map_t[cara] < 0:
                    is_valid_window = False
                else :
                    cara_to_remove.add(cara)
            for c in cara_to_remove :
                cara_to_check.remove(c)
            cara_to_remove = set()
            
            print(s[window_min:window_max+1])
            window_min += 1

            if is_valid_window:
                retuned_str = s[window_min:window_max+1]

            else :
                window_max += 1
                if window_max > window_bound :
                    return retuned_str
                if s[window_max] in map_t:
                    map_t[s[window_max]] += 1
        return retuned_str
                

