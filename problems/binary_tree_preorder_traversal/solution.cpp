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
    vector<int> res;
    
    void helperR(TreeNode* root){
        if (root == nullptr) return;
        
        res.push_back(root->val);
        helperR(root->left);
        helperR(root->right);
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        helperR(root);
        
        return res;
    }
};