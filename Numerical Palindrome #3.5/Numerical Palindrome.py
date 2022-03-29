
def polindrome3(dict_of_digits):
    for key in dict_of_digits:
        if dict_of_digits[key]==1:
            
            two_digit_polindromes=polindrome2(dict_of_digits,[0,key])
            for two_digit_polindrome_string in two_digit_polindromes:
                
                print("{}{}{}".format(two_digit_polindrome_string[0],key,two_digit_polindrome_string[1]))
            
      
def polindrome2(dict_of_digits,forbidden_keys=[]):
    print("forbidden keys are: {}".format(forbidden_keys))
    two_digit_polindromes=[]
    for key in dict_of_digits:
        if dict_of_digits[key]>=2 and (dict_of_digits[key] not in forbidden_keys):
            two_digit_polindromes.append("{}{}".format(key,key))
    #returns a list of two digit polindromes
    return two_digit_polindromes


def palindrome(num):
    list_of_digits=str(num) 
    solution_list=[]
    dict_of_digits={}
    
    for i in range(0,10):
        count=list_of_digits.count(str(i)) 
        if count:
            dict_of_digits[i]=count
    print(dict_of_digits)
    print("size of num: "+str(len(str(num))))
    for i in range(2,len(str(num))+1):
        if i ==2:
            two_digit_polindromes=polindrome2(dict_of_digits,[0])
            solution_list+=two_digit_polindromes
            print(two_digit_polindromes)

        if i==3:
            polindrome3(dict_of_digits)
palindrome(2225700)