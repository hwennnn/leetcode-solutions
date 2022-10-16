/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        return helper(root, low, high);
    }
    
    int helper(TreeNode *node, int low, int high){
        if (node == nullptr) return 0;
        int left = helper(node->left, low, high);
        int right = helper(node->right, low, high);
        
        return ((node->val >= low && node->val <= high) ? node->val : 0 ) + left + right;
    }
};