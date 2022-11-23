func search(nums []int, target int) int {
    p := len(nums) / 2
    pivot := nums[p]
    if pivot == target {
        return p
    } else if target < pivot && p - 1 >= 0 {
        return search(nums[:p], target)
    } else if target > pivot && p + 1 < len(nums) {
        val := search(nums[p + 1:], target)
        if val != -1 {
            return val + 1 + p
        }
    }
    return -1
}
