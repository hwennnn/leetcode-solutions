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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (m == n) return head;
        
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        
        ListNode *curr = head, *prev = dummy;
        
        for (int i = 0; i < m - 1; i++){
            curr = curr->next;
            prev = prev->next;
        }
        
        ListNode *temp = NULL;
        for (int i = 0; i < n-m+1; i++){
            ListNode* next = curr->next;
            curr->next = temp;
            temp = curr;
            curr = next;
        }
        
        prev->next->next = curr;
        prev->next = temp;
        
        return dummy->next;
    }
};