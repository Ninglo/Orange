import xlsxwriter

def save_data(matrix, data):
    workbook = xlsxwriter.Workbook('{data}.xlsx'.format(data = data))
    worksheet = workbook.add_worksheet('{data}'.format(data = data))
    headings = range(1, len(matrix) + 1)
    worksheet.write_row('A1',headings)
    num = 1
    for item in matrix:
        num += 1
        worksheet.write_row('A{num}'.format(num = num), item)
    workbook.close()