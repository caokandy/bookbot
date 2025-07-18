def get_num_words(i):
        num_words = i.split()
        count = len(num_words)
        return count


def get_char_count(char_lower):
	dictionary = {}
	char_lower = char_lower.lower()
	for i in char_lower:
		if i in dictionary:
			dictionary[i] += 1
		else:
		    dictionary[i] = 1

	return dictionary


def sort_on(item):
    return item["num"]

def sorted_list(char_count):
    complete_list = []
    for char, count in char_count.items():
        char_dict = {"char": char, "num": count}
        complete_list.append(char_dict)
    complete_list.sort(reverse=True, key=sort_on)
    return complete_list



