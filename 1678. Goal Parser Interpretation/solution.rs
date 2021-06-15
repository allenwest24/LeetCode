impl Solution {
    pub fn interpret(command: String) -> String {
        let mut out = String::new();
        let mut my_vec : Vec<char> = command.chars().collect();
        for ii in (0..command.len()) {
            if (my_vec[ii] == 'G') {
                out += "G";
            }
            else if (my_vec[ii] == '(' && my_vec[ii + 1] == ')') {
                out += "o";
            }
            else if (my_vec[ii] == '(') {
                out += "al";
            }
        }
        return out;
    }
}
