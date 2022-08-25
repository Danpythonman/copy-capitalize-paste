#!C:\Python\Python385\pythonw.exe
# ------------------------------------------------------------------------------
# cap_paste.py
# Daniel Di Giovanni
# August 25, 2020
# Allows user to capitalize or decapitalize text in their clipboard.
# ------------------------------------------------------------------------------


import tkinter as tk
from tkinter import ttk
import pyperclip


def clear_textbox(input_field):
    """Clears the textbox"""

    # Delete the text from the textbox
    # "1.0" means start at line 1, character 0
    # tk.END means read to the end of the string
    input_field.delete("1.0", tk.END)


def copy_string(input_field):
    """Copies the text in the textbox"""

    # Get the text from the textbox
    # "1.0" means start at line 1, character 0
    # tk.END means read to the end of the string
    user_text = input_field.get("1.0", tk.END)

    # Copy the string without the last character because it is a newline
    pyperclip.copy(user_text[:-1])


def paste_string(input_field):
    """Pastes the string the user has copied into the textbox"""

    # Insert the text the user has copied into the textbox
    # tk.END means insert the text at the end of the text in the textbox
    input_field.insert(tk.END, pyperclip.paste())


def capitalize():
    """Capitalizes the entire string that the user has copied"""

    pyperclip.copy(pyperclip.paste().upper())


def decapitalize():
    """Decapitalizes the entire string that the user has copied"""

    pyperclip.copy(pyperclip.paste().lower())


def capitalize_every_first_letter():
    """
    Capitalizes the first letter of every word in the string that the user has
    copied
    """

    # Get the string the user has copied as a list of words (split at spaces)
    user_word_list = pyperclip.paste().split()

    # Initialize new string
    new_user_string = ""

    for i in range(len(user_word_list)):
        # Add the current word to the new string with the first letter
        # capitalized and a space at the end
        new_user_string += user_word_list[i][0].upper() + \
            user_word_list[i][1:].lower() + " "

    # Copy the new string without the last space at the end
    pyperclip.copy(new_user_string[:-1])


def smart_capitalize():
    """
    Capitalizes every word except for words like "a", "the", "in", etc. in the
    string that the user has copied
    Capitalizes the String Like a Title
    """

    # List of words that should not be capitalized
    no_capitalize = ["a", "the", "in", "etc", "to", "with", "of"]

    # Get the string the user has copied as a list of words (split at spaces)
    user_word_list = pyperclip.paste().split()

    # Initialize new string with the first letter capitalized
    # The first letter in the string is always capitalized
    new_user_string = user_word_list[0][0].upper() \
        + user_word_list[0][1:].lower()

    for i in range(1, len(user_word_list)):
        # Check if the current word is in the no-capitalize list
        if user_word_list[i].lower() in no_capitalize:
            # Add the current word to the new string without capitalizing it
            # and with a space at the beginning
            new_user_string += " " + user_word_list[i].lower()
        else:
            # Add the current word to the new string with the first letter
            # capitalized and a space at the beginning
            new_user_string += " " + user_word_list[i][0].upper() \
                + user_word_list[i][1:].lower()

    # Copy the new string
    # There is no extra space at the end of this string because the space was
    # added to the beginning of each word in the for loop
    pyperclip.copy(new_user_string)


def main():
    """Main function, controls GUI"""

    # size = (500, 400)
    button_size = (15, 3)

    root = tk.Tk()

    # root.minsize(size[0], size[1])
    root.title("Copy, Capitalize, Paste")

    style = ttk.Style()
    style.configure("TButton", width=30)

    # Create and display textbox (text input field)
    # Purpose of the textbox is just so user can paste the text to view it
    textbox = tk.Text(root, width=40, height=7)
    textbox.grid(row=0, column=0, columnspan=2, padx=10, pady=(25, 10))

    # Create and display clear button
    clear_button = ttk.Button(root, command=lambda: clear_textbox(textbox),
        text="Clear")
    clear_button.grid(row=1, column=0, columnspan=2)

    # Create and display copy and paste buttons
    copy_button = ttk.Button(root, command=lambda: copy_string(textbox),
        text="Copy")
    paste_button = ttk.Button(root, command=lambda: paste_string(textbox),
        text="Paste")
    copy_button.grid(row=2, column=0)
    paste_button.grid(row=2, column=1)

    # - Capitalize functions buttons -

    # Capitalizes entire string
    capitalize_button = ttk.Button(root, command=capitalize,
        text="\nCapitalize\n")
    # Decapitalizes entire string
    decapitalize_button = ttk.Button(root, command=decapitalize,
        text="\nDecapitalize\n")
    # Capitalizes the first letter of every word in the string
    repeated_capital_button = ttk.Button(root,
        command=capitalize_every_first_letter,
        text="\nCapitalize Every Word\n")
    # Capitalizes select words
    first_capital_button = ttk.Button(root, command=smart_capitalize,
        text="\nSmart Capitalize\n")

    # Display buttons
    capitalize_button.grid(row=3, column=0)
    decapitalize_button.grid(row=3, column=1)
    first_capital_button.grid(row=4, column=0)
    repeated_capital_button.grid(row=4, column=1)

    root.mainloop()


if __name__ == "__main__":
    main()
