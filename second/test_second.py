import unittest
from second import Solution

class TestVersionComparison(unittest.TestCase):

    # Test case: Versions are equal
    def test_versions_equal(self):
        solution = Solution()
        # Both version strings are "5.6"
        # Expected result: 0 (equal)
        self.assertEqual(solution.compare_versions("5.6", "5.6"), 0)

    # Test case: version1 > version2
    def test_version1_greater(self):
        solution = Solution()
        # version1 = "5.6", version2 = "5.5"
        # Expected result: 1 (version1 is greater)
        self.assertEqual(solution.compare_versions("5.6", "5.5"), 1)
        
    # Test case: version1 < version2
    def test_version1_smaller(self):
        solution = Solution()
        # version1 = "5.5", version2 = "5.6"
        # Expected result: -1 (version1 is smaller)
        self.assertEqual(solution.compare_versions("5.5", "5.6"), -1)

    # Test case: Longer version1 > version2
    def test_longer_version_greater(self):
        solution = Solution()
        # version1 = "5.6.1", version2 = "5.6"
        # Expected result: 1 (version1 is greater)
        self.assertEqual(solution.compare_versions("5.6.1", "5.6"), 1)

    # Test case: version1 < Longer version2
    def test_longer_version_smaller(self):
        solution = Solution()
        # version1 = "5.6", version2 = "5.6.1"
        # Expected result: -1 (version1 is smaller)
        self.assertEqual(solution.compare_versions("5.6", "5.6.1"), -1)

    # Test case: Extra zeros in version1
    def test_version_with_extra_zeros(self):
        solution = Solution()
        # version1 = "5.6.0", version2 = "5.6"
        # Expected result: 0 (equal)
        self.assertEqual(solution.compare_versions("5.6.0", "5.6"), 0)
        
    # Test case: Leading zeros in version1
    def test_versions_with_leading_zeros(self):
        solution = Solution()
        # version1 = "05.006", version2 = "5.6"
        # Expected result: 0 (equal)
        self.assertEqual(solution.compare_versions("05.006", "5.6"), 0)

    # Test case: Multiple zeros in version1
    def test_versions_with_multiple_zeros(self):
        solution = Solution()
        # version1 = "5.6.000", version2 = "5.6"
        # Expected result: 0 (equal)
        self.assertEqual(solution.compare_versions("5.6.000", "5.6"), 0)

    # Test case: Versions with same length but different values
    def test_versions_with_same_length_but_different_values(self):
        solution = Solution()
        # version1 = "5.6.1", version2 = "5.6.2"
        # Expected result: -1 (version1 is smaller)
        self.assertEqual(solution.compare_versions("5.6.1", "5.6.2"), -1)

    # Test case: Versions with same length and same values
    def test_versions_with_same_length_and_same_values(self):
        solution = Solution()
        # version1 = "5.6.2", version2 = "5.6.2"
        # Expected result: 0 (equal)
        self.assertEqual(solution.compare_versions("5.6.2", "5.6.2"), 0)

    # Test case: Versions with heterogeneous chunk lengths
    def test_versions_with_heterogeneous_chunk_lengths(self):
        solution = Solution()
        # version1 = "5.06.2", version2 = "5.6.2"
        # Expected result: 0 (equal)
        self.assertEqual(solution.compare_versions("5.06.2", "5.6.2"), 0)

if __name__ == "__main__":
    unittest.main()
