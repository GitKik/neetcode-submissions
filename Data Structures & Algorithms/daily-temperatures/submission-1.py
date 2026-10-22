import heapq

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return_list = [0 for i in range(len(temperatures))]
        stack = []
        for temp_idx, temp in enumerate(temperatures):
            # Add to the stack
            pushed = False 
            while not pushed :
                if len(stack) == 0 :
                    stack = [(temp_idx, temp)]
                    pushed = True
                else : 
                    elem = stack[0]
                    if temp <= elem[1]:
                        stack = [(temp_idx, temp)] + stack
                        pushed = True 
                    else :
                        return_list[elem[0]] = temp_idx - elem[0]
                        stack.pop(0)
        return return_list
