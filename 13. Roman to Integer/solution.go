func romanToInt(s string) int {
    m := map[string]int {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    
    total := 0
    
    for ii := 0; ii < len(s); ii++ {
        total += m[string(s[ii])]
        if ii > 0 {
            if m[string(s[ii - 1])] < m[string(s[ii])] {
                total -= m[string(s[ii - 1])] * 2
            }
        }
    }
    
    return total
}
