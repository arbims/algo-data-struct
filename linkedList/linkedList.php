<?php

class Node {
    public $data;
    public $next;

    public function __construct(string $data)
    {
        $this->data = $data;
        $this->next = null;
    }

}

class LinlkedList {
    private $head = NULL;
    
    public function insertAtBegining($newData)
    {
        $newNode = new Node($newData);
        if ($this->head == null) {
            return $newNode;
        }
        $newNode->next = $this->head;
        return $this->head = $newNode;
    }

    public function insertAtEnd($newData)
    {
        $newNode = new Node($newData);
        if ($this->head == null)  {
            $this->head = $newNode;
            return;
        } 
        
        $currentNode = $this->head;
        while ($currentNode->next !== null) {
            $currentNode = $currentNode->next;
        }
        $currentNode->next = $newNode;
    }

    public function deleteNode($data) {
        $current = $this->head;
        $prev = null;
        while($current !== null) {
            if ($current->data === $data) {
                if ($prev === null) {
                    $this->head = $current->next;
                } else {
                    $prev->next = $current->next;
                }
                return;
            }
            $prev = $current;
            $current = $current->next;
        }
    }

    function printLinkedList() {
        $current = $this->head;
        while($current !== null) {
            echo $current->data . "\n";
            $current = $current->next;
        }
    }
}

$linkedList = new LinlkedList();
$linkedList->insertAtEnd('B');
$linkedList->insertAtEnd('C');
$linkedList->insertAtBegining('A');
$linkedList->deleteNode('B');

print_r($linkedList->printLinkedList());