class Solution {
public:
    void reverseString(vector<char>& s) {
        char left;
        char right;
        int size = s.size();
        for (int i = 0; i<size/2; i++){
            left = s[i];
            right = s[size-i- 1];
            s[i] = right;
            s[size - i - 1] = left;
        }
    }
};