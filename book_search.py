import sqlite3
import requests
import csv
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm

# Database Name
DB_NAME = "books.db"

# API URL
API_URL = "https://openlibrary.org/search.json"

# Console for UI
console = Console()


# Initialize the Database
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            published_year TEXT,
            subjects TEXT,
            isbn TEXT
        )
    ''')

    conn.commit()
    conn.close()


# Search for Books
def search_books():
    page = 1
    while True:
        query = Prompt.ask("\nEnter book title or author")
        response = requests.get(API_URL, params={"q": query, "page": page, "limit": 5})

        if response.status_code != 200:
            console.print("[bold red]❌ Error fetching books![/bold red]")
            return

        data = response.json()
        books = data.get("docs", [])

        if not books:
            console.print("[yellow]No books found![/yellow]")
            return

        table = Table(title=f"📚 Search Results (Page {page})", show_lines=True)
        table.add_column("ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Title", style="bold magenta")
        table.add_column("Author(s)", style="green")

        book_dict = {}
        for idx, book in enumerate(books, start=1):
            title = book.get("title", "Unknown")
            authors = ", ".join(book.get("author_name", ["Unknown"]))
            year = str(book.get("first_publish_year", "N/A"))
            subjects = ", ".join(book.get("subject", ["Unknown"])) if "subject" in book else "N/A"
            isbn = ", ".join(book.get("isbn", ["Unknown"])) if "isbn" in book else "N/A"
            table.add_row(str(idx), title, authors)
            book_dict[str(idx)] = (title, authors, year, subjects, isbn)

        console.print(table)

        choice = Prompt.ask("Enter book ID to save as favorite or press Enter to skip", default="")
        if choice in book_dict:
            save_favorite(*book_dict[choice])

        next_page = Confirm.ask("Do you want to see more results?")
        if not next_page:
            break
        else:
            page += 1


# Save Book to Favorites
def save_favorite(title, author, year, subjects, isbn):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO favorites (title, author, published_year, subjects, isbn) VALUES (?, ?, ?, ?, ?)",
        (title, author, year, subjects, isbn)
    )
    conn.commit()
    conn.close()

    console.print(f"[green]✔ Saved '{title}' to favorites![/green]")


# View Favorite Books
def view_favorites():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author FROM favorites")
    books = cursor.fetchall()
    conn.close()

    if not books:
        console.print("[yellow]No favorite books found![/yellow]")
        return

    table = Table(title="⭐ Favorite Books", show_lines=True)
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="bold magenta")
    table.add_column("Author", style="green")

    for book in books:
        table.add_row(str(book[0]), book[1], book[2])

    console.print(table)


# Remove Book from Favorites
def remove_favorite():
    view_favorites()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    book_id = Prompt.ask("\nEnter ID of the book to remove (or press Enter to cancel)", default="")

    if not book_id:
        console.print("[yellow]❌ Cancelled![/yellow]")
        return

    cursor.execute("DELETE FROM favorites WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

    console.print("[red]❌ Book removed from favorites![/red]")


# Export Favorite Books to CSV
def export_favorites_csv():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT title, author FROM favorites")
    books = cursor.fetchall()
    conn.close()

    if not books:
        console.print("[yellow]No favorite books found![/yellow]")
        return

    with open("favorites.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author"])
        writer.writerows(books)

    console.print("[green]📂 Favorites exported to favorites.csv[/green]")


# Search Within Favorite Books
def search_favorites():
    keyword = Prompt.ask("Enter keyword to search in favorites")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author FROM favorites WHERE title LIKE ? OR author LIKE ?",
                   (f"%{keyword}%", f"%{keyword}%"))
    books = cursor.fetchall()
    conn.close()

    if not books:
        console.print("[yellow]No matching books found![/yellow]")
        return

    table = Table(title="🔍 Search Results in Favorites", show_lines=True)
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="bold magenta")
    table.add_column("Author", style="green")

    for book in books:
        table.add_row(str(book[0]), book[1], book[2])

    console.print(table)


# Main Menu
def main():
    init_db()
    while True:
        console.print("\n📚 [bold cyan]Book Search CLI[/bold cyan]", style="bold underline")
        console.print("[1] 🔍 Search Books")
        console.print("[2] ⭐ View Favorites")
        console.print("[3] ❌ Remove Favorite")
        console.print("[4] 📂 Export Favorites to CSV")
        console.print("[5] 🔍 Search Favorite Books")
        console.print("[6] 🔚 Exit")

        choice = Prompt.ask("\nChoose an option", choices=["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            search_books()
        elif choice == "2":
            view_favorites()
        elif choice == "3":
            remove_favorite()
        elif choice == "4":
            export_favorites_csv()
        elif choice == "5":
            search_favorites()
        elif choice == "6":
            console.print("[bold red]Exiting... Goodbye![/bold red]")
            break


# Run the CLI
if __name__ == "__main__":
    main()

