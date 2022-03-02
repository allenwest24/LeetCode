impl Solution {
    pub fn count_operations(mut num1: i32, mut num2: i32) -> i32 {
        // We need a counter.
        let mut c = 0;
        
        // Keep going until one of the two numbers equals 0.
        while !(num1 == 0 || num2 == 0) {
            // Subtract the min from the max.
            if num1 <= num2 {
                num2 -= num1;
            }
            else {
                num1 -= num2;
            }
            // Increment each iteration.
            c += 1;
        }
        
        // Return the counter.
        return c;
    }
}
