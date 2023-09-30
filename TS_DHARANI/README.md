# Telangana Land Data Scraper

## Overview

This Python script is designed to scrape land-related data from the Telangana government's Dharani portal. The script allows users to select a district, mandal, and village, and then retrieve personal details associated with land survey numbers and Khata numbers within the chosen village. The collected data is stored in an Excel file and a JSON file for further analysis or reference.

## Prerequisites

Before using this script, ensure that you have the following dependencies installed:

- Python 3.x
- Required Python packages: `requests`, `BeautifulSoup`, `urllib`, `json`, `pandas`

You can install these packages using `pip`:

```bash
pip install requests beautifulsoup4 pandas
```


## Usage

1. **Clone or Download**: Clone this repository or download the `dharani_data_extraction.py` script to your local machine.

2. **Install Dependencies**: Ensure you have Python 3.x installed on your system. Install the required Python packages using `pip`:

   ```bash
   pip install requests beautifulsoup4 pandas
    ```
3. Run the script, and it will guide you through the following steps:

    Select a district, mandal, and village from the Dharani portal.

    Retrieve personal details for each survey number and Khata number in the selected village.

    Save the collected data to an Excel file (`land_data.xlsx`) 

4. After running the script, you will find the collected data in the `land_data.xlsx` Excel file

## Important Notes

- **Internet Connection**: Ensure that your internet connection is stable while running the script to avoid interruptions during web scraping.

- **Educational and Ethical Use**: This script is intended for educational and informational purposes. Please be mindful of legal and ethical considerations when using web scraping tools, and respect the terms of use and privacy policies of the websites you interact with.

- **Last Updated**: The script is current as of the knowledge cutoff date in September 2023. If there have been changes to the website's structure or policies since then, the script may require modifications to function correctly.


## Disclaimer

This script is not affiliated with or endorsed by the Telangana government or the Dharani portal. Use it responsibly and respect the terms of use and privacy policies of the websites you interact with.