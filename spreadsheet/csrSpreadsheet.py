from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


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
        self.sumA = []
        self.cols = 0
        self.rows = 0
        self.cells = []


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # TO BE IMPLEMENTED
        pass
        for cell in sorted(lCells, key=lambda c: (c.row, c.col)):
            if self.sumA == []:
                self.sumA.append( (0))
            self.sumA.append( (self.sumA[-1]) +  (cell.val))
            self.colA.append(cell.col)
            self.valA.append(cell.val)
            self.cols = cell.col + 1
            self.rows = cell.row + 1
            self.cells.append(cell)
        


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        pass
        self.rows += 1
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
        self.rows += 1
        for cell in sorted(self.cells, key=lambda c: (c.row, c.col)):
            if rowIndex < cell.row:
                cell.row += 1
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        self.cols += 1
        for cell in sorted(self.cells, key=lambda c: (c.row, c.col)):
            if colIndex < cell.col:
                cell.col += 1

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
        if rowIndex >= self.rows or colIndex >= self.cols:
            return False
        for cell in self.cells:
            if cell.row == rowIndex and cell.col == colIndex:
                old_value = cell.val
                cell.val = value
                for i in range(rowIndex, len(self.sumA)):
                    self.sumA[i] += value - old_value
                return True
        self.cells.append(Cell(rowIndex, colIndex, value))
        

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return self.rows


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
        
        result = []
        for cell in self.cells:
            if cell.val == value:
                result.append((cell.row, cell.col))
        
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return result




    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        # TO BE IMPLEMENTED
        
        result = []
        for cell in self.cells:
            result.append(cell)
        result.sort(key=lambda c: (c.row, c.col))
        return result

