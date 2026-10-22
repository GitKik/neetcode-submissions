class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = n < 0
        bin_n = bin(abs(n))
        bin_repr = [int(bit) for bit in list(bin_n.replace('0b',''))]
        print(bin_repr)
        bin_repr.reverse()
        print(bin_repr)
        res = 1
        pow_ = (1/x) if sign else x
        for bit in bin_repr:
            if bit: 
                res *= pow_
            pow_ = pow_ * pow_ if sign else pow_ * pow_
            print(pow_)
            
        return res
        
