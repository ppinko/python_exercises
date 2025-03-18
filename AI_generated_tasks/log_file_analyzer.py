"""
Log File Analyzer

You have a server log file that records user activity. Your task is to analyze
the log file and extract useful information.

Log File Format (logs.txt)
Each line in the log file follows this format:
[Timestamp] - [User] - [Action]

Example:
2024-03-16 10:15:32 - Alice - LOGIN
2024-03-16 10:17:45 - Bob - LOGIN
2024-03-16 10:20:10 - Alice - VIEW_PAGE
2024-03-16 10:22:05 - Alice - LOGOUT
2024-03-16 10:25:30 - Bob - VIEW_PAGE
2024-03-16 10:30:15 - Bob - LOGOUT

Your Task:
- Read the log file (logs.txt).
- Count how many times each user logged in.
- Find the user who logged in the most times.
- Write the results to an output file (report.txt).

Expected Output (report.txt):
User Login Count:
Alice: 1
Bob: 1

Most Active User: Alice, Bob (1 logins each)

Constraints:
- Ignore case differences (alice and Alice are the same).
- Handle large log files efficiently (Hint: Use dictionaries).
- Solve in O(n) time complexity (one pass through the file
"""


def log_file_analyzer(input_file: str, output_file: str) -> None:
    """
    Analyze log file and extract useful information
    """

    user_login_count = {}
    most_active_users = []  # list of most active user(s)
    max_login_count = 0

    try:
        with open(input_file, "r") as file:
            for line in file:
                user = line.split(" - ")[1].strip().lower()
                user_login_count[user] = user_login_count.get(user, 0) + 1
                max_login_count = max(max_login_count, user_login_count[user])

        with open(output_file, "w") as file:
            file.write("User Login Count:\n")
            for user, count in user_login_count.items():
                file.write(f"{user.capitalize()}: {count}\n")
                if count == max_login_count:
                    most_active_users.append(user.capitalize())

            file.write(
                "\nMost Active User: "
                + ", ".join(most_active_users)
                + f" ({max_login_count} logins each)\n"
            )
    except FileNotFoundError:
        print(f"File {input_file} not found")


if __name__ == "__main__":
    import sys

    log_file_analyzer(sys.argv[1], sys.argv[2])
