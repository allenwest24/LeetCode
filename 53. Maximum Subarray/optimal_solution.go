func maxSubArray(nums []int) int {
    curr := 0
    max := nums[0]
    if len(nums) == 1 {
        return max
    }
    
    for ii := 0; ii < len(nums); ii++ {
        curr += nums[ii]
        if curr > max {
            max = curr
        } 
        if curr < 0 {
            curr = 0
        }
    }
    return max
}
