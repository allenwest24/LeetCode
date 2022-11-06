func longestCommonPrefix(strs []string) string {
    out := ""
    for ii := 0; ii < len(strs[0]); ii++ {
        still_good := true
        for jj := 0; jj < len(strs); jj++ {
            // Would normally combine, but this check ensures the next one wont break everything.
            if len(strs[jj]) <= ii {
                still_good = false
                break
            }
            if strs[0][ii] != strs[jj][ii] {
                still_good = false
                break
            }
        }
        if still_good {
            out += string(strs[0][ii])
        } else {
            break
        }
    }
    return out
}
