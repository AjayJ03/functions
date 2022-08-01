from xlrd import open_workbook


def read_locator(sheet_name):
    wb =open_workbook(r"C:\Users\harip\Desktop\Testyentra\python_practice\_selenium\framework\objects.xls")
    ws = wb.sheet_by_name(sheet_name)
    used_rows = ws.nrows
    locators = { }
    for i in range(used_rows):
        data = ws.row_values(i)
        locators[data[0]] = (data[1], data[2])
    return locators

def read_header(sheet_name, testcase_name):
    wb = open_workbook(r"D:\Aj Files\test_data\testdata.xls")
    ws = wb.sheet_by_name(sheet_name)
    used_rows = ws.nrows
    for i in range(used_rows):
        row = ws.row_values(i)
        if row[0] == testcase_name:
            headers = ws.row_values(i-1)
            headers = [header for header in headers if header]
            return ",".join(headers[2:])


def read_data(sheet_name, testcase_name):
    wb = open_workbook(r"D:\Aj Files\test_data\testdata.xls")
    ws = wb.sheet_by_name(sheet_name)
    used_rows = ws.nrows
    final_data = [ ]
    for i in range(used_rows):
        row = ws.row_values(i)
        if row[0] == testcase_name:
            data = [item for item in row if item]
            if data[1] == "Yes":
                final_data.append(data[2:])
    return final_data


print(read_data("smoke","test_login_positive"))
print(read_header("smoke","test_login_positive"))