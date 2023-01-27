def letterCombinationsUtil(number, n, table):
 
    list = []
    q = deque()
    q.append("")
 
    while len(q) != 0:
        s = q.pop()

        if len(s) == n:
            list.append(s)
        else:

            for letter in table[number[len(s)]]:
                q.append(s + letter)
 

    return list
 
def letterCombinations(number, n):
 

    table = ["0", "1", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]
 
    list = letterCombinationsUtil(number, n, table)
 
    s = ""
    for word in list:
        s += word + " "
 
    print(s)
    return
 
 

number = [2, 3]
n = len(number)
 

letterCombinations(number, n)
