<a id="top"></a>

#

<h1 align="center">
AuthLogExplorer
</h1>

<p align="center"> 
  <kbd>
<img src="https://raw.githubusercontent.com/r0xd4n3t/AuthLogExplorer/main/img/Analyzer.png"></img>
  </kbd>
</p>

<p align="center">
<img src="https://img.shields.io/github/last-commit/r0xd4n3t/AuthLogExplorer?style=flat">
<img src="https://img.shields.io/github/stars/r0xd4n3t/AuthLogExplorer?color=brightgreen">
<img src="https://img.shields.io/github/forks/r0xd4n3t/AuthLogExplorer?color=brightgreen">
</p>

# 📜 Introduction
Auth Log Analyzer is a Python script that reads and analyzes authentication logs (auth.log) commonly found on Linux systems. 
It extracts valuable information such as login attempts, IP addresses, and timestamps from the log file and generates an HTML report summarizing the log data.

![Sample HTML Report](https://raw.githubusercontent.com/r0xd4n3t/AuthLogExplorer/main/img/report_sample.png)

## 🧩 Requirements
To run Auth Log Analyzer, you need the following:

- Python 3.x
- Linux system with an `auth.log` file (usually found in `/var/log/auth.log`)

## 📈 Key Features
- **Log Parsing**: Auth Log Analyzer parses the `auth.log` file and extracts relevant log entries related to SSH login attempts.

- **HTML Report Generation**: It generates a visually appealing HTML report that includes a summary of log data, successful and failed login attempts, and IP addresses.

- **Random Color Styling**: The HTML report uses random background colors for aesthetics.

- **Easy to Use**: The script accepts a folder path containing the `auth.log` file as a command-line argument, making it easy to analyze logs in different locations.

## 🕹️ Usage
1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/your-username/auth-log-analyzer.git
2. Navigate to the repository folder:
   ```sh
   cd auth-log-analyzer
3. Run the script with the folder containing your "auth.log" file as an argument:
   ```sh
   python auth_log_analyzer.py -f /path/to/auth/logs/
4. The script will generate an HTML report in the specified folder with the name "auth_report.html"
5. Open the HTML report in your web browser to view the analysis.

# 📑 License
This project is licensed under the **MIT License**.

<p align="center"><a href=#top>Back to Top</a></p>
