def most_frequent(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    # Find the element with the highest frequency
    max_count = 0
    most_common = None
    for key, value in freq.items():
        if value > max_count:
            max_count = value
            most_common = key

    return most_common

# Example usage
my_list = [1, 2, 302, 3, 4, 2, 5, 3, 3]
print("The most frequent element is:", most_frequent(my_list))
