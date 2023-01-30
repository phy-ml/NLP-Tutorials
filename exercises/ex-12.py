# Q: Extract the usernames from the email addresses present in the text

text = "The new registrations are potter709@gmail.com , elixir101@gmail.com. If you find any disruptions, kindly contact granger111@gamil.com or severus77@gamil.com "

# use regex for extraction
import re

user_name = re.findall('(\S+)@', text)
print(user_name)