def longest_word(str1:str):
    list1 = str1.split()
    word = list1[0]
    length= len(list1[0])

    for words in list1[1:]:
        clean_word = "".join(char for char in words if char.isalpha())
            
        if len(clean_word) > length:
            length = len(clean_word)
            word = clean_word

    print(f" Longest word is {word} and length is {length}")


longest_word("hsh hhahha hhshdhshsdh ahshdhshdhsdhsahd ,,,,,,,,,,,,,,,,,,,,, as ahshh")
