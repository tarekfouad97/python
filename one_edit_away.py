def OneEditAway(str1:str, str2:str):
    """
    Check if two strings are one edit away from each other.
    
    An edit is defined as:
    - Inserting a character
    - Removing a character
    - Replacing a character
    
    Args:
        str1 (str): First string to compare
        str2 (str): Second string to compare
        
    Returns:
        None: The function prints whether the strings are one edit away or not
        
    Raises:
        TypeError: If either input string is empty or None
    """
    if not str1 or not str2:
        raise TypeError("Error Type")
    
    sort_dict = {}
    sort_dict2 = {}

    for i in str1:
        if i.lower() not in sort_dict:
            sort_dict[i.lower()]+=1
        else:
            sort_dict[i.lower()]=1
    for i in str2:
        if i.lower() not in sort_dict2:
            sort_dict2[i.lower()]+=1
        else:
            sort_dict2[i.lower()]=1

    
    if len(sort_dict) == len(sort_dict2):

        if sort_dict == sort_dict2:
            print("Both strings are equal")
        
    elif len(sort_dict) < len(sort_dict2):
        pass
    elif len(sort_dict) > len(sort_dict2):

        pass
