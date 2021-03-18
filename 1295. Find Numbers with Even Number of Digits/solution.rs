impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        let mut counter = 0;
        for ii in (0..nums.len()) {
            if (nums[ii].to_string().len() % 2 == 0) {
            counter += 1;
            }
        }
        return counter;
    }
}
