def palindrome(num):
    if (not type(num)==int) or num<0:
        return "Not valid"
    if is_Palindrome(num):
        return num
    i=0
    while(1):
        if is_Palindrome(num+i):
            return num+i
        if is_Palindrome(num-i):
            return num-i
        i+=1
            
def is_Palindrome(num):
    string=str(num)
    if string==string[::-1] and num>9:
        return True
    return False