impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        let mut sum = 0;
        for ii in (0..mat.len()) {
            sum += mat[ii][ii];
            sum += mat[ii][mat.len() - 1 - ii];
        }
        if (mat.len() % 2 == 1) {
            sum -= mat[mat.len() / 2][mat.len() / 2];
        }
        return sum;
    }
}
