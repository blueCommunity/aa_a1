from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        pass
        self.spreadsheet = []
        


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # TO BE IMPLEMENTED 
        pass
        for cell in lCells:
            for row in range(cell.rows +1):
                if row >= len(self.spreadsheet):
                    self.spreadsheet.append([])
                for col in range(cell.cols+ 1):
                    if col >= len(self.spreadsheet[row]):
                        self.spreadsheet[row].append(None)
            self.spreadsheet[cell.row][cell.col] = cell.val

    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        pass
        temp = []
        for col in range(len(self.spreadsheet[0])):
            temp.append(None)
        self.spreadsheet.append(temp)
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        pass
        for col in range(len(self.spreadsheet)):
            self.spreadsheet[col].append(None)
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # TO BE IMPLEMENTED
        pass
        if rowIndex < 0 or rowIndex > len(self.spreadsheet):
            return False
        temp = []
        for col in range(len(self.spreadsheet[0])):
            temp.append(None)
        self.spreadsheet.insert(rowIndex, temp)
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        # TO BE IMPLEMENTED
        pass
        if colIndex < 0 or colIndex > len(self.spreadsheet[0]):
            return False
        for col in range(len(self.spreadsheet)):
            self.spreadsheet[col].insert(colIndex, None)
        
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED
        pass
        if rowIndex < 0 or rowIndex + 1 > len(self.spreadsheet) or colIndex < 0 or colIndex + 1 > len(self.spreadsheet[0]):
            return False
        self.spreadsheet[rowIndex][colIndex] = value

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return len(self.spreadsheet)


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return len(self.spreadsheet[0])



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED
        pass
        result = []
        for row in range(len(self.spreadsheet)):
            for col in range(len(self.spreadsheet[0])):
                if self.spreadsheet[row][col] == value:
                    result.append((row, col))

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return result



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # TO BE IMPLEMENTED
        pass
        result = []
        for row in range(len(self.spreadsheet)):
            for col in range(len(self.spreadsheet[0])):
                if self.spreadsheet[row][col] != None:
                    result.append(Cell(row, col, self.spreadsheet[row][col]))

        # TO BE IMPLEMENTED
        return result
    

        
