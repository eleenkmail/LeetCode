class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        current_color = image[sr][sc]

        if current_color != color:
            self.DFS(sr, sc, image, current_color, color)
               
        return image
        

    def DFS(self, i, j, image, current_color, color):

        image[i][j] = color
 
        
        if i - 1 >= 0 and image[i - 1][j] == current_color:
            self.DFS(i - 1, j, image, current_color, color)
        if i + 1 < len(image) and image[i + 1][j] == current_color:
            self.DFS(i + 1, j, image, current_color, color)
        if j - 1 >= 0 and image[i][j - 1] == current_color:
            self.DFS(i, j - 1, image, current_color, color)
        if j + 1 < len(image[0]) and image[i][j + 1] == current_color:
            self.DFS(i, j + 1, image, current_color, color)
        