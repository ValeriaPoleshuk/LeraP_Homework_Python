from book import Book

librari = [
    Book("Колобок", 'A.F'),
    Book("Машины", "S.T"),
    Book("Теремок", "D.L")
]
for book in librari:
    print(f"{book.name} - {book.author}")