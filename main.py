from manager.embedding_manager import EmbeddingManager
from helper.utils_helper import UtilsHelper
from manager.chat_manager import ChatManager
from manager.book_manager import BookManager

def prepare_book_embeddings(book_filepath):
    pages = BookManager.process_pdf(book_filepath)
    pages = BookManager.refactor_data(pages)
    sentence_with_embeddings = BookManager.get_book_data_embeddings(pages)
    return sentence_with_embeddings




def prepare_content(query, book_filepath):
    query_embedding = EmbeddingManager.generage_emedding_for_text(query)
    sentence_with_embeddings = prepare_book_embeddings(book_filepath)
    closest_neighbors = UtilsHelper.find_k_closest_to_given_vector(query_embedding, sentence_with_embeddings)
    context = ''
    for n in closest_neighbors:
        context += n[0] + "\n"
    content = f"""
        You are avid book reader. You have read lot of books, on based of given context, try to answer the query .
        Context Sections :
        {context}

        Query :
        {query}

        """
    return content


def reply(query, book_filepath):
    content = prepare_content(query, book_filepath)
    ChatManager.get_reply_to_query_with_content(query, content)


if __name__ == '__main__':
    query = input()
    book_file_path = input()
    reply(query, book_file_path)
