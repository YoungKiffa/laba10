import cProfile

def count_words(file_path):
    file = open(file_path, 'r')
    content = file.read()
    words = content.split()
    unique_words = {}
    for word in words:
        if word in unique_words:
            unique_words[word] += 1
        else:
            unique_words[word] = 1
    file.close()
    return unique_words

res = 'file.txt'
cProfile.run('count_words(res)')