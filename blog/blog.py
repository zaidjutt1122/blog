import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql

class BlogApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Blog App")
        self.geometry("1350x700+0+0")

        self.create_widgets()

    # Database connection details
    db_host = "localhost"
    db_user = "root"
    db_password = ""
    db_name = "listing"

    # Establish a connection to the MySQL database
    connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

    def create_widgets(self):

        # Header
        
        header_frame = tk.Label(self, bg="lightblue", pady=10)
        header_frame.pack(fill="x")

        title_label = tk.Label(header_frame, text="My Blog", font=("Arial", 24), fg="black", padx=10)
        title_label.pack(side="left")

        # Title label and entry
        title_label = tk.Label(self, text="Title:")
        title_label.pack(anchor=tk.W)
        self.title_entry = tk.Entry(self)
        self.title_entry.pack(anchor=tk.W, padx=10)

        # Author label and entry
        author_label = tk.Label(self, text="Author:")
        author_label.pack(anchor=tk.W)
        self.author_entry = tk.Entry(self)
        self.author_entry.pack(anchor=tk.W, padx=10)

        # Description label and text box
        description_label = tk.Label(self, text="Description:")
        description_label.pack(anchor=tk.W)
        self.description_text = tk.Text(self, height=5, width=30)
        self.description_text.pack(anchor=tk.W, padx=10)

        # Publish and Back buttons
        button_frame = tk.Frame(self)
        button_frame.pack(anchor=tk.W, pady=10)

        publish_button = tk.Button(button_frame, text="Publish", command=self.publish)
        publish_button.pack(side=tk.LEFT)

        back_button = tk.Button(button_frame, text="Back", command=self.go_back)
        back_button.pack(side=tk.LEFT, padx=5)

        # Footer
        footer_label = tk.Label(self, bg="lightblue", text="© 2023 Blog App. All rights reserved.", font=("Arial", 8))
        footer_label.pack(side=tk.BOTTOM, fill="x")

    def publish(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        description = self.description_text.get("1.0", tk.END).strip()

        if not title or not author or not description:
            messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
            return

        # Create a new blog post with the provided information
        ilist = {
            "title": title,
            "author": author,
            "description": description
        }

        # Insert the blog post data into the MySQL database
        with self.connection.cursor() as cursor:
            insert_query = "INSERT INTO ilist (title, author, description) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (title, author, description))
            self.connection.commit()
            self.connection.close()

        # Clear the entry fields
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.description_text.delete("1.0", tk.END)

        messagebox.showinfo("Success", "Blog post published successfully!")
        self.destroy()
        import home

    def print_to_home(self, ilist):
        # Code to print the blog post on the home page
        # You can customize this method according to your requirements
        print(f"Title: {ilist['title']}")
        print(f"Author: {ilist['author']}")
        print(f"Description: {ilist['description']}")
        print()
        # self.connection.close()
    
    
        

    def go_back(self):
        # Code to navigate back to the home page
        # You can customize this method according to your requirements
        # In this example, we simply destroy the current window
        self.destroy()
        import home

# Create an instance of the BlogApp class
blog_app = BlogApp()

# Run the application
blog_app.mainloop()




