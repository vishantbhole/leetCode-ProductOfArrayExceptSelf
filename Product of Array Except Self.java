class Solution {
    public int[] productExceptSelf(int[] nums) {
        int l = nums.length;
        int op[] = new int[l];
        int m = 1;
        for(int i=0;i < l; i++){
            op[i] = m;
            m = m * nums[i];
        }
        int n = 1;
        for(int i=l-1;i >= 0; i--){
            op[i] =  op[i] * n;
            n = n * nums[i];
           }
        return op;
    }
}