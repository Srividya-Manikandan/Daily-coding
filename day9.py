"""A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

Example

The string contains all letters in the English alphabet, so return pangram.

Function Description

Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

pangrams has the following parameter(s):

string s: a string to test
Returns

string: either pangram or not pangram"""

def pangrams(s):
    final_list=[0]*26
    for i in s:
        if i.isalpha():
            i=i.lower()
            final_list[ord(i)-97]+=1
    if all(final_list):
        return "pangram"
    else:
        return "not pangram"
    

if __name__ == '__main__':
    s = "The quick brown fox jumps over the lazy dog"
    result = pangrams(s)
    print(result)