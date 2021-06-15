impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut new_nums = Vec::new();
        let mut curr : i32 = 0;
        for xx in (0..nums.len()) {
            curr += nums[xx];
            new_nums.push(curr);
        }
        return new_nums;
    }
}
