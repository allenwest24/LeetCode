func longestPalindrome(s string) int {
    // Make a frequency counter.
    counter := make(map[string]int)
    for _, c := range s {
        if string(c) != " " {
            counter[string(c)]++
        }
    }
    // Count all of the doubles.
    any_odd := false
    out := 0
    for _, v := range counter {
        out += (v / 2) * 2
        if v % 2 == 1 && !any_odd {
            out += 1
            any_odd = true
        }
    }
    
    return out
}
