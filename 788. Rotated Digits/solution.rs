impl Solution {
    pub fn rotated_digits(n: i32) -> i32 {
        let mut out : i32 = 0;
        for ii in (1..(n+1)) {
            let num = ii.to_string();
            let to_chars = num.chars().collect();
            if (!((to_chars.iter().any(|&i| i == '3')) || (to_chars.iter().any(|&i| i == '4')) || (to_chars.iter().any(|&i| i == '7')) && ((to_chars.iter().any(|&i| i == '2')) || (to_chars.iter().any(|&i| i == '5')) || (to_chars.iter().any(|&i| i == '6')) || (to_chars.iter().any(|&i| i == '9'))) {
                out += 1;
            }
        }
        return out;
    }
}
