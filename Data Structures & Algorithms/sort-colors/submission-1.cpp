class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int ptr_red = 0;
        int ptr_blue = nums.size() - 1;
        int num;
        for (int i = 0; i < n; i++){
            num = nums[i];
            if (num == 0) {
                ptr_red++;
            } else if (num == 2) {
                ptr_blue--;
            } 
        }
        for (int i = 0; i < n; i++){
            if (i < ptr_red) {
                nums[i] = 0;
            } else if (i > ptr_blue) {
                nums[i] = 2;
            } else {
                nums[i] = 1;
            }
        }
    }
};