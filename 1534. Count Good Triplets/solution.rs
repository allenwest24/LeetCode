impl Solution {
    pub fn count_good_triplets(arr: Vec<i32>, a: i32, b: i32, c: i32) -> i32 {
        let mut counter = 0;
        for ii in (0..arr.len()) {
            for jj in (0..arr.len()) {
                for kk in (0..arr.len()) {
                    if ((ii < jj) && (jj < kk) && ((arr[ii] - arr[jj]).abs() <= a) && ((arr[jj] - arr[kk]).abs() <= b) && ((arr[ii] - arr[kk]).abs() <= c)) {
                      counter += 1;  
                    }
                }
            }
        }
        return counter;
    }
}
