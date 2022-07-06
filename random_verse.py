#!/usr//bin/env python3
import argparse
import random


BOOKS = [
    {
        "title": "Genesis",
        "abbrev": "Gen.",
        "verses": [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35, 46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26],
        "tags": ["Old Testament", "Pentateuch"]
    },
    {
        "title": "Exodus",
        "abbrev": "Ex.",
        "verses": [22, 25, 22, 31, 23, 30, 25, 32, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36, 31, 33, 18, 40, 37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38],
        "tags": ["Old Testament", "Pentateuch"]
    },
    {
        "title": "Leviticus",
        "abbrev": "Lev.",
        "verses": [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34],
        "tags": ["Old Testament", "Pentateuch"]
    },
    {
        "title": "Numbers",
        "abbrev": "Num.",
        "verses": [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65, 23, 31, 40, 16, 54, 42, 56, 29, 34, 13],
        "tags": ["Old Testament", "Pentateuch"]
    },
    {
        "title": "Deuteronomy",
        "abbrev": "Dt.",
        "verses": [46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23, 30, 25, 22, 19, 19, 26, 68, 29, 20, 30, 52, 29, 12],
        "tags": ["Old Testament", "Pentateuch"]
    },
    {
        "title": "Joshua",
        "abbrev": "Jos.",
        "verses": [18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45, 34, 16, 33],
        "tags": ["Old Testament", "History", "Deuteronomistic History"]
    },
    {
        "title": "Judges",
        "abbrev": "Jg.",
        "verses": [36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25],
        "tags": ["Old Testament", "History", "Deuteronomistic History"]
    },
    {
        "title": "Ruth",
        "abbrev": "Ru.",
        "verses": [22, 23, 18, 22],
        "tags": ["Old Testament", "History"]
    },
    {
        "title": "1 Samuel",
        "abbrev": "1 Sam.",
        "verses": [28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 15, 23, 29, 22, 44, 25, 12, 25, 11, 31, 13],
        "tags": ["Old Testament", "History", "Deuteronomistic History"]
    },
    {
        "title": "2 Samuel",
        "abbrev": "2 Sam.",
        "verses": [27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22, 51, 39, 25],
        "tags": ["Old Testament", "History", "Deuteronomistic History"]
    },
    {
        "title": "1 Kings",
        "abbrev": "1 Kg.",
        "verses": [53, 46, 28, 34, 18, 38, 51, 66, 28, 29, 43, 33, 34, 31, 34, 34, 24, 46, 21, 43, 29, 53],
        "tags": ["Old Testament", "History", "Deuteronomistic History"]
    },
    {
        "title": "2 Kings",
        "abbrev": "2 Kg.",
        "verses": [18, 25, 27, 44, 27, 33, 20, 29, 37, 36, 21, 21, 25, 29, 38, 20, 41, 37, 37, 21, 26, 20, 37, 20, 30],
        "tags": ["Old Testament", "History", "Deuteronomistic History"]
    },
    {
        "title": "1 Chronicles",
        "abbrev": "1 Chr.",
        "verses": [54, 55, 24, 43, 26, 81, 40, 40, 44, 14, 47, 40, 14, 17, 29, 43, 27, 17, 19, 8, 30, 19, 32, 31, 31, 32, 34, 21, 30],
        "tags": ["Old Testament", "History"]
    },
    {
        "title": "2 Chronicles",
        "abbrev": "2 Chr.",
        "verses": [17, 18, 17, 22, 14, 42, 22, 18, 31, 19, 23, 16, 22, 15, 19, 14, 19, 34, 11, 37, 20, 12, 21, 27, 28, 23, 9, 27, 36, 27, 21, 33, 25, 33, 27, 23],
        "tags": ["Old Testament", "History"]
    },
    {
        "title": "Ezra",
        "abbrev": "Ezra",
        "verses": [11, 70, 13, 24, 17, 22, 28, 36, 15, 44],
        "tags": ["Old Testament", "History"]
    },
    {
        "title": "Nehemiah",
        "abbrev": "Neh.",
        "verses": [11, 20, 32, 23, 19, 19, 73, 18, 38, 39, 36, 47, 31],
        "tags": ["Old Testament", "History"]
    },
    {
        "title": "Esther",
        "abbrev": "Est.",
        "verses": [22, 23, 15, 17, 14, 14, 10, 17, 32, 3],
        "tags": ["Old Testament", "History"]
    },
    {
        "title": "Job",
        "abbrev": "Job",
        "verses": [22, 13, 26, 21, 27, 30, 21, 22, 35, 22, 20, 25, 28, 22, 35, 22, 16, 21, 29, 29, 34, 30, 17, 25, 6, 14, 23, 28, 25, 31, 40, 22, 33, 37, 16, 33, 24, 41, 30, 24, 34, 17],
        "tags": ["Old Testament"]
    },
    {
        "title": "Psalms",
        "abbrev": "Ps.",
        "verses": [6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10, 22, 12, 14, 9, 11, 12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 13, 11, 5, 26, 17, 11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13, 11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18, 12, 13, 17, 7, 18, 52, 17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28, 22, 35, 45, 48, 43, 13, 31, 7, 10, 10, 9, 8, 18, 19, 2, 29, 176, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8, 24, 13, 10, 7, 12, 15, 21, 10, 20, 14, 9, 6],
        "tags": ["Old Testament"]
    },
    {
        "title": "Proverbs",
        "abbrev": "Pr.",
        "verses": [33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31, 29, 35, 34, 28, 28, 27, 28, 27, 33, 31],
        "tags": ["Old Testament"]
    },
    {
        "title": "Ecclesiastes",
        "abbrev": "Ec.",
        "verses": [18, 26, 22, 16, 20, 12, 29, 17, 18, 20, 10, 14],
        "tags": ["Old Testament"]
    },
    {
        "title": "Song of Solomon",
        "abbrev": "S. of S.",
        "verses": [17, 17, 11, 16, 16, 13, 13, 14],
        "tags": ["Old Testament"]
    },
    {
        "title": "Isaiah",
        "abbrev": "Is.",
        "verses": [31, 22, 26, 6, 30, 13, 25, 22, 21, 34, 16, 6, 22, 32, 9, 14, 14, 7, 25, 6, 17, 25, 18, 23, 12, 21, 13, 29, 24, 33, 9, 20, 24, 17, 10, 22, 38, 22, 8, 31, 29, 25, 28, 28, 25, 13, 15, 22, 26, 11, 23, 15, 12, 17, 13, 12, 21, 14, 21, 22, 11, 12, 19, 12, 25, 24],
        "tags": ["Old Testament", "Major Prophet", "Prophet"]
    },
    {
        "title": "Jeremiah",
        "abbrev": "Jer.",
        "verses": [19, 37, 25, 31, 31, 30, 34, 22, 26, 25, 23, 17, 27, 22, 21, 21, 27, 23, 15, 18, 14, 30, 40, 10, 38, 24, 22, 17, 32, 24, 40, 44, 26, 22, 19, 32, 21, 28, 18, 16, 18, 22, 13, 30, 5, 28, 7, 47, 39, 46, 64, 34],
        "tags": ["Old Testament", "Major Prophet", "Prophet"]
    },
    {
        "title": "Lamentations",
        "abbrev": "Lam.",
        "verses": [22, 22, 66, 22, 22],
        "tags": ["Old Testament", "Major Prophet", "Prophet"]
    },
    {
        "title": "Ezekiel",
        "abbrev": "Ezek.",
        "verses": [28, 10, 27, 17, 17, 14, 27, 18, 11, 22, 25, 28, 23, 23, 8, 63, 24, 32, 14, 49, 32, 31, 49, 27, 17, 21, 36, 26, 21, 26, 18, 32, 33, 31, 15, 38, 28, 23, 29, 49, 26, 20, 27, 31, 25, 24, 23, 35],
        "tags": ["Old Testament", "Major Prophet", "Prophet"]
    },
    {
        "title": "Daniel",
        "abbrev": "Dan.",
        "verses": [21, 49, 30, 37, 31, 28, 28, 27, 27, 21, 45, 13],
        "tags": ["Old Testament", "Major Prophet", "Prophet"]
    },
    {
        "title": "Hosea",
        "abbrev": "Hos.",
        "verses": [11, 23, 5, 19, 15, 11, 16, 14, 17, 15, 12, 14, 16, 9],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Joel",
        "abbrev": "Jl.",
        "verses": [20, 32, 21],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Amos",
        "abbrev": "Am.",
        "verses": [15, 16, 15, 13, 27, 14, 17, 14, 15],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Obadiah",
        "abbrev": "Ob.",
        "verses": [21],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Jonah",
        "abbrev": "Jon.",
        "verses": [17, 10, 10, 11],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Micah",
        "abbrev": "Mic.",
        "verses": [16, 13, 12, 13, 15, 16, 20],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Nahum",
        "abbrev": "Nah.",
        "verses": [15, 13, 19],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Habakkuk",
        "abbrev": "Hab.",
        "verses": [17, 20, 19],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Zephaniah",
        "abbrev": "Zeph.",
        "verses": [18, 15, 20],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Haggai",
        "abbrev": "Hag.",
        "verses": [15, 23],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Zechariah",
        "abbrev": "Zech.",
        "verses": [21, 13, 10, 14, 11, 15, 14, 23, 17, 12, 17, 14, 9, 21],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Malachi",
        "abbrev": "Mal.",
        "verses": [14, 17, 18, 6],
        "tags": ["Old Testament", "Minor Prophet", "Prophet"]
    },
    {
        "title": "Matthew",
        "abbrev": "Mt.",
        "verses": [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20],
        "tags": ["New Testament", "Gospel"]
    },
    {
        "title": "Mark",
        "abbrev": "Mk.",
        "verses": [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20],
        "tags": ["New Testament", "Gospel"]
    },
    {
        "title": "Luke",
        "abbrev": "Lk.",
        "verses": [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53],
        "tags": ["New Testament", "Gospel"]
    },
    {
        "title": "John",
        "abbrev": "Jn.",
        "verses": [51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25],
        "tags": ["New Testament", "Gospel"]
    },
    {
        "title": "Acts",
        "abbrev": "Acts",
        "verses": [26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 41, 38, 40, 30, 35, 27, 27, 32, 44, 31],
        "tags": ["New Testament"]
    },
    {
        "title": "Romans",
        "abbrev": "Rom.",
        "verses": [32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 26, 33, 25],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "1 Corinthians",
        "abbrev": "1 Cor.",
        "verses": [31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "2 Corinthians",
        "abbrev": "2 Cor.",
        "verses": [24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "Galatians",
        "abbrev": "Gal.",
        "verses": [24, 21, 29, 31, 26, 18],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "Ephesians",
        "abbrev": "Eph.",
        "verses": [23, 22, 21, 32, 33, 24],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "Philippians",
        "abbrev": "Phil.",
        "verses": [30, 30, 21, 23],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "Colossians",
        "abbrev": "Col.",
        "verses": [29, 23, 25, 18],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "1 Thessalonians",
        "abbrev": "1 Th.",
        "verses": [10, 20, 13, 18, 28],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "2 Thessalonians",
        "abbrev": "2 Th.",
        "verses": [12, 17, 18],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "1 Timothy",
        "abbrev": "1 Tim.",
        "verses": [20, 15, 16, 16, 25, 21],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "2 Timothy",
        "abbrev": "2 Tim.",
        "verses": [18, 26, 17, 22],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "Titus",
        "abbrev": "Tit.",
        "verses": [16, 15, 15],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "Philemon",
        "abbrev": "Philem.",
        "verses": [25],
        "tags": ["New Testament", "Pauline Epistle"]
    },
    {
        "title": "Hebrews",
        "abbrev": "Heb.",
        "verses": [14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25],
        "tags": ["New Testament"]
    },
    {
        "title": "James",
        "abbrev": "Jas.",
        "verses": [27, 26, 18, 17, 20],
        "tags": ["New Testament", "Catholic Epistle"]
    },
    {
        "title": "1 Peter",
        "abbrev": "1 Pet.",
        "verses": [25, 25, 22, 19, 14],
        "tags": ["New Testament", "Catholic Epistle"]
    },
    {
        "title": "2 Peter",
        "abbrev": "2 Pet.",
        "verses": [21, 22, 18],
        "tags": ["New Testament", "Catholic Epistle"]
    },
    {
        "title": "1 John",
        "abbrev": "1 Jn.",
        "verses": [10, 29, 24, 21, 21],
        "tags": ["New Testament", "Catholic Epistle"]
    },
    {
        "title": "2 John",
        "abbrev": "2 Jn.",
        "verses": [13],
        "tags": ["New Testament", "Catholic Epistle"]
    },
    {
        "title": "3 John",
        "abbrev": "3 Jn.",
        "verses": [14],
        "tags": ["New Testament", "Catholic Epistle"]
    },
    {
        "title": "Jude",
        "abbrev": "Jude",
        "verses": [25],
        "tags": ["New Testament", "Catholic Epistle"]
    },
    {
        "title": "Revelation",
        "abbrev": "Rev.",
        "verses": [20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20, 8, 21, 18, 24, 21, 15, 27, 21],
        "tags": ["New Testament"]
    }
]


class RandomVerse:
    def __init__(self, books, full, tags):
        if books:
            self.books = [bk for bk
                          in BOOKS
                          if bk['title'] in books or bk['abbrev'] in books]
        elif tags:
            _tags = set(tags)
            self.books = [bk for bk
                          in BOOKS
                          if set(bk['tags']) & _tags]
        else:
            self.books = BOOKS
        self.full = full
        self.num_verses = sum(sum(book['verses']) for book in self.books)

    def index_to_verse(self, idx):
        for bk_idx, book in enumerate(self.books):
            ch_idx = 0
            verses = book['verses']
            while ch_idx < len(verses) and idx > verses[ch_idx]:
                idx = idx - verses[ch_idx]
                ch_idx += 1
            if ch_idx < len(verses):
                chapter = ch_idx + 1
                _verse = idx + 1
                verse = (bk_idx, chapter, _verse, book)
                return verse
        print(f'{idx} is greater than {self.num_verses}')

    def serialize_verse(self, verse):
        bk_idx, chapter, _verse, book = verse
        bk = book['title'] if self.full else book['abbrev']
        return f'{bk} {chapter}:{_verse}'

    def random_verse(self, cnt):
        idxs = random.sample(range(self.num_verses), k=cnt)
        verses = sorted(self.index_to_verse(idx) for idx in idxs)
        for verse in verses:
            print(self.serialize_verse(verse))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--books', '-b', dest='books', nargs='+')
    parser.add_argument('--count', '-c', dest='count', type=int, default=10)
    parser.add_argument('--full', '-f',
                        dest='full',
                        action='store_true',
                        default=False)
    parser.add_argument('--tags', '-t', dest='tags', nargs='+')
    args = parser.parse_args()
    random_verse = RandomVerse(books=args.books,
                               full=args.full,
                               tags=args.tags)
    random_verse.random_verse(cnt=args.count)
