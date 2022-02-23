impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        // Start a 2d vec with the first row done.
        let mut out = vec![vec![]];
        out[0].push(1);
        
        // Fill in all following rows.
        for ii in 1..num_rows {
            out.push(vec![1]);
            let len_out = out.len();
            // Do the math to add correct numbers in current row.
            for jj in 1..(out[out.len() - 2].len()) {
                let a = out[len_out - 2][jj];
                let b = out[len_out - 2][jj - 1];
                out[len_out - 1].push(a + b);
            }
            out[len_out - 1].push(1);
        }
        
        println!("{:?}", out);
        return out;
    }
}
