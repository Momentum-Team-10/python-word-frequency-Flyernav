STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        text_string = str(text.readlines())
        text_string = text_string.replace(",", "")
        text_string = text_string.replace(".", "")
        text_string = text_string.replace("-", "")
        text_string = text_string.replace("?", "")
        text_string = text_string.replace(":", "")
        text_string = text_string.replace("'", "")
        text_string = text_string.replace("\\n", "")
        text_string = text_string.replace("[", "")
        text_string = text_string.replace("]", "")
        word_list = text_string.split()
        no_stop_words = []
        for word in word_list:
            if word in STOP_WORDS:
                pass
            else: no_stop_words.append(word)
        clean_list = {}
        for word in no_stop_words:
            clean_list[word] = no_stop_words.count(word) 
        print(clean_list)       


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
