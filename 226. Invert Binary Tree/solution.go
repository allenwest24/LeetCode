/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
    if root == nil || root.Left == nil && root.Right == nil {
        return root
    } else {
        temp := invertTree(root.Left)
        root.Left = invertTree(root.Right)
        root.Right = temp
        return root
    }
}
