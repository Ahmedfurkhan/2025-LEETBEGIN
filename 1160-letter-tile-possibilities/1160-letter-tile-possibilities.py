class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)  # Count occurrences of each letter
        
        def backtrack():
            total_sequences = 0
            for letter in count:
                if count[letter] > 0:  # If the letter is available, use it
                    total_sequences += 1  # Count this sequence
                    count[letter] -= 1  # Use the letter
                    total_sequences += backtrack()  # Recursive call to continue forming sequences
                    count[letter] += 1  # Backtrack (restore the letter)
            return total_sequences
        
        return backtrack()