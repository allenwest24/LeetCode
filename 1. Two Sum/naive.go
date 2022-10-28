func twoSum(nums []int, target int) []int {
    var mySlice = []int{} 
    for ii := 0; ii < len(nums); ii++ {
        if ii < len(nums) - 1 {
            for jj := ii + 1; jj < len(nums); jj++ {
                if nums[ii] + nums[jj] == target {
                    mySlice = append(mySlice, ii, jj)
                    return mySlice
                }
            }
        }
    }
    return mySlice
}
