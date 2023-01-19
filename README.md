# ADP Login Automation Script

This script is a Python script that uses Selenium to automate the process of logging into an ADP website. It uses Firefox browser to open the website and enters the login credentials provided in the command line arguments. It also has an option to run the browser in headless mode by passing a boolean argument.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

In order to run this script, you will need to have the following software installed on your machine:

    Firefox browser
    Selenium library
    Python 3

## Installing

1. Clone the repository to your local machine:

`git clone https://github.com/antonioromito/adp_automation.git`

2. Install Selenium by running the following command:

`pip install selenium`

## Running the script

To run the script, navigate to the directory where the script is located and run the following command:

`python adp_login.py --username YOUR_USERNAME --password YOUR_PASSWORD --headless True/False`

You can also check the help command to know more about the arguments you can pass

`python adp_login.py -h`

## Built With

    Python 3
    Selenium

## Authors

Antonio Romito  - Initial work - [My GitHub Profile](https://github.com/antonioromito/)

## License

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

## Acknowledgments

This project was inspired by the fact that the ADP portal makes your account unusable if you do not login frequently into your personal account.

Please let me know if you need me to add or modify anything.
