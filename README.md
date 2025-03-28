Book Search CLI Application
Overview
The Book Search CLI is a command-line application that allows users to search for books using the Google Books API, save them to a local SQLite database, and view their saved favorites. This README provides instructions for running the application locally and deploying it to web servers.

Features
Search for books using the Google Books API.

Save favorite books to a local SQLite database.

View saved books through the CLI.

APIs Used
Google Books API: This API allows fetching book data. No API key is required for basic usage. API Documentation

Requirements
Python 3.x

SQLite3 (for local database)

Web Servers: Ubuntu (for deployment)

How to Run Locally
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/book-search-cli.git
cd book-search-cli
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Application:

bash
Copy
Edit
python book_search.py
Deployment
To deploy this application to a web server, follow these steps:

1. Transfer Application to Server
Use SCP to transfer the project files to the server:

bash
Copy
Edit
scp -r /path/to/your/project ubuntu@your-server-ip:/home/ubuntu/project
2. Install Dependencies on the Server
SSH into the server and install Python and SQLite:

bash
Copy
Edit
ssh ubuntu@your-server-ip
sudo apt update
sudo apt install python3 python3-pip sqlite3
cd /home/ubuntu/project
pip3 install -r requirements.txt
3. Run the Application on the Server
bash
Copy
Edit
python3 book_search.py
Challenges & Solutions
Deploying to Remote Servers: Transferring files and setting up dependencies required careful attention to ensure all necessary libraries were installed on the servers.

Load Balancing: Setting up NGINX for load balancing was challenging but was resolved by configuring upstream settings to balance requests across multiple servers.

Credits
Google Books API: For fetching book data. API Documentation
