def sort_anagrams(list_of_strings):
    """Splits a list of words into sub-lists, each contains anagrams of words from
    the original list.
    :param: list_of_strings: the given list of words
    :type: list of lists
    :return: list of anagram-lists
    :rtype: list of lists
    """
    result = []
    for string in list_of_strings:
        if set(string) in [set(s[0]) for s in result]:
            for s in result:
                if set(string) == set(s[0]):
                    s.append(string)
        else:
            result.append([string])
    return result