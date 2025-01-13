#function to add weight to journal
import json


#function to read journal

#function to get one weight record

#function to edit one weight record


#class journal
#initialize from json
#add weight
#save record
#get record
#edit record
#read record
#read set of records


class WeickerLogic:
    def __init__(self, storage_link):
        self.storage_link = storage_link
        self.journal = {}
        print(self.storage_link)

    def get_all_records(self):
        with open(self.storage_link, 'r', encoding = "utf-8") as file:
            self.journal = json.load(file)
    def add_record(self, date, weight):
        self.get_all_records()
        self.journal[date] = weight
        with open(self.storage_link, 'w') as file:
            json.dump(self.journal, file, indent=4)

    def get_window_of_records(self):
        pass

    def edit_record(self):
        pass



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


    def run_ui(self):
        print(self.hello_prompt)
        while True:
            print(self.commands_prompt)
            user_command = input('Enter a command... ')
            if user_command.startswith('show'):
                self.logic.get_all_records()
                print(self.logic.journal)
            elif user_command.startswith('add'):
                date = user_command[4:7]
                weight = user_command[8:]
                self.logic.add_record(date, weight)
            elif user_command.startswith('exit'):
                break
