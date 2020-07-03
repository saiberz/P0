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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


# O(n)
def get_caller_numbers(call_records):
    caller_numbers = set()
    for call_record in call_records:
        caller_numbers.add(call_record[0])
    return caller_numbers


# O(n)
def get_receiver_numbers(call_records):
    receiver_numbers = set()
    for call_record in call_records:
        receiver_numbers.add(call_record[1])
    return receiver_numbers


# O(n)
def get_text_numbers(text_records):
    text_numbers = set()
    for text_record in text_records:
        text_numbers.add(text_record[0])
        text_numbers.add(text_record[1])
    return text_numbers


def print_list(custom_list):
    for x in custom_list:
        print(x)


# Set of numbers that:
# - at least have received a call
# - sent or received a text
numbers_with_valid_activity = \
    get_receiver_numbers(calls) | get_text_numbers(texts)

# Set of numbers that have made at least one call
caller_numbers = get_caller_numbers(calls)

# All the numbers that have made at least might be a marketing number
# but we need to remove the numbers that have valid activit
# caller_numbers - numbers_with_valid_activity

# O(n)
telemarketing_numbers = caller_numbers - numbers_with_valid_activity

print(f"These numbers could be telemarketers:")
# O(nlogn)
print_list(sorted(telemarketing_numbers))

# Complexity O(nlogn)
