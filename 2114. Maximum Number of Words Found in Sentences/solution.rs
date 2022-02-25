impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        // Keep track of the largest sentence.
        let mut best = 0;
        
        // Check each sentence.
        for ii in 0..sentences.len() {
            // In the current sentence, split into words where there is white space and count the words.
            let curr = sentences[ii].split_whitespace().collect::<Vec<_>>().len() as i32;
            // If the current sentence has the most words so far, keep track of the new best.
            if curr > best {
                best = curr;
            }
        }
        return best;
    }
}
