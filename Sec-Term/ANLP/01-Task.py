import re

txt = '''Hi I am Mahmoud Abas a CS student at my 4th grade in FCIS MU.
Here is my fake contact information..
Email : example@example.com, obviously its an example email not a real one :-)
Other emails for testing :
- example+ex@example.com
- example-ex@example.com
- example%ex@example.com
- example%%ex@example.com
- example+ex@example.com.eg
- example-ex@example.ex.com
Also i have some examples of phone numbers for testing my regex here they are..
01234567890, 01134567890, 01034567890 and finally 01534567890.
Don't call me I am not replying! but you can give me a bonus because i like bonuses <3
If your phone number is listed above you have a special phone number (Hamada Helal style :-P)
Are you still reading this ! so bonus++ OH NOOO! it's a syntax error,
Just use bonus+=1 it will solve the problem.
But since 1 is a very small value you can use bonus+=9 instead!
Just tell me why are you still reading!
I am talking nonsense here and you will be late.
'''

print("----- ----- ----- -----\n"
      "Hi i've written a script to search for emails & phone numbers in a given text"
      "\nDon't read what is in txt variable its a waste of time."
      "\nNow look what i found!\n"
      "----- ----- ----- -----\n")

emails_r = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails_matches = re.findall(emails_r, txt)
print(f'I\'ve found these emails : {emails_matches}')

phone_num_r = r'\b01[0125][0-9]{8}\b'
phone_num_matches = re.findall(phone_num_r, txt)
print(f'I\'ve found these phone numbers : {phone_num_matches}')
