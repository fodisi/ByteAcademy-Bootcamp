#def word_stats(filename, n):
#  from collections import Counter

from collections import Counter

def word_stats(n):
    with open("article.txt") as f:
        file_content = f.read().split()
    
    cnt = Counter(file_content)
    most_commom = cnt.most_common(n)
    for word, count in most_commom:
        print('\"{0}\", {1}'.format(word, count))

if __name__ == '__main__':
    print('write a number')
    word_stats(int(input()))
