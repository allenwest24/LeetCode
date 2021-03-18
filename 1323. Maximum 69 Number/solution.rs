impl Solution {
    pub fn maximum69_number (num: i32) -> i32 {
        let num_string = num.to_string();
        let mut char_vec: Vec<char> = num_string.chars().collect();
        for ii in (0..num_string.len()) {
            if (char_vec[ii] == '6') {
                char_vec[ii] = '9';
                break;
            }
        }
        num_string = char_vec.iter().collect();
        let result = num_string.parse::<i32>().unwrap();
        return result;
    }
}
