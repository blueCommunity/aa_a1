from array import array
from spreadsheet.linkedlistSpreadsheet import LinkedListSpreadsheet
from spreadsheet.cell import Cell


if __name__ == '__main__':
    spreadsheet = LinkedListSpreadsheet()
    with open("sampleData.txt", 'r') as f:
        cellsFromFiles = []
        for line in f:
            values = line.split()
            currRow = int(values[0])
            currCol = int(values[1])
            currVal = float(values[2])
            currCell = Cell(currRow, currCol, currVal)
            # each line contains a cell
            cellsFromFiles.append(currCell)
        f.close()
        # construct the spreadsheet from the read in data
        spreadsheet.buildSpreadsheet(cellsFromFiles)
    while spreadsheet.head.next is not None:
        print(spreadsheet.head.val.m_length)
        spreadsheet.head = spreadsheet.head.next