/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
    slow := head
    fast := head
    // Run through nodes until slow and fast collide, or fast hits the end.
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
        if slow == fast {
            break
        }
    }
    
    // See if it quit only because fast hit the end.
    if fast == nil || fast.Next == nil {
        return nil
    }
    
    // Because fast went twice the distance and arrived at the same spot, we know that 
    // head and slow can go the same pace and arrive at the cycle start.
    for head != slow {
        slow = slow.Next
        head = head.Next
    }
    return head
}
