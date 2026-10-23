class Solution:
    def reverseBits(self, n: int) -> int:
        n_str = '{:032b}'.format(n)
        out_ = ""
        for i in range(len(n_str)):
            if n_str[len(n_str) - 1 - i] == "1":
                out_ += "1"
            else : 
                out_ += "0"
        return int(out_, 2)
