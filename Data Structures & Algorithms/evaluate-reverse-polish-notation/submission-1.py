class Solution:
    operateur = ['+', '-', '*', '/']
    def evalRPN(self, tokens: List[str]) -> int:
        ope_stack = list()
        for token in tokens:
            if token in self.operateur :
                b = ope_stack.pop()
                a = ope_stack.pop()
                ope_stack.append(str(int(eval(a + token + b))))
            else :
                ope_stack.append(token)
        
        return int(ope_stack.pop())
        
        