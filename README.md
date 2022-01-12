# Base TSE

This is an automated script that extracts data from the TSE (Tribunal Superior Eleitoral) database, the Brazilian National Court for everything related to Elections. It takes data from all people filiated to political parties, separated by state and by city, and generating two Excel spreadsheets with compiled information from each of these categories, comparing the data between May 2018 and May 2021 of each party in each city/state. While the state original spreadsheet was manually extracted (and is in this repo), I had to create another script to automatically extract data from all 27 federative units of Brazil, using the Selenium library to scrap TSE's webpage. All spreadsheets were processed using the Pandas library.

## About the project

This project was not originally a Git repository, so it wont have commits besides the setup ones. Also, it was done for a Brazilian team, so all files names, contents and explanations are in Portuguese. This is the only file in English this project currently has (but this can change in the future).

## Usage

To generate the spreadsheet `filiados_por_estado.xlsx`, you can simply run all cells in the notebook `GeraEstados.ipynb`, which will have explanations of its process in greater detail.

To generate the spreadsheet `filiados_por_municipio.xlsx`, the script `gera_planilha.sh` will run both `scrapper.py` and `extrai_dados.py`, moving and deleting all files accordingly. The file `extrai_dados.py` is basically the same as `GeraEstados.ipybn`, but running for a `.csv` file that contains data from cities in a state instead of data from all states compiled. `scrapper.py` gets those spreadsheets from the TSE database.

You can use the spreadsheets that come with the repository, running just `extrai_dados.py`, or run `gera_planilha.sh` and retrieve the spreadsheets yourself.