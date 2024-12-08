#!/usr/bin/python3
import sys
processing = __import__('1-batch_processing')

##### print processed users in a batch of 50
try:
    for processed_batch in processing.batch_processing(50):  # Iterate through the batches
        for user in processed_batch:  # Print each user in the batch
            print(user)
except BrokenPipeError:
    sys.stderr.close()
