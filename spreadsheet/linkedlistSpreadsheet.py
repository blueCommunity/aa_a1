from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


class ListNode:
    def __init__(self, cell: Cell, prev=None, next=None,prev_row=None, next_row=None):
        self.cell = cell
        self.prev = prev
        self.next = next
        self.prev_row = prev_row
        self.next_row = next_row

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # first node in the linked list
        self.head = None
        # last node in the linked list
        self.tail = None
        self.rows = 0
        self.cols = 0


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        for cell in sorted(lCells, key=lambda c: (c.row, c.col)):
            new_node = ListNode(cell)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                if cell.row != self.tail.cell.row:
                    new_node.prev_row = self.tail
                    self.tail.next_row = new_node
                    self.tail = new_node
                else:
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node

            self.rows = max(self.rows, cell.row + 1)
            self.cols = max(self.cols, cell.col + 1)

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """
        self.rows += 1
        return True


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        self.cols += 1
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if rowIndex < 0 or rowIndex > self.rows:
            return False

        head = self.head
        while head is not None:
            if head.cell.row >= rowIndex:
                head.cell.row += 1
            if head.next_row is not None:
                head = head.next_row
            else:
                head = head.next

        self.rows += 1
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """
        if colIndex < 0 or colIndex > self.cols:
            return False

        head = self.head
        while head is not None:
            row_node = head
            while row_node is not None:
                if row_node.cell.col >= colIndex:
                    row_node.cell.col += 1
                row_node = row_node.next
            head = head.next_row

        self.cols += 1
        return True


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        head = self.head
        while head is not None:
            if head.cell.row == rowIndex and head.cell.col == colIndex:
                head.cell.val = value
                return True
            if head.next_row is not None and head.cell.row < rowIndex:
                head = head.next_row
            else:
                head = head.next

        if rowIndex < self.rows and colIndex < self.cols:
            new_cell = Cell(rowIndex, colIndex, value)
            self.buildSpreadsheet([new_cell])
            return True
        return False


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        return self.rows

    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        return self.cols



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        result = []
        head = self.head
        while head is not None:
            if head.cell.val == value:
                result.append((head.cell.row, head.cell.col))
            if head.next_row is not None:
                head = head.next_row
            else:
                head = head.next
        return result


    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        result = []
        head = self.head
        while head is not None:
            if head.cell.val is not None:
                result.append(head.cell)
            if head.next_row is not None:
                head = head.next_row
            else:
                head = head.next
        result.sort(key=lambda c: (c.row, c.col))
        return result
