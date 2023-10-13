import json
import xml.etree.ElementTree as ET

# Load JSON data from email.json
with open('email.json', 'r') as json_file:
    emails_dict = json.load(json_file)

# Create the root <emails> element
root = ET.Element("emails")

# Iterate through the emails in the JSON
for email_data in emails_dict['emails']:
    email_element = ET.SubElement(root, "email")
    
    # Add email attributes
    title = ET.SubElement(email_element, "title")
    title.text = email_data['title']
    
    # Add sender information
    sender = ET.SubElement(email_element, "sender")
    sender_name = ET.SubElement(sender, "name")
    sender_name.text = email_data['sender']['name']
    sender_email = ET.SubElement(sender, "email")
    sender_email.text = email_data['sender']['email']
    
    # Add receivers
    receivers = ET.SubElement(email_element, "receivers")
    for receiver_data in email_data['receivers']:
        receiver = ET.SubElement(receivers, "receiver")
        receiver_name = ET.SubElement(receiver, "name")
        receiver_name.text = receiver_data['name']
        receiver_email = ET.SubElement(receiver, "email")
        receiver_email.text = receiver_data['email']
    
    # Add cc recipients
    cc = ET.SubElement(email_element, "cc")
    for cc_data in email_data['cc']:
        recipient = ET.SubElement(cc, "recipient")
        recipient_name = ET.SubElement(recipient, "name")
        recipient_name.text = cc_data['name']
        recipient_email = ET.SubElement(recipient, "email")
        recipient_email.text = cc_data['email']
    
    # Add bcc recipients
    bcc = ET.SubElement(email_element, "bcc")
    for bcc_data in email_data['bcc']:
        recipient = ET.SubElement(bcc, "recipient")
        recipient_name = ET.SubElement(recipient, "name")
        recipient_name.text = bcc_data['name']
        recipient_email = ET.SubElement(recipient, "email")
        recipient_email.text = bcc_data['email']
    
    # Add daytime and content
    daytime = ET.SubElement(email_element, "daytime")
    daytime.text = email_data['daytime']
    
    content = ET.SubElement(email_element, "content")
    content.text = email_data['content']

    # Add links
    links = ET.SubElement(email_element, "links")
    for link_data in email_data['links']:
        link = ET.SubElement(links, "link")
        link.text = link_data
    
    # Add files
    files = ET.SubElement(email_element, "files")
    for file_data in email_data['files']:
        file = ET.SubElement(files, "file")
        file.text = file_data

# Create an ElementTree object and save to emailfinal.xml
email_tree = ET.ElementTree(root)
email_tree.write('emailfinal.xml', encoding="UTF-8")

print("Conversion from JSON to XML completed. Saved as emailfinal.xml.")
