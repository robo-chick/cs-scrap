"""
GCA Practice
"""

"""
Mutate the array
----------------
Given an integer n and an array a of length n, your task is to apply the following mutation to a:

Array a mutates into a new array b of length n.
For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the resulting array after the mutation will be [4, 5, -1, 2, 1].
"""
a = [4, 0, 1, -2, 3]
n = 5


def mutateTheArray(n, a):
    if len(a) < 2:
        return a
    result = []
    for i in range(len(a)):
        if i == 0:
            result.append(a[i] + a[i + 1])
        elif i == len(a) - 1:
            result.append((a[i - 1] + a[i]))
        else:
            result.append(a[i - 1] + a[i] + a[i + 1])

    return result


# print(mutateTheArray(n, a))

"""
Alternating sort
You are given an array of integers a. A new array b is generated by rearranging the elements of a in the following way:

b[0] is equal to a[0];
b[1] is equal to the last element of a;
b[2] is equal to a[1];
b[3] is equal to the second-last element of a;
b[4] is equal to a[2];
b[5] is equal to the third-last element of a;
and so on.
Here is how this process works:



Your task is to determine whether the new array b is sorted in strictly ascending order or not.

Example

For a = [1, 3, 5, 6, 4, 2], the output should be alternatingSort(a) = true.

The new array b will look like [1, 2, 3, 4, 5, 6], which is in strictly ascending order, so the answer is true.

For a = [1, 4, 5, 6, 3], the output should be alternatingSort(a) = false.

The new array b will look like [1, 3, 4, 6, 5], which is not in strictly ascending order, so the answer is false.
"""
a = [1, 3, 5, 6, 4, 2]
a = [1, 4, 5, 6, 3]
a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]


def alternatingSort(a):
    if len(a) == 1:
        return True
    b = []
    first_i = 0
    last_i = len(a) - 1
    while not first_i > last_i:
        print('first', a[first_i])
        print('last', a[last_i])

        if a[first_i] == b[len(b) - 1] and first_i != last_i:
            print(b)

            return False
        if first_i == last_i:
            b.append(a[first_i])
            print(a[first_i])
            print(b[len(b) - 2])
            if (a[first_i]) < b[len(b) - 2]:
                print(b)

                return False
        else:
            b.append(a[first_i])
            b.append(a[last_i])
            if a[first_i] > a[last_i]:
                print(b)

                return False
        last_i -= 1
        first_i += 1

    print(b)
    return True


# print(alternatingSort(a))

"""
Tiny pairs
----------
You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

Example

For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
countTinyPairs(a, b, k) = 2.

We're considering the following pairs during iteration:

(1, 3). Their concatenation equals 13, which is less than 31, so the pair is tiny;
(2, 2). Their concatenation equals 22, which is less than 31, so the pair is tiny;
(3, 1). Their concatenation equals 31, which is not less than 31, so the pair is not tiny.
As you can see, there are 2 tiny pairs during the iteration, so the answer is 2.

For a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15], and k = 743, the output should be
countTinyPairs(a, b, k) = 4.

We're considering the following pairs during iteration:

(16, 15). Their concatenation equals 1615, which is greater than 743, so the pair is not tiny;
(1, 0). Their concatenation equals 10, which is less than 743, so the pair is tiny;
(4, 2). Their concatenation equals 42, which is less than 743, so the pair is tiny.
(2, 11). Their concatenation equals 211, which is less than 743, so the pair is tiny;
(14, 7). Their concatenation equals 147, which is less than 743, so the pair is tiny.
There are 4 tiny pairs during the iteration, so the answer is 4.
"""

a = [16, 1, 4, 2, 14]
b = [7, 11, 2, 0, 15]
k = 743


def countTinyPairs(a, b, k):
    pairs = 0
    b_index = len(b) - 1
    for i in range(len(a)):
        if int(str(a[i]) + str(b[b_index])) < k:
            pairs += 1
        b_index -= 1
    return pairs


# print(countTinyPairs(a, b, k))

"""
Merging Strings
---------------
You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".



You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual lexicographical way. If both number of occurences and characters are equal, you should take the characters from the first string to the result.

Given two strings s1 and s2, return the result of the special merge function you are implementing.

Example

For s1 = "dce" and s2 = "cccbd", the output should be
mergeStrings(s1, s2) = "dcecccbd".
All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.



For s1 = "super" and s2 = "tower", the output should be
mergeStrings(s1, s2) = "stouperwer".
Because in both strings all symbols occur only 1 time, strings are merged as usual. You can find explanation for this example on the image in the description.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length ≤ 104.

[input] string s2

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length ≤ 104.

[output] string

The string that results by merging s1 and s2 using your special merge function.
"""

s1 = "super"
s2 = "tower"

s1 = "dce"
s2 = "cccbd"

s1 = "kkihj"
s2 = "jbsmfoftph"
expected = "jbsmfoftphkkihj"

s1 = "ougtaleegvrabhugzyx"
s2 = "wvieaqgaegbxg"
output = "owvieaqugaegbxggtaleegvrabhugzyx"
expected = "owvieaqugtaleegvrabhugzyxgaegbxg"


def mergeStrings(s1, s2):
    result = ''
    long_i = 0
    i = 0
    long = ''
    short = ''
    if len(s1) > len(s2):
        long = s1
        short = s2
    else:
        long = s2
        short = s1
    short_map = {}
    long_map = {}
    for letter in short:
        if letter not in short_map:
            short_map[letter] = 0
        short_map[letter] += 1

    for letter in long:
        if letter not in long_map:
            long_map[letter] = 0
        long_map[letter] += 1

    while i < len(short) and long_i < len(long):
        print('i', i)
        print('long_i', long_i)
        # print(chr(max(ord(short[i]), ord(long[long_i]))))
        if short_map[short[i]] < long_map[long[long_i]]:
            result += short[i]
            i += 1
        elif short_map[short[i]] > long_map[long[long_i]]:
            result += long[long_i]
            long_i += 1
        else:
            result += chr(min(ord(short[i]), ord(long[long_i])))
            if ord(short[i]) > ord(long[long_i]):
                long_i += 1
            else:
                i += 1
    if i == len(short):
        result += long[long_i:]
    if long_i >= len(long):
        result += short[i:]
    return result


# print(mergeStrings(s1, s2))

"""
Concatenations Sum
------------------
Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

Example

For a = [10, 2], the output should be concatenationsSum(a) = 1344.

a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.
So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

For a = [8], the output should be concatenationsSum(a) = 88.

There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.

For a = [1, 2, 3], the output should be concatenationsSum(a) = 198.

a[0] ∘ a[0] = 1 ∘ 1 = 11,
a[0] ∘ a[1] = 1 ∘ 2 = 12,
a[0] ∘ a[2] = 1 ∘ 3 = 13,
a[1] ∘ a[0] = 2 ∘ 1 = 21,
a[1] ∘ a[1] = 2 ∘ 2 = 22,
a[1] ∘ a[2] = 2 ∘ 3 = 23,
a[2] ∘ a[0] = 3 ∘ 1 = 31,
a[2] ∘ a[1] = 3 ∘ 2 = 32,
a[2] ∘ a[2] = 3 ∘ 3 = 33.
The total result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198.
"""

a = [8]


def concatenationsSum(a):
    string_sum = ''
    result = 0
    # iterate the array
    for current_num in a:
        # concat it with each num in the array
        for concat_num in a:
            string_sum = str(current_num) + str(concat_num)
            result += int(string_sum)

    return result


# print(concatenationsSum(a))


"""
HashMap
You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.
To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.

Example

For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be hashMap(queryType, query) = 5.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 2, 2: 3}
3 query: {1: 4, 2: 5}
4 query: {2: 4, 3: 5}
5 query: answer is 5
The result of the last get query for 3 is 5 in the resulting hashmap.



For queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] and query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]], the output should be hashMap(queryType, query) = 6.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 4}
3 query: answer is 4
4 query: {1: 4, 2: 3}
5 query: {2: 4, 3: 3}
6 query: {2: 3, 3: 2}
7 query: answer is 2
The sum of the results for all the get queries is equal to 4 + 2 = 6.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string queryType

Array of query types. It is guaranteed that each queryType[i] is either "addToKey", "addToValue", "get", or "insert".

Guaranteed constraints:
1 ≤ queryType.length ≤ 105.

[input] array.array.integer query

Array of queries, where each query is represented either by two numbers for insert query or by one number for other queries. It is guaranteed that during all queries all keys and values are in the range [-109, 109].

Guaranteed constraints:
query.length = queryType.length,
1 ≤ query[i].length ≤ 2.

[output] integer64

The sum of the results for all get queries.
"""

queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue",
             "get"]
query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]]

queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
query = [[1, 2], [2, 3], [2], [1], [3]]

def hashMap(queryType, query):
    sum_of_gets = 0
    first_hash = {1: 1, 2: 1}
    addedHash = {}

    def insert(key, value):
        first_hash[key] = value

    def get(key):
        return first_hash[key]

    def addToKey(value):
        for key in first_hash:
            addedHash[key + value] = first_hash[key]

    def addToValue(value):
        for key in first_hash:
            first_hash[key] = first_hash[key] + value

    for i in range(len(queryType)):
        if queryType[i] == 'insert':
            insert(query[i][0], query[i][1])
        elif queryType[i] == 'get':
            sum_of_gets += get(query[i][0])

        elif queryType[i] == 'addToValue':
            addToValue(query[i][0])
        else:
            addToKey(query[i][0])
            first_hash = addedHash

    print(first_hash)
    return sum_of_gets


print(hashMap(queryType, query))
