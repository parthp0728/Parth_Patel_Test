# Question B

'''
Question B 

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of. 

'''


from typing import List

class Solution:
    def get_next_chunk(self, version: str, n: int, p: int) -> List[int]:
        """
        Get the next chunk of the version string.

        Parameters:
            version (str): The version string.
            n (int): The length of the version string.
            p (int): The current pointer position.

        Returns:
            Tuple[int, int]: The extracted chunk and the updated pointer position.
        """
        # if pointer is set to the end of string
        # return 0
        if p > n - 1:
            return 0, p
        
        # find the end of chunk
        p_end = p
        while p_end < n and version[p_end] != '.':
            p_end += 1
        # retrieve the chunk
        i = int(version[p:p_end]) if p_end != n - 1 else int(version[p:n])
        # find the beginning of next chunk
        p = p_end + 1
        
        return i, p

    def compare_versions(self, version1: str, version2: str) -> int:
        """
        Compare two version strings.

        Parameters:
            version1 (str): The first version string.
            version2 (str): The second version string.

        Returns:
            int: 1 if version1 > version2, -1 if version1 < version2, 0 if they are equal.
        """
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        
        # compare versions
        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)            
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal
        return 0
