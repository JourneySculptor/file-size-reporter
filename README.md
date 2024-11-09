# file-size-reporter

A Python tool to generate periodic file size reports for a specified folder. This tool logs file sizes in a CSV format, allows customizable report locations, and automatically deletes old reports to save disk space.

## Features
- **Periodic File Size Reports**: Generates a CSV report of file sizes in the target folder at specified intervals.
- **Customizable Report Location**: Allows users to specify a folder where reports are saved.
- **Automatic Log Generation**: Logs file operations, including errors and skipped files.
- **Old Report Cleanup**: Deletes reports older than a specified number of days to save storage space.

## Requirements
- **Python 3.6+**

## Installation
1. **Clone the repository**:

    ```bash
    git clone https://github.com/YourUsername/file-size-reporter.git
    cd file-size-reporter
    ```

2. **Install Required Libraries**:
   - This project only uses Python’s built-in libraries (`os`, `pathlib`, `csv`, `datetime`, `logging`, `time`). No external dependencies are required.

## Configuration

- Set the target folder to monitor and the report folder where CSV reports will be saved.
- The report interval and report retention period (for deleting old reports) can be customized by setting the appropriate arguments in the `schedule_report` function.

## Usage

1. **Set Up Parameters in `schedule_report` Function**:
   - In `file_size_reporter.py`, set the desired parameters:
     - `interval_seconds`: Interval in seconds between each report generation.
     - `target_folder`: Path of the folder to monitor.
     - `report_folder`: Path of the folder where reports will be saved.
     - `days_to_keep`: Number of days to retain old reports.

2. **Run the Script**:
   - Execute the following command to start generating periodic reports:

     ```bash
     python file_size_reporter.py
     ```

3. **Check the Logs**:
   - A log file (`file_size_report.log`) is created in the project directory. This file contains details of file operations, including file sizes, total sizes, and any errors encountered.

## Example

Here’s an example configuration in `file_size_reporter.py`:

```python
# Example configuration
# Generate a report every 60 seconds for 'C:/example_folder' and save reports to 'C:/report_folder'
# Retain old reports for 7 days
schedule_report(60, 'C:/example_folder', 'C:/report_folder', days_to_keep=7)

```

## Logging
The script logs activity in `file_size_report.log`, including:

    File paths and their sizes.
    Total folder size.
    Any errors encountered (e.g., permissions issues).
    Old report deletions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
JourneySculptor 
