# Book GPT

> A project that processes PDF files, extracts text, generates embeddings, and uses GPT for contextual document search and responses.

---

## Table of Contents

- [Description](#description)
- [How It Works](#how-it-works)
- [Features](#features)

---

## Description

Book GPT is a project that leverages state-of-the-art natural language processing techniques to enable contextual document search and responses within a collection of processed PDF files. It involves several key steps, including text extraction from PDFs, text preprocessing, embedding generation, and interaction with GPT models.

---

## How It Works

1. **PDF Text Extraction**: The project starts by processing PDF files, converting each page into a text string.

2. **Text Preprocessing**: The extracted text data is refactored to improve readability and formatting, making it suitable for further analysis.

3. **Embedding Generation**: The refactored text is sent to a text model (e.g., OpenAI's GPT) that can generate embeddings for the text. These embeddings capture the semantic meaning of the text.

4. **User Query Processing**: The user provides a query, which is converted into an embedding using the same text model.

5. **Vector Search**: A vector search is performed to find similar contextual documents based on the user's query embedding. This allows the project to retrieve relevant passages from the PDFs.

6. **GPT Interaction**: Finally, a prompt is prepared for GPT, providing it with the context of the pages found in step 5. GPT generates responses based on this context.

---

## Features

- PDF text extraction and preprocessing.
- Generation of text embeddings for document understanding.
- User-friendly interface for querying and interacting with contextual documents.
- Integration with GPT models for intelligent responses.

---
