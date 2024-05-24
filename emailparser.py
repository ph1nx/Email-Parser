import os
import email

def extract_eml_contents(filepath):
    with open(filepath, 'r') as f:
        eml_data = f.read()
    eml = email.message_from_string(eml_data)
    return eml

def parse_eml(filepath):
    eml = extract_eml_contents(filepath)
    print("Subject:", eml['subject'])
    print("From:", eml['from'])
    print("To:", eml['to'])
    print("Date:", eml['date'])

    for part in eml.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print("Body:",body.decode())
        if part.get('Content-Disposition') is None:
            continue
        filename = part.get_filename()
        if bool(filename):
            attachment_path = os.path.join("/home/kali/Downloads/", filename)
            with open(attachment_path, 'wb') as f:
                f.write(part.get_payload(decode=True))

if __name__ == "__main__":
    filepath = "/home/kali/Downloads/file.eml"
    parse_eml(filepath)
