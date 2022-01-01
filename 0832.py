class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        for i in range(row):
            for j in range(int((row+1)/2)):
                if image[i][j] == image[i][row -1 - j]:
                    image[i][j], image[i][row - 1 - j] = 1 - image[i][j], 1 - image[i][row - 1 - j]
        return image