# a function that takes a string argument
# and return the number of vowels in it.
def vowel_count (string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
        return count


def test_with_my_first_name():
    assert vowel_count ('moti') == 0


def test_with_my_last_name():
    assert vowel_count ('ardelean') == 1
