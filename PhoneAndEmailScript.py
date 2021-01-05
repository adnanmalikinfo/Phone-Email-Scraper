#! python3

#UNDER DEVELOPMENT

#A script to retrieve all of phon numbers and email from a site or file

import re
import pyperclip

#Create a regex of phone Number

phoneRegex = re.compile(r'''
 (
 (0|\+92) ?            #Country Code
 (\d\d\d | \d\d\d-)            #Network Code
 \d\d\d\d\d\d\d 
 )   #Contact Number
 ''', re.VERBOSE)

#Create Regex for Email addresses

emailRegex = re.compile(r'''
 [a-zA-Z0-9_.+] +   #namepart
 @                  #@ symbol
 [a-zA-Z0-9_.+] +    #domain name part

 ''',  re.VERBOSE)
 
result = pyperclip.paste()
extractedPhoneNumbers = phoneRegex.findall(result)
extractedEmails = emailRegex.findall(result)

print(extractedPhoneNumbers)
print(extractedEmails)






