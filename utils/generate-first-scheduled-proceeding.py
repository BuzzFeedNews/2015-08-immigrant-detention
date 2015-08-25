import pandas as pd
import loaders
import sys, os
HERE = os.path.dirname(os.path.realpath(__file__))

_schedule = loaders.load_file("tbl_schedule.csv", 
                              parse_dates = ["ADJ_DATE"],
                              dtype = {"IDNCASE": str, "IDNPROCEEDING": str,
                                       "GENERATION": str})

first_scheduled_proceeding = _schedule[_schedule["GENERATION"] == "99"]\
                            .sort("ADJ_DATE", ascending = True)\
                            .groupby(["IDNCASE","IDNPROCEEDING"]).first().reset_index()

OUT_PATH = os.path.join(HERE, "../data/first_scheduled_proceeding.csv")
first_scheduled_proceeding.to_csv(OUT_PATH, index=None)
