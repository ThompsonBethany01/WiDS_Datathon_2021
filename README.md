# Women in Data Science (WiDS) Datathon 2021
## About the Project
### Goals
The primary goal of the project is to create a machine learning model to predict a patient's diagnosis of diabetes. The data is focused on patients staying in an Intensive Care Unit (ICU) because ICU's often lack verified medical histories for new patients. The patient may not be coherent enough to give information on their medical history and it can take time for the ICU to recieve their records - time the patient might not have. Knowing if the patient has diabetes sooner can improve the patient's outcome by allowing the ICU to make adjustments to their care based on this knowledge.

### Background

### Project Outline

### Deliverables

### Acknowledgments

## Data Dictionary
There are categories 6 within the one dataset. I will list each data dictionary by these categories. First is patient identifiers and demographics listed below.

| Feature Name          | Description                                                                                                                                             | Data Type | Null % |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------|
| encounter_id          | Unique ID number for patient unit stay                                                                                                                  | integer   | 0      |
| hospital_id           | Unique ID number for each hospital: 204 hospitals                                                                                                       | integer   | 0      |
| age                   | Age of patient in years: 0 - 89                                                                                                                         | float     | 4      |
| bmi                   | Body Mass Index in kg/m^2: goes to 6 decimal places                                                                                                     | float     | 4      |
| elective_surgery      | Boolean if patient was admitted for elective surgery                                                                                                    | integer   | 0      |
| ethnicity             | The common national or cultural tradition which the person belongs to: <br>African American, Asian, Caucasian, Hispanic, Native American, Other/Unknown | string    | 1      |
| gender                | The genotypical sex of the patient: 'M' or 'F'                                                                                                          | string    | 0      |
| height                | Height in centimeters                                                                                                                                   | float     | 2      |
| hospital_admit_source | Location of patient prior to being admitted to hospital                                                                                                 | string    | 26     |
| icu_admit_source      | Location of patient prior to being admitted to unit                                                                                                     | string    | 0      |
| icu_id                | Unique ID # for unit the patient was admitted                                                                                                           | integer   | 0      |
| icu_stay_type         | 3 types: admit, transfer, or readmit                                                                                                                    | string    | 0      |
| icu_type              | Classification for type of care the unit can give                                                                                                       | string    | 0      |
| pre_icu_los_days      | Length of stay between hospital admission and unit admission                                                                                            | float     | 0      |
| readmission_status    | Whether patient has been admitted to the unit previously, all values are 0                                                                              | integer   | 0      |
| weight                | The weight (body mass) in kilograms                                                                                                                     | float     | 3      |

Next category is APACHE covariate. APACHE is the Acute Physiology And Chronic Health Evaluation II. A covariate is a dataset shift, the change in the distribution of the covariates.

Next category is patient vitals.

Patient labs is a large majority of the dataset. There is a category for labs and labs blood gas.

The final category is APACHE comorbidities. This is an integer score from 0 to 71, with higher scores correlating with a higher risk of death.

## Initial Thoughts & Hypotheses
### Thoughts
### Hypotheses
## Project Steps
### Acquire
### Prepare
### Explore
### Model
### Conclusions
## How to Reproduce
### Steps
### Tools & Requirements
## Creator
[Bethany Thompson](https://github.com/ThompsonBethany01)
