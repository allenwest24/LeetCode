func runningSum(nums []int) []int {
    var out []int
    runningTotal := 0
    for ii := 0; ii < len(nums); ii++ {
        runningTotal += nums[ii]
        out = append(out, runningTotal)
    }
    return out
}
