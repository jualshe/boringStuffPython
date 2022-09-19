import PyPDF2, os

os.chdir('/Users/julia/Documents')
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

page = reader.getPage(0)
print(page.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
