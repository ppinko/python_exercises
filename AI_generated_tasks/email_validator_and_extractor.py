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
