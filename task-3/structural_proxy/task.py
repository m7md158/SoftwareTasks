import time

# Simulate access to a database
class LibraryDatabase:
    def get_book(self, title):
        print(f"Searching for '{title}' in the library database...")
        time.sleep(2)  # simulate slow database
        return f"Book: '{title}' (fetched from database)"

# Proxy with caching
class LibraryProxy:
    def __init__(self):
        self.database = LibraryDatabase()
        self.cache = {}

    def get_book(self, title):
        if title in self.cache:
            print(f"Fetching '{title}' from cache...")
            return self.cache[title]
        result = self.database.get_book(title)
        self.cache[title] = result
        return result

# Client code
library = LibraryProxy()

print(library.get_book("Design Patterns"))      # Fetched from database
print(library.get_book("Clean Code"))           # Fetched from database
print(library.get_book("Design Patterns"))      # Fetched from cache
print(library.get_book("The Pragmatic Programmer"))  # Fetched from database
print(library.get_book("Clean Code"))           # Fetched from cache
