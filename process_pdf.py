import PyPDF2

def process_pdf(pdf_file):
  """
  Processes a PDF file and loads the text into memory.

  Args:
    pdf_file: The path to the PDF file.

  Returns:
    A list of strings, where each string is a page of text from the PDF file.
  """

  pdf_reader = PyPDF2.PdfReader(pdf_file)
  num_pages = len(pdf_reader.pages)
  print(num_pages)

  text_list = []
  for i in range(num_pages):
    page = pdf_reader.pages[i]
    text = page.extract_text()
    text_list.append(text)

  return text_list


# Example usage:

pdf_file = "/content/book.pdf"

page_list = process_pdf(pdf_file)