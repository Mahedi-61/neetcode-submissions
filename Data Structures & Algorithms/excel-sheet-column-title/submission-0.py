class Solution:
    def get_letter(self, col_number):
        return chr(ord('A') - 1 + col_number)


    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while (columnNumber >= 27):
            res += self.get_letter(columnNumber % 26) 
            columnNumber = columnNumber // 26 
        
        if columnNumber < 27: 
            res += self.get_letter(columnNumber)
            
        return res[::-1] 