import xml.etree.ElementTree as ET

tree = ET.parse("email.xml")
root = tree.getroot()

for email in root:
    print()
    print('-----EMAIL-----')
    print()
    
    sender = email.find('sender')
    sender_name = sender.find('name').text
    sender_email = sender.find('email').text
    print('Sender Name:', sender_name)
    print('Sender Email:', sender_email)

    title = email.find('title').text
    content = email.find('content').text
    daytime = email.find('daytime').text
    print('Title:', title)
    print('Content:', content)
    print()

    print('-----Receivers:')
    for receiver in email.find('receivers'):
        receiver_name = receiver.find('name').text
        receiver_email = receiver.find('email').text
        print('Receiver Name:', receiver_name)
        print('Receiver Email:', receiver_email)
        print()

    print('-----CC:')
    for recipient in email.find('cc'):
        recipient_name = recipient.find('name').text
        recipient_email = recipient.find('email').text
        print('CC Name:', recipient_name)
        print('CC Email:', recipient_email)
        print()


    print('-----BCC:')
    for recipient in email.find('bcc'):
        recipient_name = recipient.find('name').text
        recipient_email = recipient.find('email').text
        print('BCC Name:', recipient_name)
        print('BCC Email:', recipient_email)
        print()

    print('Attachments: ')

    for idx, file in enumerate(email.find('files')):
        print(f'File {idx+1}:', file.text)

    for idx, link in enumerate(email.find('links')):
        print(f'Link {idx+1}:', link.text)