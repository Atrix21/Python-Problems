# 9. Given a string text, you want to use the characters of text to form as many instances of the
# word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that
# can be formed.
# Input: text = "nlaebolko" Output: 1
# Input: text = "loonbalxballpoon" Output: 2
# Input: text = "leetcode" Output: 0

d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
n = input()
for i in n:
    if i in d:
        d[i] += 1
d['l'] = d['l'] // 2
d['o'] = d['o'] // 2
print(min(d.values()))
