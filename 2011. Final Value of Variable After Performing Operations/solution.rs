impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut total = 0;
        for ii in 0..operations.len() {
            if operations[ii] == "--X" || operations[ii] == "X--" {
                total -= 1;
            }
            else if operations[ii] == "X++" || operations[ii] == "++X" {
                total += 1;
            }
        }
        return total;
    }
}
