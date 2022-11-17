func pivotIndex(nums []int) int {
    // Start backwards because on the return we want to stop at first on left.
    var totals []int
    curr := 0
    for ii := len(nums) - 1; ii >= 0; ii-- {
        totals = append(totals, curr)
        curr += nums[ii]
    }
    curr = 0
    for jj := 0; jj < len(nums); jj++ {
        if curr == totals[len(totals) - (jj + 1)] {
            return jj
        }
        curr += nums[jj]
    }
    return -1
}
