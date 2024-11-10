# TODO Найдите количество книг, которое можно разместить на дискете

diskette_size_mb = 1.44  #размер дискеты в Мб
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
size_of_char_bytes = 4  #размер одного символа в байтах

#Переводим размер дискеты в байты
diskette_size_bytes = int(diskette_size_mb * 1024 * 1024)

#Вычисляем объём одной книги в байтах
book_size_bytes = (pages_per_book * lines_per_page * chars_per_line * size_of_char_bytes)

#Вычисляем количество книг, которые можно разместить на дискете
number_of_books = diskette_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", number_of_books)
