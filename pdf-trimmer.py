import PyPDF2
import os
input_file = input("Please enter the PDF file you would like to trim: ")
pdf_file = PyPDF2.PdfFileReader(open(input_file, 'rb'))
trim_margins = []
for side in ["top", "bottom", "left", "right"]:
  trim_margins.append(int(input(f"Please enter the percentage from the {side} to trim: ")))
output_file = PyPDF2.PdfFileWriter()
for page_num in range(pdf_file.getNumPages()):
	page = pdf_file.getPage(page_num)
	page.trimBox.upperLeft = (trim_margins[2], trim_margins[0])
	page.trimBox.lowerRight = (page.mediaBox.getUpperRight_x() - trim_margins[3], 
							   page.mediaBox.getLowerLeft_y() + trim_margins[1])
	output_file.addPage(page)
output_file_name = os.path.splitext(input_file)[0]+"_trimmed.pdf"
with open(output_file_name, "wb") as outputStream:
	output_file.write(outputStream)
print("File successfully trimmed. Output file is saved as "+output_file_name)
