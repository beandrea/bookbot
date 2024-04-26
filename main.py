def word_count(txt: str) -> int:
    word_list = txt.split()
    return len(word_list)

def get_text_from_file(path: str) -> str:
    with open(path) as f:
        return f.read()

def letter_counts(txt: str) -> dict[str, int]:
    txt_list = list(txt.lower())
    counts = {}
    for letter in txt_list:
        try:
            letter = int(letter)
        except:
            if letter not in counts.keys:
                counts[letter] = 1
            else:
                counts[letter] += 1
    return counts

def main() -> None:
    text = get_text_from_file('./books/frankenstein.txt')
    print(text)
    num_words = word_count(text)
    print(f'{num_words} words found in the document')


if __name__ == '__main__':
    main()
