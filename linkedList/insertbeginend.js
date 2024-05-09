insertAtBegining(head, newData)
    {
        const node = new Node(newData)
        if (head == null) {
            return node
        }
        node.next = head
        return node
    }
    //Function to insert a node at the end of the linked list.
    insertAtEnd(head, newData)
    {
        const node = new Node(newData)
        if (head == null) return node
        
        let oldTail = head
        while (oldTail.next !== null) {
            oldTail = oldTail.next
        }
        oldTail.next = node
        node.next = null
        return head
    }