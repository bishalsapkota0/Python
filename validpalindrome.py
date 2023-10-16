def isPalindrome(string):
    #s for start and e for end shortcut
    s, e = 0, len(string) - 1
    
    #lower cases
    string = string.lower() 
    
    while (s <= e): 
        # If there is symbol in left 
        if (not(string[s] >= 'a' and string[s] <= 'z')): 
            s += 1
    
        #If there is a symbol in right 
        elif (not(string[e] >= 'a' and string[e] <= 'z')): 
            e -= 1
    
        # If characters are equal then check one by one by updating s and decreasing e
        elif (string[s] == string[e]): 
            s += 1
            e -= 1
          
        # If characters are not equal then it is not palindorme 
        else: 
            return False
    return True

def main():
   string= str(input("Enter Your String"))
   if (isPalindrome(string)): 
    print ("The Provided String is palindrome.") 
   else: 
    print ("The Provided string is not a palindrome.")
main()
            
    
    
