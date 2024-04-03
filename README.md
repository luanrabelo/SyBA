<p align="center">
  <img src="https://raw.githubusercontent.com/luanrabelo/SyBA/stable/docs/assets/SyBA.png" alt="SyBA Logo" width="25%">
</p>

<p align="center">
<a href="https://www.buymeacoffee.com/lprabelo" target="_blank">
<img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=☕&slug=lprabelo&button_colour=EEEEEE&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=000000" />
</a>
</p>

# Contents Overview
- [System Overview](#system-overview)
- [Getting Started with SyBA](#getting-started-with-syba)
    - [Prerequisites](#prerequisites)
    - [Installation Guide](#installation-guide)
- [Efficiency of SyBA](#efficiency-of-syba)
- [SyBA Class Functions](#syba-class-functions)
    - [init](#syba-init)
    - [SyBA Update](#syba-update)
    - [SyBA fixName](#syba-fixname)
    - [SyBA buildQuery](#syba-buildquery)
- [Example Codes](#example-codes)
- [Web Form for SyBA](#web-form-for-syba)
- [License Information](#license-information)
- [Development Team](#development-team)
- [Citing SyBA](#citing-syba)
***  
&nbsp;  
# System Overview
##### [Go to Contents Overview](#contents-overview)
SyBA (**Sy**nonymous of **BA**cterial Genes) is a **tool** and **database** for **standardizing gene names in bacterial genomes**. It provides a consistent nomenclature for gene names, allowing researchers to accurately search for genes from bacteria that cause **human diseases**, improving **public health** research on **foodborne illnesses** (Figure 1).

> ![MarineGEO circle logo](https://raw.githubusercontent.com/luanrabelo/SyBA/stable/assets/img/Figure1.png "Map")  Figure 1. Global snapshot of the Food Contamination Monitoring and Assessment Programme, highlighting the top 10 countries and various regions. The data is sourced from the Global Environment Monitoring System, avaliable at https://apps.who.int/foscollab/Download/DownloadConta  

The **SyBA** database is constructed using gene symbols and gene products (proteins) present in **1,215,109 functional bacterial genomes**, based on the genera _Campylobacter_, _Clostridium_, _Escherichia_, _Listeria_, _Salmonella_, _Shigella_, _Staphylococcus_, and _Vibrio_.  

**SyBA** includes a **Python class** for standardizing gene names, which can automatically find and change different name variations into a standard form. The class also generates search commands for specific genes or papers in **GenBank** or **PubMedCentral** with different bacterial gene names.  

Additionally, **SyBA** provides a **web form** that is **easy-to-use** for **researchers** to **search for specific genes or papers** in **GenBank** or **PubMedCentral**.  

The **SyBA** repository, hosted on **GitHub** and **licensed under MIT**, is a **freely accessible** resource for the **scientific community**. It offers comprehensive analysis results of bacterial gene names. In addition, it includes thorough **guidelines and sample scripts** to **assist researchers in their work**.
***  
&nbsp;  
# Getting Started with **SyBA**
##### [Go to Contents Overview](#contents-overview)
- ## Prerequisites
Before you run **SyBA**, make sure you have the following prerequisites installed on your system:
- **Python Environment**
    - Python **version 3.6 or higher**
    - conda (optional)
- Dependencies (these will be automatically installed with pip)
    - `requests`
    - `pandas`
    - `openpyxl`  
    - `numpy`
- ## Installation Guide
There are **tree** ways to install **SyBA**:
1. **Through pip**:  Install **SyBA** directly using pip:  
```bash  
pip install SyBA
```
- This will install **SyBA** and its **dependencies** in your **Python environment**.
&nbsp;  
&nbsp;  
2. **By cloning the GitHub repository**: Clone the source code of **SyBA** from GitHub:
```bash
git clone https://github.com/luanrabelo/SyBA.git
cd SyBA  
pip install -r requirements.txt
```
- This command will **clone the repository**, and then you should **navigate to the cloned directory** to **install SyBA and its dependencies** using pip.
&nbsp;  
&nbsp;   
3. Installation via **conda**:  You can also install **SyBA** using conda with the following commands:  
```bash
conda create -n SyBA -c conda-forge -c bioconda SyBA
conda activate SyBA 
```
- This method will set up **SyBA** along with its **dependencies** in a **new conda environment**.
&nbsp;  
***  
&nbsp;  
# Efficiency of SyBA
##### [Go to Contents Overview](#contents-overview)
> ![SyBA](https://raw.githubusercontent.com/luanrabelo/SyBA/stable/assets/img/Figure2.png "Comparison")  Figure 2. **(a)** Comparison between the number of gene name variations in the **SyBA database (v1.0.0)** and the number of proteins without a gene name. **(b)** The **15 genes** with the **most name variations** in the **SyBA database (v1.0.0)**. **(c)** By applying the names of proteins that do **not have a gene name**, it is possible to **recover this information** in up to **55.3%** of cases. **(d)** The **time required** for the **SyBA class** to **standardize gene names** in **1000 bacterial genomes**, with the **possibility of executing the function asynchronously** to further **reduce processing time**. **(e)** The time required to **generate 1000 search commands** with gene name variations.
&nbsp;  
  
> ![SyBA](https://raw.githubusercontent.com/luanrabelo/SyBA/stable/assets/img/Figure3.png "Comparison")  Figure 3. A comparative analysis of search results in **March 2024**, contrasting the efficiency of the **SyBA web form** against conventional searches in GenBank **(a)** and PubMedCentral **(b)**. The comparison underscores the enhanced efficiency attained through the use of combined gene nomenclature and variation in gene nomenclature for genes **birA**, **folD**, **fruA**, **hsdM**, **hsdR**, **hsdS**, **kdpD**, **mtlA**, **potD**, **pstS**, **putA**, **tnp**, **tnpA**, **wzy** and **wzx**.
&nbsp;  
***  

# SyBA Class Functions
## SyBA init
##### [Go to Contents Overview](#contents-overview)
### `__init__(self, **kwargs)`  

The **SyBA** class is initialized with this function. This function serves as the constructor for the class and is invoked when a new **SyBA** class instance is created.

Upon the creation of a **SyBA** class instance, the constructor verifies the existence of the `SyBA_database.tsv` database at the given path. If the database is not found, it will strive to establish the **SyBA directory** and **procure the database from the GitHub repository**.

If the verbose parameter is set to **True**, progress updates will be displayed in the terminal to keep the user informed about the ongoing operations.

#### Parameters:
- `verbose (bool)`: If `True`, messages will be printed during execution. The default is `True`.
#### Returns:
- `None`
#### Notes:
- This function requires the `requests` and `pandas` library to be imported.
- The `SyBA` database is available at github.com/luanrabelo/SyBA.
#### Usage Example:
```python
# Import the SyBA class from the SyBA module.
from SyBA import SyBA
# This function initializes the class and downloads the database from the GitHub repository.
sb = SyBA(verbose=True)
```
#### Output
```
############################## SyBA ##############################
SyBA Class has been initialized!
Version: 0.0.1
Status: Stable
Author: Luan Rabelo
License: MIT
GitHub Page: https://github.com/luanrabelo/SyBA
Consult the documentation in github page for more information.
############################## SyBA ##############################
```
&nbsp;  
## SyBA update
##### [Go to Contents Overview](#contents-overview)
### `update(self, **kwargs)`  
The `update` method updates the **SyBA** database by **fetching it from the GitHub repository's stable branch**. If a database already exists, it's removed before the new one is downloaded.

This method checks for the `SyBA_database.tsv` database file on the user's system. If found, the file is removed. Then, it **downloads the latest database from the GitHub repository URL**.

If verbose is **True**, console messages inform the user about the progress, including the old database's removal and the new one's download.


#### Parameters:
- `verbose (bool)`: If `True`, messages will be printed during execution. The default is `True`.

#### Returns:
- The updated `SyBA` database saved in the `SyBA` folder.

#### Notes:
- This function requires the `requests` library to be imported.
- The `SyBA` database is available at github.com/luanrabelo/SyBA.

#### Usage Example:
```python
# Import the SyBA class from the SyBA module.
from SyBA import SyBA
# This function initializes the class and downloads the database from the GitHub repository.
sb = SyBA(verbose=True)
# This function update SyBA database
sb.update(verbose=True)
```
#### Output
```
2024/03/05 - 16:20:57 - SyBA database found in the current directory!
2024/03/05 - 16:20:57 - SyBA database found in /home/luanrabelo/SyBA/ !
2024/03/05 - 16:20:57 - Removing old SyBA database...
2024/03/05 - 16:20:57 - Old SyBA database removed successfully!
2024/03/05 - 16:20:57 - Downloading SyBA database from https://github.com/luanrabelo/SyBA, please wait...
2024/03/05 - 16:21:00 - Download SyBA database successfully!
```
&nbsp;  

## SyBA fixName
##### [Go to Contents Overview](#contents-overview)
### `fixName(self, **kwargs)`
Corrects the gene name according to the **SyBA** database, ensuring it adheres to the standardized nomenclature.  

The `fixName` function takes a gene name and corrects it based on the entries in the **SyBA** database.
If the provided **gene name is found in the database**, **it is replaced with the standardized short name**.
**If not found**, **the original name is returned, and a log entry is created**.
The function provides verbose output if the verbose parameter is set to **True**.

#### Parameters:
- `dscp (str)`: The gene description, for example, lcl|AASOAZ010000001.1_cds_EFE7820019.1_2 [locus_tag=F6Q14_00010] [protein=pflagellum-specific ATP synthase FliL] [protein_id=EFE7820019.1] [location=complement(1576..1932)] [gbkey=CDS].
- `verbose (bool)`: If set to `True`, messages will be printed during execution. The default is `True`.

#### Returns:
- `ShortName (str)`: The corrected gene name.

#### Notes:
- This function requires the `pandas` and `numpy` library to be imported.
- The `SyBA` database can be found at github.com/luanrabelo/SyBA.

#### Usage Example:
 ```python
# Import the SyBA class from the SyBA module.
from SyBA import SyBA
# This function initializes the class and downloads the database from the GitHub repository.
sb = SyBA(verbose=True)
# This function fixes the gene name.
geneName = sb.fixName(dscp='[protein=flagellum-specific ATP synthase FliL]', verbose=True)
print(geneName)
```
#### Output
```
fliL
```
&nbsp;  

## SyBA buildQuery
##### [Go to Contents Overview](#contents-overview)
### `buildQuery(self, **kwargs)`
Constructs a query for **Entrez** search in **GenBank** or **PubMed** using the **SyBA** database.

The `buildQuery` function creates a query string that can be utilized to search for specific gene information in the **GenBank** or **PubMed** databases.

The **search type** is validated against a **list of acceptable formats**.

The **list of acceptable formats** includes **"Title", "Abstract", "All Fields", "MeSH Terms"**.

If the verbose parameter is set to **True**, the function will output informative messages during the process of query construction.

#### Parameters:
- `geneName`: The gene name, for example, `rpoB`.
- `specieName`: The specie name, for example, `Salmonella`.
- `searchType`: The search type, for example, `All Fields`.
- `verbose`: If `True`, the class will print the status of the database and the download process. If `False`, the class will not print anything. Default is `False`.

#### Returns:
- `query (str)`: The query for Entrez search in GenBank or PubMed.

#### Notes:
- This function requires the `pandas` library to be imported.
- The `SyBA` database is available at github.com/luanrabelo/SyBA.
- The `_listTypes` contains the valid formats for the search type.

#### Usage Example:
```python
from SyBA import SyBA
sb = SyBA()
query = sb.buildQuery(specieName='Salmonella', geneName='mntB', searchType='All Fields', verbose=True)
print(query)
```
#### Output
```
2024/03/05 - 18:17:37 - SyBA database found in the current directory!
2024/03/05 - 18:17:37 - Gene: 'mntB' found in SyBA database!
("Salmonella"[Organism] OR "Salmonella"[Title]) AND ("mntB"[All Fields] OR "zinc transport system permease protein"[All Fields] OR "manganese abc transporter (atp-binding protein)"[All Fields] OR "cation abc transporter permease protein"[All Fields] OR "putative manganese transport system membrane protein mntb"[All Fields] OR "manganese transport system membrane protein mntb"[All Fields] OR "manganese transport system membrane protein"[All Fields] OR "cation abc transporter"[All Fields] OR "abc-transporter membrane protein"[All Fields] OR "afed"[All Fields] OR "manganese abc transporter inner membrane permease sitd"[All Fields] OR "chelated iron transport system membrane protein yfed,manganese transport system membrane protein mntb,high-affinity zinc transporter membrane component,anchored repeat-type abc transporter, permease subunit,abc 3 transport family"[All Fields] OR "metal cation abc transporter membrane protein"[All Fields] OR "mn2+/zn2+ abc transporter permease"[All Fields])
```
***  
&nbsp;  

# Example Codes
##### [Go to Contents Overview](#contents-overview)
Navigate to the `Examples` folder to view a **notebook file** that showcases examples of **how to implement** the commands of **SyBA**. This notebook serves as a practical guide, providing step-by-step instructions and examples to help you understand and utilize the functionalities of **SyBA** effectively.
***  
&nbsp;  

# Web Form for SyBA
##### [Go to Contents Overview](#contents-overview)

We’ve created an intuitive web form, accessible at [SyBA web form](https://luanrabelo.github.io/SyBA/), designed for researchers interested in conducting individual searches using different names linked to the same gene. This web form produces a command that includes multiple names, facilitating accurate searches on platforms like the National Center for Biotechnology Information (NCBI) - GenBank and PubMed Central.  
&nbsp;  

![SyBA Web Form](https://raw.githubusercontent.com/luanrabelo/SyBA/stable/assets/img/SyBA.gif "SyBA")
&nbsp;  

***  
&nbsp;  

# License Information
##### [Go to Contents Overview](#contents-overview)
**SyBA** is **released** under the **MIT License**. This license permits reuse within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.

For more details, please see the **MIT License**.
&nbsp;  
***  
&nbsp;  
# Development Team
##### [Go to Contents Overview](#contents-overview)
- Luan Rabelo
- Marcelo Vallinoto
- Iracilda Sampaio
- Davidson Sodré
- Luiza Helena Meller da Silva
- Grazielle Gomes
&nbsp;  
***  
&nbsp;  
# Citing SyBA
##### [Go to Contents Overview](#contents-overview)
Soon...
