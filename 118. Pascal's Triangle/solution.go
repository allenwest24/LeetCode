func generate(numRows int) [][]int {
    out := [][]int {{1}}
    // Base case 1.
    if numRows == 1 {
        return out
    }
    
    for ii := 2; ii <= numRows; ii++ {
        temp := []int {1}
        // Base case 2.
        if len(out[len(out) -1]) >= 2 {
            prev := out[len(out) - 1]
            for jj := 1; jj < len(prev); jj++ {
                temp = append(temp, prev[jj] + prev[jj - 1])
            }
        }
        temp = append(temp, 1)
        out = append(out, temp)
    }
    return out
}
