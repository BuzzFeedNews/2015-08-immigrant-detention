# Data and Analysis: Immigration Detention by Nationality

This repository contains the data and code supporting several passages in the BuzzFeed News article, "[Vast Disparities By Nationality In Immigration Jailings](http://www.buzzfeed.com/davidnoriega/vast-disparities-by-nationality-in-immigration-jailings)," published August 25, 2015.

## Data

The analyses below use data from the Department of Justice's "CASE" database, maintained by the Executive Office of Immigration Review (EOIR). The database,  which tracks immigration proceedings, was obtained by BuzzFeed News through a Freedom of Information Request. The data cover all cases whose records were created or updated between Jan. 1, 2000 and Jan. 15, 2015.

## Analyses

__For a code-free overview, [read this general methodology](methodology.md).__

For analysis supporting specific passages in the story, see below:

***

- __Passage:__ "According to a BuzzFeed News analysis of a vast federal database of deportation cases, the first analysis of its kind in the nation, three-quarters of all Mexicans facing deportation on non-criminal grounds were placed in detention centers. For Guatemalans, the next most frequently detained group, the rate was 61%. For China and Cuba, longtime adversaries of the United States, the rates were 19% and 16%."
- __Analysis:__ See the "Per-Nationality Detention Rate" section of [the analytic code](notebooks/detention-by-nationality-analysis.ipynb).

***

- __Passage:__ "Excluding Mexican immigrants, only 39% of cases analyzed by BuzzFeed News resulted in incarceration."
- __Analysis:__ See the "Overall detention rate for non-Mexican non-criminal cases" section of [the analytic code](notebooks/detention-by-nationality-analysis.ipynb).

***

- __Passage:__ "Other than Mexico, all but one of the nationalities with the highest detention rates are from Latin America. These include immigrants from the Northern Triangle of Central America — Guatemala, Honduras, and El Salvador — who in recent years have been entering the country in larger numbers. Immigrants from China are among those with the lowest rates of detention: Fewer than two out of ten Chinese immigrants are imprisoned during deportation proceedings, even though Chinese immigrants make up the fifth largest undocumented nationality in the U.S."
- __Analysis:__ See the "Per-Nationality Detention Rate" section of [the analytic code](notebooks/detention-by-nationality-analysis.ipynb).

***

- __Passage:__ "For its analysis, BuzzFeed News examined all removal cases initiated between 2003 and 2014. Because some immigrants are initially detained but subsequently released — often on bond or at the order of an immigration judge — BuzzFeed News counted such cases as detained in order to focus on ICE’s decision. The detention rate disparities persisted even after controlling for gender, whether the case stemmed from criminal charges, and whether the immigrant had legal representation at the beginning of the case."
- __Analysis:__ See the "Regression Analysis of Removal Cases" section of [the analytic code](notebooks/detention-by-nationality-analysis.ipynb).

## Technical Notes

- To replicate the analyses, you'll need Python 2.7 as well as the Python libraries listed in [requirements.txt](requirements.txt).

- Because the raw data occupies 5.3 gigabytes of storage, this repository contains a compressed version of it. To decompress the data, run `make data` from this repository's root directory.

## Questions / Feedback

If you have questions or feedback about the data or analyses, contact John Templon at john.templon@buzzfeed.com.
