from textblob import TextBlob
from textblob import Word
import nltk

def file_spell_correct():
    file1 = open("gram.txt","r")
    a = file1.read()

    print("original text",a)

    b = TextBlob(a)
    print("corrected text"+str(b.correct()))

    file1.close()
    d = open("gram.txt","w")
    d.write(str(b.correct()))
    d.close()

def definetion():
    word = input("Enter word for getting definetion")
    s = Word(word)
    s_Word = s.definitions
    print(s_Word)

def spell_correct():
    a = input("Enter sentence")
    b = TextBlob(a)
    s = b.correct()
    print(s)

def spellcheck():
    a = input("Enter word")
    b = Word(a)
    s = b.spellcheck()
    print(s)

def word_count():
    file1 = open("gram.txt", "r")
    a = file1.read()

    b = TextBlob(a)
    words = b.word_counts()
    print(words)

def singular():
    a = input("Enter word")
    b = TextBlob(a)
    s = b.words[0]
    sin = s.singularize()
    print(sin)


def plural():
    a = input("Enter word")
    b = TextBlob(a)
    s = b.words[0]
    sin = s.pluralize()
    print(sin)


# file_spell_correct()
# definetion()
plural()
