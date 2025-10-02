import pyperclip as ppc
import re

# Create phone numbers regex
phone_re = re.compile(r'''(
	(\d{3}|\(\d{3}\))? # Area code
	(\s|-|\.)? # Separator
	(\d{3}) # First three digits
	(\s|-|\.) # Separator
	(\d{4}) # Last four digits
	(\s*(ext|x|ext\.)\s*(\d{2,5}))? # Extention
	)''', re.VERBOSE)
	
	
# Create email regex

email_re = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ # Username
	@ # @ symbol
	[a-zA-Z0-9.-]+ # Domain name
	(\.[a-zA-Z]{2,4}) # Dot something
)''', re.VERBOSE)	
	
	
mail = '''Subject: Contact Information for Upcoming Event
To: recipient1@example.com, recipient2@example.com, recipient3@example.com
Cc: cc1@example.com, cc2@example.com 
Bcc: bcc1@example.com 
Dear Team,
I hope this email finds you well. Below is the contact information for our key partners and vendors for the upcoming conference. Please ensure you have these numbers saved for easy communication:
John SmithEvent Coordinator 555-123-4567Emily JohnsonCatering Manager 555-987-6543 Michael BrownAV Technician (555) 456-7890 Sarah DavisVenue Contact (555) 234-5678
Please reach out to the appropriate contact if you have any questions or need assistance. Let me know if you need further details.
Best regards,
[Your Name]
[Your Position]
[Your Contact Information]'''

clipboardContent = str(ppc.paste())

print(f'[LOG] The initial paperclip content is: {clipboardContent}')

result = []

for detected in phone_re.findall(clipboardContent):
	phone_num = '-'.join([detected[1], detected[3], detected[5]])
	if detected[6] != '':
		phone_num += ' x' + detected[6]
	result.append(phone_num)
	
for detected in email_re.findall(clipboardContent):
	email = ''.join([detected[0],detected[1]])
	result.append(email)

if len(result) > 0:
	ppc.copy('\n'.join(result))
	print('Copied to clipboard:')	
	print('\n'.join(result))
else:
	print('No phone numbers or emails adresses found')
	





