/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    // Base case.
    if head == nil || head.Next == nil {
        return head
    }
    
    curr, mid := head, head
    odd := true
    for curr != nil {
        // Move forward.
        curr = curr.Next
        
        // Flip bit every iteration.
        if odd {
            odd = false
        } else {
            // Store on even, will stay true for next odd.
            mid = mid.Next
            odd = true
        }
    }
    
    return mid
}
