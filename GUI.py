import tkinter as tk
from dataFetching import DataFetching
import json


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.data_fetch_win()
        self.fetch_input = tk.Entry(self, width=50)
        self.fetch_input.insert(0, "http://www.ufcstats.com/fighter-details/1338e2c7480bdf9e")
        self.fetch_input.pack()
        self.data = DataFetching()
        self.stats = None

    def data_fetch_win(self):
        """ window display"""
        self.master.title("UFC fighters stats")
        self.master.minsize(1000, 500)
        fetch_button = tk.Button(text="Fetch data", command=lambda: self.fetch_data(self.fetch_input))
        fetch_button.pack()
        fetch_button = tk.Button(text="save stats", command=self.save)
        fetch_button.pack()

    def fetch_data(self, url):
        # self.data.fetch_fighter_stats("http://www.ufcstats.com/fighter-details/1338e2c7480bdf9e")
        self.data.fetch_fighter_stats(url.get())
        self.stats = self.data.get_fighter_data()
        print(self.stats)

    def save(self):
        # with open('fighters.json', 'a') as outfile:
        #     json.dump(self.stats, outfile)

        pass
