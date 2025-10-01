class Book:

  def __init__(self, title, author):
    self.title = title
    self.author = author

    self._is_checked_out = False

  def checkout(self):
    if self._is_checked_out:
      self._is_checked_out = True
      return True
    
    return False

  def returnBook(self):
    if not self._is_checked_out:
      self._is_checked_out = False
      return True
    
    return False
  
  def is_available(self):
    return not self._is_checked_out
  
  def __str__(self):
    return f"{self.title} by {self.author}"
  


class Library:

  def __init__(self):
    self._books = []

  def add_book(self, book):
    self._books.append(book)

  def check_out_book(self, title):
    for book in self._books:
      if book.title == title and book.is_available():
        book.checkout()
        print(f"Checked Out: {book}")
        return True
    
    print(f"Book {title} is not available.")
    return False
  
  def return_book(self, title):
    for book in self._books:
      if not book.is_available():
        book._is_checked_out = False
        return True
    
    print(f"Book {title} has no been checked out.")
    return False
  
  def list_available_books(self):
    available = [str(book) for book in self._books if book.is_available()]

    print("Available Books")
    for book in available:
      print(book)