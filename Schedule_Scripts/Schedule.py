import schedule
import time
import subprocess

def run_selenium_script():
    
    # Replace 'your_script.py' with the path to your Selenium script
    subprocess.run(['python', 'C:/Users/User/OneDrive/Desktop/Hiring_Selenium/API_Tests/test_hiring.py'])

# Schedule the execution of the Selenium script every day at 9:00 AM
schedule.every().day.at("10:02").do(run_selenium_script)

# You can add more schedules if needed
# schedule.every().day.at("12:00").do(run_selenium_script)
# schedule.every().day.at("15:00").do(run_selenium_script)

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(10)  # Sleep for 60 seconds before checking again
