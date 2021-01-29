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
<details>
<summary> Demographics & Identifiers </summary>

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

</details>

Next category is APACHE covariate. APACHE is the Acute Physiology And Chronic Health Evaluation II. A covariate is a dataset shift, the change in the distribution of the covariates.  

<details>
<summary> APACHE Covariates </summary>

| Feature Name          | Description                                                                                                                                                                                                                                                                            | Data Type | Null % |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------|
| albumin_apache        | Albumin concentration measured during the first 24 hours in g/L, results in the highest APACHE III score. Ranges from 1.2 - 4.6                                                                                                                                                        | float     | 60     |
| apache_2_diagnosis    | APACHE II diagnosis for the ICU admission. Ranges from 101 - 308                                                                                                                                                                                                                       | float     | 1      |
| apache_3j_diagnosis   | APACHE III-J sub-diagnosis code, best describes the reason for the ICU admission. Ranges from .01 - 2201.05                                                                                                                                                                            | float     | 1      |
| apache_post_operative | APACHE operative status; 1 for post-operative, 0 for non-operative                                                                                                                                                                                                                     | integer   | 0      |
| arf_apache            | Whether the patient had acute renal failure during the first 24 hours of their unit stay, defined as a 24 hour urine output <410ml, creatinine >=133 micromol/L and no chronic dialysis. 0 or 1                                                                                        | integer   | 0      |
| bilirubin_apache      | Bilirubin concentration measured during the first 24 hours in micromol/L, results in the highest APACHE III score. Ranges from .1 - 60.2                                                                                                                                               | float     | 63     |
| bun_apache            | Blood Urea Nitrogen concentration measured during the first 24 hours in mmol/L, results in the highest APACHE III score. Ranges from 4.0 - 27.0                                                                                                                                        | float     | 20     |
| creatinine_apache     | Creatinine concentration measured during the first 24 hours in micromol/L, results in the highest APACHE III score. Ranges from .3 - 11.18                                                                                                                                             | float     | 19     |
| fio2_apache           | Fraction of Inspired Oxygen from the arterial blood gas taken during the first 24 hours of unit admission, produces the highest APACHE III score for oxygenation. Ranges from .21 - 1.0                                                                                                | float     | 77     |
| gcs_eyes_apache       | Eye opening component of the Glasgow Coma Scale measured during the first 24 hours, results in the highest APACHE III score. Values of 1, 2, 3, or 4                                                                                                                                   | float     | 2      |
| gcs_motor_apache      | Motor component of the Glasgow Coma Scale measured during the first 24 hours, results in the highest APACHE III score. Values of 1, 2, 3, 4, 5, or 6                                                                                                                                   | float     | 2      |
| gcs_unable_apache     | Whether the Glasgow Coma Scale was unable to be assessed due to patient sedation. 0 or 1                                                                                                                                                                                               | float     | 1      |
| gcs_verbal_apache     | Verbal component of the Glasgow Coma Scale measured during the first 24 hours, results in the highest APACHE III score. Values of 1, 2, 3, 4, or 5                                                                                                                                     | float     | 2      |
| glucose_apache        | Glucose concentration measured during the first 24 hours in mmol/L, results in the highest APACHE III score. Ranges from 39.0 - 598.7                                                                                                                                                  | float     | 11     |
| heart_rate_apache     | Heart rate measured during the first 24 hours in bpm, results in the highest APACHE III score. Ranges from 30.0 - 178.0                                                                                                                                                                | float     | 0      |
| hematocrit_apache     | Hematocrit measured during the first 24 hours, results in the highest APACHE III score. Ranges from 16.2 - 51.4                                                                                                                                                                        | float     | 21     |
| intubated_apache      | Whether the patient was intubated at the time of the highest scoring arterial blood gas used in the oxygenation score. 0 or 1                                                                                                                                                          | integer   | 0      |
| map_apache            | Mean Arterial Pressure measured during the first 24 hours in ml of mercury, results in the highest APACHE III score. Ranges from 40.0 - 200.0                                                                                                                                          | float     | 1      |
| paco2_apache          | Partial Pressure of Carbon Dioxide from the arterial blood gas taken during the first 24 hours of unit admission in ml of mercury, produces the highest APACHE III score for oxygenation. Ranges from 18.0 - 95.0ml of mercury                                                         | float     | 77     |
| paco2_for_ph_apache   | Partial Pressure of Carbon Dioxide from the arterial blood gas taken during the first 24 hours of unit admission ml of mercury, produces the highest APACHE III score for acid-base disturbance. Ranges from 18.0 - 95.0                                                               | float     | 77     |
| pao2_apache           | Partial Pressure of Oxygen from the arterial blood gas taken during the first 24 hours of unit admission in ml of mercury, produces the highest APACHE III score for oxygenation. Ranges from 31.0 - 498.0                                                                             | float     | 77     |
| ph_apache             | pH from the arterial blood gas taken during the first 24 hours of unit admission, produces the highest APACHE III score for acid-base disturbance. Ranges from 6.97 - 7.59                                                                                                             | float     | 77     |
| resprate_apache       | Respiratory rate measured during the first 24 hours in breaths/minute, results in the highest APACHE III score. Ranges from 4.0 - 60.0                                                                                                                                                 | float     | 1      |
| sodium_apache         | Sodium concentration measured during the first 24 hours in mmol/L, results in the highest APACHE III score. Ranges from 117.0 - 158.0                                                                                                                                                  | float     | 19     |
| temp_apache           | Temperature measured during the first 24 hours in degrees celsius, results in the highest APACHE III score. Ranges from 32.1 - 39.7                                                                                                                                                    | float     | 5      |
| urineoutput_apache    | Total urine output for the first 24 hours in ml. Ranges from 0 - 8716.7                                                                                                                                                                                                                | float     | 49     |
| ventilated_apache     | Whether the patient was invasively ventilated at the time of the highest scoring arterial blood gas using the oxygenation scoring algorithm, including any mode of positive pressure ventilation delivered through a circuit attached to an endo-tracheal tube or tracheostomy. 0 or 1 | integer   | 0      |
| wbc_apache            | White blood cell count measured during the first 24 hours in 10^9/L, results in the highest APACHE III score. Ranges from .9 - 45.8                                                                                                                                                    | float     | 23     |

</details>

Next category is patient vitals.

<details>
<summary> Patient Vitals </summary>
  
</details>

Patient labs is a large majority of the dataset. There is a category for labs and labs blood gas.

<details>
<summary> Patient Labs </summary>
  
</details>

The final category is APACHE comorbidities. This is an integer score from 0 to 71, with higher scores correlating with a higher risk of death.

<details>
<summary> APACHE Comorbidities </summary>
  
</details>

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
