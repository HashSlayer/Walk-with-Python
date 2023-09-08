import tkinter as tk

def print_hello():
    print("hello")
    text_box.insert(tk.END, "hello\n")  # Insert "hello" into the text box

root = tk.Tk()
root.title("Hello GUI")

# Create a text box
text_box = tk.Text(root, height=10, width=30)
text_box.pack()

# Create a button that calls the print_hello function when clicked
hello_button = tk.Button(root, text="Print Hello", command=print_hello)
hello_button.pack()

# Run the GUI main loop
root.mainloop()
