from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell
from decimal import Decimal

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------




class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        pass
        self.colA = []
        self.valA = []
        self.sumA = [0]
        self.cols = 0


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # TO BE IMPLEMENTED
        pass
        for cell in sorted(lCells, key=lambda c: (c.row, c.col)):
            if cell.row > len(self.sumA):
                for i in range(len(self.sumA), cell.row + 1):
                    self.sumA.append(self.sumA[-1])
            self.sumA.append( (self.sumA[-1]) +  (cell.val))
            self.colA.append(cell.col)
            self.valA.append(cell.val)
            self.cols = cell.col + 1
        
        print(self.colA,self.valA,self.sumA)


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        pass
        
        self.sumA.append( (self.sumA[-1]))

        return True
        


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        pass
        self.cols += 1
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if rowIndex >= len(self.sumA) or rowIndex < 0:
            return False
        self.sumA.insert(rowIndex + 1, self.sumA[rowIndex])
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        self.cols += 1
        for i in range(len(self.colA)):
            if self.colA[i] >= colIndex:
                self.colA[i] += 1

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True



    def update(self, rowIndex: int, colIndex: int, value:  float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are  s.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        # TO BE IMPLEMENTED
        #update

        if rowIndex >= len(self.sumA) - 1 or colIndex >= self.cols:
            return False
        
        j =0
        temp = 0
        rowA = []
        for i in range(len(self.sumA)):
            if i > 0 and self.sumA[i] != self.sumA[i-1]:
                while(temp != self.sumA[i] and j < len(self.colA)):
                    temp += self.valA[j]
                    rowA.append(i - 1)
                    j += 1
        
        for i in range(len(rowA)):
            if rowA[i] == rowIndex and self.colA[i] == colIndex:
                temp = self.valA[i]
                self.valA[i] = value
                for j in range(rowIndex + 1 , len(self.sumA)):
                    self.sumA[j] += value - temp
                print(self.colA,self.valA,self.sumA, rowA)
                return True


        #insert
        for i in range(len(rowA)):
            if rowA[i] == rowIndex:
                if self.colA[i] > colIndex:
                    self.colA.insert(i, colIndex)
                    self.valA.insert(i, value)
                    for j in range(rowIndex + 1, len(self.sumA)):
                        self.sumA[j] += value - self.valA[i]
                    return True
            
        
        for i in range(len(rowA)):
            if rowA[i] > rowIndex:
                self.colA.insert(i, colIndex)
                self.valA.insert(i, value)
                for j in range(rowIndex + 1, len(self.sumA)):
                    self.sumA[j] += value
                return True
        self.colA.insert(len(rowA), colIndex)
        self.valA.insert(len(rowA), value)
        for j in range(rowIndex + 1, len(self.sumA)):
            self.sumA[j] += value
        return True
        
        #call to (2,5,-2.00)

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return len(self.sumA) - 1


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return self.cols




    def find(self, value: float ) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED
        # view the cell in valueA and colA, we can get the value and col of the cell
        # then view the cell in sumA, we can get the row of the cell
        
        j =0
        temp = 0
        rowA = []
        result = []
        for i in range(len(self.sumA)):
            if i > 0 and self.sumA[i] != self.sumA[i-1]:
                while(temp != self.sumA[i] and j < len(self.colA)):
                    temp += self.valA[j]
                    rowA.append(i - 1)
                    j += 1
        
        for i in range(len(self.valA)):
            if self.valA[i] == value:
                result.append((rowA[i], self.colA[i]))
        
        
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return result




    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        # TO BE IMPLEMENTED
        # view the cell in valueA and colA, we can get the value and col of the cell
        # then view the cell in sumA, we can get the row of the cell

        j =0
        temp = 0
        rowA = []
        result = []
        tolerance = 1e-10
        for i in range(len(self.sumA)):
            if i > 0 and self.sumA[i] != self.sumA[i-1]:
                while(abs(temp - self.sumA[i]) > tolerance and j < len(self.colA)):
                    temp += self.valA[j]
                    rowA.append(i - 1)
                    j += 1

        for i in range(len(self.valA)):
            cell = Cell(rowA[i], self.colA[i], self.valA[i])
            result.append(cell)
        result.sort(key=lambda c: (c.row, c.col))
        print(self.colA,self.valA,self.sumA, rowA)
        return result

