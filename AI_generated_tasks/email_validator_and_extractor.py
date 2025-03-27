"""
Email Validator & Extractor
Write a Python program that:
    1. Reads a text file containing random text and emails.
    2. Extracts all valid email addresses using regular expressions.
    3. Validates whether the emails follow the correct format (e.g.,
    example@domain.com).
    4. Saves the valid emails to valid_emails.txt.
    5. Prints the number of unique valid emails found.

Example Input (emails.txt)
Hello John, please contact me at john.doe@example.com.
Support team: support@company.org
Invalid emails: test@.com, @missinguser.com, noatsign.com
Reach out at: info@website.net or sales@business.io

Example Output (valid_emails.txt)
Valid Emails Found:
1. john.doe@example.com
2. support@company.org
3. info@website.net
4. sales@business.io

Console Output:
Found 4 unique valid emails. ✅

Constraints:
✅ Use regular expressions (re module) for email validation.
✅ Handle case insensitivity and remove duplicates.
✅ Allow the file path to be passed as a command-line argument.

Bonus Challenge:
⭐ Sort emails alphabetically before saving.
⭐ Support multiple file inputs at once.
⭐ Count and display email domains (e.g., example.com: 1 email).
"""

import re
import sys


def main(file_path: str) -> None:
    with open(file_path, "r") as file:
        text = file.read()

    # Regular expression for email validation
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    # Extract all emails from the text
    valid_emails = re.findall(email_regex, text)

    # Lowercase all emails
    valid_emails = [email.lower() for email in valid_emails]

    # Remove duplicates
    valid_emails = list(set(valid_emails))

    # Sort the emails alphabetically
    valid_emails.sort(reverse=False)

    # Save the valid emails to valid_emails.txt
    with open("valid_emails.txt", "w") as file:
        file.write("Valid Emails Found:\n")
        for i, email in enumerate(iterable=valid_emails, start=1):
            file.write(f"{i}. {email}\n")

    # Print the number of unique valid emails found
    print(f"Found {len(valid_emails)} unique valid emails. ✅")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python email_validator_and_extractor.py <file_path>")
        sys.exit(1)
