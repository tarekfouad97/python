"""
🎯 Goal:
Build a function that:

Takes a sentence as input

Returns:

Total number of consonants

A dictionary with how many of each consonant occurred

A sorted list of consonants found in order

"""

def consonant_counter(str1:str)-> int:
    if not str1:
        return False
    cons_dict = {}
    cons_list = []
    consonants = "bcdfghjklmnpqrstvwxyz"

    for words in str1:
        if words.lower() in consonants:
            cons_list.append(words.lower())

            if words.lower() in cons_dict:
                cons_dict[words.lower()] +=1
            else:
                cons_dict[words.lower()] = 1

    print(f'Total Consonant : {len(cons_list)}')
    print(f'Consonants Found {cons_list}')
    print(f"Consonents Count {cons_dict}")
    return len(cons_list)


consonant_counter("Tarek Fouad Abdallah")