#!/usr/bin/env python
"""mapper.py"""

import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:
    # parse the tweets
    tweet = json.loads(line)
    # disregard the "retweets"
    if not tweet['retweeted_status']
        # read the text
        text = tweet['text']
        # split the line into words
        words = text.split().lower()
        # increase counters
        for word in words:
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
            #
            # tab-delimited; the trivial word count is 1
            if word == 'han'
                print '%s\t%s' % (word, 1) 
            elif word == 'hon'
                print '%s\t%s' % (word, 1) 
            elif word == 'den'
                print '%s\t%s' % (word, 1) 
            elif word == 'det'
                print '%s\t%s' % (word, 1) 
            elif word == 'denna'
                print '%s\t%s' % (word, 1) 
            elif word == 'denne'
                print '%s\t%s' % (word, 1) 
            elif word == 'hen'
                print '%s\t%s' % (word, 1) 
        
        # count this tweet as 'unique'
        print '%s\t%s' % ('total_unique', 1) 
            