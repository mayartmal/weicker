import json
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class WeickerLogic:
    def __init__(self, storage_link):
        self.storage_link = storage_link
        self.analytics_storage_link = self.storage_link.replace("journal", "analytics")
        self.journal = {}
        self.analytics_journal = {}
        print(self.storage_link)
    def get_all_records(self):
        with open(self.storage_link, 'r', encoding = "utf-8") as file:
            self.journal = json.load(file)
    def add_record(self, weight):
        today_date = datetime.now().strftime("%d%m%Y")
        self.get_all_records()
        self.journal[today_date] = weight
        with open(self.storage_link, 'w') as file:
            json.dump(self.journal, file, indent=4)
    def edit_record(self, date, weight):
        self.get_all_records()
        self.journal[date] = weight
        sorted_journal = dict(sorted(self.journal.items()))
        self.journal = sorted_journal
        with open(self.storage_link, 'w') as file:
            json.dump(self.journal, file, indent=4)
    def do_analytics(self):
        self.get_all_records()
        weights = list(self.journal.values())
        smooth_window = 3
        smooth_weights = np.convolve(weights, np.ones(smooth_window)/smooth_window, mode='valid').tolist()
        for index in range(smooth_window - 1):
            smooth_weights.insert(0, None)
        for iteration, (date_id, weight) in enumerate(self.journal.items(), start=1):
            print(iteration, date_id, weight)
            self.analytics_journal[date_id] = {"current_weight": weights[iteration-1], "moving_average": smooth_weights[iteration-1]}
        print(self.analytics_journal)
        with open(self.analytics_storage_link, 'w') as file:
            json.dump(self.analytics_journal, file, indent=4)






    # def get_window_of_records(self):
    #     pass


class WeickerConsoleUI:
    def __init__(self, logic:WeickerLogic):
        self.logic = logic
        self.hello_prompt = 'Welcome to the Weicker'
        self.commands_prompt = ('\nWhat do you want to do?\n'
                             '"add" - add weight record\n'
                             '"show" - show all records\n'
                             '"edit" - edit record\n'
                             '"show DDMMYY" - show particular record\n'
                             '"exit" - close the Weicker')
    def show_all(self):
        pass
    def write_weight(self):
        pass
    def run_ui(self):
        print(self.hello_prompt)
        while True:
            print(self.commands_prompt)
            user_command = input('Enter a command... ')
            if user_command.startswith('show'):
                self.logic.get_all_records()
                for date_id, weight in self.logic.journal.items():
                    date = datetime.strptime(date_id, "%d%m%Y")
                    formatted_date = date.strftime("%d.%m.%Y")
                    print(f"{formatted_date}, {weight} kg")
            elif user_command.startswith('add'):
                weight = float(user_command[4:])
                self.logic.add_record(weight)
            elif user_command.startswith('edit'):
                date = user_command[5:15].replace('.', '')
                weight = float(user_command[16:])
                self.logic.edit_record(date, weight)
            elif user_command.startswith('analytics'):
                self.logic.do_analytics()
                date = list(self.logic.analytics_journal.keys())
                raw_weights = [record["current_weight"] for record in self.logic.analytics_journal.values()]
                smooth_weights = [record["moving_average"] for record in self.logic.analytics_journal.values()]

                plt.plot(date, raw_weights, label="Raw weights", linestyle='--')
                plt.plot(date, smooth_weights, label="Smooth weights", linestyle='-.')
                plt.xticks(rotation=90)
                plt.legend()
                plt.show()
                #do mov aver analytics and regression analitics
                pass

            elif user_command.startswith('exit'):
                break
