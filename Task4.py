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

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".


# O(1)
def is_marketing_number(phone_number):
    if(phone_number[0:3] == "140"):
        return True
    else:
        return False


# O(n)
def get_marketing_format_numbers(phone_numbers):
    marketing_numbers = []
    for phone_number in phone_numbers:
        if is_marketing_number(phone_number):
            marketing_numbers.append(phone_number)
    return marketing_numbers


# O(nlog(n))
def get_caller_numbers(call_records):
    caller_numbers = []
    for call_record in call_records:
        if(call_record[0] not in caller_numbers):
            caller_numbers.append(call_record[0])
    return sorted(caller_numbers)


# O(nlog(n))
def get_receiver_numbers(call_records):
    receiver_numbers = []
    for call_record in call_records:
        if(call_record[1] not in receiver_numbers):
            receiver_numbers.append(call_record[1])
    return sorted(receiver_numbers)


# O(nlog(n))
def get_text_numbers(text_records):
    text_numbers = []
    for text_record in text_records:
        if(text_record[0] not in text_numbers):
            text_numbers.append(text_record[0])
        if(text_record[1] not in text_numbers):
            text_numbers.append(text_record[1])
    return sorted(text_numbers)


# O(n^2)
def get_marketing_activity_numbers(phone_numbers, valid_numbers):
    marketing_numbers = []
    for phone_number in phone_numbers:
        if(phone_number not in valid_numbers):
            marketing_numbers.append(phone_number)
    return marketing_numbers


def print_list(custom_list):
    for x in custom_list:
        print(x)


numbers_with_valid_activity = \
    get_receiver_numbers(calls) + get_text_numbers(texts)
caller_numbers = get_caller_numbers(calls)
marketing_activity_numbers = \
    get_marketing_activity_numbers(caller_numbers, numbers_with_valid_activity)
telemarketing_numbers = \
    get_marketing_format_numbers(marketing_activity_numbers)

print(f"These numbers could be telemarketers:")
print_list(telemarketing_numbers)

# Complexity O(n^2)
