class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        count = 0
        total = 0
        rows = len(img)
        cols = len(img[0])
        if rows ==1 and cols==1:
            return img

        for i in range(rows):
            row = []
            for j in range(cols):
                if 0 <= i-1 < rows and 0 <= j-1 < cols:
                    total += img[i-1][j-1]
                    count += 1
                if 0 <= i-1 < rows and 0 <= j < cols:
                    total += img[i-1][j]
                    count += 1
                if 0 <= i-1 < rows and 0 <= j+1 < cols:
                    total += img[i-1][j+1]
                    count += 1
                if 0 <= i < rows and 0 <= j-1 < cols:
                    total += img[i][j-1]
                    count += 1
                if 0 <= i < rows and 0 <= j < cols:
                    total += img[i][j]
                    count += 1
                if 0 <= i < rows and 0 <= j+1 < cols:
                    total += img[i][j+1]
                    count += 1
                if 0 <= i+1 < rows and 0 <= j-1 < cols:
                    total += img[i+1][j-1]
                    count += 1
                if 0 <= i+1 < rows and 0 <= j < cols:
                    total += img[i+1][j]
                    count += 1
                if 0 <= i+1 < rows and 0 <= j+1 < cols:
                    total += img[i+1][j+1]
                    count += 1

                row.append(total // count)
                total = 0
                count = 0
            ans.append(row)

        return ans
