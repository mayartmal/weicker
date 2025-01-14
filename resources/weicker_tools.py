import json
from datetime import datetime




class WeickerLogic:
    def __init__(self, storage_link):
        self.storage_link = storage_link
        self.journal = {}
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



    # def get_window_of_records(self):
    #     pass
    #
    # def edit_record(self):
    #     pass



class WeickerUI:
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
            elif user_command.startswith('exit'):
                break
