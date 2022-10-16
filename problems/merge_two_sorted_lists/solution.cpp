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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *curr = new ListNode;
        curr->val = -1;
        curr->next = NULL;
        ListNode *res = curr;
        
        while (l1 != nullptr && l2 != nullptr){
            if (l1->val < l2->val){
                curr->next = l1;
                l1 = l1->next;
            }else{
                curr->next = l2;
                l2 = l2->next;
            }
            
            curr = curr->next;
        }
        
        ListNode *leftover = (l1 == nullptr) ? l2 : l1;
        curr->next = leftover;
        
        return res->next;
    }
};