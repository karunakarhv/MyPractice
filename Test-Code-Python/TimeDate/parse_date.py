# Fuzzy Parsing of Dates
#
# Problem
# We need to read and accept dates that don't conform to
# the datetime standard format of "YYYY MM DD"

import datetime
import dateutil.parser

def tryParse(date):
    # dateutil.parser needs a string argument
    kwargs = {}
    if isinstance(test, (tuple, list)):
        date = ' '.join([str(x) for x in date])
    elif isinstance(date, int):
        date = str(date)
    elif isinstance(date, dict):
        kwargs = date
        date = kwargs.pop('date')

    try:
        try:
            parseDate = dateutil.parser.parse(date, **kwargs)
            print('Sharp {} -> {}'.format(date, parseDate))
        except ValueError:
            parseDate = dateutil.parser.parse(date, fuzzy=True, **kwargs)
            print('Fuzzy {} -> {}'.format(date, parseDate))
    except Exception as err:
        print('Try as I may, I cannot parse {} ({})'.format(date, err))

if __name__ == '__main__':
    tests = (
        "January 3, 2003",
        (5, "Oct", 55),
        "Thursday, November 18",
        "7/24/04", # a string with slashes
        "24-7-2004", # European-format string
        {'date':"5-10-1955", "dayfirst":True}, # a dict including the kwarg
        "5-10-1955", # dayfirst, no kwarg
        19950317, # not a string
        "11AM on the 11th day of 11th month, in the year of our Lord 1945",
    )
    for test in tests:
        tryParse(test)