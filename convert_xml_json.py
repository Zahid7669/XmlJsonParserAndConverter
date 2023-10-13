import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('email.xml')
root = tree.getroot()

# Initialize an empty list to store email data
emails_data = []

# Iterate through <email> elements
for email_element in root.findall('email'):
    email_data = {}
    
    # Extract email attributes
    email_data['title'] = email_element.find('title').text
    email_data['daytime'] = email_element.find('daytime').text
    email_data['content'] = email_element.find('content').text
    
    # Extract sender information
    sender_element = email_element.find('sender')
    email_data['sender'] = {
        'name': sender_element.find('name').text,
        'email': sender_element.find('email').text
    }
    
    # Extract receivers
    receivers_element = email_element.find('receivers')
    email_data['receivers'] = []
    for receiver_element in receivers_element.findall('receiver'):
        receiver = {
            'name': receiver_element.find('name').text,
            'email': receiver_element.find('email').text
        }
        email_data['receivers'].append(receiver)
    
    # Extract cc recipients
    cc_element = email_element.find('cc')
    email_data['cc'] = []
    for recipient_element in cc_element.findall('recipient'):
        recipient = {
            'name': recipient_element.find('name').text,
            'email': recipient_element.find('email').text
        }
        email_data['cc'].append(recipient)
    
    # Extract bcc recipients
    bcc_element = email_element.find('bcc')
    email_data['bcc'] = []
    for recipient_element in bcc_element.findall('recipient'):
        recipient = {
            'name': recipient_element.find('name').text,
            'email': recipient_element.find('email').text
        }
        email_data['bcc'].append(recipient)
    
    # Extract links
    links_element = email_element.find('links')
    email_data['links'] = [link.text for link in links_element.findall('link')]
    
    # Extract files
    files_element = email_element.find('files')
    email_data['files'] = [file.text for file in files_element.findall('file')]
    
    # Append email data to the list
    emails_data.append(email_data)

# Create a dictionary for the emails
emails_dict = {'emails': emails_data}

# Convert to JSON and save to email.json
with open('email.json', 'w') as json_file:
    json.dump(emails_dict, json_file, indent=4)
