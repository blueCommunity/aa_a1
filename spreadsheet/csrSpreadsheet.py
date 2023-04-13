from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


# ------------------------------------------------------------------------
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------


class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        pass

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        
        """

        # TO BE IMPLEMENTED
        for cell in lCells:
            word = cell.getContent()  # 获取单元格的内容
        self.insert(word)  # 插入单元格内容到Trie树中

    def appendRow(self):
        """
       
        """

        # TO BE IMPLEMENTED
        if self.grid is None:
            return False  # 若电子表格为空则返回False

        empty_row = [''] * len(self.grid[0])  # 创建一个空行

        self.grid.append(empty_row)  # 将空行追加到电子表格的末尾

        return True  # 操作成功返回True

    def appendCol(self):
        """
        
        """

        # TO BE IMPLEMENTED
        if self.grid is None:
            return False  # 若电子表格为空则返回False

        for row in self.grid:
            row.append('')  # 将空字符追加到每一行的末尾，表示添加一个空列

        return True  # 操作成功返回True

    def insertRow(self, rowIndex: int) -> bool:

        # REPLACE WITH APPROPRIATE RETURN VALUE
        if rowIndex < 0 or rowIndex > self.rowNum():  # 判断 rowIndex 是否合法
            return False  # 若 rowIndex 不合法则返回 False

        new_row = [''] * self.colNum()  # 创建一个与已有行列数相同的空行

        self.grid.insert(rowIndex + 1, new_row)  # 在指定的位置插入新行

        return True  # 操作成功返回 True

    def insertCol(self, colIndex: int) -> bool:
        """

         """

        # REPLACE WITH APPROPRIATE RETURN VALUE
        if colIndex < 0 or colIndex > self.colNum():  # 判断 colIndex 是否合法
            return False  # 若 colIndex 不合法则返回 False

        for row in self.grid:
            row.insert(colIndex + 1, '')  # 在每一行的指定位置插入空字符

        return True  # 操作成功返回 True

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """

        """

        # TO BE IMPLEMENTED
        if rowIndex < 0 or rowIndex >= len(self.grid) or colIndex < 0 or colIndex >= len(self.grid[0]):
            return False  # 若 rowIndex 或 colIndex 不合法，则返回 False

        self.grid[rowIndex][colIndex] = value  # 更新指定行和列的单元格的值
        return True  # 操作成功返回 True

    def rowNum(self) -> int:
        """
        @return Number of rows .
        """
        # TO BE IMPLEMENTED
        return len(self.grid)

    def colNum(self) -> int:
        """
        @return Number of column.
        """
        # TO BE IMPLEMENTED
        if len(self.grid) > 0:
            return len(self.grid[0])  # 返回第一行的长度，即列数

        else:
            return 0  # 如果电子表格为空，则返回0

    def find(self, value: float) -> [(int, int)]:
        """

        """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        found_cells = []

        for row_idx, row in enumerate(self.grid):
            for col_idx, cell_value in enumerate(row):
                if cell_value == value:
                    found_cells.append((row_idx, col_idx))
        return found_cells

    def entries(self) -> [Cell]:
        """
        """

        non_empty_cells = []
        for row in self.grid:
            for cell_value in row:
                if cell_value is not None:
                    non_empty_cells.append(cell_value)
        return non_empty_cells
