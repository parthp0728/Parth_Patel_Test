# Parth_Patel_Test
This repository contains solutions to the assigned tasks: Line Overlap check, Version Comparison, and Geo Distributed LRU Cache.

Question A - Line Overlap Check (first.py) and (test_first.py)
The objective is to determine whether two lines on the x-axis overlap.

Usage:
from first import is_overlapping

result = is_overlapping((1, 5), (2, 6))
print(result)  # True
Test Cases:
The following are some sample test cases and their expected outputs:

(1,5) and (2,6): The output should be true as both lines overlap
(1, 5), (5, 10): The output will be true as there is common point that will overlap

Question B - Version String Comparison
The library compares two version strings and determines which one is greater or lesser.

Usage:
from second import Solution

  # version1 = "5.6.1", version2 = "5.6"
  # Expected result: 1 (version1 is greater)
  self.assertEqual(solution.compare_versions("5.6.1", "5.6"), 1)
  
  # version1 = "5.6", version2 = "5.6.1"
  # Expected result: -1 (version1 is smaller)
  self.assertEqual(solution.compare_versions("5.6", "5.6.1"), -1)
  
  # version1 = "05.006", version2 = "5.6"
  # Expected result: 0 (equal)
  self.assertEqual(solution.compare_versions("05.006", "5.6"), 0)Test Cases:
  
The following are some sample test cases and their expected outputs:

"5.6.1" vs "5.6": The output should be 1, meaning 5.6.1 is greater than 5.6.
"5.6" vs "5.6.1": The output should be -1, meaning 5.6 is less than 5.6.1.
"05.006" vs "5.6": The output should be 0, meaning the versions are equal.

Question C - Geo Distributed LRU Cache
This solution presents an LRU Cache implementation that can evict data after a certain expiration time.

Implementation Overview:
Node Class: Represents a node in the doubly linked list. Each node has key, value, creation time, next and previous references.
LRUCache Class: Represents the main LRU Cache. Implemented using a dictionary and doubly linked list. The dictionary provides O(1) access to any node using its key, and the linked list maintains the order of use of the nodes.
Main Methods:
get(key): Returns the value associated with the key if it's in the cache and not expired. If the key isn't present, it returns None.
put(key, value): Inserts or updates the value for the given key in the cache. If the cache is at its maximum capacity, it will evict the least recently used item or an expired item.
removeExpiredNodes(): Explicitly checks and removes any expired nodes from the cache.
Usage:
Navigate to the third folder to find the cache implementation. You can use the LRUCache class in your application as shown:

from geo_LRU_Cache import LRUCache

# Initialize cache with a capacity of 5 and an expiry time of 10 seconds
cache = LRUCache(5, 10)

# Put some values
cache.put('a', 1)
cache.put('b', 2)

# Retrieve a value
print(cache.get('a'))  # Should print 1

# ... after 10 seconds
print(cache.get('a'))  # Should print None since it's expired
Further Improvements:
Geo Distribution: The current solution doesn't address data replication across multiple geolocations in real-time. One possible way to achieve this is using a distributed system design, such as the publisher-subscriber model, where updates to one cache can be published and then replicated to caches in other regions.
Network Resilience: The solution should be resilient to network failures or crashes. This can be achieved using techniques like retry mechanisms, circuit breakers, and backup caches.
Tests Documentation
Question A - Line Overlaps
Located in the first folder.

Test File: test_lines_overlap.py

Tests Overview:
test_positive_numbers_overlap: Tests if two lines with positive numbers overlap.
test_positive_numbers_no_overlap: Tests if two lines with positive numbers don't overlap.
test_negative_numbers_overlap: Tests if two lines with negative numbers overlap.
test_negative_numbers_no_overlap: Tests if two lines with negative numbers don't overlap.
test_mixed_numbers_overlap: Tests if two lines with both negative and positive numbers overlap.
test_mixed_numbers_no_overlap: Tests if two lines with both negative and positive numbers don't overlap.
test_touching_points: Tests if two lines touch at a single point.
Usage:
Navigate to the first folder. You can run the test cases as shown:

python -m unittest test_lines_overlap.py
Question B - Version Comparator
Located in the second folder.

Test File: test_version_comparator.py

Tests Overview:
test_versions_equal: Tests if two versions are equal.
test_version1_greater: Tests if the first version is greater than the second version.
test_version1_smaller: Tests if the first version is smaller than the second version.
test_longer_version_greater: Tests if a version with an extra sub-version (like 1.2.1) is greater than a shorter version (like 1.2).
test_longer_version_smaller: Tests if a shorter version (like 1.2) is smaller than a longer version with an extra sub-version (like 1.2.1).
test_version_with_extra_zeros: Tests if the version number remains the same when followed by a ".0".
test_versions_with_leading_zeros: Tests if leading zeros do not affect the version comparison.
Usage:
Navigate to the second folder. You can run the test cases as shown:

python -m unittest test_version_comparator.py
Question C - Geo LRU Cache
Located in the third folder.

Test File: test_LRU_cache.py

Tests Overview:
test_basic_put_get: Verifies basic operations of putting an element in the cache and then retrieving it.
test_over_capacity: Tests the eviction policy of the cache by inserting more elements than its capacity.
test_lru_order: Checks the Least Recently Used (LRU) eviction policy of the cache to ensure elements are evicted in the correct order.
test_update_existing_key: Tests if updating the value of an existing key works as expected.
test_expiry: Tests the expiration of cache nodes based on a given time frame.
test_no_expiry: Checks if an item does not expire before the set expiry time.
test_remove_from_middle: Validates the LRU eviction policy by accessing elements and making sure the middle element gets evicted.
test_insert_head_tail: Ensures that when a single item is added to the cache, it acts as both the head and the tail.
Usage:
Navigate to the third folder. You can run the test cases as shown:

python -m unittest test_LRU_cache.py
