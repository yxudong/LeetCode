/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
    public:
        ListNode* removeNthFromEnd(ListNode* head, int n) {
            ListNode *p = head;
            while (n && p) {
                p = p->next;
                --n;
            }
            if (!p) {
                head = head->next;
                return head;
            }
            p = p->next;
            ListNode *now = head;
            while (p) {
                p = p->next;
                now = now->next;
            }
            now->next = now->next->next;
            return head;
        }
};
