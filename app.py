from resources.weicker_tools import WeickerLogic, WeickerConsoleUI
import json


if __name__ == '__main__':
    storage = "data/weight_journal.json"

    weicker_logic = WeickerLogic(storage)
    weicker_ui = WeickerConsoleUI(weicker_logic)
    weicker_logic.get_all_records()
    weicker_ui.run_ui()
    record = {
         'today': 97
    }
    # weicker_logic.add_record(record)

    # weicker_logic = WeickerLogic("data/weight_journal.json")
    # weicker_logic.load_all_records()
    # weicker_logic.show_all_records()


