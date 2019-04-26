#!/usr/bin/env python3
"""mapper.py"""

import sys
import json
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # parse the tweets
    try:
        tweet = json.loads(line)
    except:
        continue
    # disregard the "retweets"
    if 'retweeted_status' not in tweet:
        # read the text
        text = tweet['text']

        # increase counters
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if re.search('han', text, re.I):
            print('han', 1, sep='\t')
        if re.search('hon', text, re.I):
            print('hon', 1, sep='\t')
        if re.search('den', text, re.I):
            print('den', 1, sep='\t')
        if re.search('det', text, re.I):
            print('det', 1, sep='\t')
        if re.search('denna', text, re.I):
            print('denna', 1, sep='\t')
        if re.search('denne', text, re.I):
            print('denne', 1, sep='\t')
        if re.search('hen', text, re.I):
            print('hen', 1, sep='\t')
        
        
        # count this tweet as 'unique'
        print('total_unique', 1, sep='\t') 