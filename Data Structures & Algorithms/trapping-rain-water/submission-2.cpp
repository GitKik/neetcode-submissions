class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n<3){
            return 0;
        }
        int total_water = 0;
        int pointer_right = n-1;
        int pointer_left = 0;
        int max_right = height[pointer_right];
        int max_left = height[pointer_left];
        while (pointer_left < pointer_right){
            if (max_left < max_right){
                pointer_left ++;
                max_left = max(max_left, height[pointer_left]);
                total_water += max_left - height[pointer_left];
            } else {
                pointer_right --;
                max_right = max(max_right, height[pointer_right]);
                total_water += max_right - height[pointer_right];
            }
        }
        return total_water;
    }
};
