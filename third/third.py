'''
Question C 

At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:
1 - Simplicity. Integration needs to be dead simple.
2 - Resilient to network failures or crashes. 
3 - Near real time replication of data across Geolocation. Writes need to be in real time. 
4 - Data consistency across regions 
5 - Locality of reference, data should almost always be available from the closest region 
6 - Flexible Schema 
7 - Cache can expire
'''
import time

class Node:

    """
    Represents a node in the LRUCache.

    Attributes:
        _key: The key of the node.
        _value: The value associated with the key.
        _prev: Reference to the previous node in the linked list.
        _next: Reference to the next node in the linked list.
        _creation_time: Time when the node was created.
    """

    def __init__(self, key=None, value=None, prev=None, next=None):
        # Initialize a Node with a key, value, and references to previous and next nodes
        self._key = key
        self._value = value
        self._prev = prev
        self._next = next
        self._creation_time = time.time()  # Record the creation time of the node

    def getKey(self):
        # Get the key of the node
        return self._key

    def setKey(self, key=None):
        # Set the key of the node
        self._key = key

    def getValue(self):
        # Get the value of the node
        return self._value

    def setValue(self, value=None):
        # Set the value of the node
        self._value = value

    def getPrev(self):
        # Get the reference to the previous node
        return self._prev

    def setPrev(self, prev=None):
        # Set the reference to the previous node
        self._prev = prev

    def getNext(self):
        # Get the reference to the next node
        return self._next

    def setNext(self, next=None):
        # Set the reference to the next node
        self._next = next

    def isExpired(self, expiry):

        """
        Check if the node is expired.

        Args:
            expiry: Expiry time in seconds.

        Returns:
            True if the node is expired, False otherwise.
        """

        # Check if the node has expired based on the specified expiry time
        elapsedTime = time.time() - self._creation_time
        if (elapsedTime > expiry):
            return True
        else:
            return False

    def _repr_(self):
        # Representation of the Node object (used for debugging)
        return 'Node:{}, key:{}, value:{}, prev:{}, next:{}\n'.format(self._creation_time, self._key, self._value, self._prev, self._next)

class LRUCache:
    """
    Implements a Geo Distributed LRUCache with time expiration.

    Attributes:
        _max_capacity: Maximum capacity of the cache.
        _expiry: Expiry time in seconds for the nodes.
        _cache: Dictionary to store nodes.
        _head: Reference to the most recently used node.
        _tail: Reference to the least recently used node.
    """
    def __init__(self, max_capacity=10, expiry=3600):
        # Initialize the LRUCache with maximum capacity and expiry time for cache items
        self._max_capacity = max_capacity
        self._expiry = expiry
        self._cache = dict()  # Dictionary to store cache items
        self._head = None     # Reference to the most recently used item
        self._tail = None     # Reference to the least recently used item

    def get(self, key):
        # Get the value associated with the given key from the cache
        """
        Get the value associated with a key.

        Args:
            key: The key to lookup.

        Returns:
            The value associated with the key, or None if not found.
        """
        if (key in self._cache):
            node = self._cache[key]
            self.deleteFromList(node)  # Remove the node from its current position
            self.insertHead(node)      # Move the node to the front of the list
            return node.getValue()
        else:
            return None

    def deleteFromList(self, node):
        # Delete the given node from the list
        """
        Delete a node from the linked list.

        Args:
            node: The node to delete.
        """
        prevNode = node.getPrev()
        nextNode = node.getNext()
        if ((prevNode == None) and (nextNode == None)):
            # Node is the only one in the list
            self._head = None
            self._tail = None
        elif (prevNode == None):
            # Node is at the front of the list
            self._head = nextNode
            self._cache[self._head].setPrev(None)
        elif (nextNode == None):
            # Node is at the end of the list
            self._tail = prevNode
            self._cache[self._tail].setNext(None)
        else:
            # Node is in the middle of the list
            self._cache[prevNode].setNext(nextNode)
            self._cache[nextNode].setPrev(prevNode)

        del self._cache[node.getKey()]  # Remove the node from the cache dictionary

    def insertHead(self, node):
        # Insert the given node at the front of the list
        """
        Insert a node at the head of the linked list.

        Args:
            node: The node to insert.
        """
        node.setPrev(None)
        node.setNext(self.getHead())

        if (self.getLength() == 0):
            # The list is empty, so this node becomes the head and tail
            self._head = node.getKey()
            self._tail = node.getKey()
        else:
            # Update the previous node of the current head
            headNode = self._cache[self.getHead()]
            headNode.setPrev(node.getKey())

        self._head = node.getKey()  # Update the head reference
        self._cache[node.getKey()] = node  # Add the node to the cache dictionary

    def put(self, key, value):
        # Put a key-value pair into the cache
        """
        Insert or update a key-value pair in the cache.

        Args:
            key: The key.
            value: The value.
        """
        node = None
        if (key in self._cache):
            # Key already exists in the cache, update the value
            node = self._cache[key]
            node.setValue(value)
            self.deleteFromList(node)  # Move the node to the front of the list
        else:
            if (self.getLength() >= self._max_capacity):
                # Cache is at max capacity, remove the least recently used item
                self.deleteFromList(self._cache[self.getTail()])
            node = Node(key, value)  # Create a new node

        self.insertHead(node)  # Insert the node at the front of the list

    def removeExpiredNodes(self):
        # Remove expired nodes from the cache
        for node in list(self._cache.values()):
            if (node.isExpired(self._expiry)):
                self.deleteFromList(node)

    def getLength(self):
        # Get the current length of the cache
        return len(self._cache)

    def getHead(self):
        # Get the reference to the most recently used item
        return self._head

    def getTail(self):
        # Get the reference to the least recently used item
        return self._tail

    def _repr_(self):
        # Representation of the LRUCache object (used for debugging)
        output = "CACHE: Head:({}), Tail:({}), Content: ".format(self.getHead(), self.getTail())
        keyIterator = self.getHead()
        while (keyIterator != None):
            node = self._cache[keyIterator]
            output += '[key:{},value:{},prev:{},next:{}]-->'.format(
                node.getKey(), node.getValue(), node.getPrev(), node.getNext())
            keyIterator = node.getNext()

        return output

# Note: The _repr_ functions are used for debugging purposes and are not called automatically.
