# PDPM PPD Computation

# Description
Code that reads in MDS 3.0 and calculates HIPPS Code and CMS PDPM Reimbursement (PPD)

> Base Rates are computed using FY 2023 unadjusted federal rate per diem -- https://www.mossadams.com/articles/2022/09/cms-finalizes-fy-2023-rule-for-snf-payments

PPD = PT + OT + SLP + Nursing + NTA + NCM

  1. PT = PT_Base_Urban * calculate_PT_OT_adjust_factor(day) * PT_CMI
  2. OT = OT_Base_Urban * calculate_PT_OT_adjust_factor(day) * OT_CMI
  3. SLP = SLP_base_urban * SLP_CMI
  4. Nursing = nursing_base_urban * nursing_CMI
  5. NTA = NTA_Base_Urban * calculate_NTA_adjust_factor(day) * NTA_CMI
  6. NCM = Non_Case_Mix_Urban

# Output - 
1. Per Patient Day Reimbursment on Day X
2. Cumpulitive Per Patient Reimbursment for X Days 
3. Plots Showing Per Patient Reimbursment for X Days 

![image](https://github.com/shourjya/PDPM/assets/8657649/6e5bbc74-277a-483b-a520-fbfd5fe161f0)

# Current Backlogs 
1. CPS Score is not computed for SLP_CMI. 
2. In get_nursing_CMG_CMI() - Coding Needs to be duble checked

# Contributing
We welcome any and all contributions! Here are some ways you can get started

1. Report bugs: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.
Contribute code: If you are a developer and want to contribute, follow the instructions below to get started!
2. Suggestions: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or imporvements you would like to see!
3. Documentation: If you see the need for some additional documentation, feel free to add some!

# Instructions
1. Fork this repository
2. Clone the forked repository
3. Add your contributions (code or documentation)
4. Commit and push
5. Wait for pull request to be merged
