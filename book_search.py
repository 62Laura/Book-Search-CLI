import requests
import sqlite3
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from Database import DB_NAME, init_db

API_URL = "http://openlibrary.org/search.json"
console = Console()

# Initialize database
init_db()


def search_books():
    """Search for books using Open Library API."""
    query = Prompt.ask("Enter book title or author")
    response = requests.get(API_URL, params={"q": query, "limit": 5})

    if response.status_code != 200:
        console.print("[bold red]❌ Error fetching books![/bold red]")
        return

    data = response.json()
    books = data.get("docs", [])[:5]

    if not books:
        console.print("[yellow]No books found![/yellow]")
        return

    table = Table(title="📚 Search Results", show_lines=True)
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="bold magenta")
    table.add_column("Author(s)", style="green")

    book_dict = {}
    for idx, book in enumerate(books, start=1):
        title = book.get("title", "Unknown")
        authors = ", ".join(book.get("author_name", ["Unknown"]))
        table.add_row(str(idx), title, authors)
        book_dict[str(idx)] = (title, authors)

    console.print(table)

    choice = Prompt.ask("Enter book ID to save (or press Enter to skip)", default="")
    if choice and choice in book_dict:
        save_favorite(book_dict[choice][0], book_dict[choice][1])


def save_favorite(title, author):
    """Save book to favorites in SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO favorites (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()

    console.print(f"[green]✔ Saved '{title}' to favorites![/green]")


def view_favorites():
    """Display favorite books."""
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
    table.add_column("Author(s)", style="green")

    for book in books:
        table.add_row(str(book[0]), book[1], book[2])

    console.print(table)


def main():
    while True:
        console.print("\n[bold cyan]📚 Book Search CLI[/bold cyan]", justify="center")
        console.print("[1] 🔍 Search Books")
        console.print("[2] ⭐ View Favorites")
        console.print("[3] ❌ Exit")

        choice = Prompt.ask("\nChoose an option", choices=["1", "2", "3"], default="3")

        if choice == "1":
            search_books()
        elif choice == "2":
            view_favorites()
        elif choice == "3":
            console.print("[bold green]👋 Goodbye![/bold green]")
            break


if __name__ == "__main__":
    main()
