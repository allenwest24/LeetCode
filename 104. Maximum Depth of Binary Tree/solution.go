/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    } else {
        left := maxDepth(root.Left)
        right := maxDepth(root.Right)
        if left > right {
            return left + 1
        } else {
            return right + 1
        }
    }
}
