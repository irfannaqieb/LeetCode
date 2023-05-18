class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = "0123456789abcdefghijklmnopqrstuvwxyz"
        arr = []

        lowercase_converted = s.lower()

        for c in lowercase_converted:
            if c in characters:
                arr.append(c)

        joined_characters = "".join(arr)

        return joined_characters == joined_characters[::-1]
