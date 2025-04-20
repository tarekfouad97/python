def commen_suffix(*args):
    
    
    suffix = args[0]

    for words in args[1:]:
        while not words.endswith(suffix):
            suffix = suffix[1:]
        if suffix == "":
            print("No Commen Suffix")

    return suffix



    
