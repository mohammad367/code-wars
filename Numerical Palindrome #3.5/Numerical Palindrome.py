def palindrome(num):
    list_of_digits=str(num) 
    dict_of_digits={}
    for i in range(0,10):
        print(i) 
        dict_of_digits[i]=list_of_digits.count(str(i))  
    print(dict_of_digits)
palindrome(627)