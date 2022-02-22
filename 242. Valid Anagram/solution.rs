impl Solution {
    pub fn is_anagram(mut s: String, mut t: String) -> bool {
        // Break down into list of chars, sort unstable, join with collect.
        let mut l1: Vec<char> = s.chars().collect();
        l1.sort_unstable();
        let j1: String = l1.into_iter().collect();
        
        // Repeat.
        let mut l2: Vec<char> = t.chars().collect();
        l2.sort_unstable();
        let j2: String = l2.into_iter().collect();          
        
        return (j1 == j2);
    }
}
