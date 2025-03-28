# Book Search CLI Application

## Introduction
This application allows users to search for books using an external API, save their favorite books into a local SQLite database, and view those saved books through a CLI interface.

## Features
- Search for books using an external API.
- Save books to favorites.
- View favorite books.

## External API Used
- **Google Books API**: The application fetches book data from Google Books API (https://developers.google.com/books).

### API Key Management
- The Google Books API is a public API and does not require an API key for basic requests. Make sure to check the API documentation for additional features or limits.

## Requirements
- Python 3.x
- SQLite
  
## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/book-search-cli.git
cd book-search-cli
2. Install dependencies
Ensure that you have Python 3 installed, and then install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the CLI Application
After initializing the database, run the CLI application:

bash
Copy
Edit
python book_search.py
Follow the prompts to search for books, save favorites, and view your saved books.                                                                                                                                                 
