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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *curr = new ListNode;
        curr->next = list1;
        ListNode *res = curr;
        
        for (int i = 0; i < a; i++)
            curr = curr->next;
        ListNode *prev = curr;
        
        for (int i = 0; i < b-a+1; i++)
            curr = curr->next;
        
        ListNode *temp = list2;
        while (temp->next)
            temp = temp->next;
        temp->next = curr->next;
        
        prev->next = list2;
        
        
        return res->next;
    }
};