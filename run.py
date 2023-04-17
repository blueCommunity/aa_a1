from array import array
from spreadsheet.linkedlistSpreadsheet import LinkedListSpreadsheet
from spreadsheet.cell import Cell
from spreadsheet.csrSpreadsheet import CSRSpreadsheet


if __name__ == '__main__':
    spreadsheet = CSRSpreadsheet()
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
        spreadsheet.appendRow()
        spreadsheet.appendCol()

# Call to update(2,5,-1.0) returned success.
# Call to update(10,10,1.0) returned success.
# Call to update(11,11,2.5) returned failure.
        spreadsheet.update(2,5,-1.0)
        spreadsheet.update(10,10,1.0)
        spreadsheet.update(11,11,2.5)
        spreadsheet.entries()
#    Call to insertRow(1) returned success.
# Call to insertCol(4) returned success.
# Call to insertRow(-2) returned failure.
        spreadsheet.insertRow(1)
        spreadsheet.insertCol(4)
        spreadsheet.insertRow(-2)
        spreadsheet.update(2,5,-2.0)