#!/usr/bin/env python

import pandas as pd
from cStringIO import StringIO
import dateutil
import os, sys
import warnings

HERE = os.path.dirname(os.path.realpath(__file__))

BASE_CASE_PATH = os.path.join(HERE, "../data/case-foia/")

warnings.simplefilter(action="ignore", category=pd.io.common.DtypeWarning)
warnings.simplefilter(action="ignore", category=UserWarning)

def clean_date(date_string):
    try:
        return dateutil.parser.parse(date_string)
    except:
        return None

def load_file(file_path, **kwargs):
    with open(BASE_CASE_PATH + file_path) as f:
        # Remove NULL bytes from raw CSV
        denulled = StringIO(f.read().replace("\x00", "").replace('"', ""))
        dataframe = pd.read_csv(denulled,
                                sep = "\t", 
                                na_values = ["N/A", "", " "],
                                error_bad_lines = False,
                                **kwargs)
    return dataframe
