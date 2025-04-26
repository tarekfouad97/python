def common_suffix(strings):
    """
    Find the longest common suffix among multiple strings.
    
    This function takes a list of strings and returns the longest suffix
    that is common to all of them. If no common suffix exists, it returns
    an empty string.
    
    Args:
        strings (list): List of strings to compare
        
    Returns:
        str: The longest common suffix found, or empty string if none exists
    """
    if not strings:
        return ""

    # Start with the full first string as candidate suffix
    suffix = strings[0]
    
    for word in strings[1:]:
        # Compare characters from the end
        while not word.endswith(suffix):
            suffix = suffix[1:]  # Trim from the start
            if not suffix:
                return ""
    return str(suffix)

print(common_suffix(["exmed", "slahmed","ttstmed","kaled"]))