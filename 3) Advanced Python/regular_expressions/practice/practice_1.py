import re

text_to_search = """
Hi there,

You can reach out to John via email at john.doe@example.com or jane_doe123@workmail.org for business inquiries.
For more info, check out our website: https://www.example.com/about or our blog at http://blog.example.org.
If you prefer to call, contact us at +1-202-555-0183 or (415) 555-2671 during office hours. 
Our fax number is 202.555.0147.

Also, follow us on Twitter @example_handle and don't forget to use the hashtag #Example2025 when posting.

Best,
The Example Team
"""


# Find the URLs
url_pattern = re.compile(r'(https?)://([\w+.-]+)?\.(com|lk|net|org)(/[\w+]*)?')

for match in url_pattern.finditer(text_to_search):
    print(match)


# Find the Email Addresses
email_pattern = re.compile(r'([\w.]+)@([a-zA-Z]+)\.(com|net|org|lk)')

for email in email_pattern.finditer(text_to_search):
    print("Complete Email: ", email.group(0))
    print("Email Name: ", email.group(1))
    print("Email Secondary Domain: ", email.group(2))
    print("Email TLD: ", email.group(3))
    print("\n\n-----------\n\n")


# Find the Phone Numbers

