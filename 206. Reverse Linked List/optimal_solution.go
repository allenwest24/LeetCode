/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    // Base cases.
    if head == nil || head.Next == nil {
        return head
    }
    
    var seen *ListNode
    curr := head
    for curr != nil {
        // Save the next curr.
        temp := curr.Next
        // This is the final node we have seen so far, so it should be put at the start of the seen (because reversed).
        curr.Next = seen
        // Update seen with new front node.
        seen = curr
        // Set curr to what we saved as the next value.
        curr = temp
    }
    return seen
}
