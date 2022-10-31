func maxProfit(prices []int) int {
    best := 0
    max := -1
    min := -1
    for ii := 0; ii < len(prices); ii++ {
        curr := prices[ii]
        if min == -1 {
            min = curr
            max = curr
        } else if curr < min {
            min = curr
            max = -1
        } else if curr > max {
            max = curr
            if max - min > best {
                best = max - min
            }
        }
        
        // Trigger check if on the last of the array.
        if len(prices) - 1 == ii {
            if min != -1 && max != -1 && max - min > best {
                best = max - min
            } 
        }
    }
