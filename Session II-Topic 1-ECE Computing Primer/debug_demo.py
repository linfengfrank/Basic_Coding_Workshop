def calculate_average(data):
    total = 0
    count = len(data)
    for num in data:
        total += num
    average = total // count
    return average

def bubble_sort(data):
    count = len(data)
    for i in range(count):
        for j in range(count-i):
            if data[j+1] < data[j]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    return data

def calculate_median(data):
    data = bubble_sort(data)
    count = len(data)
    return data[count/2]

test_case_1 = [10, 20, 30, 40, 50]
test_case_2 = []
test_case_3 = [1, 2, 2, 2, 3]
test_case_4 = [3, 5, 1, 6, 4]


ans = calculate_average(test_case_1)
print(f"The average of {test_case_1} is {ans}")
print(f"{test_case_4} sorted is {bubble_sort(test_case_4)}")
print(f"Median of {test_case_1} is {calculate_median(test_case_1)}")
