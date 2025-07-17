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
