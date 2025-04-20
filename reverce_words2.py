def reverse(str1:str):
    reverse_list = 0
    reverse_list = str1.split()
    for i in range (len(reverse_list)):
        
        reverse_list[i] = reverse_list[i][::-1]
        
    print(' '.join(reverse_list[::-1]))


reverse("I love you")