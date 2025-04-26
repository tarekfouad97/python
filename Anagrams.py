def isAnagrams(*args:str):
    if not args:
        raise TypeError("Not String")
    
    fst_arg = args[0]
    for word in args[1:]:
        if sorted(fst_arg.lower()) != sorted(word.lower()):
            print("Not Anagrams")
            return
    print("Yup they are Anagrams!")


isAnagrams("Tarek","KTarre")
    