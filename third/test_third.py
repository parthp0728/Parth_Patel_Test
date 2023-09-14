import unittest
import time
from third import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_basic_put_get(self):
        # Test Case 1: Basic Put and Get
        cache = LRUCache(5)
        cache.put(1, "one")
        self.assertEqual(cache.get(1), "one")

    def test_over_capacity(self):
        # Test Case 2: Cache exceeds maximum capacity
        cache = LRUCache(2)
        cache.put(1, "one")
        cache.put(2, "two")
        cache.put(3, "three")

        self.assertIsNone(
            cache.get(1)
        )  # 'one' should be evicted since the capacity is 2
        self.assertEqual(cache.get(2), "two")
        self.assertEqual(cache.get(3), "three")

    def test_lru_order(self):
        # Test Case 3: Testing Least Recently Used order
        cache = LRUCache(3)
        cache.put(1, "one")
        cache.put(2, "two")
        cache.put(3, "three")

        # Access 'one', making it the most recently used
        cache.get(1)

        cache.put(4, "four")  # This should evict 'two' as it is the least recently used
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(1), "one")

    def test_update_existing_key(self):
        # Test Case 4: Updating an existing key
        cache = LRUCache(2)
        cache.put(1, "one")
        cache.put(1, "updated_one")
        self.assertEqual(cache.get(1), "updated_one")

    def test_expiry(self):
        # Test Case 5: Testing Node Expiry
        cache = LRUCache(5, expiry=1)  # 1 second expiry
        cache.put(1, "one")
        time.sleep(2)  # Wait for more than the expiry time
        cache.removeExpiredNodes()  # Explicitly removing expired nodes
        self.assertIsNone(cache.get(1))

    def test_no_expiry(self):
        # Test Case 6: No Node Expiry
        cache = LRUCache(5, expiry=10)
        cache.put(1, "one")
        self.assertEqual(cache.get(1), "one")

    def test_remove_from_middle(self):
        # Test Case 7: Removing Node from the middle
        cache = LRUCache(3)
        cache.put(1, "one")
        cache.put(2, "two")
        cache.put(3, "three")

        cache.get(1)  # Access 'one' to bring it to front
        cache.get(3)  # Access 'three' to make 'two' least recently used

        cache.put(4, "four")  # This should evict 'two'

        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(1), "one")
        self.assertEqual(cache.get(3), "three")

    def test_insert_head_tail(self):
        # Test Case 8: Insert Head and Tail
        cache = LRUCache(1)
        cache.put(1, "one")
        self.assertEqual(cache.getHead(), 1)
        self.assertEqual(cache.getTail(), 1)
    
    def test_edge_cases(self):
        # Test Case 9: Additional Edge Cases
        
        # Test Case 1: Test empty cache
        cache = LRUCache(5)
        self.assertIsNone(cache.get(1), "Test Case 1 Failed")

        # Test Case 2: Test removing expired nodes without any expired nodes
        cache = LRUCache(5, expiry=1)
        cache.put(1, "one")
        time.sleep(2)  # Wait for expiry
        cache.removeExpiredNodes()
        self.assertEqual(cache.get(1), None, "Test Case 2 Failed")

        # Test Case 3: Test removing expired nodes with expired nodes
        cache = LRUCache(5, expiry=1)
        cache.put(1, "one")
        time.sleep(2)  # Wait for expiry
        cache.put(2, "two")
        cache.removeExpiredNodes()
        self.assertIsNone(cache.get(1), "Test Case 3 Failed")
        self.assertEqual(cache.get(2), "two", "Test Case 3 Failed")

    def suite():
        # Create a suite of all the test cases
        suite = unittest.TestSuite()
        suite.addTest(TestLRUCache("test_basic_put_get"))
        suite.addTest(TestLRUCache("test_over_capacity"))
        suite.addTest(TestLRUCache("test_lru_order"))
        suite.addTest(TestLRUCache("test_update_existing_key"))
        suite.addTest(TestLRUCache("test_expiry"))
        suite.addTest(TestLRUCache("test_no_expiry"))
        suite.addTest(TestLRUCache("test_remove_from_middle"))
        suite.addTest(TestLRUCache("test_insert_head_tail"))

        # Add new test cases
        suite.addTest(TestLRUCache("test_edge_cases"))

        return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestLRUCache.suite())
    unittest.main()
