#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty.
        Running time: O(1) to check .head and .tail"""
        return self.head is None and self.tail is None

    def length(self):
        """
        Return the length of this linked list by traversing its nodes.
        Running time: worst case O(n) if traversing nodes,
        best case O(1) if using .size property
        """
        count = 0
        current = self.head
        while(current != None):
            count += 1
            current = current.next
        return count

    def append(self, item):
        """
        Insert the given item at the tail of this linked list.
        Running time: O(1) to manipulate .tail property
        """

        # Created a new node to hold given item
        last_node = Node(item)
        # append at the beginning if the linked list is empty
        if(self.head == None):
            self.head = last_node
            self.tail = self.head
        # else if append at the end using tail
        else:
            self.tail.next = last_node
            self.tail = self.tail.next

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list.
        Running time: O(1) to manipulate .head property
        """

        # Create new node to hold given item
        new_head = Node(item)
        # prepend if the head pointing to none
        if(self.head == None):
            self.head = new_head
            self.tail = self.head
        # else new_head points to head node and head points new node
        else:
            new_head.next = self.head
            self.head = new_head

    def find(self, quality):
        """
        Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if looking for item at or near head
        Worst case running time: O(n) if looking for item in the middle 
        or near tail or not present in the linked list
        """

        node = self.head
        while (node != None):
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if looking for item at or near head
        Worst case running time: O(n) if looking for item in the middle 
        or near tail or not present in the linked list
        """

        # current = None
        cur_node = self.head
        prev_node = None
        while cur_node is not None:
            if cur_node.data == item:
                if cur_node.next is None:
                    self.tail = prev_node
                if prev_node is not None:
                    prev_node.next = cur_node.next
                    return self.head
                else:
                    self.head = cur_node.next
                    return self.head
            prev_node = cur_node
            cur_node = cur_node.next
        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
