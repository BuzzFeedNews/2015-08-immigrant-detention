# Methodology

### About

In response to a public records request, the Justice Department’s Executive Office of Immigration Review provided BuzzFeed News with a (partially redacted) copy of the office’s case-tracking database, known by the acronym *CASE*. The records provided include all database entries updated or created between Jan. 1, 2000 and Jan. 15, 2015. The records exclude personally-identifying columns. The methodology below describes how BuzzFeed News analyzed the data to examine disparities in detention rates by nationality. 

BuzzFeed News' methodology was reviewed by Marc Rosenblum, Peter Markowitz, César Cuauhtémoc García Hernández, and two additional experts who requested anonymity. 

Python code that executes this analysis [can be found here](notebooks/detention-by-nationality-analysis.ipynb).

### Steps

1. **Load all `schedule` entries corresponding to an immigrant’s first court proceeding.** In the database, these entries correspond to rows where the `GENERATION` column equals "99".

2. **Load all `case` entries.** In the database, these rows contain basic information about a case, including: a unique identification number, the nationality of the immigrant, whether the immigrant was detained, when an attorney first appeared before the court, and the type of proceeding.

3. **Load all `charges` entries.** A given immigration case can have multiple proceedings (stemming from different grounds for removal), and a given proceeding can be associated with multiple charges. We group all the charges for an individual proceeding together into a single list.

4. **Combine all loaded data into one table, with one row per case.** Each row contains demographic details of the defendant and a full record of the first proceeding, including all the charges.

5. **Select only “removal” cases.** This *excludes* affirmative asylum cases and other non-removal cases. Removal cases are identified by the case type “RMV.”

6. **Select cases with a first proceeding between Jan. 1, 2003 and Dec. 31, 2014.** This leaves only cases that started after the Department of Homeland Security was created and operational. This selection is based on the first proceeding’s  `ADJ_DATE` (adjudication date) column.

7. **Remove cases containing a criminal charge in the initial proceeding.** These charges are labeled “237a02” and “212a02,” corresponding to the relevant portions of the Immigration and Nationality Act. *Note: Although this removes cases with criminal charges attached to the removal proceeding, it does not indicate whether immigrants have prior criminal records.*

8. **Calculate the number of non-criminal cases in custody by nationality.** Group all of the cases together by nationality and count how many have `CUSTODY` values of  “D” (detained), “R” (released), and “N” (never detained). A `CUSTODY` value of "released" indicates that the immigrant was at one point detained during their case but was later released. To calculate the “percent detained,” combine the defendants classified as either “released” or “detained.”

9. **Limit the calculations to nationalities with at least 20,000 cases.** This produces the first table in [the analysis notebook](notebooks/detention-by-nationality-analysis.ipynb).

10. **Run a logistic regression to elucidate the relationship between detention, nationality, and several other factors.** In the regression, “detained” is the dependent variable. Nationalities were converted to dummy variables. Other independent variables include: whether the initial proceeding contained criminal charges, whether the defendant had a lawyer, and gender. In this analysis, having a criminal charge and being Mexican had a larger effect on detention than any single other variable. (*Note: Gender is often blank in the raw data; BuzzFeed News replaced those blanks with the category “UNK.”*) This regression creates the final table in [the analysis notebook](notebooks/detention-by-nationality-analysis.ipynb).
