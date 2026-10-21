def bubble_sort(items):
  """Sort left to right: the largest elements 'bubble' to the end."""
  n = len(items)                                          # O(1)  -> runs once
  for i in range(n - 1):                                  # O(n)  -> n-1 iterations
    swapped = False                                       # O(n)  -> 1 operation x (n-1) iterations
    for j in range(n - 1 - i):                            # O(n²) -> n(n-1)/2 iterations in total
      if items[j] > items[j + 1]:                         # O(n²) -> n(n-1)/2 comparisons
        items[j], items[j + 1] = items[j + 1], items[j]   # O(n²) -> worst case (reversed list)
        swapped = True                                    # O(n²) -> worst case (reversed list)
    if not swapped:  # no swaps means the list is already sorted   # O(n) -> 1 check x (n-1) iterations
      break                                               # O(1)  -> runs at most once
  return items                                            # O(1)  -> runs once

def print_numbers_times_2(numbers_list):
	for number in numbers_list:                           # O(n) -> n iterations
		print(number * 2)                                 # O(n) -> 1 operation x n iterations

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:                              # O(n)  -> n iterations
		for element_b in list_b:                          # O(n²) -> n x n iterations
			if element_a == element_b:                    # O(n²) -> n x n comparisons
				return True                               # O(1)  -> runs at most once
	return False                                          # O(1)  -> runs at most once

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)                         # O(1) -> runs once
	for index in range(min(list_len, 10)):                # O(1) -> at most 10 iterations (constant)
		print(list_to_print[index])                       # O(1) -> at most 10 times (constant)

def generate_list_trios(list_a, list_b, list_c):
	result_list = []                                                    # O(1)  -> runs once
	for element_a in list_a:                                            # O(n)  -> n iterations
		for element_b in list_b:                                        # O(n²) -> n x n iterations
			for element_c in list_c:                                    # O(n³) -> n x n x n iterations
				result_list.append(f'{element_a} {element_b} {element_c}')  # O(n³) -> 1 append per combination
	return result_list                                                  # O(1)  -> runs once