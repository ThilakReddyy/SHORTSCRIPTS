import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import pandas as pd


# Function to get the selected district from a web page
def get_selected_district():
    # URL of the webpage to scrape
    url = "https://dharani.telangana.gov.in/knowLandStatus"

    # Send an HTTP GET request to the URL and store the response
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content of the response
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the first select element on the page
    select_element = soup.find_all("select")[0]

    # Find all option elements within the select element (excluding the first option)
    option_elements = select_element.find_all("option")[1:]

    # Create an empty dictionary to store district information
    districts_dict = {}

    # Iterate through the option elements and extract district name and value
    for index, option_element in enumerate(option_elements):
        district_name = option_element.get_text().strip().split("|")[0]
        district_value = option_element["value"]
        districts_dict[index + 1] = {"name": district_name, "value": district_value}
        # Print the district options for the user to choose from
        print(f"{index + 1}. {district_name}")

    # Prompt the user to enter the district number
    district_entered = input("Enter the District Number from the above options:")

    try:
        # Convert the user input to an integer
        district_entered = int(district_entered)

        # Check if the entered district number is within a valid range
        if 1 <= district_entered <= len(districts_dict):
            # If valid, return the district value corresponding to the selected district
            district_info = districts_dict[district_entered]
            return district_info["value"]
        else:
            # If not valid, return an error message
            return "Invalid district number."
    except ValueError:
        # If the user input is not a valid integer, return an error message
        return "Please enter a valid integer for the district number"


def get_selected_mandal(district_id):
    url = (
        "https://dharani.telangana.gov.in/getMandalFromDivisionCitizenPortal?district="
        + str(district_id)
    )

    response = requests.request("GET", url)

    # Create a BeautifulSoup object to parse the HTML content of the response
    soup = BeautifulSoup(response.text, "html.parser")

    option_elements = soup.find_all("option")[1:]
    mandals_dict = {}
    for index, option_element in enumerate(option_elements):
        mandal_name = option_element.get_text().strip().split("|")[0]
        mandal_value = option_element["value"]
        mandals_dict[index + 1] = {"name": mandal_name, "value": mandal_value}
        # Print the  mandal options for the user to choose from
        print(f"{index + 1}. {mandal_name}")

    # Prompt the user to enter the mandal number
    mandal_entered = input("Enter the Mandal Number from the above options:")

    try:
        # Convert the user input to an integer
        mandal_entered = int(mandal_entered)

        # Check if the entered  mandal number is within a valid range
        if 1 <= mandal_entered <= len(mandals_dict):
            # If valid, return the  mandal value corresponding to the selected  mandal
            mandal_info = mandals_dict[mandal_entered]
            return mandal_info["value"]
        else:
            # If not valid, return an error message
            return "Invalid Mandal number."
    except ValueError:
        # If the user input is not a valid integer, return an error message
        return "Please enter a valid integer for the Mandal number"


def get_selected_village(mandal_id):
    url = (
        "https://dharani.telangana.gov.in/getVillageFromMandalCitizenPortal?mandalId="
        + str(mandal_id)
    )

    response = requests.request("GET", url)

    # Create a BeautifulSoup object to parse the HTML content of the response
    soup = BeautifulSoup(response.text, "html.parser")

    option_elements = soup.find_all("option")[1:]
    villages_dict = {}
    for index, option_element in enumerate(option_elements):
        village_name = option_element.get_text().strip().split("|")[0]
        village_value = option_element["value"]
        villages_dict[index + 1] = {"name": village_name, "value": village_value}
        # Print the district options for the user to choose from
        print(f"{index + 1}. {village_name}")

    # Prompt the user to enter the village number
    village_entered = input("Enter the Village Number from the above options:")

    try:
        # Convert the user input to an integer
        village_entered = int(village_entered)

        # Check if the entered district number is within a valid range
        if 1 <= village_entered <= len(villages_dict):
            # If valid, return the district value corresponding to the selected district
            district_info = villages_dict[village_entered]
            return district_info["value"]
        else:
            # If not valid, return an error message
            return "Invalid Mandal number."
    except ValueError:
        # If the user input is not a valid integer, return an error message
        return "Please enter a valid integer for the Mandal number"


# Function to encode input string
def encode_input(input_str):
    encoded_str = urllib.parse.quote(input_str, safe="/")
    return encoded_str


# Function to get personal details based on Khata number and survey option


def get_personal_details(khata_number, survey_option):
    # Construct the URL for retrieving personal details
    personal_details_url = (
        f"https://dharani.telangana.gov.in/getPublicDataInfo?"
        f"villageId={village_id}&flagToSearch=surveynumber&searchData="
        f"{encode_input(survey_option)}&flagval=district&district={district_id}&mandal={mandal_id}&divi="
        f"&khataNoIdselect={khata_number}&ReqType=Citizen"
    )
    response = requests.request("GET", personal_details_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and store personal details in a dictionary
    form = soup.find_all("form")[0]
    divs = form.find_all("div")[0].find_all("div")[2]
    divis = divs.find_all("div")[1:]
    prt = {}
    for divi in divis:
        divins = divi.find_all("div")
        for divin in divins:
            strn = divin.find_all("strong")[0].get_text()
            leng = len(strn)
            prt[strn] = divin.get_text()[leng + 1 :].strip()
    print(prt)
    final_output.append(prt)


# Function to get Khata numbers based on survey number
def get_khata_number(survey_no):
    # Construct the URL for retrieving Khata numbers
    khata_number_url = (
        f"https://dharani.telangana.gov.in/getKhataNoCitizen?"
        f"villId={village_id}&flag=khatanos&surveyNo={encode_input(survey_no)}"
    )
    response = requests.request("GET", khata_number_url)
    soup = BeautifulSoup(response.text, "html.parser")
    options = soup.find_all("option")[1:]

    # Iterate through Khata numbers and get personal details
    for option in options:
        khata_number = option.get_text()
        get_personal_details(khata_number, survey_no)


# Main part of the code


# Define the ID's
district_id = get_selected_district()
mandal_id = get_selected_mandal(district_id)
village_id = get_selected_village(mandal_id)

# Define the base URL for retrieving survey information
survey_url = (
    f"https://dharani.telangana.gov.in/getSurveyCitizen?villId={village_id}&flag=survey"
)
final_output = []

response = requests.request("GET", survey_url)
soup = BeautifulSoup(response.text, "html.parser")
options = soup.find_all("option")[1:]

# Iterate through survey options and get Khata numbers and personal details
for option in options:
    survey_option = option.get_text()
    get_khata_number(survey_option)


print("Data saved in output.json")
df = pd.DataFrame(final_output)

# Save the DataFrame to an Excel file
df.to_excel("land_data.xlsx", index=False)
