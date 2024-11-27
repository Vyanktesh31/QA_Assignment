def findTotalArticlesByLanguages(languages, data):
    """
    Calculate the total number of articles for the given languages.

    :param languages: List of language names to look up.
    :param data: Dictionary containing language names as keys and their article counts as values.
    :return: Total article count for the given languages.
    """
    total_articles = 0
    for lang in languages:
        if lang in data:
            total_articles += data[lang]
        else:
            print(f"Language {lang} not found in the data.")
    return total_articles

# Example data extracted from the Wikipedia table
wikipedia_data = {
    "English": 6562386,
    "German": 2733833,
    "French": 2441600,
    "Japanese": 1325200,
    "Russian": 1824300,
    "Japanese": 1325200,
    "Russian": 1824300,
    # Add more data as needed from the table
}

# Example usage
languages = ["English", "German"]
total_articles = findTotalArticlesByLanguages(languages, wikipedia_data)
print(f"Total articles for {languages}: {total_articles}")
