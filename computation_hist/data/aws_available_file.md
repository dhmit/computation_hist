## Computation Center Files Available on Amazon Web Services


We use Amazon Web Services (AWS) S3 to host our scanned files (pdfs, pngs, txts).
Unfortunately, there is no simple way to explore what files are available in a storage
bucket. As an alternative, I (SR) am listing the available files here. Primarily, this 
list should allow you to check if a file couldn't be loaded because of a typo or 
because it is unavailable. 


### Usage

In the tree structure below, you will find things like 
``` 
├── 1_10_architecture
│   └── raw_pdf
│       └── 1_10_architecture_raw.pdf
```

This means that there's a `1_10_architecture_raw.pdf` file in the 
`1_10_architecture/raw_pdf` directory.
-> the relative path for the file is `1_10_architecture/raw_pdf/1_10_architecture_raw.pdf`

All of our urls have the root 
`https://s3.amazonaws.com/comp-hist/docs/`

To generate a valid url, you combine the root with the relative path:
[https://s3.amazonaws.com/comp-hist/docs/1_10_architecture/raw_pdf/1_10_architecture_raw.pdf](https://s3.amazonaws.com/comp-hist/docs/1_10_architecture/raw_pdf/1_10_architecture_raw.pdf)


### Full Tree
Here are all currently available files.


``` 
├── 1_10_architecture
│   └── raw_pdf
│       └── 1_10_architecture_raw.pdf
├── 1_11_cc_budget_mit
│   └── raw_pdf
│       └── 1_11_cc_budget_mit_raw.pdf
├── 1_12_cc_budget_nsf
│   └── raw_pdf
│       └── 1_12_cc_budget_nsf_raw.pdf
├── 1_14_cc_dedication
│   └── raw_pdf
│       └── 1_14_cc_dedication_raw.pdf
├── 1_15_cc_equip
│   └── raw_pdf
│       └── 1_15_cc_equip_raw.pdf
├── 1_16_cc_dr_cohn
│   └── raw_pdf
│       └── 1_16_cc_dr_cohn_raw.pdf
├── 1_17_cc_hurd_ibm
│   └── raw_pdf
│       └── 1_17_cc_hurd_ibm_raw.pdf
├── 1_18_cc_ibm_seminar
│   └── raw_pdf
│       └── 1_18_cc_ibm_seminar_raw.pdf
├── 1_19_cc_verzuh
│   └── raw_pdf
│       └── 1_19_cc_verzuh_raw.pdf
├── 1_1_committee_on_machine_methods
│   └── raw_pdf
│       └── 1_1_committee_on_machine_methods_raw.pdf
├── 1_20_cc_704_time
│   └── raw_pdf
│       └── 1_20_cc_704_time_raw.pdf
├── 1_21_cc_misc1
│   └── raw_pdf
│       └── 1_21_cc_misc1_raw.pdf
├── 1_27_cc_1960
│   └── raw_pdf
│       └── 1_27_cc_1960_raw.pdf
├── 1_29_cc_correspondence
│   └── raw_pdf
│       └── 1_29_cc_correspondence_raw.pdf
├── 1_2_project_proposal_contract
│   └── raw_pdf
│       └── 1_2_project_proposal_contract_raw.pdf
├── 1_30_cc_time_1959_1962
│   └── raw_pdf
│       └── 1_30_cc_time_1959_1962_raw.pdf
├── 1_31_social_science_advisory_committee
│   └── raw_pdf
│       └── 1_31_social_science_advisory_committee_raw.pdf
├── 1_3_statistical_service_center
│   └── raw_pdf
│       └── 1_3_statistical_service_center_raw.pdf
├── 1_4_correspondence_whirlwind
│   └── raw_pdf
│       └── 1_4_correspondence_whirlwind_raw.pdf
├── 1_5_whirlwind_time
│   └── raw_pdf
│       └── 1_5_whirlwind_time_raw.pdf
├── 1_6_nsf_proposal
│   └── raw_pdf
│       └── 1_6_nsf_proposal_raw.pdf
├── 1_7_nsf_cor
│   └── raw_pdf
│       └── 1_7_nsf_cor_raw.pdf
├── 1_8_rockefeller
│   └── raw_pdf
│       └── 1_8_rockefeller_raw.pdf
├── 1_9_cc_history_proposals
│   └── raw_pdf
│       └── 1_9_cc_history_proposals_raw.pdf
├── 2_10_bullock_ml_l
│   └── raw_pdf
│       └── 2_10_bullock_m_l_raw.pdf
├── 2_11_c
│   └── raw_pdf
│       └── 2_11_c_raw.pdf
├── 2_12_cc_ceremonies
│   └── raw_pdf
│       └── 2_12_cc_ceremonies_raw.pdf
├── 2_13_cc_memoranda
│   └── raw_pdf
│       └── 2_13_cc_memoranda_raw.pdf
├── 2_14_cc_conferences_reports_rough_drafts
│   └── raw_pdf
│       └── 2_14_cc_conferences_reports_rough_drafts_raw.pdf
├── 2_15_cc_teaching_activities
│   └── raw_pdf
│       └── 2_15_cc_teaching_activities_raw.pdf
├── 2_16_f_j_corbato
│   └── raw_pdf
│       └── 2_16_f_j_corbato_raw.pdf
├── 2_17_d
│   └── raw_pdf
│       └── 2_17_d_raw.pdf
├── 2_18_d_s_r
│   └── raw_pdf
│       └── 2_18_d_s_r_raw.pdf
├── 2_19_e
│   └── raw_pdf
│       └── 2_19_e_raw.pdf
├── 2_1_digital_comp_to_social_problems
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_1_digital_comp_to_social_problems_1.pdf
│   │   │   ├── 2_1_digital_comp_to_social_problems_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_1_digital_comp_to_social_problems_1_1.png
│   │   │       │   └── 2_1_digital_comp_to_social_problems_1_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_1_digital_comp_to_social_problems_1_2.png
│   │   │       │   └── 2_1_digital_comp_to_social_problems_1_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 2_1_digital_comp_to_social_problems_1_3.png
│   │   │       │   └── 2_1_digital_comp_to_social_problems_1_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 2_1_digital_comp_to_social_problems_1_4.png
│   │   │       │   └── 2_1_digital_comp_to_social_problems_1_4.txt
│   │   │       └── 5
│   │   │           ├── 2_1_digital_comp_to_social_problems_1_5.png
│   │   │           └── 2_1_digital_comp_to_social_problems_1_5.txt
│   │   └── 2
│   │       ├── 2_1_digital_comp_to_social_problems_2.pdf
│   │       ├── 2_1_digital_comp_to_social_problems_2.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 2_1_digital_comp_to_social_problems_2_1.png
│   │           │   └── 2_1_digital_comp_to_social_problems_2_1.txt
│   │           ├── 2
│   │           │   ├── 2_1_digital_comp_to_social_problems_2_2.png
│   │           │   └── 2_1_digital_comp_to_social_problems_2_2.txt
│   │           ├── 3
│   │           │   ├── 2_1_digital_comp_to_social_problems_2_3.png
│   │           │   └── 2_1_digital_comp_to_social_problems_2_3.txt
│   │           ├── 4
│   │           │   ├── 2_1_digital_comp_to_social_problems_2_4.png
│   │           │   └── 2_1_digital_comp_to_social_problems_2_4.txt
│   │           └── 5
│   │               ├── 2_1_digital_comp_to_social_problems_2_5.png
│   │               └── 2_1_digital_comp_to_social_problems_2_5.txt
│   └── raw_pdf
│       └── 2_1_digital_comp_to_social_problems_raw.pdf
├── 2_20_ershov_a_p
│   └── raw_pdf
│       └── 2_20_ershov_a_p_raw.pdf
├── 2_21_f
│   └── raw_pdf
│       └── 2_21_f_raw.pdf
├── 2_22_forrester_j_w
│   └── raw_pdf
│       └── 2_22_forrester_j_w_raw.pdf
├── 2_23_h
│   └── raw_pdf
│       └── 2_23_h_raw.pdf
├── 2_24_hildebrand_f_b
│   └── raw_pdf
│       └── 2_24_hildebrand_f_b_raw.pdf
├── 2_25_hunter_g_t
│   └── raw_pdf
│       └── 2_25_hunter_g_t_raw.pdf
├── 2_26_i
│   └── raw_pdf
│       └── 2_26_i_raw.pdf
├── 2_27_ibm_correspondence
│   └── raw_pdf
│       └── 2_27_ibm_correspondence_raw.pdf
├── 2_28_industrial_liaison_office
│   └── raw_pdf
│       └── 2_28_industrial_liason_office_raw.pdf
├── 2_29_j
│   └── raw_pdf
│       └── 2_29_j_raw.pdf
├── 2_2_morse_correspondence_h_l
│   └── raw_pdf
│       └── 2_2_morse_correspondence_h_l_raw.pdf
├── 2_30_r_n_johnson
│   └── raw_pdf
│       └── 2_30_r_n_johnson_raw.pdf
├── 2_3_morse_correspondence_m_z
│   └── raw_pdf
│       └── 2_3_morse_correspondence_m_z_raw.pdf
├── 2_4_a
│   └── 2_4_a_raw.pdf
├── 2_5_morse_correspondence_a_g
│   └── raw_pdf
│       └── 2_5_morse_correspondence_a_g_raw.pdf
├── 2_6_arden_dean
│   └── raw_pdf
│       └── 2_6_arden_dean_raw.pdf
├── 2_7_association_for_computing_machinery
│   └── raw_pdf
│       └── 2_7_association_for_computing_machinery_raw.pdf
├── 2_8_blackburn_j_f
│   └── raw_pdf
│       └── 2_8_blackburn_j_f_raw.pdf
├── 2_9_b
│   └── raw_pdf
│       └── 2_9_b_raw.pdf
├── 3_1_k
│   └── raw_pdf
│       └── 3_1_k_raw.pdf
├── 3_2_korbel_j
│   └── raw_pdf
│       └── 3_2_korbel_j_raw.pdf
├── 3_32_verzuh
│   └── raw_pdf
│       └── 3_32_verzuh_raw.pdf
├── 3_3_l
│   └── raw_pdf
│       └── 3_3_l_raw.pdf
├── 3_4_long_range_comp_study
│   └── raw_pdf
│       └── 3_4_long_range_comp_study_raw.pdf
├── 3_5_m
│   └── raw_pdf
│       └── 3_5_m_raw.pdf
├── 3_6_maine_med_center
│   └── raw_pdf
│       └── 3_6_maine_med_center_raw.pdf
├── 3_7_matill_j_i
│   └── raw_pdf
│       └── 3_7_matill_j_i_raw.pdf
├── 3_8_j_mccarthy
│   └── raw_pdf
│       └── 3_8_j_mccarthy_raw.pdf
└── 3_9_morse_1950_1955
    └── raw_pdf
        └── 3_9_morse_1950_1955_raw.pdf

```
