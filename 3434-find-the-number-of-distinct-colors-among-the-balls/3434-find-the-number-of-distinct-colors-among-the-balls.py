class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Maps ball to its current color
        color_count = {}  # Maps color to the number of balls with that color
        distinct_colors = set()  # Tracks distinct colors
        result = []

        for x, y in queries:
            # If the ball already has a color, update its previous color's count
            if x in ball_colors:
                prev_color = ball_colors[x]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    distinct_colors.discard(prev_color)
            
            # Assign the new color to the ball
            ball_colors[x] = y
            color_count[y] = color_count.get(y, 0) + 1
            distinct_colors.add(y)
            
            # Record the number of distinct colors
            result.append(len(distinct_colors))
        
        return result