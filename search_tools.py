if __name__ == "__main__":
    pass

import math
import numpy as np
import pandas as pd
import requests
import json

def name_search(cards,search_string):
    result = []
    for oneCard in cards:
        card_ = oneCard['name'].lower().find(search_string.lower())
        if card_ >= 0:
            result.append({'name':oneCard['name'],'supertype':oneCard['supertype'],'subtypes':oneCard['subtypes'][0],'hp':oneCard['hp'],'setName':oneCard['set']['name'],'setSeries':oneCard['set']['series'],'setLegal':oneCard['set']['legalities'],'small_image':oneCard['images']['small'],'large_image':oneCard['images']['large']})
    return result