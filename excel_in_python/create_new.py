from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"

ws.append([1, 2, 3, 4])  # 1 line, 4 cells
ws.append([1, 2, 3, 4])
ws.append([1, 2, 3, 4])
ws.append([1, 2, 3, 4])

wb.save('test2.xlsx')
