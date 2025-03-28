# Book Search CLI Application

## Overview
The **Book Search CLI** is a command-line application that allows users to search for books using the Google Books API, save them to a local SQLite database, and view their saved favorites. This README provides instructions for running the application locally and deploying it to web servers.

## Features
- Search for books using the Google Books API.
- Save favorite books to a local SQLite database.
- View saved books through the CLI.

## APIs Used
- **Google Books API**: Fetches book data from Google’s database. No API key is required for basic usage. [API Documentation](https://developers.google.com/books/docs/v1/getting_started)

## Requirements
- **Python 3.x**: Ensure you have Python 3.x installed. If not, you can download it from [python.org](https://www.python.org/).
- **SQLite3**: This is used to store the saved books. It's usually pre-installed on most systems, but you can install it with the following commands based on your OS:
  - **Ubuntu/Debian**: `sudo apt install sqlite3`
  - **macOS**: SQLite3 comes with macOS by default. You can also install it via Homebrew using `brew install sqlite`.
  - **Windows**: Download and install SQLite from [sqlite.org](https://www.sqlite.org/download.html).
- **Rich**: Python package for improved command-line output.
  - Install it using pip: `pip install rich`

## How to Run Locally
### 1. Clone the Repository
 `git clone https://github.com/your-username/book-search-cli.git
cd book-search-cli `
### 2. Install Dependencies
Make sure you have Python 3 and the required libraries installed. Use pip to install dependencies:
`pip install rich`
3. Run the Application
`python book_search.py`
### Deployment
To deploy this application to a web server, follow these steps:

 ### 1. Transfer Application to Server
Use SCP (Secure Copy Protocol) to transfer project files to the server:
`scp -r /path/to/your/project ubuntu@your-server-ip:/home/ubuntu/project`
### 2. Install Dependencies on the Server
SSH into the server and install necessary software:

`ssh ubuntu@your-server-ip
sudo apt update
sudo apt install python3 python3-pip sqlite3
pip3 install rich
cd /home/ubuntu/project`
 ### 3. Run the Application on the Server

`python3 book_search.py`

 ### Challenges & Solutions
  ### 1. Deploying to Remote Servers
**Challenge**: Transferring files and setting up dependencies required careful attention.

**Solution**: Ensured all necessary libraries were installed on the server before execution.


### Credits
**Google Books API**: Used for fetching book data. API Documentation

**Libraries Used**: Python standard libraries, SQLite3, and Rich for enhanced CLI output.
