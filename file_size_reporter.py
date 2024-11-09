import os
from pathlib import Path
import csv
from datetime import datetime, timedelta
import logging
import time

# Configure logging
log_file = 'file_size_report.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_file_size_report(target_folder, report_folder):
    """
    Generate a CSV report of file sizes in the target folder.

    Args:
        target_folder (str or Path): Path to the folder to analyze.
        report_folder (str or Path): Path to the folder where the report will be saved.
    """
    try:
        target_folder = Path(target_folder)
        report_folder = Path(report_folder)
        report_folder.mkdir(exist_ok=True)  # Ensure report folder exists

        report_file = report_folder / f'folder_size_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

        # Write file sizes to CSV
        with open(report_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['File Path', 'Size (Bytes)', 'Date'])

            total_size = 0
            for file in target_folder.rglob('*.*'):
                try:
                    size = os.path.getsize(file)
                    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    writer.writerow([str(file), size, date])
                    logging.info(f"Recorded size for {file.name}: {size} bytes")
                    total_size += size
                except Exception as e:
                    logging.error(f"Error reading file {file}: {str(e)}")

            writer.writerow([])
            writer.writerow(['Total Size (Bytes)', total_size])
            logging.info(f"Total size of files in {target_folder}: {total_size} bytes")

        print(f'File size report generated at {report_file}. Check the log file for details.')

    except Exception as e:
        logging.error(f"Error during file size report generation: {str(e)}")
        print('An error occurred. Check the log file.')

def delete_old_reports(report_folder, days=7):
    """
    Delete report files older than a specified number of days.

    Args:
        report_folder (str or Path): Path to the folder where reports are saved.
        days (int): Number of days after which reports should be deleted.
    """
    report_folder = Path(report_folder)
    cutoff_date = datetime.now() - timedelta(days=days)

    for report in report_folder.glob('*.csv'):
        try:
            report_time = datetime.fromtimestamp(report.stat().st_mtime)
            if report_time < cutoff_date:
                report.unlink()
                logging.info(f"Deleted old report: {report}")
        except Exception as e:
            logging.error(f"Error deleting file {report}: {str(e)}")

def schedule_report(interval_seconds, target_folder, report_folder, days_to_keep=7):
    """
    Schedule regular generation of file size reports and cleanup of old reports.

    Args:
        interval_seconds (int): Interval in seconds between report generations.
        target_folder (str or Path): Path to the folder to analyze.
        report_folder (str or Path): Path to the folder where reports are saved.
        days_to_keep (int): Number of days to retain old reports.
    """
    while True:
        generate_file_size_report(target_folder, report_folder)
        delete_old_reports(report_folder, days=days_to_keep)
        print(f"Report generated. Waiting {interval_seconds} seconds for the next report...")
        time.sleep(interval_seconds)

# Example usage
# Generates a report every 30 seconds and saves it to 'C:/report_folder'.
# Old reports older than 7 days will be deleted automatically.
schedule_report(30, 'C:/example_folder', 'C:/report_folder', days_to_keep=7)
