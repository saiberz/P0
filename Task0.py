"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def dict_record(tuple_record):
    return {
        'incoming_number': tuple_record[0],
        'answering_number': tuple_record[1],
        'time': tuple_record[2]
    }


first_text_record = dict_record(texts[0])
first_message = f"First record of texts, {first_text_record['incoming_number']} \
texts {first_text_record['answering_number']} at time {first_text_record['time']}"

last_call_record = dict_record(calls[-1])
second_message = f"Last record of calls, {last_call_record['incoming_number']} \
calls {last_call_record['answering_number']} at time {last_call_record['time']}"

print(first_message)
print(second_message)

# Complexity O(n)
