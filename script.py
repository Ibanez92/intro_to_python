import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("GUI Example")

# Create a label widget
label = tk.Label(window, text="Hello, GUI World!")
label.pack()

# Create a button widget
button = tk.Button(window, text="Click Me!")
button.pack()

# Start the main event loop
window.mainloop()