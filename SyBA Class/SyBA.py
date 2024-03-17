__author__      = "Luan Rabelo"
__license__     = "MIT"
__version__     = "0.0.1"
__maintainer__  = "Luan Rabelo"
__email__       = "luanrabelo@outlook.com"
__date__        = "2024/03/01"
__twitter__     = "lprabelo"
__github__      = "luanrabelo/SyBA"
__status__      = "Stable"
__tool__        = "SyBA"

import os 
import sys
import time
import re

class TerminalColors:
    Green       = '\033[92m'
    Warning     = '\033[93m'
    Fail        = '\033[91m'
    End         = '\033[0m'
    Bold        = '\033[1m'

try:
    import requests
    print(f"{TerminalColors.Green}Module 'Requests' found and imported!{TerminalColors.End}")
except ImportError:
    print(f"{TerminalColors.Fail}Module 'Requests' not found, please install it with: pip install requests{TerminalColors.End}")
    print(f"{TerminalColors.Warning}{TerminalColors.Underline}Do you want to install it now? (yes/no){TerminalColors.End}")
    Choice = str(input())
    if Choice.lower() in ['y', 'yes']:
        os.system('pip install requests')
        print(f"{TerminalColors.Green}Module 'Requests' installed successfully!{TerminalColors.End}")
        try:
            import requests
            print(f"{TerminalColors.Green}Module 'Requests' found and imported!{TerminalColors.End}")
        except ImportError:
            print(f"{TerminalColors.Fail}Module 'Requests' not found, please reinstall it with: pip install requests{TerminalColors.End}")
            sys.exit()
    else:
        print(f"{TerminalColors.Fail}Installation 'Requests' aborted!{TerminalColors.End}")
        sys.exit()
try:
    import pandas as pd
    print(f"{TerminalColors.Green}Module 'Pandas' found and imported!{TerminalColors.End}")
except ImportError:
    print(f"{TerminalColors.Fail}Module 'Pandas' not found, please install it with: pip install pandas{TerminalColors.End}")
    print(f"{TerminalColors.Warning}{TerminalColors.Underline}Do you want to install it now? (yes/no){TerminalColors.End}")
    Choice = str(input())
    if Choice.lower() in ['y', 'yes']:
        os.system('pip install pandas')
        print(f"{TerminalColors.Green}Module 'Pandas' installed successfully!{TerminalColors.End}")
        try:
            import pandas as pd
            print(f"{TerminalColors.Green}Module 'Pandas' found and imported!{TerminalColors.End}")
        except ImportError:
            print(f"{TerminalColors.Fail}Module 'Pandas' not found, please reinstall it with: pip install pandas{TerminalColors.End}")
            sys.exit()
    else:
        print(f"{TerminalColors.Fail}Installation 'Pandas' aborted!{TerminalColors.End}")
        sys.exit()
try:
    import numpy as np
    print(f"{TerminalColors.Green}Module 'Numpy' found and imported!{TerminalColors.End}")
except ImportError:
    print(f"{TerminalColors.Fail}Module 'Numpy' not found, please install it with: pip install numpy{TerminalColors.End}")
    print(f"{TerminalColors.Warning}{TerminalColors.Underline}Do you want to install it now? (yes/no){TerminalColors.End}")
    Choice = str(input())
    if Choice.lower() in ['y', 'yes']:
        os.system('pip install numpy')
        print(f"{TerminalColors.Green}Module 'Numpy' installed successfully!{TerminalColors.End}")
        try:
            import numpy as np
            print(f"{TerminalColors.Green}Module 'Numpy' found and imported!{TerminalColors.End}")
        except ImportError:
            print(f"{TerminalColors.Fail}Module 'Numpy' not found, please reinstall it with: pip install numpy{TerminalColors.End}")
            sys.exit()
    else:
        print(f"{TerminalColors.Fail}Installation 'Numpy' aborted!{TerminalColors.End}")
        sys.exit()

class SyBA:
    """
        # `SyBA`: `Sy`nonymous `BA`cteria
        ### Created by: Luan Rabelo (@lprabelo) and Marcelo Vallinoto (@mvallinoto01)

        ---
        This class is responsible for managing the SyBA database, which contains information about synonymous genes in bacteria. The database is a TSV file with the following columns:
            - `gene`: Contains the gene name, for example, `rpoB`.
            - `protein`: Contains the protein name, for example, `RNA polymerase beta subunit`.
            - `id`: Contains the gene id, for example, `NC_000913.3`.

        Functions:
            - `update`: This function updates the database from the GitHub repository.

        Notes:
            - This class requires the `requests` and `pandas` libraries to be imported.
            - The database is downloaded from the GitHub repository, available at: https://github.com/luanrabelo/SyBA

        Example:
            ```python
            # Import the SyBA class from the SyBA module.
            from SyBA import SyBA
            # This function initializes the class and downloads the database from the GitHub repository.
            sb = SyBA(verbose=True) 
            # This function updates the database from the GitHub repository.
            sb.update(verbose=True)
            ```
    """
    def __init__(self, **kwargs):
        """
            # `__init__`: `SyBA` class constructor
            ### This function initializes the class and downloads the database from the GitHub repository.

            ---
            Parameters:
                - `verbose`: If `True`, the class will print the status of the database and the download process. If `False`, the class will not print anything. Default is `False`.

            Note:
                - This function requires the `requests` and `pandas` libraries to be imported.

            Returns:
                - None

            Example:
                ```python
                # Import the SyBA class from the SyBA module.
                from SyBA import SyBA
                # This function initializes the class and downloads the database from the GitHub repository.
                sb = SyBA(verbose=True) 
                ```
        """
        self.version    = f"Version: {__version__}"
        self.status     = f"Status: {__status__}"
        self.license    = f"License: {__license__}"
        self.author     = f"Author: {__author__}"
        self.github     = f"GitHub Page: https://github.com/{__github__}"
        _verbose            = kwargs.get('verbose', False)
        dbLink = 'https://raw.githubusercontent.com/luanrabelo/SyBA/stable/database/dataSyBA.tsv'
        if _verbose:
            print("\n")
            print(f"{TerminalColors.Bold}############################## {__tool__} ##############################{TerminalColors.End}")
            print(f"{TerminalColors.Warning}{TerminalColors.Bold}{__tool__} Class has been initialized!{TerminalColors.End}")
            print(f"{TerminalColors.Green}{self.version}{TerminalColors.End}")
            print(f"{TerminalColors.Green}{self.status}{TerminalColors.End}")
            print(f"{TerminalColors.Green}{self.author}{TerminalColors.End}")
            print(f"{TerminalColors.Green}{self.license}{TerminalColors.End}")
            print(f"{TerminalColors.Green}{self.github}{TerminalColors.End}")
            print(f"Consult the documentation in github page for more information.")
            print(f"{TerminalColors.Bold}############################## {__tool__} ##############################{TerminalColors.End}\n")
        if not os.path.exists(f'{os.getcwd()}/{__tool__}/{__tool__}_database.tsv') or not os.path.isfile(f'{os.getcwd()}/{__tool__}/{__tool__}_database.tsv'):
            if _verbose:
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - {__tool__} database not found in the current directory!{TerminalColors.End}")
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Downloading the database from GitHub, please wait...{TerminalColors.End}")
            try:
                os.makedirs(f'{os.getcwd()}/{__tool__}/', exist_ok=True, mode=0o777)
                if _verbose == True:
                    print(f"{TerminalColors.Green}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Folder '{__tool__}' was created successfully!{TerminalColors.End}")
            except:
                if _verbose == True:
                    print(f"{TerminalColors.Fail}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Error creating folder '{__tool__}'! Verify if you have permission to create folders in this directory.{TerminalColors.End}")
                    sys.exit()
            if _verbose == True:
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Downloading {__tool__} database from https://github.com/luanrabelo/{__tool__}, please wait...{TerminalColors.End}")
            _fileName = f'{os.getcwd()}/{__tool__}/{__tool__}_database.tsv'
            _download = requests.get(dbLink, stream=True)
            if _download.status_code == 200:
                with open(_fileName, 'wb') as f:
                    for chunk in _download.iter_content(chunk_size=1024*16):
                        if chunk:
                            f.write(chunk)
                            f.flush()
                            os.fsync(f.fileno())
                if _verbose == True:
                    print(f"{TerminalColors.Green}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Download {__tool__} database successfully!\n{TerminalColors.End}")
            else:
                if _verbose == True:
                    print(f"{TerminalColors.Fail}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Download {__tool__} database failed: status code {_download.status_code} - {_download.text}{TerminalColors.End}")
                    sys.exit()
        else:
            if _verbose:
                print(f"{TerminalColors.Green}{time.strftime('%Y/%m/%d - %H:%M:%S')} - {__tool__} database found in the current directory!{TerminalColors.End}")
        
        self.dfQuery    = pd.read_csv(f'{os.getcwd()}/{__tool__}/{__tool__}_database.tsv', sep='\t')
        self.listTypes  = ["Title", "Abstract", "All Fields", "MeSH Terms"]

    def update(self, **kwargs):
        """
            # `update`: `SyBA` class update function
            ### This function updates the database from the GitHub repository.

            ---
            Parameters:
                - `verbose`: If `True`, the class will print the status of the database and the download process. If `False`, the class will not print anything. Default is `False`.

            Note:
                - This function requires the `requests` and `pandas` libraries to be imported.

            Returns:
                - Downloaded SyBA database in SyBA folder.

            Example:
                ```python
                # Import the SyBA class from the SyBA module.
                from SyBA import SyBA
                # This function initializes the class and downloads the database from the GitHub repository.
                sb = SyBA(verbose=True) 
                # This function updates the database from the GitHub repository.
                sb.update(verbose=True)
                ```
        """
        _verbose = kwargs.get('verbose', False)
        dbLink   = 'https://raw.githubusercontent.com/luanrabelo/SyBA/stable/database/dataSyBA.tsv'

        if os.path.exists(f'{os.getcwd()}/{__tool__}/{__tool__}_database.tsv') or os.path.isfile(f'{os.getcwd()}/{__tool__}/{__tool__}_database.tsv'):
            if _verbose:
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - {__tool__} database found in {os.getcwd()}/{__tool__}{TerminalColors.End}!\n")
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Removing old {__tool__} database...{TerminalColors.End}")
            try:
                os.remove(f'{os.getcwd()}/{__tool__}/{__tool__}_database.tsv')
                if _verbose:
                    print(f"{TerminalColors.Green}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Old {__tool__} database removed successfully!\n{TerminalColors.End}")
            except:
                if _verbose:
                    print(f"{TerminalColors.Fail}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Error removing old {__tool__} database! Verify if you have permission to remove files in this directory.{TerminalColors.End}")
                sys.exit()
        else:
            if _verbose:
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - {__tool__} database not found in {os.getcwd()}/{__tool__}/{TerminalColors.End}!\n")
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Creating folder '{__tool__}' in {os.getcwd()}{TerminalColors.End}")
            try:
                os.makedirs(f'{os.getcwd()}/{__tool__}/', exist_ok=True, mode=0o777)
                if _verbose:
                    print(f"{TerminalColors.Green}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Folder '{__tool__}' created successfully!\n{TerminalColors.End}")
            except:
                if _verbose:
                    print(f"{TerminalColors.Fail}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Error creating folder '{__tool__}'! Verify if you have permission to create folders in this directory.{TerminalColors.End}")
                sys.exit()
        print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Downloading {__tool__} database from https://github.com/luanrabelo/{__tool__}, please wait...{TerminalColors.End}")
        _fileName = f'{os.getcwd()}/{__tool__}/{__tool__}_database.tsv'
        _download = requests.get(dbLink, stream=True)
        if _download.status_code == 200:
            with open(_fileName, 'wb') as f:
                for chunk in _download.iter_content(chunk_size=1024*16):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
                if _verbose == True:
                    print(f"{TerminalColors.Green}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Download {__tool__} database successfully!\n{TerminalColors.End}")
        else:
            if _verbose == True:
                print(f"{TerminalColors.Fail}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Download {__tool__} database failed: status code {_download.status_code} - {_download.text}{TerminalColors.End}")
                sys.exit()

    def fixName(self, **kwargs):
        """
            # `fixName`: `SyBA` class fixName function
            ### This function fixes the gene name.

            ---
            Parameters:
                - `dscp`: The gene description, for example, lcl|AASOAZ010000001.1_cds_EFE7820019.1_2 [locus_tag=F6Q14_00010] [protein=phage terminase small subunit P27 family] [protein_id=EFE7820019.1] [location=complement(1576..1932)] [gbkey=CDS].
                - `verbose`: If `True`, the class will print the status of the database and the download process. If `False`, the class will not print anything. Default is `False`.

            Note:
                - This function requires the `requests` and `pandas` libraries to be imported.

            Returns:
                - A fixed gene name.

            Example:
                ```python
                # Import the SyBA class from the SyBA module.
                from SyBA import SyBA
                # This function initializes the class and downloads the database from the GitHub repository.
                sb = SyBA(verbose=True)
                # This function fixes the gene name.
                geneName = sb.fixName(dscp='[protein=phage terminase small subunit P27 family]', verbose=True)
                print(geneName)
                ```
        """
        _stringName = str(kwargs.get('dscp', ''))
        _verbose    = kwargs.get('verbose', False)
        # Pre-compile the regular expression
        _protein_re = re.compile(r'\[protein=([^\]]+)\]')
        _protein    = _protein_re.search(_stringName)
        _protein    = _protein.group(1) if _protein else _stringName
        # Store necessary data columns in variables
        gene_values     = self.dfQuery['gene'].values
        protein_values  = self.dfQuery['protein'].values
        if _verbose:
            print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Searching for '{_protein}' in {__tool__} database...{TerminalColors.End}")
        try:
            # Use numpy's where function for faster lookup
            Local       = np.where(protein_values == _protein)[0][0]
            ShortName   = gene_values[Local]
            if _verbose:
                print(f"{TerminalColors.Green}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Protein '{_protein}' found in {__tool__} database!{TerminalColors.End}")
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - '{_protein}' renamed to '{ShortName}'!{TerminalColors.End}")
        except IndexError:
            ShortName = _protein
            if _verbose:
                print(f"{TerminalColors.Fail}{time.strftime('%Y/%m/%d - %H:%M:%S')} - '{ShortName}' not found in {__tool__} database{TerminalColors.End}")
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Adding '{ShortName}' to {__tool__}.log{TerminalColors.End}")
            with open(f"{os.getcwd()}/{__tool__}/{__tool__}Error.log", "a+") as f:
                f.write(f"{ShortName}\n")
            if _verbose:
                print(f"{TerminalColors.Green}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Gene '{ShortName}' added to {__tool__}.log{TerminalColors.End}")
        return str(ShortName) 

    def buildQuery(self, **kwargs):
        """
            # `buildQuery`: `SyBA` class buildQuery function
            ### This function builds a query to search the database.

            ---
            Parameters:
                - `geneName`: The gene name, for example, `rpoB`.
                - `specieName`: The specie name, for example, `Salmonella`.
                - `searchType`: The search type, for example, `All Fields`.
                - `verbose`: If `True`, the class will print the status of the database and the download process. If `False`, the class will not print anything. Default is `False`.

            Note:
                - This function requires the `requests` and `pandas` libraries to be imported.

            Returns:
                - A query to search the database.

            Example:
                ```python
                # Import the SyBA class from the SyBA module.
                from SyBA import SyBA
                # This function initializes the class and downloads the database from the GitHub repository.
                sb = SyBA(verbose=True) 
                # This function builds a query to search the database.
                query = sb.buildQuery(specieName='Salmonella', geneName='wzx', searchType='All Fields', verbose=True)
                print(query)
                ```
        """
        _listQuery      = []
        _geneName       = str(kwargs.get('geneName', ''))
        _specieName     = str(kwargs.get('specieName', ''))
        _strTypes       = str(kwargs.get('searchType', "All Fields"))
        _verbose        = kwargs.get('verbose', False)
        if _geneName in self.dfQuery['gene'].values:
            if _verbose:
                print(f"{TerminalColors.Green}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Gene: '{_geneName}' found in {__tool__} database!{TerminalColors.End}")
            if _strTypes in self.listTypes:
                _listQuery.append(f'"{_geneName}"[{_strTypes}]')
                fullNames = self.dfQuery.loc[self.dfQuery['gene'] == _geneName, 'protein'].str.lower().values
                _listQuery.extend([f'"{fullName}"[{_strTypes}]' for fullName in fullNames if fullName not in _listQuery])
            else:
                if _verbose:
                    print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Type '{_strTypes}' is not in the correct format!{TerminalColors.End}")
                    print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Correct format is {self.listTypes}{TerminalColors.End}")
                sys.exit()
        else:
            if _verbose:
                print(f"{TerminalColors.Fail}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Gene: '{_geneName}' not found in {__tool__} database!{TerminalColors.End}")
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Please, verify if the gene name is correct and try again!{TerminalColors.End}")
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Consult the documentation in github page for more information.{TerminalColors.End}")
                print(f"{TerminalColors.Warning}{time.strftime('%Y/%m/%d - %H:%M:%S')} - If the problem persists, please contact the developer!{TerminalColors.End}")
                sys.exit()
        if _listQuery:
            _lst        = f'("{_specieName}"[Organism] OR "{_specieName}"[Title]) AND'
            _newList    = ' OR '.join(_listQuery)
            return f"{_lst} ({_newList})"
        else:
            print(f"{TerminalColors.Fail}{time.strftime('%Y/%m/%d - %H:%M:%S')} - Error building query!{TerminalColors.End}")
            sys.exit()

    def cite(self):
        """
            # `cite`: `SyBA` class cite function
            ### This function prints the citation for the SyBA database.

            ---
            Parameters:
                - None

            Note:
                - This function requires the `requests` and `pandas` libraries to be imported.

            Returns:
                - None

            Example:
                ```python
                # Import the SyBA class from the SyBA module.
                from SyBA import SyBA
                # This function initializes the class and downloads the database from the GitHub repository.
                sb = SyBA(verbose=True) 
                # This function prints the citation for the SyBA database.
                sb.cite()
                ```
        """
        
        print(f"{TerminalColors.Bold}\nCitation:{TerminalColors.End}")
        print(f"{TerminalColors.Bold}Luan Rabelo, Davidson Sodré, Luiza Helena Meller da Silva, Grazielle Gomes, Iracilda Sampaio & Marcelo Vallinoto. SyBA: a database for standardizing gene names in bacterial genomes. GitHub Repository. Available at: https://github.com/luanrabelo/SyBA. 2024.{TerminalColors.End}")