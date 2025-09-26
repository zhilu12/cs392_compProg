from collections import deque

def bfs(building, start_r, start_c, n, m):
    """
    Breadth-first search to mark all connected empty cells as visited
    """
    
    queue = deque()
    queue.append((start_r, start_c))
        
    building[start_r][start_c] = "#"
    
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            
            if (
                (0 <= new_r < n)
                and (0 <= new_c < m)
                and building[new_r][new_c] == "."
            ):
                queue.append((new_r, new_c))
                building[new_r][new_c] = "#"
    
    

def count_rooms():
    """
    Main function to count the number of rooms in the building using BFS
    """
    # Read input
    n, m = map(int, input().split())
    building = []
    
    for _ in range(n):
        building.append(list(input().strip()))
    
    n_rooms = 0
    
    # Iterate through each cell
    for i in range(n):
        for j in range(m):
            if building[i][j] == '.':
                n_rooms += 1
                bfs(building, i, j, n, m)
    
    print(n_rooms)


if __name__ == "__main__":
    count_rooms()