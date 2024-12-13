import csv

def read_inputs(file_name):
    input_list_1 = [];
    input_list_2 = [];
    with open(file_name, newline='') as file:
        file_reader = csv.DictReader(file, fieldnames=['id_1','id_2'])
        for row in file_reader:
            input_list_1.append(int(row['id_1']))
            input_list_2.append(int(row['id_2']))
    
    input_list_1.sort()
    input_list_2.sort()
    return input_list_1, input_list_2

def get_difference(input_list_1, input_list_2):
    total_difference = 0;
    for location_count in range(len(input_list_1)):
        location_diff = abs(input_list_2[location_count]-input_list_1[location_count])
        total_difference += location_diff
    
    return total_difference

def get_similarity(input_list_1, input_list_2):
    total_similarity = 0;
    for check_int in input_list_1:
        check_int_count = input_list_2.count(check_int)
        total_similarity += (check_int * check_int_count)
    
    return total_similarity

if __name__ == '__main__':
    lists = read_inputs('Day 1/input.csv')
    diff = get_difference(lists[0], lists[1])
    similarity = get_similarity(lists[0], lists[1])

    print ('Day 1 difference is: ' + str(diff))
    print ('Day 1 similarity is: ' + str(similarity))
