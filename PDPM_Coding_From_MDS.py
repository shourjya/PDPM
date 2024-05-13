#!/usr/bin/env python
# coding: utf-8

# Inisialisation and Variables from MDS

# In[369]:


import matplotlib.pyplot as plt
import csv

PT = 0
OT = 0
SLP = 0
nursing = 0
NTA = 0
NCM = 0

#01. Dependent -
#02. Substantial/maximal assistance - Helper does MORE THAN HALF the effort.
#03. Partial/moderate assistance - Helper does LESS THAN HALF the effort.
#04. Supervision or touching assistance - Helper provides verbal cues and/or touching/steadying 
#05. Setup or clean-up assistance - Helper sets up or cleans up;
#06. Independent - Resident completes the activity by themself with no assistance from a helper.
#07. Resident refused
#09. Not applicable - Not attempted and the resident did not perform this activity prior to the current illness, exacerbation, or injury.
#10. Not attempted due to environmental limitations (e.g., lack of equipment, weather constraints)
#88. Not attempted due to medical condition or safety concerns

#Largely Indipendet Resident
GG0130A1 = 3
GG0130B1 = 4
GG0130C1 = 6

GG0170B1 = 6
GG0170C1 = 6

GG0170D1 = 5
GG0170E1 = 6
GG0170F1 = 5

GG0170J1 = 6
GG0170K1 = 5

#Typhoid arthritis
I0020B = "A0104"

#NTA 
H0100C = 0 #Bladder and Bowel Appliances: Ostomy
H0100D = 0

I1300 = 0
I1700 = 0
I2500 = 1
I2900 = 0
I5200 = 0
I5600 = 0
I6200 = 0

I8000_A = " "
I8000_B = " "
I8000_C = " "
I8000_D = "D61810 "
I8000_E = "B20 "
I8000_F = " "
I8000_G = " "
I8000_H = " "
I8000_I = "D61811 "
I8000_J = "T8619 "

K0510A2 = 0
K0510B2 = 1
K0710A2 = 0
K0710B2 = 0

M1040A = 1
M1040B = 0
M1040C = 0
M0300D1 = 0

O0100B2 = 1
O0100D2 = 0
O0100E2 = 0
O0100F2 = 0
O0100H2 = 0
O0100I2 = 0
O0100M2 = 0




# In[370]:


# Base Rates
#
# Link to FY 2023  Rate - PDPM unadjusted federal rate per diem
#https://www.mossadams.com/articles/2022/09/cms-finalizes-fy-2023-rule-for-snf-payments
    
PT_base_urban = 66.06
OT_base_urban = 61.49
SLP_base_urban = 24.66
nursing_base_urban = 115.15
NTA_Base_urban = 86.88
non_case_mix_urban = 103.12

PT_base_rural = 75.30
OT_base_rural = 69.16
SLP_base_rural = 31.07
nursing_base_rural = 110.02
NTA_Base_rural = 83.00
non_case_mix_rural = 105.03


# In[371]:


# PT & OT Adjustment Factors
#

def calculate_PT_OT_adjust_factor(day):
    if 1 <= day <= 20:
        PT_OT_Adjust_Fact = 1.00
    elif 21 <= day <= 27:
        PT_OT_Adjust_Fact = 0.98
    elif 28 <= day <= 34:
        PT_OT_Adjust_Fact = 0.96
    elif 35 <= day <= 41:
        PT_OT_Adjust_Fact = 0.94
    elif 42 <= day <= 48:
        PT_OT_Adjust_Fact = 0.92
    elif 49 <= day <= 55:
        PT_OT_Adjust_Fact = 0.90
    elif 56 <= day <= 62:
        PT_OT_Adjust_Fact = 0.88
    elif 63 <= day <= 69:
        PT_OT_Adjust_Fact = 0.86
    elif 70 <= day <= 76:
        PT_OT_Adjust_Fact = 0.84
    elif 77 <= day <= 83:
        PT_OT_Adjust_Fact = 0.82    
    elif 84 <= day <= 90:
        PT_OT_Adjust_Fact = 0.80
    elif 91 <= day <= 97:
        PT_OT_Adjust_Fact = 0.78
    elif 98 <= day <= 100:
        PT_OT_Adjust_Fact = 0.76           
    else:
        PT_OT_Adjust_Fact = 0.70  # Handle cases outside defined ranges
    return PT_OT_Adjust_Fact


# In[372]:


# NTA Adjustment Factors
#

def calculate_NTA_adjust_factor(day):
    if 1 <= day <= 3:
        NTA_adjust_fact = 3.00
    elif 4 <= day <= 100:
        NTA_adjust_fact = 1.00        
    else:
        NTA_adjust_fact = 0.70  # Handle cases outside defined ranges
    return NTA_adjust_fact


# In[373]:


# PT & OT Clinical Category from I0020B
#

target_icd10 = I0020B

def get_icd10_mapping(target_icd10):
    csv_file = "PDPM_ICD10_Mappings_FY2023_clinical_category.csv"
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            #print row[1],row[3]
            if len(row) >= 2 and row[1] == target_icd10+" ":
                #print row
                if len(row) >= 4:
                    return row[3]
                else:
                    return None
                print row[3]

def get_PT_OT_clinical_category(pdpm_clinical_category):
    if pdpm_clinical_category == "Major Joint Replacement or Spinal Surgery ":
        pt_ot_clinical_category = "Major Joint Replacement or Spinal Surgery"
    elif pdpm_clinical_category == "Acute Neurologic " or "Non-Orthopedic Surgery ":
        pt_ot_clinical_category = "Non-Orthopedic Surgery and Acute Neurologic"
    elif pdpm_clinical_category == "Non-Surgical Orthopedic/Musculoskeletal " or "Orthopedic Surgery (Except Major Joint Replacement or Spinal Surgery) ":
        pt_ot_clinical_category = "Other Orthopedic"
    elif pdpm_clinical_category == "Medical Management " or "Cancer " or "Pulmonary " or "Cardiovascular and Coagulations " or "Acute Infections ":
        pt_ot_clinical_category = "Medical Management"
    return pt_ot_clinical_category

#pdpm_clinical_category = get_icd10_mapping(csv_file, target_icd10)
#pt_ot_clinical_category = get_pt_ot_clinical_category(pdpm_clinical_category)
#print pdpm_clinical_category
#print pt_ot_clinical_category


# In[374]:


# PT & OT CMI
#

def assign_CMG_PT_OT(clinical_category,pt_score):
    if clinical_category == "Major Joint Replacement or Spinal Surgery":
        if pt_score <= 5:
            pt_ot_cmg = 'TA'
            pt_cmi = 1.53
            ot_cmi = 1.49
        elif pt_score <= 9:
            pt_ot_cmg = 'TB'
            pt_cmi = 1.69
            ot_cmi = 1.63
        elif pt_score <= 23:
            pt_ot_cmg = 'TC'
            pt_cmi = 1.88
            ot_cmi = 1.68
        elif pt_score <= 24:
            pt_ot_cmg = 'TD'
            pt_cmi = 1.92
            ot_cmi = 1.53

    if clinical_category == "Other Orthopedic":
        if pt_score <= 5:
            pt_ot_cmg = 'TE'
            pt_cmi = 1.42
            ot_cmi = 1.41
        elif pt_score <= 9:
            pt_ot_cmg = 'TF'
            pt_cmi = 1.61
            ot_cmi = 1.59
        elif pt_score <= 23:
            pt_ot_cmg = 'TG'
            pt_cmi = 1.67
            ot_cmi = 1.64
        elif pt_score <= 24:
            pt_ot_cmg = 'TH'
            pt_cmi = 1.16
            ot_cmi = 1.15
         
    if clinical_category == "Medical Management":
        if pt_score <= 5:
            pt_ot_cmg = 'TI'
            pt_cmi = 1.13
            ot_cmi = 1.17
        elif pt_score <= 9:
            pt_ot_cmg = 'TJ'
            pt_cmi = 1.42
            ot_cmi = 1.44
        elif pt_score <= 23:
            pt_ot_cmg = 'TK'
            pt_cmi = 1.52
            ot_cmi = 1.54
        elif pt_score <= 24:
            pt_ot_cmg = 'TL'
            pt_cmi = 1.09
            ot_cmi = 1.11
            
    if clinical_category == "Non-Orthopedic Surgery and Acute Neurologic":
        if pt_score <= 5:
            pt_ot_cmg = 'TM'
            pt_cmi = 1.27
            ot_cmi = 1.30
        elif pt_score <= 9:
            pt_ot_cmg = 'TN'
            pt_cmi = 1.48
            ot_cmi = 1.49
        elif pt_score <= 23:
            pt_ot_cmg = 'TO'
            pt_cmi = 1.55
            ot_cmi = 1.655
        elif pt_score <= 24:
            pt_ot_cmg = 'TP'
            pt_cmi = 1.08
            ot_cmi = 1.09
            
    return pt_ot_cmg, pt_cmi, ot_cmi


# In[375]:


# PT & OT Response To Functional Score
#

def response_to_func_score(response):
    if response == 6:
        score = 4
    elif response == 5:
        score = 4  
    elif response == 4:
        score = 4 
    elif response == 3:
        score = 4 
    elif response == 2:
        score = 4 
    else: 
    #response = 01,07, 09, 10, 88, missing
        score = 0
        
    return score


# In[376]:


# PT & OT Functional Score
#

def calculate_PT_OT_func_score():
    self_care = response_to_func_score(GG0130A1) + response_to_func_score(GG0130B1) + response_to_func_score(GG0130C1)
    mobility_1 = (response_to_func_score(GG0170B1)+response_to_func_score(GG0170C1))/2
    mobility_2 = (response_to_func_score(GG0170D1)+response_to_func_score(GG0170E1)+response_to_func_score(GG0170F1))/3
    mobility_3 = (response_to_func_score(GG0170J1)+response_to_func_score(GG0170K1))/2
    pt_ot_func_score = self_care + mobility_1 + mobility_2 + mobility_3
    return pt_ot_func_score


# In[377]:


# NFS Functional Score
#

def calculate_NFS_func_score():
    self_care = response_to_func_score(GG0130A1) + response_to_func_score(GG0130C1)
    mobility_1 = (response_to_func_score(GG0170B1)+response_to_func_score(GG0170C1))/2
    mobility_2 = (response_to_func_score(GG0170D1)+response_to_func_score(GG0170E1)+response_to_func_score(GG0170F1))/3
    pt_ot_func_score = self_care + mobility_1 + mobility_2
    return NFS_func_score


# In[ ]:


# SLP CMI
#

def assign_CMG_SLP(SLP_factor1,SLP_factor2)
    


# In[378]:


# NTA Adjustment Factor
#

def calculate_NTA_case_mix(score):
    if score == 0:
        NTA_Case_Mix = 0.72
    elif 1 <= score <= 2:
        NTA_Case_Mix = 0.96 
    elif 3 <= score <= 5:
        NTA_Case_Mix = 1.34   
    elif 6 <= score <= 8:
        NTA_Case_Mix = 1.85   
    elif 9 <= score <= 11:
        NTA_Case_Mix = 2.53   
    else:
        NTA_Case_Mix = 3.25 
    return NTA_Case_Mix


# In[379]:


### NTA CMI
#

def check_I8000(target_icd10_category):
    csv_file = "PDPM_ICD10_Mappings_FY2023_NTA.csv"
    check_I8000_value = 0
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            #print row[1],row[3]
            if row[1] == target_icd10_category:
                if row[3] == I8000_A or row[3] == I8000_B or row[3] == I8000_C or row[3] == I8000_D or row[3] == I8000_E or row[3] == I8000_F or row[3] == I8000_G or row[3] == I8000_H or row[3] == I8000_I or row[3] == I8000_J:
                    check_I8000_value = 1
                    #print row[1], row[3]
    
    return check_I8000_value

def calculate_NTA_score():
    NTA_score = 0
    
    I8000_chk_0 = check_I8000("HIV/AIDS ")
    I8000_chk_1 = check_I8000("Lung Transplant Status ")
    I8000_chk_2 = check_I8000("Major Organ Transplant Status, Except Lung ")
    I8000_chk_3 = check_I8000("Opportunistic Infections ")
    I8000_chk_4 = check_I8000("Bone/Joint/Muscle Infections/Necrosis - Except ")
    I8000_chk_5 = check_I8000("Chronic Myeloid Leukemia ")
    I8000_chk_6 = check_I8000("Endocarditis ")
    I8000_chk_7 = check_I8000("Immune Disorders ")
    I8000_chk_8 = check_I8000("End-Stage Liver Disease ")
    I8000_chk_9 = check_I8000("Narcolepsy and Cataplexy ")
    I8000_chk_10 = check_I8000("Cystic Fibrosis ")
    I8000_chk_11 = check_I8000("Specified Hereditary Metabolic/Immune Disorders ")
    I8000_chk_12 = check_I8000("Morbid Obesity ")
    I8000_chk_13 = check_I8000("Psoriatic Arthropathy and Systemic Sclerosis ")
    I8000_chk_14 = check_I8000("Chronic Pancreatitis ")
    I8000_chk_15 = check_I8000("Proliferative Diabetic Retinopathy and Vitreous Hemorrhage ")
    I8000_chk_16 = check_I8000("Complications of Specified Implanted Device or Graft ")
    I8000_chk_17 = check_I8000("Aseptic Necrosis of Bone ")
    I8000_chk_18 = check_I8000("Cardio-Respiratory Failure and Shock ")
    I8000_chk_19 = check_I8000("Myelodysplastic Syndromes and Myelofibrosis ")
    I8000_chk_20 = check_I8000("Systemic Lupus Erythematosus, Other Connective Tissue Disorders, and Inflammatory Spondylopathies ")
    I8000_chk_21 = check_I8000("Diabetic Retinopathy - Except ")
    I8000_chk_22 = check_I8000("Severe Skin Burn or Condition ")
    I8000_chk_23 = check_I8000("Intractable Epilepsy ")
    I8000_chk_24 = check_I8000("Disorders of Immunity - Except : RxCC97: Immune Disorders ")
    I8000_chk_25 = check_I8000("Cirrhosis of Liver ")
    I8000_chk_26 = check_I8000("Respiratory Arrest ")
    I8000_chk_27 = check_I8000("Pulmonary Fibrosis and Other Chronic Lung Disorders ")

    if I8000_chk_0 == 1:
        NTA_score += 8
    if K0510A2 == 1 or K0510A2 == 1:
        NTA_score += 7
    if O0100H2 == 1:
        NTA_score += 5
    if O0100F2 == 1:
        NTA_score += 4
    if K0510A2 == 1 or K0710A2 == 1 or K0710B2 == 1:
        NTA_score += 3
    if I8000_chk_1 == 1:
        NTA_score += 3
    if O0100I2 == 0:
        NTA_score += 2
    if I8000_chk_2 == 1:
        NTA_score += 2
    if I5200 == 1:
        NTA_score += 2
    if I8000_chk_3 == 1:
        NTA_score += 2  
    if I6200 == 1:
        NTA_score += 2
    if I8000_chk_4 == 1:
        NTA_score += 2 
    if I8000_chk_5 == 1:
        NTA_score += 2 
    if I2500 == 1:
        NTA_score += 2
    if I2900 == 1:
        NTA_score += 2
         
    if I8000_chk_6 == 1:
        NTA_score += 1 
    if I8000_chk_7 == 1:
        NTA_score += 1 
    if I8000_chk_8 == 1:
        NTA_score += 1 
    if M1040B == 1:
        NTA_score += 2
    if I8000_chk_9 == 1:
        NTA_score += 1 
    if I8000_chk_10 == 1:
        NTA_score += 1 
    if O0100E2 == 1:
        NTA_score += 1        
    if I1700 == 1:
        NTA_score += 1   
    if O0100M2 == 1:
        NTA_score += 1   
    if I8000_chk_11 == 1:
        NTA_score += 1 
    if I8000_chk_12 == 1:
        NTA_score += 1 
    if O0100B2 == 1:
        NTA_score += 1   
    if M0300D1 == 1:
        NTA_score += 1        
    if I8000_chk_13 == 1:
        NTA_score += 1 
    if I8000_chk_14 == 1:
        NTA_score += 1
    if I8000_chk_15 == 1:
        NTA_score += 1
        
    if M1040A == 1 or M1040B == 1 or M1040C == 1:
        NTA_score += 1
    if I8000_chk_16 == 1:
        NTA_score += 1
    if H0100D == 1:
        NTA_score += 1
    if I1300 == 1:
        NTA_score += 1
    if I8000_chk_17 == 1:
        NTA_score += 1
    if O0100D2 == 1:
        NTA_score += 1
    if I8000_chk_18 == 1:
        NTA_score += 1
    if I8000_chk_19 == 1:
        NTA_score += 1        
    if I8000_chk_20 == 1:
        NTA_score += 1
    if I8000_chk_21 == 1:
        NTA_score += 1
    if K0510B2 == 1:
        NTA_score += 1
    if I8000_chk_22 == 1:
        NTA_score += 1
    if I8000_chk_23 == 1:
        NTA_score += 1
    if I5600 == 1:
        NTA_score += 1
     
    if I8000_chk_24 == 1:
        NTA_score += 1
    if I8000_chk_25 == 1:
        NTA_score += 1
    if H0100C == 1:
        NTA_score += 1        
    if I8000_chk_26 == 1:
        NTA_score += 1
    if I8000_chk_27 == 1:
        NTA_score += 1
        
    return NTA_score

#print calculate_NTA_Score()


# In[380]:


# Per Diem Payment
#

def calculate_case_mix_adjusted_payment_day_X(urban,day):
    PT_OT_func_score = calculate_PT_OT_func_score()
    PDPM_clinical_category = get_icd10_mapping(target_icd10)
    PT_OT_clinical_category = get_PT_OT_clinical_category(PDPM_clinical_category)
    PT_OT_CMG, PT_CMI, OT_CMI = assign_CMG_PT_OT(PT_OT_clinical_category,PT_OT_func_score)
    
    SLP_factor1 = 1
    SLP_factor2 = 2
    SLP_CMI = assign_CMG_SLP(SLP_factor1,SLP_factor2)
    
    NTA_CMI = calculate_NTA_case_mix(calculate_NTA_Score())

    if urban == 1:
        PT = PT_Base_Urban * calculate_PT_OT_adjust_factor(day) * PT_CMI
        #print ("PT-Urban = ",PT)
        #print ("Factor",calculate_PT_OT_Adjust_Fact(Day))
        OT = OT_Base_Urban * calculate_PT_OT_adjust_factor(day) * OT_CMI
        SLP = SLP_base_urban * SLP_CMI
        nursing = nursing_base_urban
        NTA = NTA_Base_Urban * calculate_PT_OT_adjust_factor(day) * NTA_CMI
        NCM = Non_Case_Mix_Urban
    else:
        PT = PT_base_rural * calculate_PT_OT_adjust_factor(day) * PT_CMI
        OT = OT_base_rural * calculate_PT_OT_adjust_factor(day) * OT_CMI
        SLP = SLP_base_rural * SLP_CMI 
        nursing = nursing_base_rural
        NTA = NTA_Base_Rural * calculate_PT_OT_adjust_factor(day) * NTA_CMI
        NCM = Non_Case_Mix_Rural

         
    case_mix_adjusted_payment_day_X = PT+OT+SLP+nursing+NTA+NCM
    
    return case_mix_adjusted_payment_day_X

CMAP_Day_40 = calculate_case_mix_adjusted_payment_day_X(1,40)


# In[381]:


# Calculate Cumulitive Payment
#

def calculate_case_mix_adjusted_payment_cumulitive_day_X(urban,day):   
    
    case_mix_adjusted_payment_cumulitive_day_X = 0
    for i in range(1, day):
        case_mix_adjusted_payment_cumulitive_day_X += calculate_case_mix_adjusted_payment_day_X(urban,day)
        
    return case_mix_adjusted_payment_cumulitive_day_X


# In[382]:


# Print Per Diem Payment and Cumulitive Payment
#

CMAP_day_40 = calculate_case_mix_adjusted_payment_day_X(1,40)
CMAP_cumulitive_day_40 = calculate_case_mix_adjusted_payment_cumulitive_day_X(1,40)

print round(CMAP_day_40)
print round(CMAP_cumulitive_day_40)

#Error Backlog - 


# In[368]:


# Plot Cumulitive Payment
#

def calculate_case_mix_adjusted_payment_array_day_X(urban, days):
    revenues = []
    
    for i in range(1, days):
        revenue = calculate_case_mix_adjusted_payment_day_X(urban,i)
        revenues.append(revenue)
    
    return revenues

def plot_revenue_per_day(urban, days):
    revenues = calculate_case_mix_adjusted_payment_array_day_X(urban, days)
    plt.plot(range(1, days), revenues, marker='o')
    plt.title("Revenue per Day")
    plt.ylim(600,700)
    plt.xlabel("Day")
    plt.ylabel("Revenue")
    plt.grid(True)
    plt.show()
    
plot_revenue_per_day(urban=1, days=40)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




