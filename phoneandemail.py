#! python3

import re, pyperclip

# Create a regex for phone number
phoneregex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?       # area code(optional)
(\s|-)?     # first seperator
\d\d\d   # first 3 digits
-        # seperator
\d\d\d\d        # last 4 digits
(((ext(\.)?\s)|x)        # extension (optional)
(\d{2,5}))?
)
''',re.VERBOSE)

#Create a regex fro email addresses

emailregex = re.compile(r'''
#some.+_thing@something.com
[a-zA-Z0-9_.+]+        # name part
@        # @ symbol
[a-zA-Z0-9_.+]+        # domain name part


''',re.VERBOSE)
#Get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from the text
extractedphone = phoneregex.findall(text)
extractedemail = emailregex.findall(text)

allphonenumbers = []
for i in extractedphone:
    allphonenumbers.append(i[0])
results = '\n'.join(allphonenumbers) + '\n' +'\n' + '\n'.join(extractedemail)

#Copy the extracted email/phone to the clipboard
pyperclip.copy(results)
