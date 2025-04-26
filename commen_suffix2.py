def commen_suffix(*args):
    """
    Find the longest common suffix among multiple strings.
    
    This function takes multiple strings as input and returns the longest
    suffix that is common to all of them. If no common suffix exists,
    it prints a message and returns an empty string.
    
    Args:
        *args: Variable number of strings to compare
        
    Returns:
        str: The longest common suffix found, or empty string if none exists
        
    Note:
        The function prints "No Commen Suffix" if no common suffix is found
    """
    
    suffix = args[0]

    for words in args[1:]:
        while not words.endswith(suffix):
            suffix = suffix[1:]
        if suffix == "":
            print("No Commen Suffix")

    return suffix



    
