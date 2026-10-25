class ListNode {
public:
    int value;
    ListNode* next;

    ListNode() : value(0), next(nullptr) {}
    ListNode(int value, ListNode* next = nullptr): value(value), next(next) {}
};

class LinkedList {
public:
    int size;
    ListNode* head;
    LinkedList() : size(0), head(nullptr) {}

    int get(int index) {
        ListNode* node = head;
        // Case where the index is ill defined
        if ((index > size - 1) || (index<0) ) {
            return -1;
        }
        while (index > 0) {
            index --;
            node = node->next;
        }
        return node->value;
    }

    void insertHead(int val) {
        ListNode* new_head = new ListNode(val, head);
        size++;
        head = new_head;
    }
    
    void insertTail(int val) {
        ListNode* tail = head;
        ListNode* new_tail = new ListNode(val);
        if (head == nullptr){
            head = new_tail;
            size ++;
            return ;
        }
        while (tail->next != nullptr){
            tail = tail->next;
        }
        tail->next = new_tail;
        size++;
    }

    bool remove(int index) {
        ListNode* node = head;
        ListNode* prev_node = head;
        // Case where the index is ill defined
        if ((index > size - 1) || (index<0) ) {
            return false;
        }
        if (index==0){
            head = head->next;
        }
        else {
            while (index != 0){
                prev_node = node;
                index --;
                node = node->next;
            }
            prev_node->next = node->next;
        }
        delete node;
        size--;
        return true;
    }

    vector<int> getValues() {
        vector <int> values;
        ListNode* node = head;
        while (node != nullptr) {
            values.push_back(node->value);
            node = node->next;
        }
        return values;
    }
};
