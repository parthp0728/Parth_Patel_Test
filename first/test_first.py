import unittest
from first import is_overlapping

class TestIsOverlapping(unittest.TestCase):

    # Test case for lines with positive numbers that overlap
    def test_positive_numbers_overlap(self):
        self.assertTrue(is_overlapping((1,5), (2,6)))

    # Test case for lines with positive numbers that do not overlap
    def test_positive_numbers_no_overlap(self):
        self.assertFalse(is_overlapping((1,5), (6,8)))

    # Test case for lines with negative numbers that overlap
    def test_negative_numbers_overlap(self):
        self.assertTrue(is_overlapping((-5,-3), (-4,-3.5)))

    # Test case for lines with negative numbers that do not overlap
    def test_negative_numbers_no_overlap(self):
        self.assertFalse(is_overlapping((-5,-3), (-2,-1)))

    # Test case for lines with mixed positive and negative numbers that overlap
    def test_mixed_numbers_overlap(self):
        self.assertTrue(is_overlapping((-5,3), (-4,2)))

    # Test case for lines with mixed positive and negative numbers that do not overlap
    def test_mixed_numbers_no_overlap(self):
        self.assertFalse(is_overlapping((-5,-3), (1,2)))

    # Test case for lines with touching points that overlap
    def test_touching_points(self):
        self.assertTrue(is_overlapping((-5,-3), (-3,-2)))

    # Test case for lines with common endpoint that overlap
    def test_overlapping_lines_with_common_endpoint(self):
        self.assertTrue(is_overlapping((1, 5), (5, 10)))

    # Test case for lines with one inside another that overlap
    def test_overlapping_lines_one_inside_another(self):
        self.assertTrue(is_overlapping((1, 10), (3, 6)))

    # Test case for lines with the same endpoint that overlap
    def test_overlapping_lines_same_endpoint(self):
        self.assertTrue(is_overlapping((1, 5), (5, 10)))

    # Test case for lines with the same endpoint that do not overlap
    def test_lines_do_not_overlap_same_endpoint(self):
        self.assertFalse(is_overlapping((1, 5), (6, 10)))

    # Test case for lines with opposite directions that do not overlap
    def test_lines_do_not_overlap_opposite_directions(self):
        self.assertFalse(is_overlapping((1, 5), (-5, -1)))

if __name__ == "__main__":
    unittest.main()
