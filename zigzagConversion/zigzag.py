class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s
        currentRow = 0
        previousRow = 0
        rows = [""] * numRows
        for i in range(len(s)) :
            temp = currentRow
            rows[currentRow] += s[i]
            if (currentRow == previousRow + 1) or (currentRow == previousRow) :
                if currentRow == numRows - 1 :
                    currentRow -= 1
                else :
                    currentRow += 1
            elif currentRow == previousRow - 1 :
                if currentRow == 0 :
                    currentRow += 1
                else : 
                    currentRow -= 1
            previousRow = temp
        return "".join(rows)
