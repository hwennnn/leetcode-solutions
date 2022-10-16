/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *curr = new ListNode;
        curr->next = head;
        ListNode *res = curr;
        
        while (curr){
            while (curr->next && curr->next->val == val)
                curr->next = curr->next->next;
            curr = curr->next;
        }
        
        return res->next;
    }
};