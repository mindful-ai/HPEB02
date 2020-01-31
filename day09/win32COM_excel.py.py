
(base) C:\Users\Purushotham\day08>python
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from win32com.client import Dispatch
>>> xlApp = Dispatch("Excel.Application")
>>> xlApp.Visible = 1
>>> xlApp.Workbooks.Add()
<win32com.gen_py.None.Workbook>
>>> ##################################################################
...
>>> xlApp.ActiveSheet.Cells(1,1).Value = 'Python Rules!'

>>> xlApp.ActiveWorkbook.ActiveSheet.Cells(1,1).Value = 'Python Rules!'
>>> xlApp.Workbooks("Book1").Sheets("Sheet1").Cells(1,1).Value = "Python Rules!"
>>> xlApp.Workbooks(1).Sheets(1).Cells(1,1).Value = "Python Rules!"
>>> xlBook = xlApp.Workbook(1)

>>> xlBook = xlApp.Workbooks(1)
>>> xlSheet = xlApp.Sheets(1)
>>> xlSheet.Cells(1,1).Value = "Python Rules!"
>>> ######################### Select the sheet to work with
...
>>> xlBook.Sheets(1)
<win32com.gen_py.Microsoft Excel 16.0 Object Library._Worksheet instance at 0x1744713709832>
>>> xlBook.Sheets[1]
<win32com.gen_py.Microsoft Excel 16.0 Object Library._Worksheet instance at 0x1744706562312>
>>> xlBook.Sheets(1).Name
'Sheet1'
>>> ############################# Keyword Arguements
...
>>> xlBook.SaveAs(Filename='mysheet.xls')
>>> ############################### Passing data in and out
...
>>> xlSheet.Cells(1,1).Value = 'What shall be the number of thy counting?'
>>> xlSheet.Cells(2,1).Value = 3
>>> xlSheet.Cells(4,1).Formula = '=A2*2'
>>> ################################## Accessing Ranges
...
>>> myRange1 = xlSheet.Cells(4,1)
>>> myRange2 = xlSheet.Range("B5:C10")
>>> myRange3 = xlSheet.Range(xlSheet.Cells(2,2), xlSheet.Cells(3,8))
>>> myRange3
<win32com.gen_py.Microsoft Excel 16.0 Object Library.Range instance at 0x1744724563592>
>>> myRange3.Value
((None, None, None, None, None, None, None), (None, None, None, None, None, None, None))
