/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func preorder(root *Node) []int {
    var curr []int
    if root == nil {
        return curr
    }
    curr = append(curr, root.Val)
    if len(root.Children) == 0 {
        return curr
    } 
    for ii := 0; ii < len(root.Children); ii++ {
        temp := preorder(root.Children[ii])
        for jj := 0; jj < len(temp); jj++ {
            curr = append(curr, temp[jj])
        }
    }
    return curr
}
