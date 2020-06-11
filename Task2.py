"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

durations = {}
phone_number = ""
# Populate duration record with accumulated for each call
for call in calls:
    call_duration = int(call[3])
    calling_phone = call[0]
    receiving_phone = call[1]
    if calling_phone in durations:
        durations[calling_phone] = durations[calling_phone] + call_duration
    else:
        durations[calling_phone] = call_duration

    if receiving_phone in durations:
        durations[receiving_phone] = durations[receiving_phone] + call_duration
    else:
        durations[receiving_phone] = call_duration

max_duration = 0
phone_with_max_duration = ""
# Traverse the durations and get the maxium
for number in durations:
    if (durations[number] > max_duration):
        max_duration = durations[number]
        phone_with_max_duration = number

print(f"{phone_with_max_duration} spent the longest time,\
{max_duration} seconds, on the phone during September 2016.")

# Complexity O(n)
