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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# O(1)
def get_area_code(fixed_phone_number):
    area_code = ""
    for char in fixed_phone_number[1:]:
        if(char == ")"):
            break
        else:
            area_code = area_code + char
    return area_code


# O(1)
def get_mobile_prefix(mobile_phone_number):
    prefix = ""
    for char in mobile_phone_number[:4]:
        prefix = prefix + char
    return prefix


# O(1)
def is_fixed(phone_number):
    if ("(" in phone_number and ")" in phone_number):
        return True
    return False


# O(1)
def is_mobile(phone_number):
    if (" " in phone_number and phone_number[0] in ["7", "8", "9"]):
        return True
    return False


bangalore_list = []
from_fixed_to_fixed_bangalore = 0
from_fixed_to_other = 0


# O(n)
def add_to_list(code):
    if(code not in bangalore_list):
        bangalore_list.append(code)


# O(n)
for call in calls:
    calling_phone = call[0]
    receiving_phone = call[1]
    if(is_fixed(calling_phone) and get_area_code(calling_phone) == "080"):
        if(is_fixed(receiving_phone)):
            receiver_area_code = get_area_code(receiving_phone)
            if(receiver_area_code == "080"):
                from_fixed_to_fixed_bangalore = \
                    from_fixed_to_fixed_bangalore + 1
            else:
                from_fixed_to_other = from_fixed_to_other + 1
            add_to_list(receiver_area_code)
        if(is_mobile(receiving_phone)):
            from_fixed_to_other = from_fixed_to_other + 1
            add_to_list(get_mobile_prefix(receiving_phone))


# O(nlog(n))
def print_sorted_list(custom_list):
    for x in sorted(custom_list):
        print(x)


print("The numbers called by people in Bangalore have codes:")
print_sorted_list(bangalore_list)

# Complexity O(nlog(n))


from_fixed = from_fixed_to_fixed_bangalore + from_fixed_to_other
percentage = round(from_fixed_to_fixed_bangalore * 100 / from_fixed, 2)
print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


