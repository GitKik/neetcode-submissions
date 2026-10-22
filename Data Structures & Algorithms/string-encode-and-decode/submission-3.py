


class Solution:

    def encode(self, strs: List[str]) -> str:
        s_ret = ""
        for str_ in strs :
            for s in str_ :
                s_ret += str(ord(s)) + ','
            s_ret += ";"
        print(s_ret)
        return s_ret
    def decode(self, s: str) -> List[str]:
        split_ord = s.split(";")
        print(split_ord)
        list_ret = []
        for elem in split_ord[:-1] :
            s_temp = ""
            for e in elem.split(',')[:-1] :
                s_temp += chr(int(e))
                print(s_temp)
            list_ret.append(s_temp)
        return list_ret
