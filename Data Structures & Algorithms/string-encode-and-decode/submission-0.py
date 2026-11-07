class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:

            result = result + str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
         
        i = 0

        while i < len(s):

            j=i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # The actual string starts after "#"
            start = j + 1

            # Take exactly 'length' characters
            word = s[start:start + length]

            # Add the decoded word
            result.append(word)

            # Move i to the beginning of the next encoded string
            i = start + length

        return result
