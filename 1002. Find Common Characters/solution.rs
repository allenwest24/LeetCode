impl Solution {
    pub fn common_chars(a: Vec<String>) -> Vec<String> {
        let mut tracker: Vec<String> = Vec::new();
        let mut starter = &a[0];
        let mut times: usize = 1;
        let mut curr;
        let mut truforall = false;
        for ii in (0..starter.len()) {
            curr = starter.chars().nth(ii).unwrap();
            times = starter[0..ii + 1].matches(curr).count();
            truforall = true;
            for jj in (1..a.len()) {
                if !(a[jj].matches(curr).count() >= times) {
                    truforall = false;
                }
            }
            if (truforall) {
                tracker.push(starter.chars().nth(ii).unwrap().to_string());
            }
        }
        return tracker;
    }
}
