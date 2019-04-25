#!/usr/bin/env python
"""mapper.py"""

import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:
    # parse the tweets
    tweet = json.loads(line)
    # disregard the "retweets"
    if 'retweeted_status' not in tweet:
        # read the text
        text = tweet['text']
        # split the line into words
        words = text.split()
        # increase counters
        for word in words:
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
            #
            # tab-delimited; the trivial word count is 1
            if word.lower() == 'han':
                print(word, 1, sep='\t') 
            elif word.lower() == 'hon':
                print(word, 1, sep='\t') 
            elif word.lower() == 'den':
                print(word, 1, sep='\t') 
            elif word.lower() == 'det':
                print(word, 1, sep='\t') 
            elif word.lower() == 'denna':
                print(word, 1, sep='\t')
            elif word.lower() == 'denne':
                print(word, 1, sep='\t') 
            elif word.lower() == 'hen':
                print(word, 1, sep='\t')
        
        # count this tweet as 'unique'
        print('total_unique', 1, sep='\t') 