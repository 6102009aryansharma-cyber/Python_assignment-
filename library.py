import csv
import os
from datetime import datetime
# -------------------------
# Data structures
# -------------------------
# books: dict mapping book_id -> {"title":..., "author":..., "copies": int}
books = {}
# borrowed: dict mapping student_name -> list of borrowed book_ids
borrowed = {}
# set for unique names (demonstration of set usage)
student_names = set()
# -------------------------
# Helper functions
# -------------------------
def clear_screen():
    """Clear console screen (works for Windows and Unix)."""
    os.system('cls' if os.name == 'nt' else 'clear')
def add_book():

    """Add a new book (or update copies if ID exists)."""
    print("\n--- Add / Update Book ---")
    book_id = input("Enter Book ID (e.g., B101): ").strip()
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()    
    try:
        copies = int(input("Enter number of copies: "))
        if copies < 0:
            raise ValueError
    except ValueError:
        print("Invalid number of copies. Operation cancelled.")
        return
    if book_id in books:
        # update existing entry
        books[book_id]['copies'] += copies
        print(f"Updated copies for {book_id}. New copies: {books[book_id]['copies']}")
    else:
        books[book_id] = {"title": title, "author": author, "copies": copies}
        print(f"Book {book_id} added successfully.")
    def view_books():
        """Display all books in a tabular format."""
        print("\n--- Library Books ---")
        if not books:
           print("No books available.")
           return
        print(f"{'Book ID':<8} {'Title':<30} {'Author':<20} {'Copies':<6}")
        print("-" * 70)
        for bid, info in books.items():
           print(f"{bid:<8} {info['title'][:28]:<30} {info['author'][:18]:<20} {info['copies']:<6}")
        print("-" * 70)   
    def search_book():
        """Search book by ID or by title substring."""
        print("\n--- Search Book ---")
        print("1. Search by Book ID")
        print("2. Search by Title keyword")
        choice = input("Choose option (1/2): ").strip() 
        if choice == "1":
             bid = input("Enter Book ID: ").strip()
             info = books.get(bid)
             if info:
                 print(f"Found: {bid} -> Title: {info['title']}, Author: {info['author']}, Copies: {info['copies']}")
             else:
               print("Book ID not found.")
        elif choice == "2":
               keyword = input("Enter title keyword: ").strip().lower()
               results = [(bid, info) for bid, info in books.items() if keyword in info['title'].lower()]
               if results:
                   print(f"\nFound {len(results)} result(s):")
                   for bid, info in results:
                       print(f"{bid}: {info['title']} by {info['author']} (Copies: {info['copies']})")
               else:
                   print("No matching titles found.")
        else:
            print("Invalid option.")
        def borrow_book():
             """Borrow a book: check availability, reduce copies, record student."""
             print("\n--- Borrow Book ---")
             student = input("Enter Student Name: ").strip()
             if not student:
                print("Student name required.")
             return
             book_id = input("Enter Book ID to borrow: ").strip()
             if book_id not in books:
                 print("Book ID does not exist.")
                 return
             if books[book_id]['copies'] <= 0:
                 print("No copies available for this book.")
                 return
             # proceed to borrow
             books[book_id]['copies'] -= 1
             student_names.add(student)
             borrowed.setdefault(student, []).append(book_id)
             print(f"{student} has successfully borrowed {book_id} ({books[book_id]['title']}).")
             # Optional extra: record datetime
             # borrowed_records.append({"student": student, "book_id": book_id, "time":datetime.now()})
        def return_book():
            """Return a borrowed book: validate and increment copies."""
            print("\n--- Return Book ---")
            student = input("Enter Student Name: ").strip()
            if student not in borrowed or not borrowed[student]:
                      print("No borrowing record found for this student.")
                      return
                      print(f"Borrowed books by {student}: {borrowed[student]}")
                      book_id = input("Enter Book ID to return: ").strip()
                      if book_id not in borrowed[student]:
                            print(f"{student} did not borrow book {book_id}.")
                            return
                         # proceed to return
                            borrowed[student].remove(book_id)
                            books.setdefault(book_id, {"title": "Unknown","author": "Unknown", "copies": 0})
                            books[book_id]['copies'] += 1
                            print(f"{student} has returned {book_id}. Copies now: {books[book_id]['copies']}")
                            def view_borrowed_books():
                                """Display all borrowed books by student."""
    print("\n--- Borrowed Books ---")
    if not borrowed or all(len(v) == 0 for v in borrowed.values()):
        print("No borrowed books.")
        return
    lines = [f"{student} -> {', '.join(book_list)}" for student, book_list in borrowed.items() if book_list]
    for line in lines:
        print(line)

def save_books_to_csv(filename="books.csv"):
    """Save current books dictionary to a CSV file."""
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["book_id", "title", "author", "copies"])
            for bid, info in books.items():
                writer.writerow([bid, info['title'], info['author'], info['copies']])
        print(f"Books saved to {filename}")
    except Exception as e:
        print("Error saving books:", e)

def load_books_from_csv(filename="books.csv"):
    """Load books from CSV file into books dict (overwrites current books)."""
    if not os.path.exists(filename):
        print(f"{filename} not found.")
        return
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            books.clear()
            for row in reader:
                try:
                    copies = int(row.get("copies", 0))
                except ValueError:
                    copies = 0
                books[row["book_id"]] = {
                    "title": row.get("title", ""),
                    "author": row.get("author", ""),
                    "copies": copies
                }
        print(f"Books loaded from {filename}")
    except Exception as e:
        print("Error loading books:", e)
 
def save_borrowed_to_csv(filename="borrowed.csv"):
      
    """Save borrowed dictionary to CSV."""
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as f:writer = csv.writer(f)
        writer.writerow(["student", "book_id"])
        for student, book_list in borrowed.items():
            for bid in book_list:
                writer.writerow([student, bid])
            print(f"Borrowed records saved to {filename}")
    except Exception as e:
        print("Error saving borrowed records:", e)


def load_borrowed_from_csv(filename="borrowed.csv"):
    """Load borrowed records from CSV (appends to current borrowed)."""
    if not os.path.exists(filename):
       print(f"{filename} not found.")
       return
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            borrowed.clear()
            for row in reader:
                student = row.get("student", "").strip()
                book_id = row.get("book_id", "").strip()
                if student and book_id:
                   borrowed.setdefault(student, []).append(book_id)
                   student_names.add(student)
        print(f"Borrowed records loaded from {filename}")
    except Exception as e:
        print("Error loading borrowed records:", e)
def sample_data():
 """Populate sample data (for quick testing/demo)."""
 books.clear()
 books.update
 ({"B101": {"title": "Python Programming", "author": "John Doe", "copies": 3},
 "B102": {"title": "Data Structures", "author": "Jane Smith", "copies": 2},
 "B103": {"title": "Algorithms", "author": "Cormen", "copies": 1},
 "B104": {"title": "Database Systems", "author": "Elmasri", "copies": 4},
 "B105": {"title": "Operating Systems", "author": "Tanenbaum", "copies": 2} })
 borrowed.clear()
 student_names.clear()
 print("Sample data loaded.")
 
def view_borrowed():
    """Display borrowed books by student (book IDs and titles)."""
    print("\n--- Borrowed Books ---")
    if not borrowed or all(not v for v in borrowed.values()):
        print("No borrowed books.")
        return
    for student, book_list in borrowed.items():
        if not book_list:
            continue
        entries = []
        for bid in book_list:
            title = books.get(bid, {}).get("title", "Unknown")
            entries.append(f"{bid} ({title})")
        print(f"{student}: {', '.join(entries)}")

def view_books():
    """Display all books in a simple table."""
    print("\n--- Library Books ---")
    if not books:
        print("No books available.")
        return
    print(f"{'Book ID':<8} {'Title':<30} {'Author':<20} {'Copies':<6}")
    print("-" * 70)
    for bid, info in books.items():
        title = info.get("title", "")[:28]
        author = info.get("author", "")[:18]
        copies = info.get("copies", 0)
        print(f"{bid:<8} {title:<30} {author:<20} {copies:<6}")
    print("-" * 70)

    
def search_book():
    """Search book by ID or title keyword (top-level function)."""
    print("\n--- Search Book ---")
    print("1. Search by Book ID")
    print("2. Search by Title keyword")
    choice = input("Choose option (1/2): ").strip()
    if choice == "1":
        bid = input("Enter Book ID: ").strip()
        info = books.get(bid)
        if info:
            print(f"Found: {bid} -> Title: {info.get('title','')}, Author: {info.get('author','')}, Copies: {info.get('copies',0)}")
        else:
            print("Book ID not found.")
    elif choice == "2":
        keyword = input("Enter title keyword: ").strip().lower()
        results = [(bid, info) for bid, info in books.items() if keyword in info.get("title","").lower()]
        if results:
            for bid, info in results:
                print(f"{bid} -> {info.get('title','')} by {info.get('author','')} (Copies: {info.get('copies',0)})")
        else:
            print("No matching titles found.")
    else:
        print("Invalid choice.")

def borrow_book():
    """Borrow a book: validate availability and record borrowing."""
    print("\n--- Borrow Book ---")
    student = input("Enter Student Name: ").strip()
    if not student:
        print("Student name cannot be empty.")
        return
    student_names.add(student)
    if student not in borrowed:
        borrowed[student] = []
    book_id = input("Enter Book ID: ").strip()
    if not book_id:
        print("Book ID cannot be empty.")
        return
    info = books.get(book_id)
    if not info or info.get("copies", 0) <= 0:
        print(f"Book {book_id} is not available.")
        return
    borrowed[student].append(book_id)
    books[book_id]["copies"] = info.get("copies", 0) - 1
    print(f"{student} has successfully borrowed {book_id} ({info.get('title','Unknown')}).")
    
def return_book():
    """Return a borrowed book: validate student and book, update records."""
    print("\n--- Return Book ---")
    student = input("Enter Student Name: ").strip()
    if not student:
        print("Student name cannot be empty.")
        return
    if student not in borrowed or not borrowed[student]:
        print("No borrowing record found for this student.")
        return
    print(f"Borrowed books by {student}: {borrowed[student]}")
    book_id = input("Enter Book ID to return: ").strip()
    if not book_id:
        print("Book ID cannot be empty.")
        return
    if book_id not in borrowed[student]:
        print(f"{student} did not borrow book {book_id}.")
        return
    # proceed to return
    borrowed[student].remove(book_id)
    # ensure book exists in books dict and increment copies
    books.setdefault(book_id, {"title": "Unknown", "author": "Unknown", "copies": 0})
    books[book_id]["copies"] = books[book_id].get("copies", 0) + 1
    print(f"{student} has returned {book_id}. Copies now: {books[book_id]['copies']}")




def show_menu():
    """Display main menu options."""
    print("\n" + "=" * 60)
    print("Library Book Manager")
    print("=" * 60)
    print("1. Add / Update Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View Borrowed Records")
    print("7. Save books & borrowed records to CSV")
    print("8. Load books & borrowed records from CSV")
    print("9. Load Sample Data (demo)")
    print("0. Exit")
    # ...existing code...
def main_loop():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            view_borrowed()  # or use view_borrowed_books() if that's the function in your file
        elif choice == "7":
            save_books_to_csv()
            save_borrowed_to_csv()
        elif choice == "8":
            load_books_from_csv()
            load_borrowed_from_csv()
        elif choice == "9":
            sample_data()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
        input("\nPress Enter to continue...")  # pause before showing menu again
        clear_screen()

if __name__ == "__main__":
    clear_screen()
    print("Welcome to Library Book Manager CLI")
    print("Use option 9 to load sample data for quick testing.")
    main_loop()
# ...existing code...