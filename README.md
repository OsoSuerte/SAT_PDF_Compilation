<!--lint disable no-literal-urls-->
<p align="center">
  <a href="https://Oso.com/">
    <img
      alt="Oso"
      src="http://clipart-library.com/images/ki8pMekir.png" width="192" height="120" 
    />
  </a>
</p>

�SAT PDF Compilation� (SPC) is designed to scrap, clean and compile data from a specific web source. 

Every year over 2 million of high school students across the United States participate in Scholastic Aptitude Tests (SATs). [CollegeBoard][] makes this data easily accessible in PDF form by individual state but the data is not easily analyzed in this form. There is also no readily available source where the raw data can be found. SPC is designed to remedy this dilemma.

# Table of contents

* [Support](#support)
* [Overview](#overview)
* [The Process](#the-process)
  * [Imports](#imports)
  * [Web Scrapping](#web-scraping)
  * [PDF Conversion](#pdf-conversion)
  * [Data Cleaning](#data-cleaning)
  * [DataFrame Building](#dataframe-building)
  * [Data Export](#data-Export)

* [Current Project Team Members](#current-project-team-members) 

* [Collaborators](#collaborators)
  
## Support

Looking for help? Send an email for direct support &lt;hizstor@gmail.com&gt;

## Overview
SPC was built with PyCharm 2020.3.3 running Python 3.9.1.

SPC is designed as a first step to automating the process of compiling SAT data. It will scrape a specific website where individual state SAT data is maintained. The data is collected from the website reformatted and combined into a single source that can easily be referenced and analyzed. This makes it simple to compare groups of SAT takers. Comparisons can be made between states, regions, demographic groups, previous years, etc. Having the data stored in this manner also makes visualization of the data simple and modular. 


## Imports
Libraries that must be imported to python environment for code to run successfully 

* **pandas**: Used to build DataFrames.
* **BeautifulSoup**: from bs4, used for web scraping.
* **requests**: Used for web scraping.
* **urljoin**: From urllib.parse, used for web scraping.   
* **tabula**: Used to extract data from PDFs.
* **glob, os**: Used to work with directories on a local machine. 


## Web Scraping
explaine the webscraping process


* **imports**: List needed imports
  
## PDF Conversion

## Data Cleaning

## DataFrame Building

## Data Export

## Current project team members
* [OsoSuerte](https://github.com/OsoSuerte) -
**Ben Sadler** &lt;hizstor@gmail.com&gt; (he/him)


<!--lint disable prohibited-strings-->

### Collaborators

* [OsoSuerte](https://github.com/OsoSuerte) -
**Ben Sadler** &lt;hizstor@gmail.com&gt; (he/him)

<!--lint enable prohibited-strings-->

[CollegeBoard]: https://reports.collegeboard.org/sat-suite-program-results/
