from xlrd import open_workbook

def read_locators(pagename):
    wb=open_workbook(r"D:\Aj Files\_excel_files\file.xlsx")
    ws=wb.sheet_by_name(pagename)  # return address of an object...(mentioned sheet)
    used_rows=ws.nrows  # return total no. of rows present in a sheet... 
    
    # ws.row_values(0) # it takes index as an argument,
    # will return the list of entire row's as an item in the 0th index

    locators={}
    for i in range(1,used_rows):  # if we use 0- it will print header also
        data=ws.row_values(i)     # data=["txt_email", "id", "email"]
        locators[data[0]]=(data[1],data[2])   # making dictionary from list
    return locators

print(read_locators("loginpage"))

# all_sheets=wb.sheet_names()  # for getting all sheet names...

def read_headers(sheet_name, test_case_name):
    wb=open_workbook(r"D:\Aj Files\_excel_files\testdata.xls")
    ws=wb.sheet_by_name(sheet_name)
    used_rows=ws.nrows
    for i in range(0,used_rows):
        row=ws.row_values(i)
        if row[0] == test_case_name:
            headers=ws.row_values(i-1)
            headers=[header for header in headers if header]
            return ",".join(headers[2:])

print(read_headers("smoke", "test_payment"))
           

