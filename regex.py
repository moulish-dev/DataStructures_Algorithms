#Regular Expressions
#to match character combinations in strings
import re
#supported by re model

#Metacharacters: Special characters with specific meanings like . ^ $ * + ? { } [ ] \ | ( )

pattern=f"hii"
text = "hii everyone"

match = re.search(pattern,text)
print("Match Found") if match else print("Match not found")
#search()
#match() only in beginning of string
#findall()
#sub() to replace the pattern
#split()
m = re.sub(pattern, "Hello", text )
print(m)
# Special Sequences:
special_text = "The speed of light is 3*10^8 m/s."
# \d: Matches any digit (0–9).
digit_pattern = r"\d+"
print(re.findall(digit_pattern,special_text))
# \D: Matches any non-digit character.
# \w: Matches any word character (letters, digits, and underscores).
# \W: Matches any non-word character.
# \s: Matches any whitespace (spaces, tabs, line breaks).
# \S: Matches any non-whitespace character.



# Flags in Regex:
# re.IGNORECASE (or re.I): Ignore case when matching.
# re.MULTILINE (or re.M): Makes ^ and $ match the start and end of each line.
# re.DOTALL (or re.S): Makes . match any character, including newlines.