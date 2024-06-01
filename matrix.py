def num_holes(strArr):
    # Convert input strings to 2D matrix of integers
    matrix = [list(map(int, row.strip())) for row in strArr]
    rows, cols = len(matrix), len(matrix[0])
    
    def dfs(r, c):
        # If out of bounds or not a 0, return
        if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] != 0:
            return
        # Mark the cell as visited
        matrix[r][c] = -1
        # Explore neighbors in all four directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    holes_count = 0
    
    # Iterate through the matrix to find unvisited 0s
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:  # Found a new region of 0s
                holes_count += 1
                dfs(r, c)  # Perform DFS to mark all contiguous 0s
    
    return holes_count

# Example usage
strArr = ["10111", "10101", "11101", "11111"]
print(num_holes(strArr))  # Output: 2
