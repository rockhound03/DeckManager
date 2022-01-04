if __name__ == "__main__":
    pass

import math
import numpy as np
import pandas as pd
import requests
import json

def load_set_list():
    try:
        with open("sets.json","r") as sets_file:
            temp_obj = json.load(sets_file)
            result = temp_obj['data']
    except:
        result = "Failed to read set list."
    return result