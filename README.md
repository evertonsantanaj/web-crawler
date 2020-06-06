# web-crawler
Example for extracting reports in a specific website using Python

For this you'll need to first install selenium and dowload the driver for your browser (here I'll use Google Chrome). 
Check the Drivers section for more information: https://www.selenium.dev/selenium/docs/api/py/index.html

For getting the XPath, use the developer tools of your Browser. Example for finding Xpath from username field:
Open the website you want to log in -> F12 -> Ctrl+Shift+C ->  Click on username field (the element will be highlighted) -> Right click on the highlighted element and select Copy -> Copy full XPath

Then paste the path in username_field valiable in login_actions.py

You can use the same logic to get whetever field you should click on or fill in.

This code was developed using Python 3.6.1 and Selenium 3.14

Disclaimer: Use this code only for legal applications and when the login information belongs to you
