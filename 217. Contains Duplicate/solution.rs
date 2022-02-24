impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        // Check every number for copies later on.
        for ii in 0..(nums.len() - 1) {
            for jj in (ii + 1)..nums.len() {
                if nums[ii] == nums[jj] {
                    return true;
                }
            }
        }
        return false;
    }
}
