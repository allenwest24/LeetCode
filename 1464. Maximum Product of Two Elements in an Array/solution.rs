impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut best : i32 = 0;
        let mut next_best : i32 = 0;
        for ii in (0..nums.len()) {
            if (nums[ii] >= best) {
                next_best = best;
                best = nums[ii];
            }
            else if (nums[ii] > next_best) {
                next_best = nums[ii];
            }
        }
        return ((best - 1) * (next_best - 1));
    }
}
