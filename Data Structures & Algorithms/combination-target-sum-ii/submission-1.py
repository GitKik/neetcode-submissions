class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)          # ascending → lets us stop early
        result = []                              

        def explore(i, remaining, current):
            if remaining == 0:                   
                result.append(current)
                return
            if i == len(candidates) or candidates[i] > remaining:
                return
            c = candidates[i]
            explore(i + 1, remaining - c, current + [c])
            j = i
            while j < len(candidates) and candidates[j] == c:
                j += 1
            explore(j, remaining, current)

        explore(0, target, [])
        return result