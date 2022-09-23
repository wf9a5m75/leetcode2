//
//  C++ / pass : Runtime: 326 ms, faster than 34.24% of C++
//
class Solution {
public:
    int concatenatedBinary(int n) {
        int result = 0;
        int factor = 1;
        int MOD = 1e9+7;
        for (int i = n; i > 0; i--) {
            int j = i;
            while(j > 0) {
                result = (result + ((j & 1) * factor)) % MOD;
                j >>= 1;
                factor = (factor * 2) % MOD;
            }
        }

        return result;
    }
};
