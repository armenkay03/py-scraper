# PY-SCRAPER
### A simple web scraper using Python, Twilio, Google Cloud web service, and (NoMachine)
##### Hosted on a Google Cloud web server running Ubuntu 20.04 
##
## Powered by 
![Python](https://a11ybadges.com/badge?logo=python) ![Twilio](https://a11ybadges.com/badge?logo=twilio) 
![Google Cloud](https://a11ybadges.com/badge?logo=googlecloud) ![Selenium](https://a11ybadges.com/badge?logo=selenium)

## Usage


The main purpose of this project is to automate the task of opening the user dashboard of my ISP and sending a message to my WhatsApp every hour.


- Install selenium webdriver and all dependencies 
- Enter your credentials (ISP & Twilio)
- Change the appropriate XPATHs and add them if needed
- Signup for Twilio and follow the instructions
- Make a Google Cloud server (preferably the cheapest one), and install NoMachine on it so you can remotely manage the program.


## More 
- It is obvious that this is not the most efficient way to do this but its how I did it.
- The "schedule.every(60).minutes.do(main)" is very janky I'm sure there are other ways to do this. e.i. make it so that every certain event triggers a notification.
- Moreover, the Twilio sandbox runs for 72 hours at a time so it needs a reset every 72 hours.






## Tech

This project uses several open source tools to work properly:

- [Selenium] - Selenium automates browsers. That's it!
What you do with that power is entirely up to you.
- [Google Cloud] - Google Cloud is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for their own consumer products, such as Google Search, Gmail, and YouTube.
- [Twilio] - Twilio is the industry-leading and trusted platform that efficiently powers your customer engagement innovation.
- [No Machine] - Connect to your remote computer at the speed of light.
- [Python] -Python is a programming language that lets you work quickly and integrate systems more effectively.

[Selenium]: <https://www.selenium.dev/>
[Google Cloud]: <https://cloud.google.com>
[Twilio]: <https://www.twilio.com/en-us>
[No Machine]: <https://www.nomachine.com/>
[Python]: <https://www.python.org/>
