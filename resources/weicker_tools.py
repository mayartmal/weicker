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

    def load_all_records(self):
        with open(self.storage_link, 'r', encoding = "utf-8") as file:
            content = file.read().strip()
            if content:
                self.journal = json.load(file)
            else:
                self.journal = {}


    def show_all_records(self):
        print(self.journal)

    def get_record(self):
        pass

    def get_window_of_records(self):
        pass

    def add_record(self):
        pass

    def edit_record(self):
        pass

class WeickerUI:
    def __init__(self):
        self.hello_prompt = 'Welcome to the Weicker'
        self.commands_prompt = ('\nWhat do you want to do?\n'
                             '"add" - add weight record\n'
                             '"show all" - show all records\n'
                             '"edit" - edit record\n'
                             '"show DDMMYY" - show particular record\n'
                             '"exit" - close the Weicker')


    def run_ui(self):
        print(self.hello_prompt)
        while True:
            print(self.commands_prompt)
            user_command = input('Enter a command... ')
            if user_command != 'exit':
                print('Thanks for the command')
            elif user_command.startswith('exit'):
                break
