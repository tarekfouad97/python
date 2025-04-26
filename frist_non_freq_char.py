def most_freq(str1:str):
    if not str1:
        raise TypeError
    chars_list=[]
    chars_dict={}

    for char in str1:
        if char.lower() ==  " " or char.isalpha() != True:
            continue
        else:
            chars_list.append(char.lower())

            if char.lower() in chars_dict:
                chars_dict[char.lower()]+=1
            else:
                chars_dict[char.lower()]=1
    last_value=0
    last_key=""
    for key , value in chars_dict.items():
        if value == 1:
            last_key = key
            last_value =value
            break
    print(f"{last_key} index {chars_list.index(last_key)} ")
    print(f"{chars_dict}")
        
most_freq("Tarek Fouad Abdallah")