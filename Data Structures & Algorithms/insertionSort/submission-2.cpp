// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
        vector<vector<Pair>> sorting_algo;
        int index = 1;
        int n = pairs.size();
        if (n==0){
            return sorting_algo;
        }
        sorting_algo.push_back(pairs);
        sorting_algo.reserve(n); // One alloc for the size that is already know 
        if (n==1){
            return sorting_algo;
        }
        int temp_index;
        // Using move 
        while (index < n){
            Pair current_pair = std::move(pairs[index]);
            temp_index = index - 1;
            while ((temp_index>=0) &&
                    (current_pair.key < pairs[temp_index].key)){
                pairs[temp_index + 1] = std::move(pairs[temp_index]);
                temp_index --;
            }
            pairs[temp_index + 1] = std::move(current_pair);
            sorting_algo.push_back(pairs);
            index ++;
        }
        return sorting_algo;
    }
};
