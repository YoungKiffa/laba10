from collections import Counter
import cProfile

def count_words(file_path):
    with open(file_path, 'r') as file:
        words = []
        for line in file:
            words.extend(line.split())
        unique_words = Counter(words)
    return unique_words

if __name__ == "__main__":
    res = 'file.txt'
    word_counts = count_words(res)
    cProfile.run('count_words(res)')
    print(word_counts)