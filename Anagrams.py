def isAnagrams(*args:str):
    """
    Check if all given strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    
    Args:
        *args (str): Variable number of strings to check for anagram property
        
    Returns:
        None: The function prints whether the strings are anagrams or not
        
    Raises:
        TypeError: If no arguments are provided
    """
    if not args:
        raise TypeError("Not String")
    
    fst_arg = args[0]
    for word in args[1:]:
        if sorted(fst_arg.lower()) != sorted(word.lower()):
            print("Not Anagrams")
            return
    print("Yup they are Anagrams!")


isAnagrams("Tarek","KTarre")
    