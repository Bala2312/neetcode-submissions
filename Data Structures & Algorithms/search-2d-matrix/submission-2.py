class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        column = len(matrix[0]) - 1      # CHANGE 1: Last valid column index

        while row < len(matrix):         # CHANGE 2: Don't use while True

            if matrix[row][column] >= target:    # CHANGE 3: >= instead of >

                for c in range(column + 1):      # CHANGE 4: Include last column
                    if matrix[row][c] == target:
                        return True

                return False                     # CHANGE 5: Target not in this row

            else:
                row += 1

        return False                            # CHANGE 6: Target larger than all rows