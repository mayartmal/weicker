import json
from resources.weicker_tools import WeickerLogic, WeickerUI
if __name__ == '__main__':
    print("started")
    storage = "data/weight_journal.json"
    weicker_logic = WeickerLogic(storage)
    weicker_ui = WeickerUI()
    weicker_ui.run_ui()
    # weicker_logic = WeickerLogic("data/weight_journal.json")
    # weicker_logic.load_all_records()
    # weicker_logic.show_all_records()


