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
        if (n==1){
            return sorting_algo;
        }
        int temp_index;
        while (index < n){
            vector<Pair> temp_vector(sorting_algo[index-1]);
            temp_index = index;
            while ((temp_index>0) &&
                    (temp_vector[temp_index].key < temp_vector[temp_index-1].key)){
                Pair temp_pair = Pair(temp_vector[temp_index - 1]);
                temp_vector[temp_index - 1] = temp_vector[temp_index];
                temp_vector[temp_index] = temp_pair;
                temp_index --;
            }
            sorting_algo.push_back(temp_vector);
            index ++;
        }
        return sorting_algo;
    }
};
