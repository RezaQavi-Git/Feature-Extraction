# Feature-Extraction

This project is a feature-extraction mechanism that extracts indicator-based features. It's designed to work with specific data and extract features using specific indicators.

## Data

The project is intended to work with data in a specific format. Please make sure that the data you want to use is in the correct format and located in the `./data/` folder, next to the `main.py` script.

## Indicators

The project extracts features using specific indicators. You can find a list of available indicators in the `main.py` script, which you can edit to select the indicators you want to use.

## Installation

Before you can run the project, you'll need to install its dependencies. You can do this by running the following command:

‍‍```pip install -r requirements.txt```

This will install all the necessary libraries for the project to run.

## Usage

To use the project, follow these steps:

1. Clone the project using the following command:

``git clone https://github.com/RezaQavi-git/featuer-extraction.git``

2. Navigate to the project directory:

3. Edit the list of coins and duration in the `main.py` script to match your requirements.

4. Run the `main.py` script using the following command:

``python3 main.py``


The features will be extracted and saved to the following path: `./extracts/extracted_{COINNAME}_{DURATION}.csv`.

## License

The project is licensed under the MIT license, which means that you're free to use, modify, and distribute the code as long as you include the license file.
