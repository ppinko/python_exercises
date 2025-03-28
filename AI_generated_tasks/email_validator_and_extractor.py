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


def main(file_path: list[str]) -> None:
    """
    This function reads text files containing random text and emails.
    Extracts all valid email addresses using regular expressions.

    @param file_path: list[str] - A list of file paths
    @return None - It saves the valid emails to valid_emails.txt and prints the
    number of unique valid emails found.
    """

    # Regular expression for email validation
    email_regex = (
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Z|a-z]{2,}\b"
    )

    # Regular expression for invalid emails
    invalid_emails_regex = r"[\w\.-]+@[\w\.-]+"

    valid_emails = []
    invalid_emails = []

    for file in file_path:
        try:
            with open(file, "r") as f:
                text = f.read()

                # Extract all emails from the text
                valid_emails.extend(re.findall(email_regex, text))
                invalid_emails.extend(re.findall(invalid_emails_regex, text))

        except FileNotFoundError:
            print(f"File {file} not found. ❌")
            sys.exit(1)

    # Lowercase all emails
    valid_emails = [email.lower() for email in valid_emails]
    invalid_emails = [email.lower() for email in invalid_emails]

    # Remove duplicates
    valid_emails = list(set(valid_emails))
    invalid_emails = list(set(invalid_emails))

    # Remove invalid emails from valid emails
    invalid_emails = [email for email in invalid_emails if email not in valid_emails]

    # Sort the emails alphabetically
    valid_emails.sort(reverse=False)
    invalid_emails.sort(reverse=False)

    # Save the valid emails to valid_emails.txt
    with open("valid_emails.txt", "w") as file:
        file.write("Valid Emails Found:\n")
        for i, email in enumerate(iterable=valid_emails, start=1):
            file.write(f"{i}. {email}\n")

    # Print the number of unique valid emails found
    print(f"Found {len(valid_emails)} unique valid emails. ✅")

    # Save the invalid emails to invalid_emails.txt
    with open("invalid_emails.txt", "w") as file:
        file.write("Invalid Emails Found:\n")
        for i, email in enumerate(iterable=invalid_emails, start=1):
            file.write(f"{i}. {email}\n")

    # Print the number of unique invalid emails found
    print(f"Found {len(invalid_emails)} unique invalid emails. ❌")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print("Usage: python email_validator_and_extractor.py <file_path>")
        sys.exit(1)
