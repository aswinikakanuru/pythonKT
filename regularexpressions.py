#Regular Expressions
#A Regular Expression (Regex) is a pattern used to search, match, validate, extract, split, or replace text.
#Python lo Regex kosam "re" module use chestham.
'''
re.search()
re.match()
re.fullmatch()
re.findall()
re.finditer()
re.sub()
re.split()

'''
#1.re.search() -> search() searches the entire string and returns the first match.
import re
text="I am Learning Python"
result=re.search(r"Python",text)
print(result.group())

#2.re.match() -> match() checks whether the pattern matches from the beginning of the string.
import re
text="Java programming"
res=re.match(r"Java",text)
print(res.group())

#3.re.match()
text = "I love Python"
result = re.match(r"Python", text)
print(result)

#4.re.fullmatch() -> fullmatch() requires the entire string to match the pattern
text="12abc"
result=re.fullmatch(r"12abc",text)
print(result.group())

#5.re.findall() -> findall() returns all matching values as a list.
import re
text="I have 10 Apples and 20 Oranges"
numbers=re.findall(r"\d+",text)
print(numbers)

#6.re.finditer() -> finditer() returns an iterator of Match objects.
import re
text = "I have 10 apples and 20 oranges"
matches = re.finditer(r"\d+", text)
for match in matches:
    print(match.group())

'''
\d — Digit
Matches digits:

\D — Not a digit

\w — Word character

\W — Not a word character Opposite of \w.
\s — Whitespace Matches spaces, tabs, and line breaks.
\S — Non-whitespace ,Opposite of \s.
Dot . -> . means almost any single character except newline by default.
'''

