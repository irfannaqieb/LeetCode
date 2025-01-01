class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        current_color = image[sr][sc]
        new_color = color

        # Get the dimensions of the image
        height = len(image)
        width = len(image[0])

        # DFS function to perform the flood fill
        def dfs(sr, sc):
            if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == current_color and image[sr][sc] != new_color:
                
                # Change the color of the current cell
                image[sr][sc] = new_color

                # Perform recursive calls
                dfs(sr + 1, sc)
                dfs(sr - 1, sc)
                dfs(sr, sc + 1)
                dfs(sr, sc - 1)
        
        # Start DFS from the source cell
        dfs(sr, sc)

        return image