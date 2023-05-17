import tkinter as tk
import subprocess
import pymysql

db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "listing"

# Establish a connection to the MySQL database
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

# Create a new Tkinter window
window = tk.Tk()
window.title("Home Page")
window.geometry("1350x700+0+0")

def search():
    search_query = search_entry.get()
    # Functionality for performing a search based on the query
    print("Searching for:", search_query)
    show_search_results(search_query)
    window.title("Search Page")
    
def show_search_results(search_query):
    # Clear existing search results
    clear_search_results()

    with connection.cursor() as cursor:
        select_query = "SELECT * FROM ilist WHERE title LIKE %s OR author LIKE %s"
        cursor.execute(select_query, (f'%{search_query}%', f'%{search_query}%'))
        result = cursor.fetchall()

        if not result:
            # Display a message when no results are found
            no_results_label = tk.Label(window, text="No results found.")
            no_results_label.pack(anchor=tk.W)
        else:
            for row in result:
                title = row[0]
                author = row[1]
                description = row[2]

                # Create labels to display the data
                title_label = tk.Label(window, text=f"Title: {title}")
                title_label.pack(anchor=tk.W)
                author_label = tk.Label(window, text=f"Author: {author}")
                author_label.pack(anchor=tk.W)
                description_label = tk.Label(window, text=f"Description: {description}")
                description_label.pack(anchor=tk.W)
                separator = tk.Label(window, text="-------------------------")
                separator.pack(anchor=tk.W)

    # Create a "Back" button to return to the home page
    back_button = tk.Button(window, text="Back", cursor="hand2", font=("Arial", 12), command=back_to_home)
    back_button.pack()

def clear_search_results():
    # Clear existing search results
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

def back_to_home():
    # Destroy the current search page window and recreate the home page window
    window.destroy()
    subprocess.call(['python', 'home.py'])

def create_post():
    # Functionality for creating a post
    window.destroy()
    subprocess.call(['python', 'blog.py'])


# Create the header with a title, search bar, and search button
header_frame = tk.Frame(window, bg="lightblue", pady=10)
header_frame.pack(fill="x")

title_label = tk.Label(header_frame, text="My Blog", font=("Arial", 24), fg="black", padx=10)
title_label.pack(side="left")

search_button = tk.Button(header_frame, text="Search", cursor="hand2", font=("Arial", 12), command=search)
search_button.pack(side="right", padx=(0, 10))

search_entry = tk.Entry(header_frame, width=30, font=("Arial", 12))
search_entry.pack(side="right", padx=10)

# Create the footer
footer_frame = tk.Frame(window, bg="lightblue", pady=10)
footer_frame.pack(fill="x", side="bottom")

footer_label = tk.Label(footer_frame, text="© 2023 My Blog. All rights reserved.", font=("Arial", 10), fg="black")
footer_label.pack()

# Create the "Create Post
button_frame = tk.Frame(window, pady=20)
button_frame.pack()

create_post_button = tk.Button(button_frame, text="Create Post", cursor="hand2", font=("Arial", 14), command=create_post)
create_post_button.pack()

def fetch_data():
    with connection.cursor() as cursor:
        select_query = "SELECT * FROM ilist"
        cursor.execute(select_query)
        result = cursor.fetchall()

        for row in result:
            title = row[1]
            author = row[2]
            description = row[3]

            # Format the data
            formatted_title = f"Title: {title}"
            formatted_author = f"Author: {author}"
            formatted_description = f"Description: {description}"

            # Create labels to display the formatted data
            title_label = tk.Label(window, text=formatted_title)
            title_label.pack(anchor=tk.W)
            author_label = tk.Label(window, text=formatted_author)
            author_label.pack(anchor=tk.W)
            description_label = tk.Label(window, text=formatted_description)
            description_label.pack(anchor=tk.W)
            separator = tk.Label(window, text="-------------------------")
            separator.pack(anchor=tk.W)

fetch_data()

window.mainloop()
connection.close()