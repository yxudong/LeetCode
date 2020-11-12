#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start

#Tips: linked-list, hash-table

class DLinkedNode:
    def __init__(self, key=0, val=0, next=None, pre=None):
        # 使用双向链表
        # 额外记录一个 key，这样得到 node 时，可以获取到对应的 key
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.key_to_node_hash = {}
        self.link_tail = None
        # 链表头用一个虚构的结点
        self.link_head = DLinkedNode(0, 0)

    def get(self, key: int) -> int:
        if self.key_to_node_hash.get(key, None):
            # key 存在
            node = self.key_to_node_hash[key]
            # 移动到链表尾
            self.move_to_tail(node)
            return node.val
        else:
            # key 不存在
            return -1

    def put(self, key: int, value: int) -> None:
        if self.key_to_node_hash.get(key, None):
            # 如果 key 存在
            node = self.key_to_node_hash[key]
            # 更新结点的值
            node.val = value
            # 移动到链表尾
            self.move_to_tail(node)
            return
        else:
            # 如果 key 不存在
            if self.length == self.capacity:
                # 容量达到上限
                # 删除链表头部元素
                to_delete_node = self.link_head.next
                if self.length != 1:
                    # 这里针对链表长度做一个判断，否则链表只有一个元素会报错
                    self.link_head.next = to_delete_node.next
                    to_delete_node.next.pre = self.link_head
                to_delete_key = to_delete_node.key
                self.key_to_node_hash[to_delete_key] = None
                self.length = self.length - 1

            new_node = DLinkedNode(key, value)
            if not self.link_tail:
                # 如果链表还没有元素
                self.link_tail = new_node
                new_node.pre = self.link_head
                self.link_head.next = new_node
            else:
                # 如果链表已经有元素
                self.link_tail.next = new_node
                new_node.pre = self.link_tail
                self.link_tail = new_node
            self.length = self.length + 1
            self.key_to_node_hash[key] = new_node
            return

    def move_to_tail(self, node):
        if self.link_tail != node:
            # 如果不在链表尾部，插入链表尾部
            node.pre.next = node.next
            node.next.pre = node.pre
            node.next = None
            node.pre = self.link_tail
            self.link_tail.next = node
            self.link_tail = node
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

