impl Solution {
    pub fn find_words(words: Vec<String>) -> Vec<String> {
        let top : Vec<char> = "qwertyuiopQWERTYUIOP".to_string().chars().collect();
        let middle : Vec<char> = "asdfghjklASDFGHJKL".to_string().chars().collect();
        let bottom : Vec<char> = "zxcvbnmZXCVBNM".to_string().chars().collect();
        let mut out : Vec<String> = Vec::new();
        let mut lane : i32 = 0;
        let mut good : bool = true;
        for ii in (0..words.len()) {
            let curr : Vec<char> = words[ii].chars().collect();
            lane = 0;
            good = true;
            for jj in (0..curr.len()) {
                if (lane == 0) {
                    if (top.iter().any(|&i| i == curr[jj])) {
                        lane = 1;
                    }
                    else if (middle.iter().any(|&i| i == curr[jj])) {
                        lane = 2;
                    }
                    else {
                        lane = 3;
                    }
                }
                else if (lane == 1 && top.iter().any(|&i| i == curr[jj])) {
                    good = true;
                }
                else if (lane == 2 && middle.iter().any(|&i| i == curr[jj])) {
                    good = true;
                }
                else if (lane == 3 && bottom.iter().any(|&i| i == curr[jj])) {
                    good = true;
                }
                else {
                    good = false;
                    break;
                }
            }
            if (good) {
                out.push(words[ii].to_string());
            }
        }
        return out;
    }
}
