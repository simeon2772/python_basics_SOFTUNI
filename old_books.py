looking_for_book = input()
book_counter = 0
is_book = False
current_book = input()
while current_book != "No More Books":
    if current_book == looking_for_book:
        is_book = True
        print(f"You checked {book_counter} books and found it.")
        break
    book_counter += 1
    current_book = input()

if not is_book:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")