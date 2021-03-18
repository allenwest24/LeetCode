impl Solution {
    pub fn odd_cells(m: i32, n: i32, indices: Vec<Vec<i32>>) -> i32 {
        let mut matrix = vec![vec![0; n as usize]; m as usize];
        for ii in (0..indices.len()) {
            for jj in 0..n as usize {
                matrix[indices[ii][0] as usize][jj] += 1;
            }
            for kk in 0..m as usize {
                matrix[kk][indices[ii][1] as usize] += 1;
            }
        }
        let mut counter = 0;
        for ll in 0..n as usize {
            for mm in 0..m as usize {
                if matrix[mm][ll] % 2 != 0 {
                    counter += 1;
                }
            }
        }
        return counter;
    }
}
