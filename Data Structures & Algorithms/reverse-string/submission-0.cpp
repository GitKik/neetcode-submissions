class Solution {
public:
    void reverseString(vector<char>& s) {
        char left;
        char right;
        for (int i = 0; i<s.size()/2; i++){
            left = s[i];
            right = s[ s.size()-i- 1];
            s[i] = right;
            s[s.size() - i - 1] = left;
        }
    }
};