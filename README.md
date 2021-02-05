# Women in Data Science (WiDS) Datathon 2021
![repo-header](https://github.com/ThompsonBethany01/WiDS_Datathon_2021/blob/main/images/header.png?raw=true)
## About the Project
### Goals
The primary goal of the project is to create a machine learning model to predict a patient's diagnosis of diabetes. The data is focused on patients staying in an Intensive Care Unit (ICU) because ICU's often lack verified medical histories for new patients. The patient may not be coherent enough to give information on their medical history and it can take time for the ICU to recieve their records - time the patient might not have. Knowing if the patient has diabetes sooner can improve the patient's outcome by allowing the ICU to make adjustments to their care based on this knowledge.

### Background
Diabetes is a chronic health condition that causes elevated blood sugar levels when not in control by necessary medications and/or healthy lifestyle habits. Prolonged high blood sugars can cause additional health problems, such as vision loss and heart disease. In addition, acute extreme low or high blood sugars can cause the patient to have siezures or become comatose. The sooner a patient can recieve the needed medication, the lower the risk of these complications and better chance at recovery.  

Read more about diabetes [here](https://www.cdc.gov/diabetes/basics/diabetes.html) from the CDC.

### Project Outline

### Deliverables

### Acknowledgments

## Data Dictionary
The target variable in the data set is the variable diabetes_mellitus - a 1 representing the patient being diagnosed with the crhonic disease, and 0 for no diagnosis of it. There are 180 additional features in the original dataset, categorized by the 6 labels below.  

#### First category of features is patient identifiers and demographics listed below.
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

#### Next category is APACHE covariate. APACHE is the Acute Physiology And Chronic Health Evaluation II. A covariate is a dataset shift, the change in the distribution of the covariates.  

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

#### The next category in the data is patient vitals. Vital signs are measurements to assess the general health of the patient and can be used as possible diagnositic measures. All variables beginning with d1 are taken in the first 24 hours of their stay. All variables beginning with h1 are taken in the first hour of their stay.  

<details>
<summary> Patient Vitals </summary>
  
  **Day 1 Vitals**
  
  | Variable Name             | Description                                                                                                           | Data Type | Null % |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------|--------|
| d1_diasbp_invasive_max    | Highest diastolic blood pressure in ml of mercury, invasively measured. Ranges from 37 - 181                          | integer   | 73     |
| d1_diasbp_invasive_min    | Lowest diastolic blood pressure in ml of mercury, invasively measured. Ranges from 5 - 89                             | integer   | 73     |
| d1_diasbp_max             | Highest diastolic blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 46 - 165 | integer   | 0      |
| d1_diasbp_min             | Lowest diastolic blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 13 - 90   | integer   | 0      |
| d1_diasbp_noninvasive_max | Highest diastolic blood pressure in ml of mercury, non-invasively measured. Ranges from 46 - 165                      | integer   | 1      |
| d1_diasbp_noninvasive_min | Lowest diastolic blood pressure in ml of mercury, non-invasively measured. Ranges from 13 - 90                        | integer   | 1      |
| d1_heartrate_max          | Highest heart rate in beats/minute. Ranges from 58 - 177                                                              | integer   | 0      |
| d1_heartrate_min          | Lowest heart rate in beats/minute. Ranges from 0 - 175                                                                | integer   | 0      |
| d1_mbp_invasive_max       | Highest mean blood pressure in ml of mercury, invasively measured. Ranges from 38 - 322                               | integer   | 73     |
| d1_mbp_invasive_min       | Lowest mean blood pressure in ml of mercury, invasively measured. Ranges from 2 - 119                                 | integer   | 73     |
| d1_mbp_max                | Highest mean blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 60 - 184      | integer   | 0      |
| d1_mbp_min                | Lowest mean blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 22 - 112       | integer   | 0      |
| d1_mbp_noninvasive_max    | Highest mean blood pressure in ml of mercury, non-invasively measured. Ranges from 60 - 181                           | integer   | 2      |
| d1_mbp_noninvasive_min    | Lowest mean blood pressure in ml of mercury, non-invasively measured. Ranges from 22 - 112                            | integer   | 2      |
| d1_resprate_max           | Highest respiratory rate in breaths/minute. Ranges from 14 - 92                                                       | integer   | 1      |
| d1_resprate_min           | Lowest respiratory rate in breaths/minute. Ranges from 0 - 100                                                        | integer   | 1      |
| d1_spo2_max               | Highest peripheral oxygen saturation as a %. Ranges from 0 - 100                                                      | integer   | 0      |
| d1_spo2_min               | Lowest peripheral oxygen saturation as a %. Ranges from 0 - 100                                                       | integer   | 0      |
| d1_sysbp_invasive_max     | Highest systolic blood pressure in ml of mercury, invasively measured. Ranges from 71 - 295                           | integer   | 73     |
| d1_sysbp_invasive_min     | Lowest systolic blood pressure in ml of mercury, invasively measured. Ranges from 10 - 172                            | integer   | 73     |
| d1_sysbp_max              | Highest systolic blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 90 - 232  | integer   | 0      |
| d1_sysbp_min              | Lowest systolic blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 41 - 160   | integer   | 0      |
| d1_sysbp_noninvasive_max  | Highest systolic blood pressure in ml of mercury, non-invasively measured. Ranges from 90 - 232                       | integer   | 1      |
| d1_sysbp_noninvasive_min  | Lowest systolic blood pressure in ml of mercury, non-invasively measured. Ranges from 41 - 160                        | integer   | 1      |
| d1_temp_max               | Highest core temperature in degrees Celsius, invasively measured. Ranges from 35 - 40                                 | integer   | 3      |
| d1_temp_min               | Lowest core temperature in degrees Celsius. Ranges from 32 - 38                                                       | integer   | 3      |
  
  **Hour 1 Vitals**
  
  | Variable Name             | Description                                                                                                           | Data Type | Null % |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------|--------|
|h1_diasbp_invasive_max    | Highest diastolic blood pressure in ml of mercury, invasively measured. Ranges from 33 - 135                          | integer   | 81     |
| h1_diasbp_invasive_min    | Lowest diastolic blood pressure in ml of mercury, invasively measured. Ranges from 19 - 104                           | integer   | 81     |
| h1_diasbp_max             | Highest diastolic blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 37 - 143 | integer   | 4      |
| h1_diasbp_min             | Lowest diastolic blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 22 - 113  | integer   | 4      |
| h1_diasbp_noninvasive_max | Highest diastolic blood pressure in ml of mercury, non-invasively measured. Ranges from 37 - 144                      | integer   | 9      |
| h1_diasbp_noninvasive_min | Lowest diastolic blood pressure in ml of mercury, non-invasively measured. Ranges from 22 - 114                       | integer   | 9      |
| h1_heartrate_max          | Highest heart rate in beats/minute. Ranges from 46 - 164                                                              | integer   | 3      |
| h1_heartrate_min          | Lowest heart rate in beats/minute. Ranges from 36 - 144                                                               | integer   | 3      |
| h1_mbp_invasive_max       | Highest mean blood pressure in ml of mercury, invasively measured. Ranges from 36 - 293                               | integer   | 80     |
| h1_mbp_invasive_min       | Lowest mean blood pressure in ml of mercury, invasively measured. Ranges from 8 - 140                                 | integer   | 80     |
| h1_mbp_max                | Highest mean blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 49 - 165      | integer   | 5      |
| h1_mbp_min                | Lowest mean blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 32 - 138       | integer   | 5      |
| h1_mbp_noninvasive_max    | Highest mean blood pressure in ml of mercury, non-invasively measured. Ranges from 49 - 163                           | integer   | 10     |
| h1_mbp_noninvasive_min    | Lowest mean blood pressure in ml of mercury, non-invasively measured. Ranges from 32 - 138                            | integer   | 10     |
| h1_resprate_max           | Highest respiratory rate in breaths/minute. Ranges from 10 - 59                                                       | integer   | 5      |
| h1_resprate_min           | Lowest respiratory rate in breaths/minute. Ranges from 0 - 189                                                        | integer   | 5      |
| h1_spo2_max               | Highest peripheral oxygen saturation as a %. Ranges from 0 - 100                                                      | integer   | 5      |
| h1_spo2_min               | Lowest peripheral oxygen saturation as a %. Ranges from 0 - 100                                                       | integer   | 5      |
| h1_sysbp_invasive_max     | Highest systolic blood pressure in ml of mercury, invasively measured. Ranges from 65 - 246                           | integer   | 81     |
| h1_sysbp_invasive_min     | Lowest systolic blood pressure in ml of mercury, invasively measured. Ranges from 31 - 198                            | integer   | 81     |
| h1_sysbp_max              | Highest systolic blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 75 - 223  | integer   | 4      |
| h1_sysbp_min              | Lowest systolic blood pressure in ml of mercury, either non-invasively or invasively measured. Ranges from 53 - 194   | integer   | 4      |
| h1_sysbp_noninvasive_max  | Highest systolic blood pressure in ml of mercury, non-invasively measured. Ranges from 75 - 223                       | integer   | 9      |
| h1_sysbp_noninvasive_min  | Lowest systolic blood pressure in ml of mercury, non-invasively measured. Ranges from 53 - 195                        | integer   | 9      |
| h1_temp_max               | Highest core temperature in degrees Celsius, invasively measured. Ranges from 33 - 40                                 | integer   | 23     |
| h1_temp_min               | Lowest core temperature in degrees Celsius. Ranges from 33 - 39                                                       | integer   | 23     |
  
</details>

#### Patient labs is a large majority of the dataset. There is a category for labs and labs blood gas.

<details>
<summary> Patient Labs </summary>
  
   **Day 1 Labs**
   
   | Variable Name        | Description                                                                                                          | Data Type | Null % |
|----------------------|----------------------------------------------------------------------------------------------------------------------|-----------|--------|
| d1_albumin_max       | The lowest albumin concentration of the patient in their serum in g/L. Ranges from 1 - 5                             | Float     | 55     |
| d1_albumin_min       | The lowest albumin concentration of the patient in their serum in g/L. Ranges from 1 - 4                             | Float     | 55     |
| d1_bilirubin_max     | The highest bilirubin concentration of the patient in their serum or plasma in micromol/L. Ranges from 0 - 60        | Float     | 59     |
| d1_bilirubin_min     | The lowest bilirubin concentration of the patient in their serum or plasma in micromol/L. Ranges from 0 - 58         | Float     | 59     |
| d1_bun_max           | The highest blood urea nitrogen concentration of the patient in their serum or plasma in mmol/L. Ranges from 4 - 126 | Float     | 11     |
| d1_bun_min           | The lowest blood urea nitrogen concentration of the patient in their serum or plasma in mmol/L. Ranges from 3 - 113  | Float     | 11     |
| d1_calcium_max       | The highest calcium concentration of the patient in their serum in mmol/L. Ranges from 6 - 11                        | Float     | 13     |
| d1_calcium_min       | The lowest calcium concentration of the patient in their serum in mmol/L. Ranges from 6 - 10                         | Float     | 13     |
| d1_creatinine_max    | The highest creatinine concentration of the patient in their serum or plasma in micromol/L. Ranges from 0 - 11       | Float     | 10     |
| d1_creatinine_min    | The lowest creatinine concentration of the patient in their serum or plasma in micromol/L. Ranges from 0 - 10        | Float     | 10     |
| d1_glucose_max       | The highest glucose concentration of the patient in their serum or plasma in mmol/L. Ranges from 73 - 611            | Integer   | 6      |
| d1_glucose_min       | The lowest glucose concentration of the patient in their serum or plasma in mmol/L. Ranges from 33 - 288             | Integer   | 6      |
| d1_hco3_max          | The highest bicarbonate concentration for the patient in their serum or plasma in mmol/L. Ranges from 12 - 40        | Float     | 15     |
| d1_hco3_min          | The lowest bicarbonate concentration for the patient in their serum or plasma in mmol/L. Ranges from 7 - 39          | Float     | 15     |
| d1_hemaglobin_max    | The highest hemoglobin concentration for the patient in g/dL. Ranges from 7 - 17                                     | Float     | 12     |
| d1_hemaglobin_min    | The lowest hemoglobin concentration for the patient in g/dL. Ranges from 7 - 17                                      | Float     | 12     |
| d1_hematocrit_max    | The highest volume proportion of red blood cells in a patient's blood, expressed as a fraction. Ranges from 20 - 52  | Float     | 12     |
| d1_hematocrit_min    | The lowest volume proportion of red blood cells in a patient's blood, expressed as a fraction. Ranges from 16 - 50   | Float     | 12     |
| d1_inr_max           | The highest international normalized ratio for the patient in micromol/L. Ranges from 1 - 8                          | Float     | 62     |
| d1_inr_min           | The lowest international normalized ratio for the patient in micromol/L. Ranges from 1 - 6                           | Float     | 62     |
| d1_lactate_max       | The highest lactate concentration for the patient in their serum or plasma in mmol/L. Ranges from 0 - 20             | Float     | 73     |
| d1_lactate_min       | The lowest lactate concentration for the patient in their serum or plasma in mmol/L. Ranges from 0 - 15              | Float     | 73     |
| d1_platelets_max     | The highest platelet count for the patient in 10^9/L. Ranges from 27 - 585                                           | Integer   | 14     |
| d1_platelets_min     | The lowest platelet count for the patient in 10^9/L. Ranges from 19 - 557                                            | Integer   | 14     |
| d1_potassium_max     | The highest potassium concentration for the patient in their serum or plasma in mmol/L. Ranges from 3 - 7            | Float     | 10     |
| d1_potassium_min     | The lowest potassium concentration for the patient in their serum or plasma in mmol/L. Ranges from 2 - 6             | Float     | 10     |
| d1_sodium_max        | The highest sodium concentration for the patient in their serum or plasma in mmol/L. Ranges from 123 - 158           | Float     | 10     |
| d1_sodium_min        | The lowest sodium concentration for the patient in their serum or plasma in mmol/L. Ranges from 117 - 153            | Float     | 10     |
| d1_wbc_max           | The highest white blood cell count for the patient in 10^9/L. Ranges from 1 - 46                                     | Float     | 13     |
| d1_wbc_min           | The lowest white blood cell count for the patient in 10^9/L. Ranges from 1 - 41                                      | Float     | 13     |
   
   **Hour 1 Labs**
   
   | Variable Name        | Description                                                                                                          | Data Type | Null % |
|----------------------|----------------------------------------------------------------------------------------------------------------------|-----------|--------|
| h1_albumin_max       | The lowest albumin concentration of the patient in their serum in g/L. Ranges from 1 - 5                             | Float     | 91     |
| h1_albumin_min       | The lowest albumin concentration of the patient in their serum in g/L. Ranges from 1 - 5                             | Float     | 91     |
| h1_bilirubin_max     | The highest bilirubin concentration of the patient in their serum or plasma in micromol/L. Ranges from 0 - 58        | Float     | 92     |
| h1_bilirubin_min     | The lowest bilirubin concentration of the patient in their serum or plasma in micromol/L. Ranges from 0 - 58         | Float     | 92     |
| h1_bun_max           | The highest blood urea nitrogen concentration of the patient in their serum or plasma in mmol/L. Ranges from 4 - 135 | Float     | 81     |
| h1_bun_min           | The lowest blood urea nitrogen concentration of the patient in their serum or plasma in mmol/L. Ranges from 4 - 135  | Float     | 81     |
| h1_calcium_max       | The highest calcium concentration of the patient in their serum in mmol/L. Ranges from 6 - 11                        | Float     | 81     |
| h1_calcium_min       | The lowest calcium concentration of the patient in their serum in mmol/L. Ranges from 5 - 11                         | Float     | 81     |
| h1_creatinine_max    | The highest creatinine concentration of the patient in their serum or plasma in micromol/L. Ranges from 0 - 12       | Float     | 81     |
| h1_creatinine_min    | The lowest creatinine concentration of the patient in their serum or plasma in micromol/L. Ranges from 0 - 12        | Float     | 81     |
| h1_glucose_max       | The highest glucose concentration of the patient in their serum or plasma in mmol/L. Ranges from 59 - 695            | Integer   | 58     |
| h1_glucose_min       | The lowest glucose concentration of the patient in their serum or plasma in mmol/L. Ranges from 42 - 670             | Integer   | 58     |
| h1_hco3_max          | The highest bicarbonate concentration for the patient in their serum or plasma in mmol/L. Ranges from 6 - 39         | Float     | 82     |
| h1_hco3_min          | The lowest bicarbonate concentration for the patient in their serum or plasma in mmol/L. Ranges from 6 - 39          | Float     | 82     |
| h1_hemaglobin_max    | The highest hemoglobin concentration for the patient in g/dL 5 - 17                                                  | Float     | 79     |
| h1_hemaglobin_min    | The lowest hemoglobin concentration for the patient in g/dL. Ranges from 5 - 17                                      | Float     | 79     |
| h1_hematocrit_max    | The highest volume proportion of red blood cells in a patient's blood, expressed as a fraction. Ranges from 16 - 52  | Float     | 79     |
| h1_hematocrit_min    | The lowest volume proportion of red blood cells in a patient's blood, expressed as a fraction. Ranges from 16 - 52   | Float     | 79     |
| h1_inr_max           | The highest international normalized ratio for the patient in micromol/L. Ranges from 1 - 8                          | Float     | 62     |
| h1_inr_min           | The lowest international normalized ratio for the patient in micromol/L. Ranges from 1 - 6                           | Float     | 62     |
| h1_lactate_max       | The highest lactate concentration for the patient in their serum or plasma in mmol/L. Ranges from 0 - 18             | Float     | 91     |
| h1_lactate_min       | The lowest lactate concentration for the patient in their serum or plasma in mmol/L. Ranges from 0 - 18              | Float     | 91     |
| h1_platelets_max     | The highest platelet count for the patient in 10^9/L. Ranges from 20 - 585                                           | Integer   | 81     |
| h1_platelets_min     | The lowest platelet count for the patient in 10^9/L. Ranges from 20 - 585                                            | Integer   | 81     |
| h1_potassium_max     | The highest potassium concentration for the patient in their serum or plasma in mmol/L. Ranges from 2 - 7            | Float     | 77     |
| h1_potassium_min     | The lowest potassium concentration for the patient in their serum or plasma in mmol/L. Ranges from 2 - 7             | Float     | 77     |
| h1_sodium_max        | The highest sodium concentration for the patient in their serum or plasma in mmol/L. Ranges from 114 - 157           | Float     | 78     |
| h1_sodium_min        | The lowest sodium concentration for the patient in their serum or plasma in mmol/L. Ranges from 114 - 157            | Float     | 78     |
| h1_wbc_max           | The highest white blood cell count for the patient in 10^9/L. Ranges from 1 - 44                                     | Float     | 81     |
| h1_wbc_min           | The lowest white blood cell count for the patient in 10^9/L. Ranges from 1 - 44                                      | Float     | 81     |
   
   **Day 1 Blood Labs**
   
   | Variable Name        | Description                                                                                                          | Data Type | Null % |
|----------------------|----------------------------------------------------------------------------------------------------------------------|-----------|--------|
| d1_arterial_pco2_max | The highest arterial partial pressure of carbon dioxide for the patient in ml of mercury. Ranges from 18 - 111       | Float     | 65     |
| d1_arterial_pco2_min | The lowest arterial partial pressure of carbon dioxide for the patient in ml of mercury. Ranges from 15 - 86         | Float     | 65     |
| d1_arterial_ph_max   | The highest arterial pH for the patient. Ranges from 7 - 8                                                           | Float     | 65     |
| d1_arterial_ph_min   | The lowest arterial pH for the patient. Ranges from 7 - 8                                                            | Float     | 65     |
| d1_arterial_po2_max  | The highest arterial partial pressure of oxygen for the patient in ml of mercury. Ranges from 39 - 541               | Float     | 65     |
| d1_arterial_po2_min  | The lowest arterial partial pressure of oxygen for the patient in ml of mercury. Ranges from 28 - 449                | Float     | 65     |
| d1_pao2fio2ratio_max | The highest fraction of inspired oxygen for the patient. Ranges from 55 - 835                                        | Float     | 72     |
| d1_pao2fio2ratio_min | The lowest fraction of inspired oxygen for the patient. Ranges from 36 - 604                                         | Float     | 72     |
   
   **Hour 1 Blood Labs**
   | Variable Name        | Description                                                                                                          | Data Type | Null % |
|----------------------|----------------------------------------------------------------------------------------------------------------------|-----------|--------|
| h1_arterial_pco2_max | The highest arterial partial pressure of carbon dioxide for the patient in ml of mercury. Ranges from 15 - 112       | Float     | 83     |
| h1_arterial_pco2_min | The lowest arterial partial pressure of carbon dioxide for the patient in ml of mercury. Ranges from 15 - 107        | Float     | 83     |
| h1_arterial_ph_max   | The highest arterial pH for the patient. Ranges from 7 - 8                                                           | Float     | 83     |
| h1_arterial_ph_min   | The lowest arterial pH for the patient. Ranges from 7 - 8                                                            | Float     | 83     |
| h1_arterial_po2_max  | The highest arterial partial pressure of oxygen for the patient in ml of mercury. Ranges from 34 - 535               | Float     | 83     |
| h1_arterial_po2_min  | The lowest arterial partial pressure of oxygen for the patient in ml of mercury 31 - 515                             | Float     | 83     |
| h1_pao2fio2ratio_max | The highest fraction of inspired oxygen for the patient. Ranges from 42 - 720                                        | Float     | 87     |
| h1_pao2fio2ratio_min | The lowest fraction of inspired oxygen for the patient. Ranges from 38 - 655                                         | Float     | 87     |
   
   
</details>

#### The final category is APACHE comorbidities. These are all binary integers representing if the patient has the corresponding disease or not.

<details>
<summary> APACHE Comorbidities </summary>
  
  | Variable Name               | Description                                                                                                                                                                                                                                                                                                             | Data Type  | Null % |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|--------|
| aids                        | Whether the patient has a definitive diagnosis of acquired immune deficiency syndrome (AIDS) (not HIV positive alone)                                                                                                                                                                                                   | Binary Int | 0      |
| cirrhosis                   | Whether the patient has a history of heavy alcohol use with portal hypertension and varices, other causes of cirrhosis with evidence of portal hypertension and varices, or biopsy proven cirrhosis. This comorbidity does not apply to patients with a functioning liver transplant.                                   | Binary Int | 0      |
| hepatic_failure             | Whether the patient has cirrhosis and additional complications including jaundice and ascites, upper GI bleeding, hepatic encephalopathy, or coma.                                                                                                                                                                      | Binary Int | 0      |
| immunosuppression           | Whether the patient has their immune system suppressed within six months prior to ICU admission for any of the following reasons; radiation therapy, chemotherapy, use of non-cytotoxic immunosuppressive drugs, high dose steroids (at least 0.3 mg/kg/day of methylprednisolone or equivalent for at least 6 months). | Binary Int | 0      |
| leukemia                    | Whether the patient has been diagnosed with acute or chronic myelogenous leukemia, acute or chronic lymphocytic leukemia, or multiple myeloma.                                                                                                                                                                          | Binary Int | 0      |
| lymphoma                    | Whether the patient has been diagnosed with non-Hodgkin lymphoma.                                                                                                                                                                                                                                                       | Binary Int | 0      |
| solid_tumor_with_metastasis | Whether the patient has been diagnosed with any solid tumor carcinoma (including malignant melanoma) which has evidence of metastasis.                                                                                                                                                                                  | Binary Int | 0      |
  
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
