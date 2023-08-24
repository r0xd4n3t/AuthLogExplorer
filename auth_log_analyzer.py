import os
import random
import re
import argparse
from datetime import datetime

def read_auth_log(file_path):
    logs = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            match = re.search(r'^(\w+\s+\d+\s\d+:\d+:\d+).*?(sshd.*?)$', line)
            if match:
                timestamp = match.group(1)
                message = match.group(2)
                logs.append((timestamp, message))
    return logs

def extract_ip_addresses(logs, keyword):
    log_entries = []
    for log in logs:
        timestamp, message = log
        if keyword in message:
            ip_match = re.search(r'from\s+(\d+\.\d+\.\d+\.\d+)', message)
            user_match = re.search(r'(\S+)\s+from', message)
            if ip_match and user_match:
                ip_address = ip_match.group(1)
                user_id = user_match.group(1)
                log_entries.append("{} {} {}".format(ip_address, timestamp, user_id))
    return log_entries

def generate_random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_html_report(logs):
    total_entries = len(logs)
    successful_logins = len([log for log in logs if "Accepted" in log[1]])
    failed_logins = len([log for log in logs if "Failed" in log[1]])

    successful_entries = extract_ip_addresses(logs, "Accepted")
    failed_entries = extract_ip_addresses(logs, "Failed")

    # Generate a random background color for the #4CAF50 element
    th_background_color = generate_random_color()

    # Use the same random background color for the footer as for th_background_color
    footer_background_color = th_background_color

    table_rows = ""
    for log in logs:
        timestamp, message = log
        table_row = "<tr><td>{}</td><td>{}</td></tr>".format(timestamp, message)
        table_rows += table_row

    successful_entries_list = "\n".join("<li>{}</li>".format(entry) for entry in successful_entries)
    successful_entries_list = successful_entries_list if successful_entries else "None"

    failed_entries_list = "\n".join("<li>{}</li>".format(entry) for entry in failed_entries)
    failed_entries_list = failed_entries_list if failed_entries else "None"

    copyleft_footer = """
    <footer style="background-color: {};">
        <p>&copy; {} Let's Rock the Net! All rights reserved.</p>
    </footer>
    """.format(footer_background_color, datetime.now().year)

    html = """
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}

            h1 {{
                text-align: center;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
            }}

            th, td {{
                text-align: left;
                padding: 8px;
                border: 1px solid #ddd; /* Add border to th and td */
            }}

            th {{
                background-color: {};
                color: white;
            }}

            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}

            .report {{
                margin-top: 20px;
                background-color: #f9f9f9;
                padding: 10px;
                border: 1px solid #ddd;
            }}

            footer {{
                text-align: center;
                margin-top: 20px;
                color: white;
                padding: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>Authentication Log Report</h1>
        <table>
            <tr>
                <th>Timestamp</th>
                <th>Message</th>
            </tr>
            {}
        </table>
        <div class="report">
            <h2>Report</h2>
            <p>Total log entries: {}</p>
            <p>Successful logins: {}</p>
            <p>Failed logins: {}</p>
            <h3>Successful IPs:</h3>
            {}
            <h3>Failed IPs:</h3>
            {}
        </div>
        {}
    </body>
    </html>
    """.format(th_background_color, table_rows, total_entries, successful_logins, failed_logins, successful_entries_list, failed_entries_list, copyleft_footer)

    return html

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate HTML report for auth.log')
parser.add_argument('-f', '--folder', type=str, help='Folder path containing auth.log file')
args = parser.parse_args()

folder_path = args.folder

# Find the auth.log file in the folder
auth_log_file = None
for file_name in os.listdir(folder_path):
    if file_name == "auth.log":
        auth_log_file = os.path.join(folder_path, file_name)
        break

if auth_log_file:
    logs = read_auth_log(auth_log_file)
    html_report = generate_html_report(logs)

    # Write the HTML report to a file
    report_file = os.path.join(folder_path, "auth_report.html")
    with open(report_file, 'w') as file:
        file.write(html_report)

    print("[*] HTML report generated successfully!")
    print("[i] Report file path: {}".format(report_file))
else:
    print("[x] auth.log file not found in the specified folder.")
