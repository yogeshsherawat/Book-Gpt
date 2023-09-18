import PyPDF2
from .embedding_manager import EmbeddingManager
from helper.utils_helper import UtilsHelper


class BookManager(object):
    @staticmethod
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

    @staticmethod
    def refactor_data(pages):
        """
        This refactoring function would be different for each pdf file, so change accordingly
        """
        page_texts = []
        for page in pages:
            page_text = page.replace("\t", " ").replace("\n", " ")
            page_texts.append(page_text)
        return page_texts

    @staticmethod
    def get_book_data_embeddings(pages):
        sentence_with_embeddings = []
        for page in pages:
            embedding = EmbeddingManager.generage_emedding_for_text(page)['data'][0]['embedding']
            sentence_with_embeddings.append((page, embedding))

