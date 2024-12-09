import math

def read_input(file_name):
    page_ordering_rules = []
    updates = []

    with open(file_name, 'r') as file:
        for line in (item for item in file if item.strip()):
            if ',' in line:
                updates.append([int(update.strip()) for update in line.split(',')])
            else:
                page_ordering_rules.append([int(rule.strip()) for rule in line.split('|')])

    return page_ordering_rules, updates

def do_ordering_rules_exist(page_to_validate, subsequent_pages_as_list, page_ordering_rules_lists):
    for subsequent_page in subsequent_pages_as_list:
        if [page_to_validate, subsequent_page] not in page_ordering_rules_lists:
            return False
    
    return True

def is_valid_update(update_as_list, page_ordering_rules_lists):
    for update_count in range(0, len(update_as_list) - 1):
        subsequent_pages = [subsequent_page for subsequent_page in update_as_list[update_count+1:]]
        if not do_ordering_rules_exist(update_as_list[update_count], subsequent_pages, page_ordering_rules_lists):
            return False
    
    return True

def get_valid_and_invalid_updates_lists(updates_lists, page_ordering_rules_lists):
    valid_updates = []
    invalid_updates = []
    for updates_list in updates_lists:
        if is_valid_update(updates_list, page_ordering_rules_lists):
            valid_updates.append(updates_list)
        else:
            invalid_updates.append(updates_list)
    return valid_updates, invalid_updates

def get_middle_page(update_as_list):
    if not (len(update_as_list) % 2):
        raise Exception("Not even")
    
    return update_as_list[math.ceil(len(update_as_list) / 2) - 1]

def get_value_of_middle_pages(valid_updates_as_lists):
    value_of_middle_pages = 0
    for valid_update_as_list in valid_updates_as_lists:
        value_of_middle_pages += get_middle_page(valid_update_as_list)
    
    return value_of_middle_pages

def fix_invalid_update(update_as_list, page_ordering_rules_lists):
    fixed_update = update_as_list.copy()
    for update_number in update_as_list:
        other_numbers = update_as_list.copy()
        other_numbers.remove(update_number)
        page_ordering_exists_count = 0
        for other_number in other_numbers:
            if [update_number, other_number] in page_ordering_rules_lists:
                page_ordering_exists_count += 1

        fixed_update[(len(fixed_update) - page_ordering_exists_count)-1] = update_number

    return fixed_update

def fix_invalid_updates(invalid_updates_as_lists, page_ordering_rules_lists):
    fixed_updates = []
    for invalid_update_as_list in invalid_updates_as_lists:
        fixed_updates.append(fix_invalid_update(invalid_update_as_list, page_ordering_rules_lists))
    
    return fixed_updates

input = read_input('Day 5/input.txt')
valid_updates = get_valid_and_invalid_updates_lists(input[1], input[0])
valid_updates_middle_number_total = get_value_of_middle_pages(valid_updates[0])
print('Day 5 total middle page numbers from valid updates is: ' + str(valid_updates_middle_number_total))

fixed_updates = fix_invalid_updates(valid_updates[1], input[0])
fixed_updates_middle_number_total = get_value_of_middle_pages(fixed_updates)
print('Day 5 total middle page numbers from fixed updates is: ' + str(fixed_updates_middle_number_total))
