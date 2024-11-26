data = [
    {
        "lan": "English",
        "article": "askbdsa"
    },
    {
        "lan": "English",
        "artical": "ahsbdas"
    },
    {
        "lan": "German",
        "article": "ajksndkas"
    },
    {
        "lan": "German",
        "article": "ajksndkas"
    },
    {
        "lan": "Russian",
        "article": "ajksndkas"
    }
]

def get_num_of_articles(languages):
    filtered_data = [item for item in data if item["lan"] in languages]
    return len(filtered_data)

# Example usage:
print(get_num_of_articles(["English", "German"]))