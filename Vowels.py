"""
✅ Challenge 1/100: Vowel Counter 
🎯 Goal:
Build a function that:

Takes a sentence as input

Returns:

Total number of vowels

A dictionary with the count of each vowel

A list of all vowels found in order
"""

def vowel_counter(str1:str)-> int:
    if not str1:
        return -1
    vowel_dict = {

    }
    vowel_list = []
    vowels = "aeiou"
    for words in str1:
        if words.lower() in vowels:
            vowel_list.append(words.lower())
            
            if words.lower() in vowel_dict:
                vowel_dict[words.lower()] +=1
            else:
                vowel_dict[words.lower()] = 1
    print(f"Total Vowels : {len(vowel_list)}\n")
    print(f"Vowels Found {vowel_list}\n")
    print(f"Vowels Count {vowel_dict}\n")

    return len(vowel_list)

vowel_counter("Tarek Fouad Abdallah")

