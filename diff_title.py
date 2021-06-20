# 安装
# pip install python-Levenshtein
# pip install fuzzywuzzy

from fuzzywuzzy import fuzz
from difflib import SequenceMatcher

def is_similar(title1, title2, threshold=0.5):

    # difflib
    sequenceMatcher = SequenceMatcher()
    sequenceMatcher.set_seqs(title1, title2)
    sml1 = sequenceMatcher.ratio()

    sml2 = fuzz.ratio(title1, title2)
    print(sml1,sml2)
    if sml1 > threshold and sml2>threshold:
        return True 
    return False 
