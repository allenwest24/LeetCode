impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        // Alphabet used for easy alphabetical assessment.
        let alphabet = "abcdefghijklmnopqrstuvwxyz";
        // Counter.
        let mut c = 0;
        
        // For each letter..
        for ii in 0..strs[0].len() {
            let mut curr = 0;
            let mut prev = 0;
            // For each word..
            for jj in 0..strs.len() {
                // Determine whether the current character in the current word is
                // lower in the alphabet than the current character in the previous word.
                let ch = strs[jj].chars().nth(ii).unwrap();
                curr = alphabet.find(ch).unwrap() as i32;
                
                // If yes, replace the previous with the current and new previous.
                if curr >= prev {
                    prev = curr;
                }
                // If not, we delete a column and move on immediately.
                else {
                    c += 1;
                    break;
                }
            }
        }
        
        // Output the number of columns deleted.
        return c;
    }
}
