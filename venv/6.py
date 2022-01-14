# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
#
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
#
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

s = "cookiesandcream"
dictionary = ["cookie", "cookies", "and", "sand", "cream"]
result = []
max_l = len(max(dictionary, key=len))
length = len(s) + 1
for j in range(1,length):
    i = j - 1
    flag = 0
    ans = []
    x = 0
    # Letting setting x to j - max_l optimization,
    # the code will work even if x is always set to 0
    if j > max_l:
        x = j - max_l
    while(i >= x):
        if s[i:j] in dictionary:
            if i > 0 and result[(i - 1)]:
                    # appending the word to all the valid sentences
                    # formed by the substring ending at i-1
                    temp = list((map(lambda x : x + " "+ s[i:j],\
                    result[(i - 1)])))
                    for elem in temp:
                        ans.append(elem)
                    flag = 2
            else:
                flag = 1
                result.append([s[i:j]])
        i=i-1
    # if the substring does not belong to the
    # dictionary append an empty list to result
    if flag == 0:
        result.append([])
    if flag == 2:
        result.append(ans)
if s in dictionary:
  result[len(s) - 1].append(s)
# Printing the result.
temp = ", result [{}]: "
for i in range(len(s)):
    print("s:", s[:(i+1)], temp.format(i), result[i])
# If result[len(s)-1] is empty then the string cannot be
# broken down into valid strings
print("Final answer for cookies and cream:", result[len(s) - 1])
