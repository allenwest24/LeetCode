impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut alt = 0;
        let mut best = 0;
        for ii in (0..gain.len()) {
          alt = alt + gain[ii];
          if alt > best {
              best = alt;
            }
        }
        return best;
    }
}
