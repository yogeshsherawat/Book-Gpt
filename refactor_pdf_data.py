def refactor_data(pages):
    """
    This refactoring function would be different for each pdf file, so change accordingly
    """
    page_texts = []
    for page in pages:
        page_text = page.replace("\t", " ").replace("\n", " ")
        page_texts.append(page_text)
    return page_texts
