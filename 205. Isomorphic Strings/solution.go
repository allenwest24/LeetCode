func isIsomorphic(s string, t string) bool {
    return helper(s, t, true)
}

func helper(s string, t string, go_again bool) bool {
    if len(s) != len(t) {
        return false
    }
    var storage map[string]string
    storage = make(map[string]string)
    for ii := 0; ii < len(s); ii++ {
        if storage[string(s[ii])] == "" {
            storage[string(s[ii])] = string(t[ii])
        } else if storage[string(s[ii])] != string(t[ii]) {
            return false
        }
    }
    if go_again {
        return true && helper(t, s, false)
    } else {
        return true
    }
}
