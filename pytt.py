
def common_suffix(strings):
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