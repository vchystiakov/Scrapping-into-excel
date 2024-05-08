# file that writes scrapped data into excel file
# import libraries
import xlsxwriter
from main import array


# function that creates excel table and writes scrapped data into file
def writer(parametr):
    # variable with excel file
    book = xlsxwriter.Workbook(
        # path to your Excel file!
        r"D:\Courses\PythonLearning\Projects\Scrapping\Course\Scrappingintofile\data.xlsx")
    # page with goods(items)
    page = book.add_worksheet('goods')

    # rows and columns counter
    row = 0
    column = 0
    # setting length of columns
    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)
    # for every item write it's info into created columns
    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        row += 1
    # close file
    book.close()


# calling function with parametr - function-generator
writer(array)
