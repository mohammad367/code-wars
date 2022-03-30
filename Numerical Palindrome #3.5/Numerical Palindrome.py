def palindrome(num):
    if not type(num)==int or num<0:
        return "Not valid"
    string=str(num)
    answer_list=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            if is_Palindrome(string[i:j]):
                if (not int(string[i:j]) in answer_list) and len(string[i:j])>1 and int(string[i]):
                    answer_list.append(int(string[i:j]))
    answer_list=sorted(answer_list)
    if len(answer_list):
        return answer_list
    return "No palindromes found"

def is_Palindrome(num):
    string=str(num)
    if string==string[::-1]:
        return True
    return False