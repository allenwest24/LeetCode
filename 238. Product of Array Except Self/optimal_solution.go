func productExceptSelf(nums []int) []int {
    var out []int
    pre := 1
    pos := 1
    for ii := 0; ii < len(nums); ii++ {
        out = append(out, pre)
        pre *= nums[ii]
    }
    
    for jj := len(nums) - 1; jj >= 0; jj-- {
        out[jj] *= pos
        pos *= nums[jj]
    }
    return out
}
