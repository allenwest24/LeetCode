func isSubsequence(s string, t string) bool {
    jj := 0
    for ii := 0; ii < len(s); ii++ {
        next := false
        for jj < len(t) {
            if t[jj] == s[ii] {
                jj++
                next = true
                break
            }
            jj++
        }
        if !next {
            return false
        }
    }
    return true
}
