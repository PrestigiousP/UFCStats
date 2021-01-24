import tkinter as tk
from GUI import GUI
import psycopg2
import json
from Fighter import Fighter


def main():

    conn = psycopg2.connect("dbname=UFCStats user=postgres password=196432")
    if not conn:
        return 1
    fighters = Fighter()

    root = tk.Tk()
    gui = GUI(master=root)
    gui.mainloop()


# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
