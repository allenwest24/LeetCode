impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut expected : Vec<_> = heights.iter().cloned().collect();
        expected.sort();
        let mut out : i32 = 0;
        for ii in (0..expected.len()) {
            if (expected[ii] != heights[ii]) {
                out += 1;
            }
        }
        return out;
    }
}
