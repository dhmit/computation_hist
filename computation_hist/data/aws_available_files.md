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
.
├── 1_10_architecture
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_10_architecture_1.pdf
│   │   │   ├── 1_10_architecture_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_1_1.png
│   │   │           └── 1_10_architecture_1_1.txt
│   │   ├── 10
│   │   │   ├── 1_10_architecture_10.pdf
│   │   │   ├── 1_10_architecture_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_10_1.png
│   │   │           └── 1_10_architecture_10_1.txt
│   │   ├── 11
│   │   │   ├── 1_10_architecture_11.pdf
│   │   │   ├── 1_10_architecture_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_11_1.png
│   │   │           └── 1_10_architecture_11_1.txt
│   │   ├── 12
│   │   │   ├── 1_10_architecture_12.pdf
│   │   │   ├── 1_10_architecture_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_12_1.png
│   │   │           └── 1_10_architecture_12_1.txt
│   │   ├── 13
│   │   │   ├── 1_10_architecture_13.pdf
│   │   │   ├── 1_10_architecture_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_13_1.png
│   │   │           └── 1_10_architecture_13_1.txt
│   │   ├── 14
│   │   │   ├── 1_10_architecture_14.pdf
│   │   │   ├── 1_10_architecture_14.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_10_architecture_14_1.png
│   │   │       │   └── 1_10_architecture_14_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_10_architecture_14_2.png
│   │   │       │   └── 1_10_architecture_14_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_10_architecture_14_3.png
│   │   │       │   └── 1_10_architecture_14_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_10_architecture_14_4.png
│   │   │       │   └── 1_10_architecture_14_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_10_architecture_14_5.png
│   │   │       │   └── 1_10_architecture_14_5.txt
│   │   │       └── 6
│   │   │           ├── 1_10_architecture_14_6.png
│   │   │           └── 1_10_architecture_14_6.txt
│   │   ├── 15
│   │   │   ├── 1_10_architecture_15.pdf
│   │   │   ├── 1_10_architecture_15.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_10_architecture_15_1.png
│   │   │       │   └── 1_10_architecture_15_1.txt
│   │   │       └── 2
│   │   │           ├── 1_10_architecture_15_2.png
│   │   │           └── 1_10_architecture_15_2.txt
│   │   ├── 16
│   │   │   ├── 1_10_architecture_16.pdf
│   │   │   ├── 1_10_architecture_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_16_1.png
│   │   │           └── 1_10_architecture_16_1.txt
│   │   ├── 17
│   │   │   ├── 1_10_architecture_17.pdf
│   │   │   ├── 1_10_architecture_17.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_10_architecture_17_1.png
│   │   │       │   └── 1_10_architecture_17_1.txt
│   │   │       └── 2
│   │   │           ├── 1_10_architecture_17_2.png
│   │   │           └── 1_10_architecture_17_2.txt
│   │   ├── 2
│   │   │   ├── 1_10_architecture_2.pdf
│   │   │   ├── 1_10_architecture_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_2_1.png
│   │   │           └── 1_10_architecture_2_1.txt
│   │   ├── 3
│   │   │   ├── 1_10_architecture_3.pdf
│   │   │   ├── 1_10_architecture_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_3_1.png
│   │   │           └── 1_10_architecture_3_1.txt
│   │   ├── 4
│   │   │   ├── 1_10_architecture_4.pdf
│   │   │   ├── 1_10_architecture_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_4_1.png
│   │   │           └── 1_10_architecture_4_1.txt
│   │   ├── 5
│   │   │   ├── 1_10_architecture_5.pdf
│   │   │   ├── 1_10_architecture_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_5_1.png
│   │   │           └── 1_10_architecture_5_1.txt
│   │   ├── 6
│   │   │   ├── 1_10_architecture_6.pdf
│   │   │   ├── 1_10_architecture_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_6_1.png
│   │   │           └── 1_10_architecture_6_1.txt
│   │   ├── 7
│   │   │   ├── 1_10_architecture_7.pdf
│   │   │   ├── 1_10_architecture_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_7_1.png
│   │   │           └── 1_10_architecture_7_1.txt
│   │   ├── 8
│   │   │   ├── 1_10_architecture_8.pdf
│   │   │   ├── 1_10_architecture_8.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_10_architecture_8_1.png
│   │   │           └── 1_10_architecture_8_1.txt
│   │   └── 9
│   │       ├── 1_10_architecture_9.pdf
│   │       ├── 1_10_architecture_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_10_architecture_9_1.png
│   │               └── 1_10_architecture_9_1.txt
│   └── raw_pdf
│       └── 1_10_architecture_raw.pdf
├── 1_11_cc_budget_mit
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_11_cc_budget_mit_1.pdf
│   │   │   ├── 1_11_cc_budget_mit_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_11_cc_budget_mit_1_1.png
│   │   │           └── 1_11_cc_budget_mit_1_1.txt
│   │   ├── 2
│   │   │   ├── 1_11_cc_budget_mit_2.pdf
│   │   │   ├── 1_11_cc_budget_mit_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_11_cc_budget_mit_2_1.png
│   │   │       │   └── 1_11_cc_budget_mit_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_11_cc_budget_mit_2_2.png
│   │   │       │   └── 1_11_cc_budget_mit_2_2.txt
│   │   │       └── 3
│   │   │           ├── 1_11_cc_budget_mit_2_3.png
│   │   │           └── 1_11_cc_budget_mit_2_3.txt
│   │   ├── 3
│   │   │   ├── 1_11_cc_budget_mit_3.pdf
│   │   │   ├── 1_11_cc_budget_mit_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_11_cc_budget_mit_3_1.png
│   │   │       │   └── 1_11_cc_budget_mit_3_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_11_cc_budget_mit_3_2.png
│   │   │       │   └── 1_11_cc_budget_mit_3_2.txt
│   │   │       └── 3
│   │   │           ├── 1_11_cc_budget_mit_3_3.png
│   │   │           └── 1_11_cc_budget_mit_3_3.txt
│   │   └── 4
│   │       ├── 1_11_cc_budget_mit_4.pdf
│   │       ├── 1_11_cc_budget_mit_4.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_11_cc_budget_mit_4_1.png
│   │               └── 1_11_cc_budget_mit_4_1.txt
│   └── raw_pdf
│       └── 1_11_cc_budget_mit_raw.pdf
├── 1_12_cc_budget_nsf
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_12_cc_budget_nsf_1.pdf
│   │   │   ├── 1_12_cc_budget_nsf_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_12_cc_budget_nsf_1_1.png
│   │   │       │   └── 1_12_cc_budget_nsf_1_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_12_cc_budget_nsf_1_2.png
│   │   │       │   └── 1_12_cc_budget_nsf_1_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_12_cc_budget_nsf_1_3.png
│   │   │       │   └── 1_12_cc_budget_nsf_1_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_12_cc_budget_nsf_1_4.png
│   │   │       │   └── 1_12_cc_budget_nsf_1_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_12_cc_budget_nsf_1_5.png
│   │   │       │   └── 1_12_cc_budget_nsf_1_5.txt
│   │   │       └── 6
│   │   │           ├── 1_12_cc_budget_nsf_1_6.png
│   │   │           └── 1_12_cc_budget_nsf_1_6.txt
│   │   └── 2
│   │       ├── 1_12_cc_budget_nsf_2.pdf
│   │       ├── 1_12_cc_budget_nsf_2.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 1_12_cc_budget_nsf_2_1.png
│   │           │   └── 1_12_cc_budget_nsf_2_1.txt
│   │           ├── 2
│   │           │   ├── 1_12_cc_budget_nsf_2_2.png
│   │           │   └── 1_12_cc_budget_nsf_2_2.txt
│   │           ├── 3
│   │           │   ├── 1_12_cc_budget_nsf_2_3.png
│   │           │   └── 1_12_cc_budget_nsf_2_3.txt
│   │           ├── 4
│   │           │   ├── 1_12_cc_budget_nsf_2_4.png
│   │           │   └── 1_12_cc_budget_nsf_2_4.txt
│   │           ├── 5
│   │           │   ├── 1_12_cc_budget_nsf_2_5.png
│   │           │   └── 1_12_cc_budget_nsf_2_5.txt
│   │           ├── 6
│   │           │   ├── 1_12_cc_budget_nsf_2_6.png
│   │           │   └── 1_12_cc_budget_nsf_2_6.txt
│   │           ├── 7
│   │           │   ├── 1_12_cc_budget_nsf_2_7.png
│   │           │   └── 1_12_cc_budget_nsf_2_7.txt
│   │           ├── 8
│   │           │   ├── 1_12_cc_budget_nsf_2_8.png
│   │           │   └── 1_12_cc_budget_nsf_2_8.txt
│   │           └── 9
│   │               ├── 1_12_cc_budget_nsf_2_9.png
│   │               └── 1_12_cc_budget_nsf_2_9.txt
│   └── raw_pdf
│       └── 1_12_cc_budget_nsf_raw.pdf
├── 1_14_cc_dedication
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_14_cc_dedication_1.pdf
│   │   │   ├── 1_14_cc_dedication_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_14_cc_dedication_1_1.png
│   │   │       │   └── 1_14_cc_dedication_1_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_14_cc_dedication_1_2.png
│   │   │       │   └── 1_14_cc_dedication_1_2.txt
│   │   │       └── 3
│   │   │           ├── 1_14_cc_dedication_1_3.png
│   │   │           └── 1_14_cc_dedication_1_3.txt
│   │   ├── 2
│   │   │   ├── 1_14_cc_dedication_2.pdf
│   │   │   ├── 1_14_cc_dedication_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_14_cc_dedication_2_1.png
│   │   │       │   └── 1_14_cc_dedication_2_1.txt
│   │   │       └── 2
│   │   │           ├── 1_14_cc_dedication_2_2.png
│   │   │           └── 1_14_cc_dedication_2_2.txt
│   │   ├── 3
│   │   │   ├── 1_14_cc_dedication_3.pdf
│   │   │   ├── 1_14_cc_dedication_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_14_cc_dedication_3_1.png
│   │   │       │   └── 1_14_cc_dedication_3_1.txt
│   │   │       └── 2
│   │   │           ├── 1_14_cc_dedication_3_2.png
│   │   │           └── 1_14_cc_dedication_3_2.txt
│   │   ├── 4
│   │   │   ├── 1_14_cc_dedication_4.pdf
│   │   │   ├── 1_14_cc_dedication_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_14_cc_dedication_4_1.png
│   │   │       │   └── 1_14_cc_dedication_4_1.txt
│   │   │       └── 2
│   │   │           ├── 1_14_cc_dedication_4_2.png
│   │   │           └── 1_14_cc_dedication_4_2.txt
│   │   └── 5
│   │       ├── 1_14_cc_dedication_5.pdf
│   │       ├── 1_14_cc_dedication_5.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 1_14_cc_dedication_5_1.png
│   │           │   └── 1_14_cc_dedication_5_1.txt
│   │           └── 2
│   │               ├── 1_14_cc_dedication_5_2.png
│   │               └── 1_14_cc_dedication_5_2.txt
│   └── raw_pdf
│       └── 1_14_cc_dedication_raw.pdf
├── 1_15_cc_equip
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_15_cc_equip_1.pdf
│   │   │   ├── 1_15_cc_equip_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_15_cc_equip_1_1.png
│   │   │       │   └── 1_15_cc_equip_1_1.txt
│   │   │       └── 2
│   │   │           ├── 1_15_cc_equip_1_2.png
│   │   │           └── 1_15_cc_equip_1_2.txt
│   │   ├── 10
│   │   │   ├── 1_15_cc_equip_10.pdf
│   │   │   ├── 1_15_cc_equip_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_10_1.png
│   │   │           └── 1_15_cc_equip_10_1.txt
│   │   ├── 11
│   │   │   ├── 1_15_cc_equip_11.pdf
│   │   │   ├── 1_15_cc_equip_11.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_15_cc_equip_11_1.png
│   │   │       │   └── 1_15_cc_equip_11_1.txt
│   │   │       └── 2
│   │   │           ├── 1_15_cc_equip_11_2.png
│   │   │           └── 1_15_cc_equip_11_2.txt
│   │   ├── 12
│   │   │   ├── 1_15_cc_equip_12.pdf
│   │   │   ├── 1_15_cc_equip_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_12_1.png
│   │   │           └── 1_15_cc_equip_12_1.txt
│   │   ├── 13
│   │   │   ├── 1_15_cc_equip_13.pdf
│   │   │   ├── 1_15_cc_equip_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_13_1.png
│   │   │           └── 1_15_cc_equip_13_1.txt
│   │   ├── 14
│   │   │   ├── 1_15_cc_equip_14.pdf
│   │   │   ├── 1_15_cc_equip_14.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_15_cc_equip_14_1.png
│   │   │       │   └── 1_15_cc_equip_14_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_15_cc_equip_14_2.png
│   │   │       │   └── 1_15_cc_equip_14_2.txt
│   │   │       └── 3
│   │   │           ├── 1_15_cc_equip_14_3.png
│   │   │           └── 1_15_cc_equip_14_3.txt
│   │   ├── 15
│   │   │   ├── 1_15_cc_equip_15.pdf
│   │   │   ├── 1_15_cc_equip_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_15_1.png
│   │   │           └── 1_15_cc_equip_15_1.txt
│   │   ├── 16
│   │   │   ├── 1_15_cc_equip_16.pdf
│   │   │   ├── 1_15_cc_equip_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_16_1.png
│   │   │           └── 1_15_cc_equip_16_1.txt
│   │   ├── 17
│   │   │   ├── 1_15_cc_equip_17.pdf
│   │   │   ├── 1_15_cc_equip_17.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_15_cc_equip_17_1.png
│   │   │       │   └── 1_15_cc_equip_17_1.txt
│   │   │       └── 2
│   │   │           ├── 1_15_cc_equip_17_2.png
│   │   │           └── 1_15_cc_equip_17_2.txt
│   │   ├── 18
│   │   │   ├── 1_15_cc_equip_18.pdf
│   │   │   ├── 1_15_cc_equip_18.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_15_cc_equip_18_1.png
│   │   │       │   └── 1_15_cc_equip_18_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_15_cc_equip_18_2.png
│   │   │       │   └── 1_15_cc_equip_18_2.txt
│   │   │       └── 3
│   │   │           ├── 1_15_cc_equip_18_3.png
│   │   │           └── 1_15_cc_equip_18_3.txt
│   │   ├── 19
│   │   │   ├── 1_15_cc_equip_19.pdf
│   │   │   ├── 1_15_cc_equip_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_19_1.png
│   │   │           └── 1_15_cc_equip_19_1.txt
│   │   ├── 2
│   │   │   ├── 1_15_cc_equip_2.pdf
│   │   │   ├── 1_15_cc_equip_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_2_1.png
│   │   │           └── 1_15_cc_equip_2_1.txt
│   │   ├── 20
│   │   │   ├── 1_15_cc_equip_20.pdf
│   │   │   ├── 1_15_cc_equip_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_20_1.png
│   │   │           └── 1_15_cc_equip_20_1.txt
│   │   ├── 21
│   │   │   ├── 1_15_cc_equip_21.pdf
│   │   │   ├── 1_15_cc_equip_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_21_1.png
│   │   │           └── 1_15_cc_equip_21_1.txt
│   │   ├── 22
│   │   │   ├── 1_15_cc_equip_22.pdf
│   │   │   ├── 1_15_cc_equip_22.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_22_1.png
│   │   │           └── 1_15_cc_equip_22_1.txt
│   │   ├── 23
│   │   │   ├── 1_15_cc_equip_23.pdf
│   │   │   ├── 1_15_cc_equip_23.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_23_1.png
│   │   │           └── 1_15_cc_equip_23_1.txt
│   │   ├── 24
│   │   │   ├── 1_15_cc_equip_24.pdf
│   │   │   ├── 1_15_cc_equip_24.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_15_cc_equip_24_1.png
│   │   │       │   └── 1_15_cc_equip_24_1.txt
│   │   │       └── 2
│   │   │           ├── 1_15_cc_equip_24_2.png
│   │   │           └── 1_15_cc_equip_24_2.txt
│   │   ├── 25
│   │   │   ├── 1_15_cc_equip_25.pdf
│   │   │   ├── 1_15_cc_equip_25.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_25_1.png
│   │   │           └── 1_15_cc_equip_25_1.txt
│   │   ├── 26
│   │   │   ├── 1_15_cc_equip_26.pdf
│   │   │   ├── 1_15_cc_equip_26.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_26_1.png
│   │   │           └── 1_15_cc_equip_26_1.txt
│   │   ├── 3
│   │   │   ├── 1_15_cc_equip_3.pdf
│   │   │   ├── 1_15_cc_equip_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_3_1.png
│   │   │           └── 1_15_cc_equip_3_1.txt
│   │   ├── 4
│   │   │   ├── 1_15_cc_equip_4.pdf
│   │   │   ├── 1_15_cc_equip_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_15_cc_equip_4_1.png
│   │   │       │   └── 1_15_cc_equip_4_1.txt
│   │   │       └── 2
│   │   │           ├── 1_15_cc_equip_4_2.png
│   │   │           └── 1_15_cc_equip_4_2.txt
│   │   ├── 5
│   │   │   ├── 1_15_cc_equip_5.pdf
│   │   │   ├── 1_15_cc_equip_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_15_cc_equip_5_1.png
│   │   │       │   └── 1_15_cc_equip_5_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_15_cc_equip_5_2.png
│   │   │       │   └── 1_15_cc_equip_5_2.txt
│   │   │       └── 3
│   │   │           ├── 1_15_cc_equip_5_3.png
│   │   │           └── 1_15_cc_equip_5_3.txt
│   │   ├── 6
│   │   │   ├── 1_15_cc_equip_6.pdf
│   │   │   ├── 1_15_cc_equip_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_6_1.png
│   │   │           └── 1_15_cc_equip_6_1.txt
│   │   ├── 7
│   │   │   ├── 1_15_cc_equip_7.pdf
│   │   │   ├── 1_15_cc_equip_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_15_cc_equip_7_1.png
│   │   │           └── 1_15_cc_equip_7_1.txt
│   │   ├── 8
│   │   │   ├── 1_15_cc_equip_8.pdf
│   │   │   ├── 1_15_cc_equip_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_15_cc_equip_8_1.png
│   │   │       │   └── 1_15_cc_equip_8_1.txt
│   │   │       └── 2
│   │   │           ├── 1_15_cc_equip_8_2.png
│   │   │           └── 1_15_cc_equip_8_2.txt
│   │   └── 9
│   │       ├── 1_15_cc_equip_9.pdf
│   │       ├── 1_15_cc_equip_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_15_cc_equip_9_1.png
│   │               └── 1_15_cc_equip_9_1.txt
│   └── raw_pdf
│       └── 1_15_cc_equip_raw.pdf
├── 1_16_cc_dr_cohn
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_16_cc_dr_cohn_1.pdf
│   │   │   ├── 1_16_cc_dr_cohn_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_16_cc_dr_cohn_1_1.png
│   │   │           └── 1_16_cc_dr_cohn_1_1.txt
│   │   ├── 10
│   │   │   ├── 1_16_cc_dr_cohn_10.pdf
│   │   │   ├── 1_16_cc_dr_cohn_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_10_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_10_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_10_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_10_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_10_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_10_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_16_cc_dr_cohn_10_4.png
│   │   │       │   └── 1_16_cc_dr_cohn_10_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_16_cc_dr_cohn_10_5.png
│   │   │       │   └── 1_16_cc_dr_cohn_10_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_16_cc_dr_cohn_10_6.png
│   │   │       │   └── 1_16_cc_dr_cohn_10_6.txt
│   │   │       └── 7
│   │   │           ├── 1_16_cc_dr_cohn_10_7.png
│   │   │           └── 1_16_cc_dr_cohn_10_7.txt
│   │   ├── 11
│   │   │   ├── 1_16_cc_dr_cohn_11.pdf
│   │   │   ├── 1_16_cc_dr_cohn_11.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_11_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_11_1.txt
│   │   │       └── 2
│   │   │           ├── 1_16_cc_dr_cohn_11_2.png
│   │   │           └── 1_16_cc_dr_cohn_11_2.txt
│   │   ├── 12
│   │   │   ├── 1_16_cc_dr_cohn_12.pdf
│   │   │   ├── 1_16_cc_dr_cohn_12.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_12_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_12_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_12_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_12_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_12_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_12_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_16_cc_dr_cohn_12_4.png
│   │   │       │   └── 1_16_cc_dr_cohn_12_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_16_cc_dr_cohn_12_5.png
│   │   │       │   └── 1_16_cc_dr_cohn_12_5.txt
│   │   │       └── 6
│   │   │           ├── 1_16_cc_dr_cohn_12_6.png
│   │   │           └── 1_16_cc_dr_cohn_12_6.txt
│   │   ├── 13
│   │   │   ├── 1_16_cc_dr_cohn_13.pdf
│   │   │   ├── 1_16_cc_dr_cohn_13.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_13_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_13_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_13_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_13_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_13_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_13_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_16_cc_dr_cohn_13_4.png
│   │   │       │   └── 1_16_cc_dr_cohn_13_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_16_cc_dr_cohn_13_5.png
│   │   │       │   └── 1_16_cc_dr_cohn_13_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_16_cc_dr_cohn_13_6.png
│   │   │       │   └── 1_16_cc_dr_cohn_13_6.txt
│   │   │       └── 7
│   │   │           ├── 1_16_cc_dr_cohn_13_7.png
│   │   │           └── 1_16_cc_dr_cohn_13_7.txt
│   │   ├── 14
│   │   │   ├── 1_16_cc_dr_cohn_14.pdf
│   │   │   ├── 1_16_cc_dr_cohn_14.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_14_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_14_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_14_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_14_2.txt
│   │   │       └── 3
│   │   │           ├── 1_16_cc_dr_cohn_14_3.png
│   │   │           └── 1_16_cc_dr_cohn_14_3.txt
│   │   ├── 15
│   │   │   ├── 1_16_cc_dr_cohn_15.pdf
│   │   │   ├── 1_16_cc_dr_cohn_15.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_15_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_15_1.txt
│   │   │       ├── 10
│   │   │       │   ├── 1_16_cc_dr_cohn_15_10.png
│   │   │       │   └── 1_16_cc_dr_cohn_15_10.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_15_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_15_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_15_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_15_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_16_cc_dr_cohn_15_4.png
│   │   │       │   └── 1_16_cc_dr_cohn_15_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_16_cc_dr_cohn_15_5.png
│   │   │       │   └── 1_16_cc_dr_cohn_15_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_16_cc_dr_cohn_15_6.png
│   │   │       │   └── 1_16_cc_dr_cohn_15_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_16_cc_dr_cohn_15_7.png
│   │   │       │   └── 1_16_cc_dr_cohn_15_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_16_cc_dr_cohn_15_8.png
│   │   │       │   └── 1_16_cc_dr_cohn_15_8.txt
│   │   │       └── 9
│   │   │           ├── 1_16_cc_dr_cohn_15_9.png
│   │   │           └── 1_16_cc_dr_cohn_15_9.txt
│   │   ├── 16
│   │   │   ├── 1_16_cc_dr_cohn_16.pdf
│   │   │   ├── 1_16_cc_dr_cohn_16.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_16_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_16_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_16_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_16_2.txt
│   │   │       └── 3
│   │   │           ├── 1_16_cc_dr_cohn_16_3.png
│   │   │           └── 1_16_cc_dr_cohn_16_3.txt
│   │   ├── 17
│   │   │   ├── 1_16_cc_dr_cohn_17.pdf
│   │   │   ├── 1_16_cc_dr_cohn_17.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_17_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_17_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_17_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_17_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_17_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_17_3.txt
│   │   │       └── 4
│   │   │           ├── 1_16_cc_dr_cohn_17_4.png
│   │   │           └── 1_16_cc_dr_cohn_17_4.txt
│   │   ├── 18
│   │   │   ├── 1_16_cc_dr_cohn_18.pdf
│   │   │   ├── 1_16_cc_dr_cohn_18.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_18_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_18_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_18_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_18_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_18_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_18_3.txt
│   │   │       └── 4
│   │   │           ├── 1_16_cc_dr_cohn_18_4.png
│   │   │           └── 1_16_cc_dr_cohn_18_4.txt
│   │   ├── 19
│   │   │   ├── 1_16_cc_dr_cohn_19.pdf
│   │   │   ├── 1_16_cc_dr_cohn_19.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_19_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_19_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_19_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_19_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_19_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_19_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_16_cc_dr_cohn_19_4.png
│   │   │       │   └── 1_16_cc_dr_cohn_19_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_16_cc_dr_cohn_19_5.png
│   │   │       │   └── 1_16_cc_dr_cohn_19_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_16_cc_dr_cohn_19_6.png
│   │   │       │   └── 1_16_cc_dr_cohn_19_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_16_cc_dr_cohn_19_7.png
│   │   │       │   └── 1_16_cc_dr_cohn_19_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_16_cc_dr_cohn_19_8.png
│   │   │       │   └── 1_16_cc_dr_cohn_19_8.txt
│   │   │       └── 9
│   │   │           ├── 1_16_cc_dr_cohn_19_9.png
│   │   │           └── 1_16_cc_dr_cohn_19_9.txt
│   │   ├── 2
│   │   │   ├── 1_16_cc_dr_cohn_2.pdf
│   │   │   ├── 1_16_cc_dr_cohn_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_16_cc_dr_cohn_2_1.png
│   │   │           └── 1_16_cc_dr_cohn_2_1.txt
│   │   ├── 3
│   │   │   ├── 1_16_cc_dr_cohn_3.pdf
│   │   │   ├── 1_16_cc_dr_cohn_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_3_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_3_1.txt
│   │   │       └── 2
│   │   │           ├── 1_16_cc_dr_cohn_3_2.png
│   │   │           └── 1_16_cc_dr_cohn_3_2.txt
│   │   ├── 4
│   │   │   ├── 1_16_cc_dr_cohn_4.pdf
│   │   │   ├── 1_16_cc_dr_cohn_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_16_cc_dr_cohn_4_1.png
│   │   │           └── 1_16_cc_dr_cohn_4_1.txt
│   │   ├── 5
│   │   │   ├── 1_16_cc_dr_cohn_5.pdf
│   │   │   ├── 1_16_cc_dr_cohn_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_5_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_5_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_5_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_5_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_5_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_5_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_16_cc_dr_cohn_5_4.png
│   │   │       │   └── 1_16_cc_dr_cohn_5_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_16_cc_dr_cohn_5_5.png
│   │   │       │   └── 1_16_cc_dr_cohn_5_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_16_cc_dr_cohn_5_6.png
│   │   │       │   └── 1_16_cc_dr_cohn_5_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_16_cc_dr_cohn_5_7.png
│   │   │       │   └── 1_16_cc_dr_cohn_5_7.txt
│   │   │       └── 8
│   │   │           ├── 1_16_cc_dr_cohn_5_8.png
│   │   │           └── 1_16_cc_dr_cohn_5_8.txt
│   │   ├── 6
│   │   │   ├── 1_16_cc_dr_cohn_6.pdf
│   │   │   ├── 1_16_cc_dr_cohn_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_6_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_6_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_6_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_6_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_6_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_6_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_16_cc_dr_cohn_6_4.png
│   │   │       │   └── 1_16_cc_dr_cohn_6_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_16_cc_dr_cohn_6_5.png
│   │   │       │   └── 1_16_cc_dr_cohn_6_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_16_cc_dr_cohn_6_6.png
│   │   │       │   └── 1_16_cc_dr_cohn_6_6.txt
│   │   │       └── 7
│   │   │           ├── 1_16_cc_dr_cohn_6_7.png
│   │   │           └── 1_16_cc_dr_cohn_6_7.txt
│   │   ├── 7
│   │   │   ├── 1_16_cc_dr_cohn_7.pdf
│   │   │   ├── 1_16_cc_dr_cohn_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_7_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_7_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_7_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_7_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_16_cc_dr_cohn_7_3.png
│   │   │       │   └── 1_16_cc_dr_cohn_7_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_16_cc_dr_cohn_7_4.png
│   │   │       │   └── 1_16_cc_dr_cohn_7_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_16_cc_dr_cohn_7_5.png
│   │   │       │   └── 1_16_cc_dr_cohn_7_5.txt
│   │   │       └── 6
│   │   │           ├── 1_16_cc_dr_cohn_7_6.png
│   │   │           └── 1_16_cc_dr_cohn_7_6.txt
│   │   ├── 8
│   │   │   ├── 1_16_cc_dr_cohn_8.pdf
│   │   │   ├── 1_16_cc_dr_cohn_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_16_cc_dr_cohn_8_1.png
│   │   │       │   └── 1_16_cc_dr_cohn_8_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_16_cc_dr_cohn_8_2.png
│   │   │       │   └── 1_16_cc_dr_cohn_8_2.txt
│   │   │       └── 3
│   │   │           ├── 1_16_cc_dr_cohn_8_3.png
│   │   │           └── 1_16_cc_dr_cohn_8_3.txt
│   │   └── 9
│   │       ├── 1_16_cc_dr_cohn_9.pdf
│   │       ├── 1_16_cc_dr_cohn_9.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 1_16_cc_dr_cohn_9_1.png
│   │           │   └── 1_16_cc_dr_cohn_9_1.txt
│   │           ├── 2
│   │           │   ├── 1_16_cc_dr_cohn_9_2.png
│   │           │   └── 1_16_cc_dr_cohn_9_2.txt
│   │           ├── 3
│   │           │   ├── 1_16_cc_dr_cohn_9_3.png
│   │           │   └── 1_16_cc_dr_cohn_9_3.txt
│   │           ├── 4
│   │           │   ├── 1_16_cc_dr_cohn_9_4.png
│   │           │   └── 1_16_cc_dr_cohn_9_4.txt
│   │           ├── 5
│   │           │   ├── 1_16_cc_dr_cohn_9_5.png
│   │           │   └── 1_16_cc_dr_cohn_9_5.txt
│   │           ├── 6
│   │           │   ├── 1_16_cc_dr_cohn_9_6.png
│   │           │   └── 1_16_cc_dr_cohn_9_6.txt
│   │           ├── 7
│   │           │   ├── 1_16_cc_dr_cohn_9_7.png
│   │           │   └── 1_16_cc_dr_cohn_9_7.txt
│   │           ├── 8
│   │           │   ├── 1_16_cc_dr_cohn_9_8.png
│   │           │   └── 1_16_cc_dr_cohn_9_8.txt
│   │           └── 9
│   │               ├── 1_16_cc_dr_cohn_9_9.png
│   │               └── 1_16_cc_dr_cohn_9_9.txt
│   └── raw_pdf
│       └── 1_16_cc_dr_cohn_raw.pdf
├── 1_19_cc_verzuh
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_19_cc_verzuh_1.pdf
│   │   │   ├── 1_19_cc_verzuh_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_19_cc_verzuh_1_1.png
│   │   │           └── 1_19_cc_verzuh_1_1.txt
│   │   ├── 2
│   │   │   ├── 1_19_cc_verzuh_2.pdf
│   │   │   ├── 1_19_cc_verzuh_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_19_cc_verzuh_2_1.png
│   │   │           └── 1_19_cc_verzuh_2_1.txt
│   │   ├── 3
│   │   │   ├── 1_19_cc_verzuh_3.pdf
│   │   │   ├── 1_19_cc_verzuh_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_19_cc_verzuh_3_1.png
│   │   │       │   └── 1_19_cc_verzuh_3_1.txt
│   │   │       └── 2
│   │   │           ├── 1_19_cc_verzuh_3_2.png
│   │   │           └── 1_19_cc_verzuh_3_2.txt
│   │   ├── 4
│   │   │   ├── 1_19_cc_verzuh_4.pdf
│   │   │   ├── 1_19_cc_verzuh_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_19_cc_verzuh_4_1.png
│   │   │           └── 1_19_cc_verzuh_4_1.txt
│   │   ├── 5
│   │   │   ├── 1_19_cc_verzuh_5.pdf
│   │   │   ├── 1_19_cc_verzuh_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_19_cc_verzuh_5_1.png
│   │   │           └── 1_19_cc_verzuh_5_1.txt
│   │   ├── 6
│   │   │   ├── 1_19_cc_verzuh_6.pdf
│   │   │   ├── 1_19_cc_verzuh_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_19_cc_verzuh_6_1.png
│   │   │           └── 1_19_cc_verzuh_6_1.txt
│   │   └── 7
│   │       ├── 1_19_cc_verzuh_7.pdf
│   │       ├── 1_19_cc_verzuh_7.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_19_cc_verzuh_7_1.png
│   │               └── 1_19_cc_verzuh_7_1.txt
│   └── raw_pdf
│       └── 1_19_cc_verzuh_raw.pdf
├── 1_1_committee_on_machine_methods
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_1_committee_on_machine_methods_1.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_1_1.png
│   │   │           └── 1_1_committee_on_machine_methods_1_1.txt
│   │   ├── 10
│   │   │   ├── 1_1_committee_on_machine_methods_10.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_10_1.png
│   │   │           └── 1_1_committee_on_machine_methods_10_1.txt
│   │   ├── 11
│   │   │   ├── 1_1_committee_on_machine_methods_11.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_11_1.png
│   │   │           └── 1_1_committee_on_machine_methods_11_1.txt
│   │   ├── 12
│   │   │   ├── 1_1_committee_on_machine_methods_12.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_12.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_12_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_12_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_12_2.png
│   │   │           └── 1_1_committee_on_machine_methods_12_2.txt
│   │   ├── 13
│   │   │   ├── 1_1_committee_on_machine_methods_13.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_13_1.png
│   │   │           └── 1_1_committee_on_machine_methods_13_1.txt
│   │   ├── 14
│   │   │   ├── 1_1_committee_on_machine_methods_14.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_14.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_14_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_14_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_14_2.png
│   │   │           └── 1_1_committee_on_machine_methods_14_2.txt
│   │   ├── 15
│   │   │   ├── 1_1_committee_on_machine_methods_15.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_15_1.png
│   │   │           └── 1_1_committee_on_machine_methods_15_1.txt
│   │   ├── 16
│   │   │   ├── 1_1_committee_on_machine_methods_16.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_16_1.png
│   │   │           └── 1_1_committee_on_machine_methods_16_1.txt
│   │   ├── 17
│   │   │   ├── 1_1_committee_on_machine_methods_17.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_17.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_17_1.png
│   │   │           └── 1_1_committee_on_machine_methods_17_1.txt
│   │   ├── 18
│   │   │   ├── 1_1_committee_on_machine_methods_18.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_18_1.png
│   │   │           └── 1_1_committee_on_machine_methods_18_1.txt
│   │   ├── 19
│   │   │   ├── 1_1_committee_on_machine_methods_19.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_19_1.png
│   │   │           └── 1_1_committee_on_machine_methods_19_1.txt
│   │   ├── 2
│   │   │   ├── 1_1_committee_on_machine_methods_2.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_2_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_2_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_2_2.png
│   │   │           └── 1_1_committee_on_machine_methods_2_2.txt
│   │   ├── 20
│   │   │   ├── 1_1_committee_on_machine_methods_20.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_20_1.png
│   │   │           └── 1_1_committee_on_machine_methods_20_1.txt
│   │   ├── 21
│   │   │   ├── 1_1_committee_on_machine_methods_21.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_21_1.png
│   │   │           └── 1_1_committee_on_machine_methods_21_1.txt
│   │   ├── 22
│   │   │   ├── 1_1_committee_on_machine_methods_22.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_22.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_22_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_22_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_22_2.png
│   │   │           └── 1_1_committee_on_machine_methods_22_2.txt
│   │   ├── 23
│   │   │   ├── 1_1_committee_on_machine_methods_23.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_23.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_23_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_23_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_23_2.png
│   │   │           └── 1_1_committee_on_machine_methods_23_2.txt
│   │   ├── 24
│   │   │   ├── 1_1_committee_on_machine_methods_24.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_24.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_24_1.png
│   │   │           └── 1_1_committee_on_machine_methods_24_1.txt
│   │   ├── 25
│   │   │   ├── 1_1_committee_on_machine_methods_25.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_25.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_25_1.png
│   │   │           └── 1_1_committee_on_machine_methods_25_1.txt
│   │   ├── 26
│   │   │   ├── 1_1_committee_on_machine_methods_26.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_26.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_26_1.png
│   │   │           └── 1_1_committee_on_machine_methods_26_1.txt
│   │   ├── 27
│   │   │   ├── 1_1_committee_on_machine_methods_27.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_27.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_27_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_27_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_1_committee_on_machine_methods_27_2.png
│   │   │       │   └── 1_1_committee_on_machine_methods_27_2.txt
│   │   │       └── 3
│   │   │           ├── 1_1_committee_on_machine_methods_27_3.png
│   │   │           └── 1_1_committee_on_machine_methods_27_3.txt
│   │   ├── 28
│   │   │   ├── 1_1_committee_on_machine_methods_28.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_28.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_28_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_28_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_28_2.png
│   │   │           └── 1_1_committee_on_machine_methods_28_2.txt
│   │   ├── 29
│   │   │   ├── 1_1_committee_on_machine_methods_29.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_29.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_29_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_29_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_29_2.png
│   │   │           └── 1_1_committee_on_machine_methods_29_2.txt
│   │   ├── 3
│   │   │   ├── 1_1_committee_on_machine_methods_3.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_3_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_3_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_3_2.png
│   │   │           └── 1_1_committee_on_machine_methods_3_2.txt
│   │   ├── 30
│   │   │   ├── 1_1_committee_on_machine_methods_30.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_30.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_30_1.png
│   │   │           └── 1_1_committee_on_machine_methods_30_1.txt
│   │   ├── 31
│   │   │   ├── 1_1_committee_on_machine_methods_31.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_31.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_31_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_31_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_31_2.png
│   │   │           └── 1_1_committee_on_machine_methods_31_2.txt
│   │   ├── 32
│   │   │   ├── 1_1_committee_on_machine_methods_32.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_32.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_32_1.png
│   │   │           └── 1_1_committee_on_machine_methods_32_1.txt
│   │   ├── 33
│   │   │   ├── 1_1_committee_on_machine_methods_33.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_33.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_33_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_33_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_33_2.png
│   │   │           └── 1_1_committee_on_machine_methods_33_2.txt
│   │   ├── 34
│   │   │   ├── 1_1_committee_on_machine_methods_34.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_34.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_34_1.png
│   │   │           └── 1_1_committee_on_machine_methods_34_1.txt
│   │   ├── 35
│   │   │   ├── 1_1_committee_on_machine_methods_35.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_35.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_35_1.png
│   │   │           └── 1_1_committee_on_machine_methods_35_1.txt
│   │   ├── 36
│   │   │   ├── 1_1_committee_on_machine_methods_36.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_36.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_36_1.png
│   │   │           └── 1_1_committee_on_machine_methods_36_1.txt
│   │   ├── 37
│   │   │   ├── 1_1_committee_on_machine_methods_37.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_37.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_37_1.png
│   │   │           └── 1_1_committee_on_machine_methods_37_1.txt
│   │   ├── 38
│   │   │   ├── 1_1_committee_on_machine_methods_38.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_38.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_38_1.png
│   │   │           └── 1_1_committee_on_machine_methods_38_1.txt
│   │   ├── 39
│   │   │   ├── 1_1_committee_on_machine_methods_39.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_39.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_39_1.png
│   │   │           └── 1_1_committee_on_machine_methods_39_1.txt
│   │   ├── 4
│   │   │   ├── 1_1_committee_on_machine_methods_4.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_4_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_4_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_4_2.png
│   │   │           └── 1_1_committee_on_machine_methods_4_2.txt
│   │   ├── 40
│   │   │   ├── 1_1_committee_on_machine_methods_40.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_40.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_40_1.png
│   │   │           └── 1_1_committee_on_machine_methods_40_1.txt
│   │   ├── 41
│   │   │   ├── 1_1_committee_on_machine_methods_41.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_41.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_41_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_41_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_41_2.png
│   │   │           └── 1_1_committee_on_machine_methods_41_2.txt
│   │   ├── 42
│   │   │   ├── 1_1_committee_on_machine_methods_42.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_42.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_42_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_42_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_42_2.png
│   │   │           └── 1_1_committee_on_machine_methods_42_2.txt
│   │   ├── 43
│   │   │   ├── 1_1_committee_on_machine_methods_43.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_43.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_43_1.png
│   │   │           └── 1_1_committee_on_machine_methods_43_1.txt
│   │   ├── 44
│   │   │   ├── 1_1_committee_on_machine_methods_44.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_44.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_44_1.png
│   │   │           └── 1_1_committee_on_machine_methods_44_1.txt
│   │   ├── 45
│   │   │   ├── 1_1_committee_on_machine_methods_45.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_45.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_45_1.png
│   │   │           └── 1_1_committee_on_machine_methods_45_1.txt
│   │   ├── 46
│   │   │   ├── 1_1_committee_on_machine_methods_46.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_46.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_46_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_46_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_1_committee_on_machine_methods_46_2.png
│   │   │       │   └── 1_1_committee_on_machine_methods_46_2.txt
│   │   │       └── 3
│   │   │           ├── 1_1_committee_on_machine_methods_46_3.png
│   │   │           └── 1_1_committee_on_machine_methods_46_3.txt
│   │   ├── 47
│   │   │   ├── 1_1_committee_on_machine_methods_47.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_47.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_47_1.png
│   │   │           └── 1_1_committee_on_machine_methods_47_1.txt
│   │   ├── 48
│   │   │   ├── 1_1_committee_on_machine_methods_48.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_48.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_48_1.png
│   │   │           └── 1_1_committee_on_machine_methods_48_1.txt
│   │   ├── 49
│   │   │   ├── 1_1_committee_on_machine_methods_49.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_49.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_1_committee_on_machine_methods_49_1.png
│   │   │           └── 1_1_committee_on_machine_methods_49_1.txt
│   │   ├── 5
│   │   │   ├── 1_1_committee_on_machine_methods_5.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_5_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_5_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_5_2.png
│   │   │           └── 1_1_committee_on_machine_methods_5_2.txt
│   │   ├── 6
│   │   │   ├── 1_1_committee_on_machine_methods_6.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_6_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_6_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_6_2.png
│   │   │           └── 1_1_committee_on_machine_methods_6_2.txt
│   │   ├── 7
│   │   │   ├── 1_1_committee_on_machine_methods_7.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_7_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_7_1.txt
│   │   │       └── 2
│   │   │           ├── 1_1_committee_on_machine_methods_7_2.png
│   │   │           └── 1_1_committee_on_machine_methods_7_2.txt
│   │   ├── 8
│   │   │   ├── 1_1_committee_on_machine_methods_8.pdf
│   │   │   ├── 1_1_committee_on_machine_methods_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_1_committee_on_machine_methods_8_1.png
│   │   │       │   └── 1_1_committee_on_machine_methods_8_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_1_committee_on_machine_methods_8_2.png
│   │   │       │   └── 1_1_committee_on_machine_methods_8_2.txt
│   │   │       └── 3
│   │   │           ├── 1_1_committee_on_machine_methods_8_3.png
│   │   │           └── 1_1_committee_on_machine_methods_8_3.txt
│   │   └── 9
│   │       ├── 1_1_committee_on_machine_methods_9.pdf
│   │       ├── 1_1_committee_on_machine_methods_9.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 1_1_committee_on_machine_methods_9_1.png
│   │           │   └── 1_1_committee_on_machine_methods_9_1.txt
│   │           ├── 2
│   │           │   ├── 1_1_committee_on_machine_methods_9_2.png
│   │           │   └── 1_1_committee_on_machine_methods_9_2.txt
│   │           └── 3
│   │               ├── 1_1_committee_on_machine_methods_9_3.png
│   │               └── 1_1_committee_on_machine_methods_9_3.txt
│   └── raw_pdf
│       └── 1_1_committee_on_machine_methods_raw.pdf
├── 1_20_cc_704_time
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_20_cc_704_time_1.pdf
│   │   │   ├── 1_20_cc_704_time_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_20_cc_704_time_1_1.png
│   │   │       │   └── 1_20_cc_704_time_1_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_20_cc_704_time_1_2.png
│   │   │       │   └── 1_20_cc_704_time_1_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_20_cc_704_time_1_3.png
│   │   │       │   └── 1_20_cc_704_time_1_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_20_cc_704_time_1_4.png
│   │   │       │   └── 1_20_cc_704_time_1_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_20_cc_704_time_1_5.png
│   │   │       │   └── 1_20_cc_704_time_1_5.txt
│   │   │       └── 6
│   │   │           ├── 1_20_cc_704_time_1_6.png
│   │   │           └── 1_20_cc_704_time_1_6.txt
│   │   ├── 10
│   │   │   ├── 1_20_cc_704_time_10.pdf
│   │   │   ├── 1_20_cc_704_time_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_10_1.png
│   │   │           └── 1_20_cc_704_time_10_1.txt
│   │   ├── 11
│   │   │   ├── 1_20_cc_704_time_11.pdf
│   │   │   ├── 1_20_cc_704_time_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_11_1.png
│   │   │           └── 1_20_cc_704_time_11_1.txt
│   │   ├── 12
│   │   │   ├── 1_20_cc_704_time_12.pdf
│   │   │   ├── 1_20_cc_704_time_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_12_1.png
│   │   │           └── 1_20_cc_704_time_12_1.txt
│   │   ├── 13
│   │   │   ├── 1_20_cc_704_time_13.pdf
│   │   │   ├── 1_20_cc_704_time_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_13_1.png
│   │   │           └── 1_20_cc_704_time_13_1.txt
│   │   ├── 14
│   │   │   ├── 1_20_cc_704_time_14.pdf
│   │   │   ├── 1_20_cc_704_time_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_14_1.png
│   │   │           └── 1_20_cc_704_time_14_1.txt
│   │   ├── 15
│   │   │   ├── 1_20_cc_704_time_15.pdf
│   │   │   ├── 1_20_cc_704_time_15.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_20_cc_704_time_15_1.png
│   │   │       │   └── 1_20_cc_704_time_15_1.txt
│   │   │       └── 2
│   │   │           ├── 1_20_cc_704_time_15_2.png
│   │   │           └── 1_20_cc_704_time_15_2.txt
│   │   ├── 16
│   │   │   ├── 1_20_cc_704_time_16.pdf
│   │   │   ├── 1_20_cc_704_time_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_16_1.png
│   │   │           └── 1_20_cc_704_time_16_1.txt
│   │   ├── 17
│   │   │   ├── 1_20_cc_704_time_17.pdf
│   │   │   ├── 1_20_cc_704_time_17.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_17_1.png
│   │   │           └── 1_20_cc_704_time_17_1.txt
│   │   ├── 18
│   │   │   ├── 1_20_cc_704_time_18.pdf
│   │   │   ├── 1_20_cc_704_time_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_18_1.png
│   │   │           └── 1_20_cc_704_time_18_1.txt
│   │   ├── 19
│   │   │   ├── 1_20_cc_704_time_19.pdf
│   │   │   ├── 1_20_cc_704_time_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_19_1.png
│   │   │           └── 1_20_cc_704_time_19_1.txt
│   │   ├── 2
│   │   │   ├── 1_20_cc_704_time_2.pdf
│   │   │   ├── 1_20_cc_704_time_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_20_cc_704_time_2_1.png
│   │   │       │   └── 1_20_cc_704_time_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_20_cc_704_time_2_2.png
│   │   │       │   └── 1_20_cc_704_time_2_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_20_cc_704_time_2_3.png
│   │   │       │   └── 1_20_cc_704_time_2_3.txt
│   │   │       └── 4
│   │   │           ├── 1_20_cc_704_time_2_4.png
│   │   │           └── 1_20_cc_704_time_2_4.txt
│   │   ├── 20
│   │   │   ├── 1_20_cc_704_time_20.pdf
│   │   │   ├── 1_20_cc_704_time_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_20_1.png
│   │   │           └── 1_20_cc_704_time_20_1.txt
│   │   ├── 3
│   │   │   ├── 1_20_cc_704_time_3.pdf
│   │   │   ├── 1_20_cc_704_time_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_3_1.png
│   │   │           └── 1_20_cc_704_time_3_1.txt
│   │   ├── 4
│   │   │   ├── 1_20_cc_704_time_4.pdf
│   │   │   ├── 1_20_cc_704_time_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_4_1.png
│   │   │           └── 1_20_cc_704_time_4_1.txt
│   │   ├── 5
│   │   │   ├── 1_20_cc_704_time_5.pdf
│   │   │   ├── 1_20_cc_704_time_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_5_1.png
│   │   │           └── 1_20_cc_704_time_5_1.txt
│   │   ├── 6
│   │   │   ├── 1_20_cc_704_time_6.pdf
│   │   │   ├── 1_20_cc_704_time_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_20_cc_704_time_6_1.png
│   │   │       │   └── 1_20_cc_704_time_6_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_20_cc_704_time_6_2.png
│   │   │       │   └── 1_20_cc_704_time_6_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_20_cc_704_time_6_3.png
│   │   │       │   └── 1_20_cc_704_time_6_3.txt
│   │   │       └── 4
│   │   │           ├── 1_20_cc_704_time_6_4.png
│   │   │           └── 1_20_cc_704_time_6_4.txt
│   │   ├── 7
│   │   │   ├── 1_20_cc_704_time_7.pdf
│   │   │   ├── 1_20_cc_704_time_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_7_1.png
│   │   │           └── 1_20_cc_704_time_7_1.txt
│   │   ├── 8
│   │   │   ├── 1_20_cc_704_time_8.pdf
│   │   │   ├── 1_20_cc_704_time_8.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_20_cc_704_time_8_1.png
│   │   │           └── 1_20_cc_704_time_8_1.txt
│   │   └── 9
│   │       ├── 1_20_cc_704_time_9.pdf
│   │       ├── 1_20_cc_704_time_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_20_cc_704_time_9_1.png
│   │               └── 1_20_cc_704_time_9_1.txt
│   └── raw_pdf
│       └── 1_20_cc_704_time_raw.pdf
├── 1_27_cc_1960
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_27_cc_1960_1.pdf
│   │   │   ├── 1_27_cc_1960_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_1_1.png
│   │   │       │   └── 1_27_cc_1960_1_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_1_2.png
│   │   │       │   └── 1_27_cc_1960_1_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_27_cc_1960_1_3.png
│   │   │       │   └── 1_27_cc_1960_1_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_27_cc_1960_1_4.png
│   │   │       │   └── 1_27_cc_1960_1_4.txt
│   │   │       └── 5
│   │   │           ├── 1_27_cc_1960_1_5.png
│   │   │           └── 1_27_cc_1960_1_5.txt
│   │   ├── 10
│   │   │   ├── 1_27_cc_1960_10.pdf
│   │   │   ├── 1_27_cc_1960_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_10_1.png
│   │   │       │   └── 1_27_cc_1960_10_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_10_2.png
│   │   │       │   └── 1_27_cc_1960_10_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_27_cc_1960_10_3.png
│   │   │       │   └── 1_27_cc_1960_10_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_27_cc_1960_10_4.png
│   │   │       │   └── 1_27_cc_1960_10_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_27_cc_1960_10_5.png
│   │   │       │   └── 1_27_cc_1960_10_5.txt
│   │   │       └── 6
│   │   │           ├── 1_27_cc_1960_10_6.png
│   │   │           └── 1_27_cc_1960_10_6.txt
│   │   ├── 11
│   │   │   ├── 1_27_cc_1960_11.pdf
│   │   │   ├── 1_27_cc_1960_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_27_cc_1960_11_1.png
│   │   │           └── 1_27_cc_1960_11_1.txt
│   │   ├── 12
│   │   │   ├── 1_27_cc_1960_12.pdf
│   │   │   ├── 1_27_cc_1960_12.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_12_1.png
│   │   │       │   └── 1_27_cc_1960_12_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_12_2.png
│   │   │       │   └── 1_27_cc_1960_12_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_27_cc_1960_12_3.png
│   │   │       │   └── 1_27_cc_1960_12_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_27_cc_1960_12_4.png
│   │   │       │   └── 1_27_cc_1960_12_4.txt
│   │   │       └── 5
│   │   │           ├── 1_27_cc_1960_12_5.png
│   │   │           └── 1_27_cc_1960_12_5.txt
│   │   ├── 13
│   │   │   ├── 1_27_cc_1960_13.pdf
│   │   │   ├── 1_27_cc_1960_13.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_13_1.png
│   │   │       │   └── 1_27_cc_1960_13_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_13_2.png
│   │   │       │   └── 1_27_cc_1960_13_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_27_cc_1960_13_3.png
│   │   │       │   └── 1_27_cc_1960_13_3.txt
│   │   │       └── 4
│   │   │           ├── 1_27_cc_1960_13_4.png
│   │   │           └── 1_27_cc_1960_13_4.txt
│   │   ├── 14
│   │   │   ├── 1_27_cc_1960_14.pdf
│   │   │   ├── 1_27_cc_1960_14.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_14_1.png
│   │   │       │   └── 1_27_cc_1960_14_1.txt
│   │   │       └── 2
│   │   │           ├── 1_27_cc_1960_14_2.png
│   │   │           └── 1_27_cc_1960_14_2.txt
│   │   ├── 15
│   │   │   ├── 1_27_cc_1960_15.pdf
│   │   │   ├── 1_27_cc_1960_15.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_15_1.png
│   │   │       │   └── 1_27_cc_1960_15_1.txt
│   │   │       └── 2
│   │   │           ├── 1_27_cc_1960_15_2.png
│   │   │           └── 1_27_cc_1960_15_2.txt
│   │   ├── 16
│   │   │   ├── 1_27_cc_1960_16.pdf
│   │   │   ├── 1_27_cc_1960_16.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_16_1.png
│   │   │       │   └── 1_27_cc_1960_16_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_16_2.png
│   │   │       │   └── 1_27_cc_1960_16_2.txt
│   │   │       └── 3
│   │   │           ├── 1_27_cc_1960_16_3.png
│   │   │           └── 1_27_cc_1960_16_3.txt
│   │   ├── 2
│   │   │   ├── 1_27_cc_1960_2.pdf
│   │   │   ├── 1_27_cc_1960_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_2_1.png
│   │   │       │   └── 1_27_cc_1960_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_2_2.png
│   │   │       │   └── 1_27_cc_1960_2_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_27_cc_1960_2_3.png
│   │   │       │   └── 1_27_cc_1960_2_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_27_cc_1960_2_4.png
│   │   │       │   └── 1_27_cc_1960_2_4.txt
│   │   │       └── 5
│   │   │           ├── 1_27_cc_1960_2_5.png
│   │   │           └── 1_27_cc_1960_2_5.txt
│   │   ├── 3
│   │   │   ├── 1_27_cc_1960_3.pdf
│   │   │   ├── 1_27_cc_1960_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_3_1.png
│   │   │       │   └── 1_27_cc_1960_3_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_3_2.png
│   │   │       │   └── 1_27_cc_1960_3_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_27_cc_1960_3_3.png
│   │   │       │   └── 1_27_cc_1960_3_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_27_cc_1960_3_4.png
│   │   │       │   └── 1_27_cc_1960_3_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_27_cc_1960_3_5.png
│   │   │       │   └── 1_27_cc_1960_3_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_27_cc_1960_3_6.png
│   │   │       │   └── 1_27_cc_1960_3_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_27_cc_1960_3_7.png
│   │   │       │   └── 1_27_cc_1960_3_7.txt
│   │   │       └── 8
│   │   │           ├── 1_27_cc_1960_3_8.png
│   │   │           └── 1_27_cc_1960_3_8.txt
│   │   ├── 4
│   │   │   ├── 1_27_cc_1960_4.pdf
│   │   │   ├── 1_27_cc_1960_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_4_1.png
│   │   │       │   └── 1_27_cc_1960_4_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_4_2.png
│   │   │       │   └── 1_27_cc_1960_4_2.txt
│   │   │       └── 3
│   │   │           ├── 1_27_cc_1960_4_3.png
│   │   │           └── 1_27_cc_1960_4_3.txt
│   │   ├── 5
│   │   │   ├── 1_27_cc_1960_5.pdf
│   │   │   ├── 1_27_cc_1960_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_5_1.png
│   │   │       │   └── 1_27_cc_1960_5_1.txt
│   │   │       └── 2
│   │   │           ├── 1_27_cc_1960_5_2.png
│   │   │           └── 1_27_cc_1960_5_2.txt
│   │   ├── 6
│   │   │   ├── 1_27_cc_1960_6.pdf
│   │   │   ├── 1_27_cc_1960_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_6_1.png
│   │   │       │   └── 1_27_cc_1960_6_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_6_2.png
│   │   │       │   └── 1_27_cc_1960_6_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_27_cc_1960_6_3.png
│   │   │       │   └── 1_27_cc_1960_6_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_27_cc_1960_6_4.png
│   │   │       │   └── 1_27_cc_1960_6_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_27_cc_1960_6_5.png
│   │   │       │   └── 1_27_cc_1960_6_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_27_cc_1960_6_6.png
│   │   │       │   └── 1_27_cc_1960_6_6.txt
│   │   │       └── 7
│   │   │           ├── 1_27_cc_1960_6_7.png
│   │   │           └── 1_27_cc_1960_6_7.txt
│   │   ├── 7
│   │   │   ├── 1_27_cc_1960_7.pdf
│   │   │   ├── 1_27_cc_1960_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_7_1.png
│   │   │       │   └── 1_27_cc_1960_7_1.txt
│   │   │       └── 2
│   │   │           ├── 1_27_cc_1960_7_2.png
│   │   │           └── 1_27_cc_1960_7_2.txt
│   │   ├── 8
│   │   │   ├── 1_27_cc_1960_8.pdf
│   │   │   ├── 1_27_cc_1960_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_27_cc_1960_8_1.png
│   │   │       │   └── 1_27_cc_1960_8_1.txt
│   │   │       ├── 10
│   │   │       │   ├── 1_27_cc_1960_8_10.png
│   │   │       │   └── 1_27_cc_1960_8_10.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_27_cc_1960_8_2.png
│   │   │       │   └── 1_27_cc_1960_8_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_27_cc_1960_8_3.png
│   │   │       │   └── 1_27_cc_1960_8_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_27_cc_1960_8_4.png
│   │   │       │   └── 1_27_cc_1960_8_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_27_cc_1960_8_5.png
│   │   │       │   └── 1_27_cc_1960_8_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_27_cc_1960_8_6.png
│   │   │       │   └── 1_27_cc_1960_8_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_27_cc_1960_8_7.png
│   │   │       │   └── 1_27_cc_1960_8_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_27_cc_1960_8_8.png
│   │   │       │   └── 1_27_cc_1960_8_8.txt
│   │   │       └── 9
│   │   │           ├── 1_27_cc_1960_8_9.png
│   │   │           └── 1_27_cc_1960_8_9.txt
│   │   └── 9
│   │       ├── 1_27_cc_1960_9.pdf
│   │       ├── 1_27_cc_1960_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_27_cc_1960_9_1.png
│   │               └── 1_27_cc_1960_9_1.txt
│   └── raw_pdf
│       └── 1_27_cc_1960_raw.pdf
├── 1_2_project_proposal_contract
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_2_project_proposal_contract_1.pdf
│   │   │   ├── 1_2_project_proposal_contract_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_1_1.png
│   │   │       │   └── 1_2_project_proposal_contract_1_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_1_2.png
│   │   │       │   └── 1_2_project_proposal_contract_1_2.txt
│   │   │       └── 3
│   │   │           ├── 1_2_project_proposal_contract_1_3.png
│   │   │           └── 1_2_project_proposal_contract_1_3.txt
│   │   ├── 10
│   │   │   ├── 1_2_project_proposal_contract_10.pdf
│   │   │   ├── 1_2_project_proposal_contract_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_10_1.png
│   │   │       │   └── 1_2_project_proposal_contract_10_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_10_2.png
│   │   │       │   └── 1_2_project_proposal_contract_10_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_2_project_proposal_contract_10_3.png
│   │   │       │   └── 1_2_project_proposal_contract_10_3.txt
│   │   │       └── 4
│   │   │           ├── 1_2_project_proposal_contract_10_4.png
│   │   │           └── 1_2_project_proposal_contract_10_4.txt
│   │   ├── 11
│   │   │   ├── 1_2_project_proposal_contract_11.pdf
│   │   │   ├── 1_2_project_proposal_contract_11.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_11_1.png
│   │   │       │   └── 1_2_project_proposal_contract_11_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_11_2.png
│   │   │       │   └── 1_2_project_proposal_contract_11_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_2_project_proposal_contract_11_3.png
│   │   │       │   └── 1_2_project_proposal_contract_11_3.txt
│   │   │       └── 4
│   │   │           ├── 1_2_project_proposal_contract_11_4.png
│   │   │           └── 1_2_project_proposal_contract_11_4.txt
│   │   ├── 12
│   │   │   ├── 1_2_project_proposal_contract_12.pdf
│   │   │   ├── 1_2_project_proposal_contract_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_12_1.png
│   │   │           └── 1_2_project_proposal_contract_12_1.txt
│   │   ├── 13
│   │   │   ├── 1_2_project_proposal_contract_13.pdf
│   │   │   ├── 1_2_project_proposal_contract_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_13_1.png
│   │   │           └── 1_2_project_proposal_contract_13_1.txt
│   │   ├── 14
│   │   │   ├── 1_2_project_proposal_contract_14.pdf
│   │   │   ├── 1_2_project_proposal_contract_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_14_1.png
│   │   │           └── 1_2_project_proposal_contract_14_1.txt
│   │   ├── 15
│   │   │   ├── 1_2_project_proposal_contract_15.pdf
│   │   │   ├── 1_2_project_proposal_contract_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_15_1.png
│   │   │           └── 1_2_project_proposal_contract_15_1.txt
│   │   ├── 16
│   │   │   ├── 1_2_project_proposal_contract_16.pdf
│   │   │   ├── 1_2_project_proposal_contract_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_16_1.png
│   │   │           └── 1_2_project_proposal_contract_16_1.txt
│   │   ├── 17
│   │   │   ├── 1_2_project_proposal_contract_17.pdf
│   │   │   ├── 1_2_project_proposal_contract_17.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_17_1.png
│   │   │       │   └── 1_2_project_proposal_contract_17_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_17_2.png
│   │   │       │   └── 1_2_project_proposal_contract_17_2.txt
│   │   │       └── 3
│   │   │           ├── 1_2_project_proposal_contract_17_3.png
│   │   │           └── 1_2_project_proposal_contract_17_3.txt
│   │   ├── 18
│   │   │   ├── 1_2_project_proposal_contract_18.pdf
│   │   │   ├── 1_2_project_proposal_contract_18.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_18_1.png
│   │   │       │   └── 1_2_project_proposal_contract_18_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_18_2.png
│   │   │       │   └── 1_2_project_proposal_contract_18_2.txt
│   │   │       └── 3
│   │   │           ├── 1_2_project_proposal_contract_18_3.png
│   │   │           └── 1_2_project_proposal_contract_18_3.txt
│   │   ├── 19
│   │   │   ├── 1_2_project_proposal_contract_19.pdf
│   │   │   ├── 1_2_project_proposal_contract_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_19_1.png
│   │   │           └── 1_2_project_proposal_contract_19_1.txt
│   │   ├── 2
│   │   │   ├── 1_2_project_proposal_contract_2.pdf
│   │   │   ├── 1_2_project_proposal_contract_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_2_1.png
│   │   │       │   └── 1_2_project_proposal_contract_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_2_2.png
│   │   │       │   └── 1_2_project_proposal_contract_2_2.txt
│   │   │       └── 3
│   │   │           ├── 1_2_project_proposal_contract_2_3.png
│   │   │           └── 1_2_project_proposal_contract_2_3.txt
│   │   ├── 20
│   │   │   ├── 1_2_project_proposal_contract_20.pdf
│   │   │   ├── 1_2_project_proposal_contract_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_20_1.png
│   │   │           └── 1_2_project_proposal_contract_20_1.txt
│   │   ├── 21
│   │   │   ├── 1_2_project_proposal_contract_21.pdf
│   │   │   ├── 1_2_project_proposal_contract_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_21_1.png
│   │   │           └── 1_2_project_proposal_contract_21_1.txt
│   │   ├── 22
│   │   │   ├── 1_2_project_proposal_contract_22.pdf
│   │   │   ├── 1_2_project_proposal_contract_22.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_22_1.png
│   │   │           └── 1_2_project_proposal_contract_22_1.txt
│   │   ├── 23
│   │   │   ├── 1_2_project_proposal_contract_23.pdf
│   │   │   ├── 1_2_project_proposal_contract_23.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_23_1.png
│   │   │       │   └── 1_2_project_proposal_contract_23_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_23_2.png
│   │   │           └── 1_2_project_proposal_contract_23_2.txt
│   │   ├── 24
│   │   │   ├── 1_2_project_proposal_contract_24.pdf
│   │   │   ├── 1_2_project_proposal_contract_24.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_24_1.png
│   │   │       │   └── 1_2_project_proposal_contract_24_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_24_2.png
│   │   │           └── 1_2_project_proposal_contract_24_2.txt
│   │   ├── 25
│   │   │   ├── 1_2_project_proposal_contract_25.pdf
│   │   │   ├── 1_2_project_proposal_contract_25.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_25_1.png
│   │   │       │   └── 1_2_project_proposal_contract_25_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_25_2.png
│   │   │           └── 1_2_project_proposal_contract_25_2.txt
│   │   ├── 26
│   │   │   ├── 1_2_project_proposal_contract_26.pdf
│   │   │   ├── 1_2_project_proposal_contract_26.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_26_1.png
│   │   │       │   └── 1_2_project_proposal_contract_26_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_26_2.png
│   │   │           └── 1_2_project_proposal_contract_26_2.txt
│   │   ├── 27
│   │   │   ├── 1_2_project_proposal_contract_27.pdf
│   │   │   ├── 1_2_project_proposal_contract_27.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_27_1.png
│   │   │       │   └── 1_2_project_proposal_contract_27_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_27_2.png
│   │   │           └── 1_2_project_proposal_contract_27_2.txt
│   │   ├── 28
│   │   │   ├── 1_2_project_proposal_contract_28.pdf
│   │   │   ├── 1_2_project_proposal_contract_28.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_28_1.png
│   │   │       │   └── 1_2_project_proposal_contract_28_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_28_2.png
│   │   │           └── 1_2_project_proposal_contract_28_2.txt
│   │   ├── 29
│   │   │   ├── 1_2_project_proposal_contract_29.pdf
│   │   │   ├── 1_2_project_proposal_contract_29.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_29_1.png
│   │   │       │   └── 1_2_project_proposal_contract_29_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_29_2.png
│   │   │           └── 1_2_project_proposal_contract_29_2.txt
│   │   ├── 3
│   │   │   ├── 1_2_project_proposal_contract_3.pdf
│   │   │   ├── 1_2_project_proposal_contract_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_3_1.png
│   │   │           └── 1_2_project_proposal_contract_3_1.txt
│   │   ├── 30
│   │   │   ├── 1_2_project_proposal_contract_30.pdf
│   │   │   ├── 1_2_project_proposal_contract_30.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_30_1.png
│   │   │           └── 1_2_project_proposal_contract_30_1.txt
│   │   ├── 31
│   │   │   ├── 1_2_project_proposal_contract_31.pdf
│   │   │   ├── 1_2_project_proposal_contract_31.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_31_1.png
│   │   │           └── 1_2_project_proposal_contract_31_1.txt
│   │   ├── 32
│   │   │   ├── 1_2_project_proposal_contract_32.pdf
│   │   │   ├── 1_2_project_proposal_contract_32.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_32_1.png
│   │   │       │   └── 1_2_project_proposal_contract_32_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_32_2.png
│   │   │           └── 1_2_project_proposal_contract_32_2.txt
│   │   ├── 33
│   │   │   ├── 1_2_project_proposal_contract_33.pdf
│   │   │   ├── 1_2_project_proposal_contract_33.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_33_1.png
│   │   │           └── 1_2_project_proposal_contract_33_1.txt
│   │   ├── 34
│   │   │   ├── 1_2_project_proposal_contract_34.pdf
│   │   │   ├── 1_2_project_proposal_contract_34.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_34_1.png
│   │   │           └── 1_2_project_proposal_contract_34_1.txt
│   │   ├── 35
│   │   │   ├── 1_2_project_proposal_contract_35.pdf
│   │   │   ├── 1_2_project_proposal_contract_35.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_35_1.png
│   │   │       │   └── 1_2_project_proposal_contract_35_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_35_2.png
│   │   │           └── 1_2_project_proposal_contract_35_2.txt
│   │   ├── 36
│   │   │   ├── 1_2_project_proposal_contract_36.pdf
│   │   │   ├── 1_2_project_proposal_contract_36.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_36_1.png
│   │   │           └── 1_2_project_proposal_contract_36_1.txt
│   │   ├── 37
│   │   │   ├── 1_2_project_proposal_contract_37.pdf
│   │   │   ├── 1_2_project_proposal_contract_37.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_37_1.png
│   │   │           └── 1_2_project_proposal_contract_37_1.txt
│   │   ├── 38
│   │   │   ├── 1_2_project_proposal_contract_38.pdf
│   │   │   ├── 1_2_project_proposal_contract_38.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_38_1.png
│   │   │           └── 1_2_project_proposal_contract_38_1.txt
│   │   ├── 39
│   │   │   ├── 1_2_project_proposal_contract_39.pdf
│   │   │   ├── 1_2_project_proposal_contract_39.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_39_1.png
│   │   │           └── 1_2_project_proposal_contract_39_1.txt
│   │   ├── 4
│   │   │   ├── 1_2_project_proposal_contract_4.pdf
│   │   │   ├── 1_2_project_proposal_contract_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_4_1.png
│   │   │       │   └── 1_2_project_proposal_contract_4_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_4_2.png
│   │   │       │   └── 1_2_project_proposal_contract_4_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_2_project_proposal_contract_4_3.png
│   │   │       │   └── 1_2_project_proposal_contract_4_3.txt
│   │   │       └── 4
│   │   │           ├── 1_2_project_proposal_contract_4_4.png
│   │   │           └── 1_2_project_proposal_contract_4_4.txt
│   │   ├── 40
│   │   │   ├── 1_2_project_proposal_contract_40.pdf
│   │   │   ├── 1_2_project_proposal_contract_40.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_40_1.png
│   │   │           └── 1_2_project_proposal_contract_40_1.txt
│   │   ├── 41
│   │   │   ├── 1_2_project_proposal_contract_41.pdf
│   │   │   ├── 1_2_project_proposal_contract_41.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_41_1.png
│   │   │       │   └── 1_2_project_proposal_contract_41_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_41_2.png
│   │   │           └── 1_2_project_proposal_contract_41_2.txt
│   │   ├── 42
│   │   │   ├── 1_2_project_proposal_contract_42.pdf
│   │   │   ├── 1_2_project_proposal_contract_42.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_42_1.png
│   │   │       │   └── 1_2_project_proposal_contract_42_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_42_2.png
│   │   │           └── 1_2_project_proposal_contract_42_2.txt
│   │   ├── 43
│   │   │   ├── 1_2_project_proposal_contract_43.pdf
│   │   │   ├── 1_2_project_proposal_contract_43.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_43_1.png
│   │   │       │   └── 1_2_project_proposal_contract_43_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_43_2.png
│   │   │           └── 1_2_project_proposal_contract_43_2.txt
│   │   ├── 44
│   │   │   ├── 1_2_project_proposal_contract_44.pdf
│   │   │   ├── 1_2_project_proposal_contract_44.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_44_1.png
│   │   │       │   └── 1_2_project_proposal_contract_44_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_44_2.png
│   │   │           └── 1_2_project_proposal_contract_44_2.txt
│   │   ├── 45
│   │   │   ├── 1_2_project_proposal_contract_45.pdf
│   │   │   ├── 1_2_project_proposal_contract_45.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_45_1.png
│   │   │       │   └── 1_2_project_proposal_contract_45_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_45_2.png
│   │   │           └── 1_2_project_proposal_contract_45_2.txt
│   │   ├── 46
│   │   │   ├── 1_2_project_proposal_contract_46.pdf
│   │   │   ├── 1_2_project_proposal_contract_46.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_46_1.png
│   │   │       │   └── 1_2_project_proposal_contract_46_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_46_2.png
│   │   │       │   └── 1_2_project_proposal_contract_46_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_2_project_proposal_contract_46_3.png
│   │   │       │   └── 1_2_project_proposal_contract_46_3.txt
│   │   │       └── 4
│   │   │           ├── 1_2_project_proposal_contract_46_4.png
│   │   │           └── 1_2_project_proposal_contract_46_4.txt
│   │   ├── 47
│   │   │   ├── 1_2_project_proposal_contract_47.pdf
│   │   │   ├── 1_2_project_proposal_contract_47.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_47_1.png
│   │   │           └── 1_2_project_proposal_contract_47_1.txt
│   │   ├── 48
│   │   │   ├── 1_2_project_proposal_contract_48.pdf
│   │   │   ├── 1_2_project_proposal_contract_48.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_48_1.png
│   │   │           └── 1_2_project_proposal_contract_48_1.txt
│   │   ├── 49
│   │   │   ├── 1_2_project_proposal_contract_49.pdf
│   │   │   ├── 1_2_project_proposal_contract_49.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_49_1.png
│   │   │       │   └── 1_2_project_proposal_contract_49_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_49_2.png
│   │   │       │   └── 1_2_project_proposal_contract_49_2.txt
│   │   │       └── 3
│   │   │           ├── 1_2_project_proposal_contract_49_3.png
│   │   │           └── 1_2_project_proposal_contract_49_3.txt
│   │   ├── 5
│   │   │   ├── 1_2_project_proposal_contract_5.pdf
│   │   │   ├── 1_2_project_proposal_contract_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_5_1.png
│   │   │           └── 1_2_project_proposal_contract_5_1.txt
│   │   ├── 50
│   │   │   ├── 1_2_project_proposal_contract_50.pdf
│   │   │   ├── 1_2_project_proposal_contract_50.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_50_1.png
│   │   │           └── 1_2_project_proposal_contract_50_1.txt
│   │   ├── 51
│   │   │   ├── 1_2_project_proposal_contract_51.pdf
│   │   │   ├── 1_2_project_proposal_contract_51.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_51_1.png
│   │   │           └── 1_2_project_proposal_contract_51_1.txt
│   │   ├── 52
│   │   │   ├── 1_2_project_proposal_contract_52.pdf
│   │   │   ├── 1_2_project_proposal_contract_52.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_52_1.png
│   │   │       │   └── 1_2_project_proposal_contract_52_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_2_project_proposal_contract_52_2.png
│   │   │       │   └── 1_2_project_proposal_contract_52_2.txt
│   │   │       └── 3
│   │   │           ├── 1_2_project_proposal_contract_52_3.png
│   │   │           └── 1_2_project_proposal_contract_52_3.txt
│   │   ├── 53
│   │   │   ├── 1_2_project_proposal_contract_53.pdf
│   │   │   ├── 1_2_project_proposal_contract_53.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_53_1.png
│   │   │           └── 1_2_project_proposal_contract_53_1.txt
│   │   ├── 54
│   │   │   ├── 1_2_project_proposal_contract_54.pdf
│   │   │   ├── 1_2_project_proposal_contract_54.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_54_1.png
│   │   │           └── 1_2_project_proposal_contract_54_1.txt
│   │   ├── 6
│   │   │   ├── 1_2_project_proposal_contract_6.pdf
│   │   │   ├── 1_2_project_proposal_contract_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_6_1.png
│   │   │           └── 1_2_project_proposal_contract_6_1.txt
│   │   ├── 7
│   │   │   ├── 1_2_project_proposal_contract_7.pdf
│   │   │   ├── 1_2_project_proposal_contract_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_2_project_proposal_contract_7_1.png
│   │   │           └── 1_2_project_proposal_contract_7_1.txt
│   │   ├── 8
│   │   │   ├── 1_2_project_proposal_contract_8.pdf
│   │   │   ├── 1_2_project_proposal_contract_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_2_project_proposal_contract_8_1.png
│   │   │       │   └── 1_2_project_proposal_contract_8_1.txt
│   │   │       └── 2
│   │   │           ├── 1_2_project_proposal_contract_8_2.png
│   │   │           └── 1_2_project_proposal_contract_8_2.txt
│   │   └── 9
│   │       ├── 1_2_project_proposal_contract_9.pdf
│   │       ├── 1_2_project_proposal_contract_9.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 1_2_project_proposal_contract_9_1.png
│   │           │   └── 1_2_project_proposal_contract_9_1.txt
│   │           ├── 2
│   │           │   ├── 1_2_project_proposal_contract_9_2.png
│   │           │   └── 1_2_project_proposal_contract_9_2.txt
│   │           ├── 3
│   │           │   ├── 1_2_project_proposal_contract_9_3.png
│   │           │   └── 1_2_project_proposal_contract_9_3.txt
│   │           ├── 4
│   │           │   ├── 1_2_project_proposal_contract_9_4.png
│   │           │   └── 1_2_project_proposal_contract_9_4.txt
│   │           ├── 5
│   │           │   ├── 1_2_project_proposal_contract_9_5.png
│   │           │   └── 1_2_project_proposal_contract_9_5.txt
│   │           ├── 6
│   │           │   ├── 1_2_project_proposal_contract_9_6.png
│   │           │   └── 1_2_project_proposal_contract_9_6.txt
│   │           └── 7
│   │               ├── 1_2_project_proposal_contract_9_7.png
│   │               └── 1_2_project_proposal_contract_9_7.txt
│   └── raw_pdf
│       └── 1_2_project_proposal_contract_raw.pdf
├── 1_30_cc_time_1959_1962
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_30_cc_time_1959_1962_1.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_30_cc_time_1959_1962_1_1.png
│   │   │           └── 1_30_cc_time_1959_1962_1_1.txt
│   │   ├── 10
│   │   │   ├── 1_30_cc_time_1959_1962_10.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_10_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_10_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_10_2.png
│   │   │           └── 1_30_cc_time_1959_1962_10_2.txt
│   │   ├── 11
│   │   │   ├── 1_30_cc_time_1959_1962_11.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_11.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_11_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_11_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_11_2.png
│   │   │           └── 1_30_cc_time_1959_1962_11_2.txt
│   │   ├── 12
│   │   │   ├── 1_30_cc_time_1959_1962_12.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_12.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_12_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_12_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_12_2.png
│   │   │           └── 1_30_cc_time_1959_1962_12_2.txt
│   │   ├── 13
│   │   │   ├── 1_30_cc_time_1959_1962_13.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_30_cc_time_1959_1962_13_1.png
│   │   │           └── 1_30_cc_time_1959_1962_13_1.txt
│   │   ├── 14
│   │   │   ├── 1_30_cc_time_1959_1962_14.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_30_cc_time_1959_1962_14_1.png
│   │   │           └── 1_30_cc_time_1959_1962_14_1.txt
│   │   ├── 15
│   │   │   ├── 1_30_cc_time_1959_1962_15.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_15.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_15_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_15_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_15_2.png
│   │   │           └── 1_30_cc_time_1959_1962_15_2.txt
│   │   ├── 16
│   │   │   ├── 1_30_cc_time_1959_1962_16.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_16.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_16_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_16_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_16_2.png
│   │   │           └── 1_30_cc_time_1959_1962_16_2.txt
│   │   ├── 17
│   │   │   ├── 1_30_cc_time_1959_1962_17.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_17.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_17_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_17_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_17_2.png
│   │   │           └── 1_30_cc_time_1959_1962_17_2.txt
│   │   ├── 18
│   │   │   ├── 1_30_cc_time_1959_1962_18.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_18.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_18_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_18_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_18_2.png
│   │   │           └── 1_30_cc_time_1959_1962_18_2.txt
│   │   ├── 19
│   │   │   ├── 1_30_cc_time_1959_1962_19.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_30_cc_time_1959_1962_19_1.png
│   │   │           └── 1_30_cc_time_1959_1962_19_1.txt
│   │   ├── 2
│   │   │   ├── 1_30_cc_time_1959_1962_2.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_2_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_30_cc_time_1959_1962_2_2.png
│   │   │       │   └── 1_30_cc_time_1959_1962_2_2.txt
│   │   │       └── 3
│   │   │           ├── 1_30_cc_time_1959_1962_2_3.png
│   │   │           └── 1_30_cc_time_1959_1962_2_3.txt
│   │   ├── 20
│   │   │   ├── 1_30_cc_time_1959_1962_20.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_20.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_20_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_20_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_20_2.png
│   │   │           └── 1_30_cc_time_1959_1962_20_2.txt
│   │   ├── 21
│   │   │   ├── 1_30_cc_time_1959_1962_21.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_30_cc_time_1959_1962_21_1.png
│   │   │           └── 1_30_cc_time_1959_1962_21_1.txt
│   │   ├── 4
│   │   │   ├── 1_30_cc_time_1959_1962_4.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_4_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_4_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_4_2.png
│   │   │           └── 1_30_cc_time_1959_1962_4_2.txt
│   │   ├── 5
│   │   │   ├── 1_30_cc_time_1959_1962_5.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_5_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_5_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_5_2.png
│   │   │           └── 1_30_cc_time_1959_1962_5_2.txt
│   │   ├── 6
│   │   │   ├── 1_30_cc_time_1959_1962_6.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_6_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_6_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_6_2.png
│   │   │           └── 1_30_cc_time_1959_1962_6_2.txt
│   │   ├── 7
│   │   │   ├── 1_30_cc_time_1959_1962_7.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_7_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_7_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_7_2.png
│   │   │           └── 1_30_cc_time_1959_1962_7_2.txt
│   │   ├── 8
│   │   │   ├── 1_30_cc_time_1959_1962_8.pdf
│   │   │   ├── 1_30_cc_time_1959_1962_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_30_cc_time_1959_1962_8_1.png
│   │   │       │   └── 1_30_cc_time_1959_1962_8_1.txt
│   │   │       └── 2
│   │   │           ├── 1_30_cc_time_1959_1962_8_2.png
│   │   │           └── 1_30_cc_time_1959_1962_8_2.txt
│   │   └── 9
│   │       ├── 1_30_cc_time_1959_1962_9.pdf
│   │       ├── 1_30_cc_time_1959_1962_9.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 1_30_cc_time_1959_1962_9_1.png
│   │           │   └── 1_30_cc_time_1959_1962_9_1.txt
│   │           └── 2
│   │               ├── 1_30_cc_time_1959_1962_9_2.png
│   │               └── 1_30_cc_time_1959_1962_9_2.txt
│   └── raw_pdf
│       └── 1_30_cc_time_1959_1962_raw.pdf
├── 1_31_social_science_advisory_committee
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_31_social_science_advisory_committee_1.pdf
│   │   │   ├── 1_31_social_science_advisory_committee_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_31_social_science_advisory_committee_1_1.png
│   │   │           └── 1_31_social_science_advisory_committee_1_1.txt
│   │   ├── 2
│   │   │   ├── 1_31_social_science_advisory_committee_2.pdf
│   │   │   ├── 1_31_social_science_advisory_committee_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_31_social_science_advisory_committee_2_1.png
│   │   │           └── 1_31_social_science_advisory_committee_2_1.txt
│   │   ├── 3
│   │   │   ├── 1_31_social_science_advisory_committee_3.pdf
│   │   │   ├── 1_31_social_science_advisory_committee_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_31_social_science_advisory_committee_3_1.png
│   │   │       │   └── 1_31_social_science_advisory_committee_3_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_31_social_science_advisory_committee_3_2.png
│   │   │       │   └── 1_31_social_science_advisory_committee_3_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_31_social_science_advisory_committee_3_3.png
│   │   │       │   └── 1_31_social_science_advisory_committee_3_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_31_social_science_advisory_committee_3_4.png
│   │   │       │   └── 1_31_social_science_advisory_committee_3_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_31_social_science_advisory_committee_3_5.png
│   │   │       │   └── 1_31_social_science_advisory_committee_3_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_31_social_science_advisory_committee_3_6.png
│   │   │       │   └── 1_31_social_science_advisory_committee_3_6.txt
│   │   │       └── 7
│   │   │           ├── 1_31_social_science_advisory_committee_3_7.png
│   │   │           └── 1_31_social_science_advisory_committee_3_7.txt
│   │   └── 4
│   │       ├── 1_31_social_science_advisory_committee_4.pdf
│   │       ├── 1_31_social_science_advisory_committee_4.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 1_31_social_science_advisory_committee_4_1.png
│   │           │   └── 1_31_social_science_advisory_committee_4_1.txt
│   │           └── 2
│   │               ├── 1_31_social_science_advisory_committee_4_2.png
│   │               └── 1_31_social_science_advisory_committee_4_2.txt
│   └── raw_pdf
│       └── 1_31_social_science_advisory_committee_raw.pdf
├── 1_3_statistical_service_center
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_3_statistical_service_center_1.pdf
│   │   │   ├── 1_3_statistical_service_center_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_1_1.png
│   │   │       │   └── 1_3_statistical_service_center_1_1.txt
│   │   │       ├── 10
│   │   │       │   ├── 1_3_statistical_service_center_1_10.png
│   │   │       │   └── 1_3_statistical_service_center_1_10.txt
│   │   │       ├── 11
│   │   │       │   ├── 1_3_statistical_service_center_1_11.png
│   │   │       │   └── 1_3_statistical_service_center_1_11.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_1_2.png
│   │   │       │   └── 1_3_statistical_service_center_1_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_1_3.png
│   │   │       │   └── 1_3_statistical_service_center_1_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_3_statistical_service_center_1_4.png
│   │   │       │   └── 1_3_statistical_service_center_1_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_3_statistical_service_center_1_5.png
│   │   │       │   └── 1_3_statistical_service_center_1_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_3_statistical_service_center_1_6.png
│   │   │       │   └── 1_3_statistical_service_center_1_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_3_statistical_service_center_1_7.png
│   │   │       │   └── 1_3_statistical_service_center_1_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_3_statistical_service_center_1_8.png
│   │   │       │   └── 1_3_statistical_service_center_1_8.txt
│   │   │       └── 9
│   │   │           ├── 1_3_statistical_service_center_1_9.png
│   │   │           └── 1_3_statistical_service_center_1_9.txt
│   │   ├── 10
│   │   │   ├── 1_3_statistical_service_center_10.pdf
│   │   │   ├── 1_3_statistical_service_center_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_10_1.png
│   │   │       │   └── 1_3_statistical_service_center_10_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_10_2.png
│   │   │       │   └── 1_3_statistical_service_center_10_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_10_3.png
│   │   │       │   └── 1_3_statistical_service_center_10_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_3_statistical_service_center_10_4.png
│   │   │       │   └── 1_3_statistical_service_center_10_4.txt
│   │   │       └── 5
│   │   │           ├── 1_3_statistical_service_center_10_5.png
│   │   │           └── 1_3_statistical_service_center_10_5.txt
│   │   ├── 11
│   │   │   ├── 1_3_statistical_service_center_11.pdf
│   │   │   ├── 1_3_statistical_service_center_11.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_11_1.png
│   │   │       │   └── 1_3_statistical_service_center_11_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_11_2.png
│   │   │       │   └── 1_3_statistical_service_center_11_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_11_3.png
│   │   │       │   └── 1_3_statistical_service_center_11_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_3_statistical_service_center_11_4.png
│   │   │       │   └── 1_3_statistical_service_center_11_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_3_statistical_service_center_11_5.png
│   │   │       │   └── 1_3_statistical_service_center_11_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_3_statistical_service_center_11_6.png
│   │   │       │   └── 1_3_statistical_service_center_11_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_3_statistical_service_center_11_7.png
│   │   │       │   └── 1_3_statistical_service_center_11_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_3_statistical_service_center_11_8.png
│   │   │       │   └── 1_3_statistical_service_center_11_8.txt
│   │   │       └── 9
│   │   │           ├── 1_3_statistical_service_center_11_9.png
│   │   │           └── 1_3_statistical_service_center_11_9.txt
│   │   ├── 12
│   │   │   ├── 1_3_statistical_service_center_12.pdf
│   │   │   ├── 1_3_statistical_service_center_12.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_12_1.png
│   │   │       │   └── 1_3_statistical_service_center_12_1.txt
│   │   │       └── 2
│   │   │           ├── 1_3_statistical_service_center_12_2.png
│   │   │           └── 1_3_statistical_service_center_12_2.txt
│   │   ├── 13
│   │   │   ├── 1_3_statistical_service_center_13.pdf
│   │   │   ├── 1_3_statistical_service_center_13.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_13_1.png
│   │   │       │   └── 1_3_statistical_service_center_13_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_13_2.png
│   │   │       │   └── 1_3_statistical_service_center_13_2.txt
│   │   │       └── 3
│   │   │           ├── 1_3_statistical_service_center_13_3.png
│   │   │           └── 1_3_statistical_service_center_13_3.txt
│   │   ├── 14
│   │   │   ├── 1_3_statistical_service_center_14.pdf
│   │   │   ├── 1_3_statistical_service_center_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_14_1.png
│   │   │           └── 1_3_statistical_service_center_14_1.txt
│   │   ├── 15
│   │   │   ├── 1_3_statistical_service_center_15.pdf
│   │   │   ├── 1_3_statistical_service_center_15.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_15_1.png
│   │   │       │   └── 1_3_statistical_service_center_15_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_15_2.png
│   │   │       │   └── 1_3_statistical_service_center_15_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_15_3.png
│   │   │       │   └── 1_3_statistical_service_center_15_3.txt
│   │   │       └── 4
│   │   │           ├── 1_3_statistical_service_center_15_4.png
│   │   │           └── 1_3_statistical_service_center_15_4.txt
│   │   ├── 16
│   │   │   ├── 1_3_statistical_service_center_16.pdf
│   │   │   ├── 1_3_statistical_service_center_16.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_16_1.png
│   │   │       │   └── 1_3_statistical_service_center_16_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_16_2.png
│   │   │       │   └── 1_3_statistical_service_center_16_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_16_3.png
│   │   │       │   └── 1_3_statistical_service_center_16_3.txt
│   │   │       └── 4
│   │   │           ├── 1_3_statistical_service_center_16_4.png
│   │   │           └── 1_3_statistical_service_center_16_4.txt
│   │   ├── 17
│   │   │   ├── 1_3_statistical_service_center_17.pdf
│   │   │   ├── 1_3_statistical_service_center_17.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_17_1.png
│   │   │       │   └── 1_3_statistical_service_center_17_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_17_2.png
│   │   │       │   └── 1_3_statistical_service_center_17_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_17_3.png
│   │   │       │   └── 1_3_statistical_service_center_17_3.txt
│   │   │       └── 4
│   │   │           ├── 1_3_statistical_service_center_17_4.png
│   │   │           └── 1_3_statistical_service_center_17_4.txt
│   │   ├── 18
│   │   │   ├── 1_3_statistical_service_center_18.pdf
│   │   │   ├── 1_3_statistical_service_center_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_18_1.png
│   │   │           └── 1_3_statistical_service_center_18_1.txt
│   │   ├── 19
│   │   │   ├── 1_3_statistical_service_center_19.pdf
│   │   │   ├── 1_3_statistical_service_center_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_19_1.png
│   │   │           └── 1_3_statistical_service_center_19_1.txt
│   │   ├── 2
│   │   │   ├── 1_3_statistical_service_center_2.pdf
│   │   │   ├── 1_3_statistical_service_center_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_2_1.png
│   │   │       │   └── 1_3_statistical_service_center_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_2_2.png
│   │   │       │   └── 1_3_statistical_service_center_2_2.txt
│   │   │       └── 3
│   │   │           ├── 1_3_statistical_service_center_2_3.png
│   │   │           └── 1_3_statistical_service_center_2_3.txt
│   │   ├── 20
│   │   │   ├── 1_3_statistical_service_center_20.pdf
│   │   │   ├── 1_3_statistical_service_center_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_20_1.png
│   │   │           └── 1_3_statistical_service_center_20_1.txt
│   │   ├── 21
│   │   │   ├── 1_3_statistical_service_center_21.pdf
│   │   │   ├── 1_3_statistical_service_center_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_21_1.png
│   │   │           └── 1_3_statistical_service_center_21_1.txt
│   │   ├── 22
│   │   │   ├── 1_3_statistical_service_center_22.pdf
│   │   │   ├── 1_3_statistical_service_center_22.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_22_1.png
│   │   │           └── 1_3_statistical_service_center_22_1.txt
│   │   ├── 23
│   │   │   ├── 1_3_statistical_service_center_23.pdf
│   │   │   ├── 1_3_statistical_service_center_23.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_23_1.png
│   │   │           └── 1_3_statistical_service_center_23_1.txt
│   │   ├── 24
│   │   │   ├── 1_3_statistical_service_center_24.pdf
│   │   │   ├── 1_3_statistical_service_center_24.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_24_1.png
│   │   │           └── 1_3_statistical_service_center_24_1.txt
│   │   ├── 25
│   │   │   ├── 1_3_statistical_service_center_25.pdf
│   │   │   ├── 1_3_statistical_service_center_25.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_25_1.png
│   │   │           └── 1_3_statistical_service_center_25_1.txt
│   │   ├── 26
│   │   │   ├── 1_3_statistical_service_center_26.pdf
│   │   │   ├── 1_3_statistical_service_center_26.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_26_1.png
│   │   │           └── 1_3_statistical_service_center_26_1.txt
│   │   ├── 27
│   │   │   ├── 1_3_statistical_service_center_27.pdf
│   │   │   ├── 1_3_statistical_service_center_27.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_27_1.png
│   │   │           └── 1_3_statistical_service_center_27_1.txt
│   │   ├── 28
│   │   │   ├── 1_3_statistical_service_center_28.pdf
│   │   │   ├── 1_3_statistical_service_center_28.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_28_1.png
│   │   │           └── 1_3_statistical_service_center_28_1.txt
│   │   ├── 29
│   │   │   ├── 1_3_statistical_service_center_29.pdf
│   │   │   ├── 1_3_statistical_service_center_29.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_29_1.png
│   │   │           └── 1_3_statistical_service_center_29_1.txt
│   │   ├── 3
│   │   │   ├── 1_3_statistical_service_center_3.pdf
│   │   │   ├── 1_3_statistical_service_center_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_3_1.png
│   │   │           └── 1_3_statistical_service_center_3_1.txt
│   │   ├── 30
│   │   │   ├── 1_3_statistical_service_center_30.pdf
│   │   │   ├── 1_3_statistical_service_center_30.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_30_1.png
│   │   │           └── 1_3_statistical_service_center_30_1.txt
│   │   ├── 31
│   │   │   ├── 1_3_statistical_service_center_31.pdf
│   │   │   ├── 1_3_statistical_service_center_31.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_31_1.png
│   │   │           └── 1_3_statistical_service_center_31_1.txt
│   │   ├── 32
│   │   │   ├── 1_3_statistical_service_center_32.pdf
│   │   │   ├── 1_3_statistical_service_center_32.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_32_1.png
│   │   │           └── 1_3_statistical_service_center_32_1.txt
│   │   ├── 33
│   │   │   ├── 1_3_statistical_service_center_33.pdf
│   │   │   ├── 1_3_statistical_service_center_33.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_33_1.png
│   │   │           └── 1_3_statistical_service_center_33_1.txt
│   │   ├── 34
│   │   │   ├── 1_3_statistical_service_center_34.pdf
│   │   │   ├── 1_3_statistical_service_center_34.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_34_1.png
│   │   │           └── 1_3_statistical_service_center_34_1.txt
│   │   ├── 35
│   │   │   ├── 1_3_statistical_service_center_35.pdf
│   │   │   ├── 1_3_statistical_service_center_35.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_35_1.png
│   │   │           └── 1_3_statistical_service_center_35_1.txt
│   │   ├── 36
│   │   │   ├── 1_3_statistical_service_center_36.pdf
│   │   │   ├── 1_3_statistical_service_center_36.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_36_1.png
│   │   │           └── 1_3_statistical_service_center_36_1.txt
│   │   ├── 37
│   │   │   ├── 1_3_statistical_service_center_37.pdf
│   │   │   ├── 1_3_statistical_service_center_37.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_37_1.png
│   │   │           └── 1_3_statistical_service_center_37_1.txt
│   │   ├── 38
│   │   │   ├── 1_3_statistical_service_center_38.pdf
│   │   │   ├── 1_3_statistical_service_center_38.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_38_1.png
│   │   │           └── 1_3_statistical_service_center_38_1.txt
│   │   ├── 39
│   │   │   ├── 1_3_statistical_service_center_39.pdf
│   │   │   ├── 1_3_statistical_service_center_39.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_39_1.png
│   │   │           └── 1_3_statistical_service_center_39_1.txt
│   │   ├── 4
│   │   │   ├── 1_3_statistical_service_center_4.pdf
│   │   │   ├── 1_3_statistical_service_center_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_4_1.png
│   │   │       │   └── 1_3_statistical_service_center_4_1.txt
│   │   │       └── 2
│   │   │           ├── 1_3_statistical_service_center_4_2.png
│   │   │           └── 1_3_statistical_service_center_4_2.txt
│   │   ├── 40
│   │   │   ├── 1_3_statistical_service_center_40.pdf
│   │   │   ├── 1_3_statistical_service_center_40.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_40_1.png
│   │   │           └── 1_3_statistical_service_center_40_1.txt
│   │   ├── 41
│   │   │   ├── 1_3_statistical_service_center_41.pdf
│   │   │   ├── 1_3_statistical_service_center_41.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_41_1.png
│   │   │           └── 1_3_statistical_service_center_41_1.txt
│   │   ├── 42
│   │   │   ├── 1_3_statistical_service_center_42.pdf
│   │   │   ├── 1_3_statistical_service_center_42.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_42_1.png
│   │   │           └── 1_3_statistical_service_center_42_1.txt
│   │   ├── 43
│   │   │   ├── 1_3_statistical_service_center_43.pdf
│   │   │   ├── 1_3_statistical_service_center_43.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_43_1.png
│   │   │           └── 1_3_statistical_service_center_43_1.txt
│   │   ├── 44
│   │   │   ├── 1_3_statistical_service_center_44.pdf
│   │   │   ├── 1_3_statistical_service_center_44.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_44_1.png
│   │   │           └── 1_3_statistical_service_center_44_1.txt
│   │   ├── 45
│   │   │   ├── 1_3_statistical_service_center_45.pdf
│   │   │   ├── 1_3_statistical_service_center_45.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_45_1.png
│   │   │           └── 1_3_statistical_service_center_45_1.txt
│   │   ├── 46
│   │   │   ├── 1_3_statistical_service_center_46.pdf
│   │   │   ├── 1_3_statistical_service_center_46.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_46_1.png
│   │   │           └── 1_3_statistical_service_center_46_1.txt
│   │   ├── 47
│   │   │   ├── 1_3_statistical_service_center_47.pdf
│   │   │   ├── 1_3_statistical_service_center_47.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_47_1.png
│   │   │           └── 1_3_statistical_service_center_47_1.txt
│   │   ├── 48
│   │   │   ├── 1_3_statistical_service_center_48.pdf
│   │   │   ├── 1_3_statistical_service_center_48.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_48_1.png
│   │   │           └── 1_3_statistical_service_center_48_1.txt
│   │   ├── 49
│   │   │   ├── 1_3_statistical_service_center_49.pdf
│   │   │   ├── 1_3_statistical_service_center_49.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_49_1.png
│   │   │           └── 1_3_statistical_service_center_49_1.txt
│   │   ├── 5
│   │   │   ├── 1_3_statistical_service_center_5.pdf
│   │   │   ├── 1_3_statistical_service_center_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_5_1.png
│   │   │           └── 1_3_statistical_service_center_5_1.txt
│   │   ├── 50
│   │   │   ├── 1_3_statistical_service_center_50.pdf
│   │   │   ├── 1_3_statistical_service_center_50.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_50_1.png
│   │   │           └── 1_3_statistical_service_center_50_1.txt
│   │   ├── 51
│   │   │   ├── 1_3_statistical_service_center_51.pdf
│   │   │   ├── 1_3_statistical_service_center_51.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_51_1.png
│   │   │           └── 1_3_statistical_service_center_51_1.txt
│   │   ├── 52
│   │   │   ├── 1_3_statistical_service_center_52.pdf
│   │   │   ├── 1_3_statistical_service_center_52.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_52_1.png
│   │   │       │   └── 1_3_statistical_service_center_52_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_52_2.png
│   │   │       │   └── 1_3_statistical_service_center_52_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_52_3.png
│   │   │       │   └── 1_3_statistical_service_center_52_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_3_statistical_service_center_52_4.png
│   │   │       │   └── 1_3_statistical_service_center_52_4.txt
│   │   │       └── 5
│   │   │           ├── 1_3_statistical_service_center_52_5.png
│   │   │           └── 1_3_statistical_service_center_52_5.txt
│   │   ├── 53
│   │   │   ├── 1_3_statistical_service_center_53.pdf
│   │   │   ├── 1_3_statistical_service_center_53.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_53_1.png
│   │   │       │   └── 1_3_statistical_service_center_53_1.txt
│   │   │       └── 2
│   │   │           ├── 1_3_statistical_service_center_53_2.png
│   │   │           └── 1_3_statistical_service_center_53_2.txt
│   │   ├── 54
│   │   │   ├── 1_3_statistical_service_center_54.pdf
│   │   │   ├── 1_3_statistical_service_center_54.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_54_1.png
│   │   │       │   └── 1_3_statistical_service_center_54_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_54_2.png
│   │   │       │   └── 1_3_statistical_service_center_54_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_54_3.png
│   │   │       │   └── 1_3_statistical_service_center_54_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_3_statistical_service_center_54_4.png
│   │   │       │   └── 1_3_statistical_service_center_54_4.txt
│   │   │       └── 5
│   │   │           ├── 1_3_statistical_service_center_54_5.png
│   │   │           └── 1_3_statistical_service_center_54_5.txt
│   │   ├── 55
│   │   │   ├── 1_3_statistical_service_center_55.pdf
│   │   │   ├── 1_3_statistical_service_center_55.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_55_1.png
│   │   │       │   └── 1_3_statistical_service_center_55_1.txt
│   │   │       └── 2
│   │   │           ├── 1_3_statistical_service_center_55_2.png
│   │   │           └── 1_3_statistical_service_center_55_2.txt
│   │   ├── 56
│   │   │   ├── 1_3_statistical_service_center_56.pdf
│   │   │   ├── 1_3_statistical_service_center_56.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_56_1.png
│   │   │       │   └── 1_3_statistical_service_center_56_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_56_2.png
│   │   │       │   └── 1_3_statistical_service_center_56_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_56_3.png
│   │   │       │   └── 1_3_statistical_service_center_56_3.txt
│   │   │       └── 4
│   │   │           ├── 1_3_statistical_service_center_56_4.png
│   │   │           └── 1_3_statistical_service_center_56_4.txt
│   │   ├── 57
│   │   │   ├── 1_3_statistical_service_center_57.pdf
│   │   │   ├── 1_3_statistical_service_center_57.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_57_1.png
│   │   │           └── 1_3_statistical_service_center_57_1.txt
│   │   ├── 58
│   │   │   ├── 1_3_statistical_service_center_58.pdf
│   │   │   ├── 1_3_statistical_service_center_58.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_58_1.png
│   │   │           └── 1_3_statistical_service_center_58_1.txt
│   │   ├── 59
│   │   │   ├── 1_3_statistical_service_center_59.pdf
│   │   │   ├── 1_3_statistical_service_center_59.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_59_1.png
│   │   │       │   └── 1_3_statistical_service_center_59_1.txt
│   │   │       └── 2
│   │   │           ├── 1_3_statistical_service_center_59_2.png
│   │   │           └── 1_3_statistical_service_center_59_2.txt
│   │   ├── 6
│   │   │   ├── 1_3_statistical_service_center_6.pdf
│   │   │   ├── 1_3_statistical_service_center_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_3_statistical_service_center_6_1.png
│   │   │           └── 1_3_statistical_service_center_6_1.txt
│   │   ├── 60
│   │   │   ├── 1_3_statistical_service_center_60.pdf
│   │   │   ├── 1_3_statistical_service_center_60.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_60_1.png
│   │   │       │   └── 1_3_statistical_service_center_60_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_60_2.png
│   │   │       │   └── 1_3_statistical_service_center_60_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_60_3.png
│   │   │       │   └── 1_3_statistical_service_center_60_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_3_statistical_service_center_60_4.png
│   │   │       │   └── 1_3_statistical_service_center_60_4.txt
│   │   │       └── 5
│   │   │           ├── 1_3_statistical_service_center_60_5.png
│   │   │           └── 1_3_statistical_service_center_60_5.txt
│   │   ├── 61
│   │   │   ├── 1_3_statistical_service_center_61.pdf
│   │   │   ├── 1_3_statistical_service_center_61.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_61_1.png
│   │   │       │   └── 1_3_statistical_service_center_61_1.txt
│   │   │       └── 2
│   │   │           ├── 1_3_statistical_service_center_61_2.png
│   │   │           └── 1_3_statistical_service_center_61_2.txt
│   │   ├── 7
│   │   │   ├── 1_3_statistical_service_center_7.pdf
│   │   │   ├── 1_3_statistical_service_center_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_7_1.png
│   │   │       │   └── 1_3_statistical_service_center_7_1.txt
│   │   │       ├── 10
│   │   │       │   ├── 1_3_statistical_service_center_7_10.png
│   │   │       │   └── 1_3_statistical_service_center_7_10.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_7_2.png
│   │   │       │   └── 1_3_statistical_service_center_7_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_3_statistical_service_center_7_3.png
│   │   │       │   └── 1_3_statistical_service_center_7_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_3_statistical_service_center_7_4.png
│   │   │       │   └── 1_3_statistical_service_center_7_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_3_statistical_service_center_7_5.png
│   │   │       │   └── 1_3_statistical_service_center_7_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_3_statistical_service_center_7_6.png
│   │   │       │   └── 1_3_statistical_service_center_7_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_3_statistical_service_center_7_7.png
│   │   │       │   └── 1_3_statistical_service_center_7_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_3_statistical_service_center_7_8.png
│   │   │       │   └── 1_3_statistical_service_center_7_8.txt
│   │   │       └── 9
│   │   │           ├── 1_3_statistical_service_center_7_9.png
│   │   │           └── 1_3_statistical_service_center_7_9.txt
│   │   ├── 8
│   │   │   ├── 1_3_statistical_service_center_8.pdf
│   │   │   ├── 1_3_statistical_service_center_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_3_statistical_service_center_8_1.png
│   │   │       │   └── 1_3_statistical_service_center_8_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_3_statistical_service_center_8_2.png
│   │   │       │   └── 1_3_statistical_service_center_8_2.txt
│   │   │       └── 3
│   │   │           ├── 1_3_statistical_service_center_8_3.png
│   │   │           └── 1_3_statistical_service_center_8_3.txt
│   │   └── 9
│   │       ├── 1_3_statistical_service_center_9.pdf
│   │       ├── 1_3_statistical_service_center_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_3_statistical_service_center_9_1.png
│   │               └── 1_3_statistical_service_center_9_1.txt
│   └── raw_pdf
│       └── 1_3_statistical_service_center_raw.pdf
├── 1_4_correspondence_whirlwind
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_4_correspondence_whirlwind_1.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_4_correspondence_whirlwind_1_1.png
│   │   │       │   └── 1_4_correspondence_whirlwind_1_1.txt
│   │   │       └── 2
│   │   │           ├── 1_4_correspondence_whirlwind_1_2.png
│   │   │           └── 1_4_correspondence_whirlwind_1_2.txt
│   │   ├── 10
│   │   │   ├── 1_4_correspondence_whirlwind_10.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_4_correspondence_whirlwind_10_1.png
│   │   │       │   └── 1_4_correspondence_whirlwind_10_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_4_correspondence_whirlwind_10_2.png
│   │   │       │   └── 1_4_correspondence_whirlwind_10_2.txt
│   │   │       └── 3
│   │   │           ├── 1_4_correspondence_whirlwind_10_3.png
│   │   │           └── 1_4_correspondence_whirlwind_10_3.txt
│   │   ├── 11
│   │   │   ├── 1_4_correspondence_whirlwind_11.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_11.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_1.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_1.txt
│   │   │       ├── 10
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_10.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_10.txt
│   │   │       ├── 11
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_11.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_11.txt
│   │   │       ├── 12
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_12.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_12.txt
│   │   │       ├── 13
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_13.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_13.txt
│   │   │       ├── 14
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_14.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_14.txt
│   │   │       ├── 15
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_15.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_15.txt
│   │   │       ├── 16
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_16.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_16.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_2.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_3.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_4.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_5.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_6.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_7.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_4_correspondence_whirlwind_11_8.png
│   │   │       │   └── 1_4_correspondence_whirlwind_11_8.txt
│   │   │       └── 9
│   │   │           ├── 1_4_correspondence_whirlwind_11_9.png
│   │   │           └── 1_4_correspondence_whirlwind_11_9.txt
│   │   ├── 12
│   │   │   ├── 1_4_correspondence_whirlwind_12.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_12.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_4_correspondence_whirlwind_12_1.png
│   │   │       │   └── 1_4_correspondence_whirlwind_12_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_4_correspondence_whirlwind_12_2.png
│   │   │       │   └── 1_4_correspondence_whirlwind_12_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_4_correspondence_whirlwind_12_3.png
│   │   │       │   └── 1_4_correspondence_whirlwind_12_3.txt
│   │   │       └── 4
│   │   │           ├── 1_4_correspondence_whirlwind_12_4.png
│   │   │           └── 1_4_correspondence_whirlwind_12_4.txt
│   │   ├── 13
│   │   │   ├── 1_4_correspondence_whirlwind_13.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_4_correspondence_whirlwind_13_1.png
│   │   │           └── 1_4_correspondence_whirlwind_13_1.txt
│   │   ├── 14
│   │   │   ├── 1_4_correspondence_whirlwind_14.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_14.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_4_correspondence_whirlwind_14_1.png
│   │   │       │   └── 1_4_correspondence_whirlwind_14_1.txt
│   │   │       └── 2
│   │   │           ├── 1_4_correspondence_whirlwind_14_2.png
│   │   │           └── 1_4_correspondence_whirlwind_14_2.txt
│   │   ├── 2
│   │   │   ├── 1_4_correspondence_whirlwind_2.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_4_correspondence_whirlwind_2_1.png
│   │   │           └── 1_4_correspondence_whirlwind_2_1.txt
│   │   ├── 3
│   │   │   ├── 1_4_correspondence_whirlwind_3.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_4_correspondence_whirlwind_3_1.png
│   │   │       │   └── 1_4_correspondence_whirlwind_3_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_4_correspondence_whirlwind_3_2.png
│   │   │       │   └── 1_4_correspondence_whirlwind_3_2.txt
│   │   │       └── 3
│   │   │           ├── 1_4_correspondence_whirlwind_3_3.png
│   │   │           └── 1_4_correspondence_whirlwind_3_3.txt
│   │   ├── 4
│   │   │   ├── 1_4_correspondence_whirlwind_4.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_4_correspondence_whirlwind_4_1.png
│   │   │           └── 1_4_correspondence_whirlwind_4_1.txt
│   │   ├── 5
│   │   │   ├── 1_4_correspondence_whirlwind_5.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_4_correspondence_whirlwind_5_1.png
│   │   │       │   └── 1_4_correspondence_whirlwind_5_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_4_correspondence_whirlwind_5_2.png
│   │   │       │   └── 1_4_correspondence_whirlwind_5_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_4_correspondence_whirlwind_5_3.png
│   │   │       │   └── 1_4_correspondence_whirlwind_5_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_4_correspondence_whirlwind_5_4.png
│   │   │       │   └── 1_4_correspondence_whirlwind_5_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_4_correspondence_whirlwind_5_5.png
│   │   │       │   └── 1_4_correspondence_whirlwind_5_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_4_correspondence_whirlwind_5_6.png
│   │   │       │   └── 1_4_correspondence_whirlwind_5_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_4_correspondence_whirlwind_5_7.png
│   │   │       │   └── 1_4_correspondence_whirlwind_5_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_4_correspondence_whirlwind_5_8.png
│   │   │       │   └── 1_4_correspondence_whirlwind_5_8.txt
│   │   │       └── 9
│   │   │           ├── 1_4_correspondence_whirlwind_5_9.png
│   │   │           └── 1_4_correspondence_whirlwind_5_9.txt
│   │   ├── 6
│   │   │   ├── 1_4_correspondence_whirlwind_6.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_4_correspondence_whirlwind_6_1.png
│   │   │       │   └── 1_4_correspondence_whirlwind_6_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_4_correspondence_whirlwind_6_2.png
│   │   │       │   └── 1_4_correspondence_whirlwind_6_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_4_correspondence_whirlwind_6_3.png
│   │   │       │   └── 1_4_correspondence_whirlwind_6_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_4_correspondence_whirlwind_6_4.png
│   │   │       │   └── 1_4_correspondence_whirlwind_6_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_4_correspondence_whirlwind_6_5.png
│   │   │       │   └── 1_4_correspondence_whirlwind_6_5.txt
│   │   │       └── 6
│   │   │           ├── 1_4_correspondence_whirlwind_6_6.png
│   │   │           └── 1_4_correspondence_whirlwind_6_6.txt
│   │   ├── 7
│   │   │   ├── 1_4_correspondence_whirlwind_7.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_4_correspondence_whirlwind_7_1.png
│   │   │       │   └── 1_4_correspondence_whirlwind_7_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_4_correspondence_whirlwind_7_2.png
│   │   │       │   └── 1_4_correspondence_whirlwind_7_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_4_correspondence_whirlwind_7_3.png
│   │   │       │   └── 1_4_correspondence_whirlwind_7_3.txt
│   │   │       └── 4
│   │   │           ├── 1_4_correspondence_whirlwind_7_4.png
│   │   │           └── 1_4_correspondence_whirlwind_7_4.txt
│   │   ├── 8
│   │   │   ├── 1_4_correspondence_whirlwind_8.pdf
│   │   │   ├── 1_4_correspondence_whirlwind_8.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_4_correspondence_whirlwind_8_1.png
│   │   │           └── 1_4_correspondence_whirlwind_8_1.txt
│   │   └── 9
│   │       ├── 1_4_correspondence_whirlwind_9.pdf
│   │       ├── 1_4_correspondence_whirlwind_9.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 1_4_correspondence_whirlwind_9_1.png
│   │           │   └── 1_4_correspondence_whirlwind_9_1.txt
│   │           ├── 2
│   │           │   ├── 1_4_correspondence_whirlwind_9_2.png
│   │           │   └── 1_4_correspondence_whirlwind_9_2.txt
│   │           ├── 3
│   │           │   ├── 1_4_correspondence_whirlwind_9_3.png
│   │           │   └── 1_4_correspondence_whirlwind_9_3.txt
│   │           └── 4
│   │               ├── 1_4_correspondence_whirlwind_9_4.png
│   │               └── 1_4_correspondence_whirlwind_9_4.txt
│   └── raw_pdf
│       └── 1_4_correspondence_whirlwind_raw.pdf
├── 1_5_whirlwind_time
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_5_whirlwind_time_1.pdf
│   │   │   ├── 1_5_whirlwind_time_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_1_1.png
│   │   │           └── 1_5_whirlwind_time_1_1.txt
│   │   ├── 10
│   │   │   ├── 1_5_whirlwind_time_10.pdf
│   │   │   ├── 1_5_whirlwind_time_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_10_1.png
│   │   │           └── 1_5_whirlwind_time_10_1.txt
│   │   ├── 100
│   │   │   ├── 1_5_whirlwind_time_100.pdf
│   │   │   ├── 1_5_whirlwind_time_100.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_100_1.png
│   │   │           └── 1_5_whirlwind_time_100_1.txt
│   │   ├── 101
│   │   │   ├── 1_5_whirlwind_time_101.pdf
│   │   │   ├── 1_5_whirlwind_time_101.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_101_1.png
│   │   │           └── 1_5_whirlwind_time_101_1.txt
│   │   ├── 102
│   │   │   ├── 1_5_whirlwind_time_102.pdf
│   │   │   ├── 1_5_whirlwind_time_102.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_102_1.png
│   │   │           └── 1_5_whirlwind_time_102_1.txt
│   │   ├── 103
│   │   │   ├── 1_5_whirlwind_time_103.pdf
│   │   │   ├── 1_5_whirlwind_time_103.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_103_1.png
│   │   │           └── 1_5_whirlwind_time_103_1.txt
│   │   ├── 104
│   │   │   ├── 1_5_whirlwind_time_104.pdf
│   │   │   ├── 1_5_whirlwind_time_104.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_104_1.png
│   │   │           └── 1_5_whirlwind_time_104_1.txt
│   │   ├── 105
│   │   │   ├── 1_5_whirlwind_time_105.pdf
│   │   │   ├── 1_5_whirlwind_time_105.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_105_1.png
│   │   │           └── 1_5_whirlwind_time_105_1.txt
│   │   ├── 106
│   │   │   ├── 1_5_whirlwind_time_106.pdf
│   │   │   ├── 1_5_whirlwind_time_106.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_106_1.png
│   │   │           └── 1_5_whirlwind_time_106_1.txt
│   │   ├── 107
│   │   │   ├── 1_5_whirlwind_time_107.pdf
│   │   │   ├── 1_5_whirlwind_time_107.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_107_1.png
│   │   │           └── 1_5_whirlwind_time_107_1.txt
│   │   ├── 108
│   │   │   ├── 1_5_whirlwind_time_108.pdf
│   │   │   ├── 1_5_whirlwind_time_108.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_108_1.png
│   │   │           └── 1_5_whirlwind_time_108_1.txt
│   │   ├── 109
│   │   │   ├── 1_5_whirlwind_time_109.pdf
│   │   │   ├── 1_5_whirlwind_time_109.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_109_1.png
│   │   │           └── 1_5_whirlwind_time_109_1.txt
│   │   ├── 11
│   │   │   ├── 1_5_whirlwind_time_11.pdf
│   │   │   ├── 1_5_whirlwind_time_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_11_1.png
│   │   │           └── 1_5_whirlwind_time_11_1.txt
│   │   ├── 110
│   │   │   ├── 1_5_whirlwind_time_110.pdf
│   │   │   ├── 1_5_whirlwind_time_110.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_110_1.png
│   │   │           └── 1_5_whirlwind_time_110_1.txt
│   │   ├── 111
│   │   │   ├── 1_5_whirlwind_time_111.pdf
│   │   │   ├── 1_5_whirlwind_time_111.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_111_1.png
│   │   │           └── 1_5_whirlwind_time_111_1.txt
│   │   ├── 112
│   │   │   ├── 1_5_whirlwind_time_112.pdf
│   │   │   ├── 1_5_whirlwind_time_112.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_112_1.png
│   │   │           └── 1_5_whirlwind_time_112_1.txt
│   │   ├── 113
│   │   │   ├── 1_5_whirlwind_time_113.pdf
│   │   │   ├── 1_5_whirlwind_time_113.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_113_1.png
│   │   │           └── 1_5_whirlwind_time_113_1.txt
│   │   ├── 114
│   │   │   ├── 1_5_whirlwind_time_114.pdf
│   │   │   ├── 1_5_whirlwind_time_114.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_114_1.png
│   │   │           └── 1_5_whirlwind_time_114_1.txt
│   │   ├── 115
│   │   │   ├── 1_5_whirlwind_time_115.pdf
│   │   │   ├── 1_5_whirlwind_time_115.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_115_1.png
│   │   │           └── 1_5_whirlwind_time_115_1.txt
│   │   ├── 116
│   │   │   ├── 1_5_whirlwind_time_116.pdf
│   │   │   ├── 1_5_whirlwind_time_116.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_116_1.png
│   │   │           └── 1_5_whirlwind_time_116_1.txt
│   │   ├── 117
│   │   │   ├── 1_5_whirlwind_time_117.pdf
│   │   │   ├── 1_5_whirlwind_time_117.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_117_1.png
│   │   │           └── 1_5_whirlwind_time_117_1.txt
│   │   ├── 118
│   │   │   ├── 1_5_whirlwind_time_118.pdf
│   │   │   ├── 1_5_whirlwind_time_118.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_5_whirlwind_time_118_1.png
│   │   │       │   └── 1_5_whirlwind_time_118_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_5_whirlwind_time_118_2.png
│   │   │       │   └── 1_5_whirlwind_time_118_2.txt
│   │   │       └── 3
│   │   │           ├── 1_5_whirlwind_time_118_3.png
│   │   │           └── 1_5_whirlwind_time_118_3.txt
│   │   ├── 119
│   │   │   ├── 1_5_whirlwind_time_119.pdf
│   │   │   ├── 1_5_whirlwind_time_119.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_119_1.png
│   │   │           └── 1_5_whirlwind_time_119_1.txt
│   │   ├── 12
│   │   │   ├── 1_5_whirlwind_time_12.pdf
│   │   │   ├── 1_5_whirlwind_time_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_12_1.png
│   │   │           └── 1_5_whirlwind_time_12_1.txt
│   │   ├── 120
│   │   │   ├── 1_5_whirlwind_time_120.pdf
│   │   │   ├── 1_5_whirlwind_time_120.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_120_1.png
│   │   │           └── 1_5_whirlwind_time_120_1.txt
│   │   ├── 121
│   │   │   ├── 1_5_whirlwind_time_121.pdf
│   │   │   ├── 1_5_whirlwind_time_121.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_121_1.png
│   │   │           └── 1_5_whirlwind_time_121_1.txt
│   │   ├── 122
│   │   │   ├── 1_5_whirlwind_time_122.pdf
│   │   │   ├── 1_5_whirlwind_time_122.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_122_1.png
│   │   │           └── 1_5_whirlwind_time_122_1.txt
│   │   ├── 123
│   │   │   ├── 1_5_whirlwind_time_123.pdf
│   │   │   ├── 1_5_whirlwind_time_123.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_123_1.png
│   │   │           └── 1_5_whirlwind_time_123_1.txt
│   │   ├── 124
│   │   │   ├── 1_5_whirlwind_time_124.pdf
│   │   │   ├── 1_5_whirlwind_time_124.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_124_1.png
│   │   │           └── 1_5_whirlwind_time_124_1.txt
│   │   ├── 125
│   │   │   ├── 1_5_whirlwind_time_125.pdf
│   │   │   ├── 1_5_whirlwind_time_125.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_125_1.png
│   │   │           └── 1_5_whirlwind_time_125_1.txt
│   │   ├── 126
│   │   │   ├── 1_5_whirlwind_time_126.pdf
│   │   │   ├── 1_5_whirlwind_time_126.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_126_1.png
│   │   │           └── 1_5_whirlwind_time_126_1.txt
│   │   ├── 127
│   │   │   ├── 1_5_whirlwind_time_127.pdf
│   │   │   ├── 1_5_whirlwind_time_127.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_127_1.png
│   │   │           └── 1_5_whirlwind_time_127_1.txt
│   │   ├── 128
│   │   │   ├── 1_5_whirlwind_time_128.pdf
│   │   │   ├── 1_5_whirlwind_time_128.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_128_1.png
│   │   │           └── 1_5_whirlwind_time_128_1.txt
│   │   ├── 129
│   │   │   ├── 1_5_whirlwind_time_129.pdf
│   │   │   ├── 1_5_whirlwind_time_129.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_129_1.png
│   │   │           └── 1_5_whirlwind_time_129_1.txt
│   │   ├── 13
│   │   │   ├── 1_5_whirlwind_time_13.pdf
│   │   │   ├── 1_5_whirlwind_time_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_13_1.png
│   │   │           └── 1_5_whirlwind_time_13_1.txt
│   │   ├── 130
│   │   │   ├── 1_5_whirlwind_time_130.pdf
│   │   │   ├── 1_5_whirlwind_time_130.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_130_1.png
│   │   │           └── 1_5_whirlwind_time_130_1.txt
│   │   ├── 131
│   │   │   ├── 1_5_whirlwind_time_131.pdf
│   │   │   ├── 1_5_whirlwind_time_131.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_131_1.png
│   │   │           └── 1_5_whirlwind_time_131_1.txt
│   │   ├── 132
│   │   │   ├── 1_5_whirlwind_time_132.pdf
│   │   │   ├── 1_5_whirlwind_time_132.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_132_1.png
│   │   │           └── 1_5_whirlwind_time_132_1.txt
│   │   ├── 133
│   │   │   ├── 1_5_whirlwind_time_133.pdf
│   │   │   ├── 1_5_whirlwind_time_133.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_133_1.png
│   │   │           └── 1_5_whirlwind_time_133_1.txt
│   │   ├── 134
│   │   │   ├── 1_5_whirlwind_time_134.pdf
│   │   │   ├── 1_5_whirlwind_time_134.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_134_1.png
│   │   │           └── 1_5_whirlwind_time_134_1.txt
│   │   ├── 135
│   │   │   ├── 1_5_whirlwind_time_135.pdf
│   │   │   ├── 1_5_whirlwind_time_135.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_135_1.png
│   │   │           └── 1_5_whirlwind_time_135_1.txt
│   │   ├── 136
│   │   │   ├── 1_5_whirlwind_time_136.pdf
│   │   │   ├── 1_5_whirlwind_time_136.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_136_1.png
│   │   │           └── 1_5_whirlwind_time_136_1.txt
│   │   ├── 14
│   │   │   ├── 1_5_whirlwind_time_14.pdf
│   │   │   ├── 1_5_whirlwind_time_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_14_1.png
│   │   │           └── 1_5_whirlwind_time_14_1.txt
│   │   ├── 15
│   │   │   ├── 1_5_whirlwind_time_15.pdf
│   │   │   ├── 1_5_whirlwind_time_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_15_1.png
│   │   │           └── 1_5_whirlwind_time_15_1.txt
│   │   ├── 16
│   │   │   ├── 1_5_whirlwind_time_16.pdf
│   │   │   ├── 1_5_whirlwind_time_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_16_1.png
│   │   │           └── 1_5_whirlwind_time_16_1.txt
│   │   ├── 17
│   │   │   ├── 1_5_whirlwind_time_17.pdf
│   │   │   ├── 1_5_whirlwind_time_17.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_17_1.png
│   │   │           └── 1_5_whirlwind_time_17_1.txt
│   │   ├── 18
│   │   │   ├── 1_5_whirlwind_time_18.pdf
│   │   │   ├── 1_5_whirlwind_time_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_18_1.png
│   │   │           └── 1_5_whirlwind_time_18_1.txt
│   │   ├── 19
│   │   │   ├── 1_5_whirlwind_time_19.pdf
│   │   │   ├── 1_5_whirlwind_time_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_19_1.png
│   │   │           └── 1_5_whirlwind_time_19_1.txt
│   │   ├── 2
│   │   │   ├── 1_5_whirlwind_time_2.pdf
│   │   │   ├── 1_5_whirlwind_time_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_2_1.png
│   │   │           └── 1_5_whirlwind_time_2_1.txt
│   │   ├── 20
│   │   │   ├── 1_5_whirlwind_time_20.pdf
│   │   │   ├── 1_5_whirlwind_time_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_20_1.png
│   │   │           └── 1_5_whirlwind_time_20_1.txt
│   │   ├── 21
│   │   │   ├── 1_5_whirlwind_time_21.pdf
│   │   │   ├── 1_5_whirlwind_time_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_21_1.png
│   │   │           └── 1_5_whirlwind_time_21_1.txt
│   │   ├── 22
│   │   │   ├── 1_5_whirlwind_time_22.pdf
│   │   │   ├── 1_5_whirlwind_time_22.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_22_1.png
│   │   │           └── 1_5_whirlwind_time_22_1.txt
│   │   ├── 23
│   │   │   ├── 1_5_whirlwind_time_23.pdf
│   │   │   ├── 1_5_whirlwind_time_23.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_23_1.png
│   │   │           └── 1_5_whirlwind_time_23_1.txt
│   │   ├── 24
│   │   │   ├── 1_5_whirlwind_time_24.pdf
│   │   │   ├── 1_5_whirlwind_time_24.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_24_1.png
│   │   │           └── 1_5_whirlwind_time_24_1.txt
│   │   ├── 25
│   │   │   ├── 1_5_whirlwind_time_25.pdf
│   │   │   ├── 1_5_whirlwind_time_25.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_25_1.png
│   │   │           └── 1_5_whirlwind_time_25_1.txt
│   │   ├── 26
│   │   │   ├── 1_5_whirlwind_time_26.pdf
│   │   │   ├── 1_5_whirlwind_time_26.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_26_1.png
│   │   │           └── 1_5_whirlwind_time_26_1.txt
│   │   ├── 27
│   │   │   ├── 1_5_whirlwind_time_27.pdf
│   │   │   ├── 1_5_whirlwind_time_27.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_27_1.png
│   │   │           └── 1_5_whirlwind_time_27_1.txt
│   │   ├── 28
│   │   │   ├── 1_5_whirlwind_time_28.pdf
│   │   │   ├── 1_5_whirlwind_time_28.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_28_1.png
│   │   │           └── 1_5_whirlwind_time_28_1.txt
│   │   ├── 29
│   │   │   ├── 1_5_whirlwind_time_29.pdf
│   │   │   ├── 1_5_whirlwind_time_29.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_29_1.png
│   │   │           └── 1_5_whirlwind_time_29_1.txt
│   │   ├── 3
│   │   │   ├── 1_5_whirlwind_time_3.pdf
│   │   │   ├── 1_5_whirlwind_time_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_3_1.png
│   │   │           └── 1_5_whirlwind_time_3_1.txt
│   │   ├── 30
│   │   │   ├── 1_5_whirlwind_time_30.pdf
│   │   │   ├── 1_5_whirlwind_time_30.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_30_1.png
│   │   │           └── 1_5_whirlwind_time_30_1.txt
│   │   ├── 31
│   │   │   ├── 1_5_whirlwind_time_31.pdf
│   │   │   ├── 1_5_whirlwind_time_31.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_31_1.png
│   │   │           └── 1_5_whirlwind_time_31_1.txt
│   │   ├── 32
│   │   │   ├── 1_5_whirlwind_time_32.pdf
│   │   │   ├── 1_5_whirlwind_time_32.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_32_1.png
│   │   │           └── 1_5_whirlwind_time_32_1.txt
│   │   ├── 33
│   │   │   ├── 1_5_whirlwind_time_33.pdf
│   │   │   ├── 1_5_whirlwind_time_33.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_33_1.png
│   │   │           └── 1_5_whirlwind_time_33_1.txt
│   │   ├── 34
│   │   │   ├── 1_5_whirlwind_time_34.pdf
│   │   │   ├── 1_5_whirlwind_time_34.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_34_1.png
│   │   │           └── 1_5_whirlwind_time_34_1.txt
│   │   ├── 35
│   │   │   ├── 1_5_whirlwind_time_35.pdf
│   │   │   ├── 1_5_whirlwind_time_35.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_35_1.png
│   │   │           └── 1_5_whirlwind_time_35_1.txt
│   │   ├── 36
│   │   │   ├── 1_5_whirlwind_time_36.pdf
│   │   │   ├── 1_5_whirlwind_time_36.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_36_1.png
│   │   │           └── 1_5_whirlwind_time_36_1.txt
│   │   ├── 37
│   │   │   ├── 1_5_whirlwind_time_37.pdf
│   │   │   ├── 1_5_whirlwind_time_37.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_37_1.png
│   │   │           └── 1_5_whirlwind_time_37_1.txt
│   │   ├── 38
│   │   │   ├── 1_5_whirlwind_time_38.pdf
│   │   │   ├── 1_5_whirlwind_time_38.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_38_1.png
│   │   │           └── 1_5_whirlwind_time_38_1.txt
│   │   ├── 39
│   │   │   ├── 1_5_whirlwind_time_39.pdf
│   │   │   ├── 1_5_whirlwind_time_39.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_39_1.png
│   │   │           └── 1_5_whirlwind_time_39_1.txt
│   │   ├── 4
│   │   │   ├── 1_5_whirlwind_time_4.pdf
│   │   │   ├── 1_5_whirlwind_time_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_5_whirlwind_time_4_1.png
│   │   │       │   └── 1_5_whirlwind_time_4_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_5_whirlwind_time_4_2.png
│   │   │       │   └── 1_5_whirlwind_time_4_2.txt
│   │   │       └── 3
│   │   │           ├── 1_5_whirlwind_time_4_3.png
│   │   │           └── 1_5_whirlwind_time_4_3.txt
│   │   ├── 40
│   │   │   ├── 1_5_whirlwind_time_40.pdf
│   │   │   ├── 1_5_whirlwind_time_40.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_40_1.png
│   │   │           └── 1_5_whirlwind_time_40_1.txt
│   │   ├── 41
│   │   │   ├── 1_5_whirlwind_time_41.pdf
│   │   │   ├── 1_5_whirlwind_time_41.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_41_1.png
│   │   │           └── 1_5_whirlwind_time_41_1.txt
│   │   ├── 42
│   │   │   ├── 1_5_whirlwind_time_42.pdf
│   │   │   ├── 1_5_whirlwind_time_42.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_42_1.png
│   │   │           └── 1_5_whirlwind_time_42_1.txt
│   │   ├── 43
│   │   │   ├── 1_5_whirlwind_time_43.pdf
│   │   │   ├── 1_5_whirlwind_time_43.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_43_1.png
│   │   │           └── 1_5_whirlwind_time_43_1.txt
│   │   ├── 44
│   │   │   ├── 1_5_whirlwind_time_44.pdf
│   │   │   ├── 1_5_whirlwind_time_44.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_44_1.png
│   │   │           └── 1_5_whirlwind_time_44_1.txt
│   │   ├── 45
│   │   │   ├── 1_5_whirlwind_time_45.pdf
│   │   │   ├── 1_5_whirlwind_time_45.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_45_1.png
│   │   │           └── 1_5_whirlwind_time_45_1.txt
│   │   ├── 46
│   │   │   ├── 1_5_whirlwind_time_46.pdf
│   │   │   ├── 1_5_whirlwind_time_46.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_46_1.png
│   │   │           └── 1_5_whirlwind_time_46_1.txt
│   │   ├── 47
│   │   │   ├── 1_5_whirlwind_time_47.pdf
│   │   │   ├── 1_5_whirlwind_time_47.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_47_1.png
│   │   │           └── 1_5_whirlwind_time_47_1.txt
│   │   ├── 48
│   │   │   ├── 1_5_whirlwind_time_48.pdf
│   │   │   ├── 1_5_whirlwind_time_48.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_48_1.png
│   │   │           └── 1_5_whirlwind_time_48_1.txt
│   │   ├── 49
│   │   │   ├── 1_5_whirlwind_time_49.pdf
│   │   │   ├── 1_5_whirlwind_time_49.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_49_1.png
│   │   │           └── 1_5_whirlwind_time_49_1.txt
│   │   ├── 5
│   │   │   ├── 1_5_whirlwind_time_5.pdf
│   │   │   ├── 1_5_whirlwind_time_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_5_1.png
│   │   │           └── 1_5_whirlwind_time_5_1.txt
│   │   ├── 50
│   │   │   ├── 1_5_whirlwind_time_50.pdf
│   │   │   ├── 1_5_whirlwind_time_50.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_50_1.png
│   │   │           └── 1_5_whirlwind_time_50_1.txt
│   │   ├── 51
│   │   │   ├── 1_5_whirlwind_time_51.pdf
│   │   │   ├── 1_5_whirlwind_time_51.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_51_1.png
│   │   │           └── 1_5_whirlwind_time_51_1.txt
│   │   ├── 52
│   │   │   ├── 1_5_whirlwind_time_52.pdf
│   │   │   ├── 1_5_whirlwind_time_52.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_52_1.png
│   │   │           └── 1_5_whirlwind_time_52_1.txt
│   │   ├── 53
│   │   │   ├── 1_5_whirlwind_time_53.pdf
│   │   │   ├── 1_5_whirlwind_time_53.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_53_1.png
│   │   │           └── 1_5_whirlwind_time_53_1.txt
│   │   ├── 54
│   │   │   ├── 1_5_whirlwind_time_54.pdf
│   │   │   ├── 1_5_whirlwind_time_54.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_54_1.png
│   │   │           └── 1_5_whirlwind_time_54_1.txt
│   │   ├── 55
│   │   │   ├── 1_5_whirlwind_time_55.pdf
│   │   │   ├── 1_5_whirlwind_time_55.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_55_1.png
│   │   │           └── 1_5_whirlwind_time_55_1.txt
│   │   ├── 56
│   │   │   ├── 1_5_whirlwind_time_56.pdf
│   │   │   ├── 1_5_whirlwind_time_56.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_56_1.png
│   │   │           └── 1_5_whirlwind_time_56_1.txt
│   │   ├── 57
│   │   │   ├── 1_5_whirlwind_time_57.pdf
│   │   │   ├── 1_5_whirlwind_time_57.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_57_1.png
│   │   │           └── 1_5_whirlwind_time_57_1.txt
│   │   ├── 58
│   │   │   ├── 1_5_whirlwind_time_58.pdf
│   │   │   ├── 1_5_whirlwind_time_58.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_58_1.png
│   │   │           └── 1_5_whirlwind_time_58_1.txt
│   │   ├── 59
│   │   │   ├── 1_5_whirlwind_time_59.pdf
│   │   │   ├── 1_5_whirlwind_time_59.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_59_1.png
│   │   │           └── 1_5_whirlwind_time_59_1.txt
│   │   ├── 6
│   │   │   ├── 1_5_whirlwind_time_6.pdf
│   │   │   ├── 1_5_whirlwind_time_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_6_1.png
│   │   │           └── 1_5_whirlwind_time_6_1.txt
│   │   ├── 60
│   │   │   ├── 1_5_whirlwind_time_60.pdf
│   │   │   ├── 1_5_whirlwind_time_60.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_60_1.png
│   │   │           └── 1_5_whirlwind_time_60_1.txt
│   │   ├── 61
│   │   │   ├── 1_5_whirlwind_time_61.pdf
│   │   │   ├── 1_5_whirlwind_time_61.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_61_1.png
│   │   │           └── 1_5_whirlwind_time_61_1.txt
│   │   ├── 62
│   │   │   ├── 1_5_whirlwind_time_62.pdf
│   │   │   ├── 1_5_whirlwind_time_62.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_62_1.png
│   │   │           └── 1_5_whirlwind_time_62_1.txt
│   │   ├── 63
│   │   │   ├── 1_5_whirlwind_time_63.pdf
│   │   │   ├── 1_5_whirlwind_time_63.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_63_1.png
│   │   │           └── 1_5_whirlwind_time_63_1.txt
│   │   ├── 64
│   │   │   ├── 1_5_whirlwind_time_64.pdf
│   │   │   ├── 1_5_whirlwind_time_64.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_64_1.png
│   │   │           └── 1_5_whirlwind_time_64_1.txt
│   │   ├── 65
│   │   │   ├── 1_5_whirlwind_time_65.pdf
│   │   │   ├── 1_5_whirlwind_time_65.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_65_1.png
│   │   │           └── 1_5_whirlwind_time_65_1.txt
│   │   ├── 66
│   │   │   ├── 1_5_whirlwind_time_66.pdf
│   │   │   ├── 1_5_whirlwind_time_66.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_66_1.png
│   │   │           └── 1_5_whirlwind_time_66_1.txt
│   │   ├── 67
│   │   │   ├── 1_5_whirlwind_time_67.pdf
│   │   │   ├── 1_5_whirlwind_time_67.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_67_1.png
│   │   │           └── 1_5_whirlwind_time_67_1.txt
│   │   ├── 68
│   │   │   ├── 1_5_whirlwind_time_68.pdf
│   │   │   ├── 1_5_whirlwind_time_68.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_68_1.png
│   │   │           └── 1_5_whirlwind_time_68_1.txt
│   │   ├── 69
│   │   │   ├── 1_5_whirlwind_time_69.pdf
│   │   │   ├── 1_5_whirlwind_time_69.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_69_1.png
│   │   │           └── 1_5_whirlwind_time_69_1.txt
│   │   ├── 7
│   │   │   ├── 1_5_whirlwind_time_7.pdf
│   │   │   ├── 1_5_whirlwind_time_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_7_1.png
│   │   │           └── 1_5_whirlwind_time_7_1.txt
│   │   ├── 70
│   │   │   ├── 1_5_whirlwind_time_70.pdf
│   │   │   ├── 1_5_whirlwind_time_70.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_70_1.png
│   │   │           └── 1_5_whirlwind_time_70_1.txt
│   │   ├── 71
│   │   │   ├── 1_5_whirlwind_time_71.pdf
│   │   │   ├── 1_5_whirlwind_time_71.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_71_1.png
│   │   │           └── 1_5_whirlwind_time_71_1.txt
│   │   ├── 72
│   │   │   ├── 1_5_whirlwind_time_72.pdf
│   │   │   ├── 1_5_whirlwind_time_72.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_72_1.png
│   │   │           └── 1_5_whirlwind_time_72_1.txt
│   │   ├── 73
│   │   │   ├── 1_5_whirlwind_time_73.pdf
│   │   │   ├── 1_5_whirlwind_time_73.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_73_1.png
│   │   │           └── 1_5_whirlwind_time_73_1.txt
│   │   ├── 74
│   │   │   ├── 1_5_whirlwind_time_74.pdf
│   │   │   ├── 1_5_whirlwind_time_74.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_74_1.png
│   │   │           └── 1_5_whirlwind_time_74_1.txt
│   │   ├── 75
│   │   │   ├── 1_5_whirlwind_time_75.pdf
│   │   │   ├── 1_5_whirlwind_time_75.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_75_1.png
│   │   │           └── 1_5_whirlwind_time_75_1.txt
│   │   ├── 76
│   │   │   ├── 1_5_whirlwind_time_76.pdf
│   │   │   ├── 1_5_whirlwind_time_76.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_76_1.png
│   │   │           └── 1_5_whirlwind_time_76_1.txt
│   │   ├── 77
│   │   │   ├── 1_5_whirlwind_time_77.pdf
│   │   │   ├── 1_5_whirlwind_time_77.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_77_1.png
│   │   │           └── 1_5_whirlwind_time_77_1.txt
│   │   ├── 78
│   │   │   ├── 1_5_whirlwind_time_78.pdf
│   │   │   ├── 1_5_whirlwind_time_78.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_78_1.png
│   │   │           └── 1_5_whirlwind_time_78_1.txt
│   │   ├── 79
│   │   │   ├── 1_5_whirlwind_time_79.pdf
│   │   │   ├── 1_5_whirlwind_time_79.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_79_1.png
│   │   │           └── 1_5_whirlwind_time_79_1.txt
│   │   ├── 8
│   │   │   ├── 1_5_whirlwind_time_8.pdf
│   │   │   ├── 1_5_whirlwind_time_8.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_8_1.png
│   │   │           └── 1_5_whirlwind_time_8_1.txt
│   │   ├── 80
│   │   │   ├── 1_5_whirlwind_time_80.pdf
│   │   │   ├── 1_5_whirlwind_time_80.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_80_1.png
│   │   │           └── 1_5_whirlwind_time_80_1.txt
│   │   ├── 81
│   │   │   ├── 1_5_whirlwind_time_81.pdf
│   │   │   ├── 1_5_whirlwind_time_81.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_81_1.png
│   │   │           └── 1_5_whirlwind_time_81_1.txt
│   │   ├── 82
│   │   │   ├── 1_5_whirlwind_time_82.pdf
│   │   │   ├── 1_5_whirlwind_time_82.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_82_1.png
│   │   │           └── 1_5_whirlwind_time_82_1.txt
│   │   ├── 83
│   │   │   ├── 1_5_whirlwind_time_83.pdf
│   │   │   ├── 1_5_whirlwind_time_83.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_83_1.png
│   │   │           └── 1_5_whirlwind_time_83_1.txt
│   │   ├── 84
│   │   │   ├── 1_5_whirlwind_time_84.pdf
│   │   │   ├── 1_5_whirlwind_time_84.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_84_1.png
│   │   │           └── 1_5_whirlwind_time_84_1.txt
│   │   ├── 85
│   │   │   ├── 1_5_whirlwind_time_85.pdf
│   │   │   ├── 1_5_whirlwind_time_85.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_85_1.png
│   │   │           └── 1_5_whirlwind_time_85_1.txt
│   │   ├── 86
│   │   │   ├── 1_5_whirlwind_time_86.pdf
│   │   │   ├── 1_5_whirlwind_time_86.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_86_1.png
│   │   │           └── 1_5_whirlwind_time_86_1.txt
│   │   ├── 87
│   │   │   ├── 1_5_whirlwind_time_87.pdf
│   │   │   ├── 1_5_whirlwind_time_87.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_87_1.png
│   │   │           └── 1_5_whirlwind_time_87_1.txt
│   │   ├── 88
│   │   │   ├── 1_5_whirlwind_time_88.pdf
│   │   │   ├── 1_5_whirlwind_time_88.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_88_1.png
│   │   │           └── 1_5_whirlwind_time_88_1.txt
│   │   ├── 89
│   │   │   ├── 1_5_whirlwind_time_89.pdf
│   │   │   ├── 1_5_whirlwind_time_89.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_89_1.png
│   │   │           └── 1_5_whirlwind_time_89_1.txt
│   │   ├── 9
│   │   │   ├── 1_5_whirlwind_time_9.pdf
│   │   │   ├── 1_5_whirlwind_time_9.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_9_1.png
│   │   │           └── 1_5_whirlwind_time_9_1.txt
│   │   ├── 90
│   │   │   ├── 1_5_whirlwind_time_90.pdf
│   │   │   ├── 1_5_whirlwind_time_90.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_90_1.png
│   │   │           └── 1_5_whirlwind_time_90_1.txt
│   │   ├── 91
│   │   │   ├── 1_5_whirlwind_time_91.pdf
│   │   │   ├── 1_5_whirlwind_time_91.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_91_1.png
│   │   │           └── 1_5_whirlwind_time_91_1.txt
│   │   ├── 92
│   │   │   ├── 1_5_whirlwind_time_92.pdf
│   │   │   ├── 1_5_whirlwind_time_92.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_92_1.png
│   │   │           └── 1_5_whirlwind_time_92_1.txt
│   │   ├── 93
│   │   │   ├── 1_5_whirlwind_time_93.pdf
│   │   │   ├── 1_5_whirlwind_time_93.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_93_1.png
│   │   │           └── 1_5_whirlwind_time_93_1.txt
│   │   ├── 94
│   │   │   ├── 1_5_whirlwind_time_94.pdf
│   │   │   ├── 1_5_whirlwind_time_94.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_94_1.png
│   │   │           └── 1_5_whirlwind_time_94_1.txt
│   │   ├── 95
│   │   │   ├── 1_5_whirlwind_time_95.pdf
│   │   │   ├── 1_5_whirlwind_time_95.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_95_1.png
│   │   │           └── 1_5_whirlwind_time_95_1.txt
│   │   ├── 96
│   │   │   ├── 1_5_whirlwind_time_96.pdf
│   │   │   ├── 1_5_whirlwind_time_96.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_96_1.png
│   │   │           └── 1_5_whirlwind_time_96_1.txt
│   │   ├── 97
│   │   │   ├── 1_5_whirlwind_time_97.pdf
│   │   │   ├── 1_5_whirlwind_time_97.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_97_1.png
│   │   │           └── 1_5_whirlwind_time_97_1.txt
│   │   ├── 98
│   │   │   ├── 1_5_whirlwind_time_98.pdf
│   │   │   ├── 1_5_whirlwind_time_98.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_5_whirlwind_time_98_1.png
│   │   │           └── 1_5_whirlwind_time_98_1.txt
│   │   └── 99
│   │       ├── 1_5_whirlwind_time_99.pdf
│   │       ├── 1_5_whirlwind_time_99.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_5_whirlwind_time_99_1.png
│   │               └── 1_5_whirlwind_time_99_1.txt
│   └── raw_pdf
│       └── 1_5_whirlwind_time_raw.pdf
├── 1_6_nsf_proposal
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_6_nsf_proposal_1.pdf
│   │   │   ├── 1_6_nsf_proposal_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_6_nsf_proposal_1_1.png
│   │   │           └── 1_6_nsf_proposal_1_1.txt
│   │   ├── 2
│   │   │   ├── 1_6_nsf_proposal_2.pdf
│   │   │   ├── 1_6_nsf_proposal_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_6_nsf_proposal_2_1.png
│   │   │           └── 1_6_nsf_proposal_2_1.txt
│   │   ├── 3
│   │   │   ├── 1_6_nsf_proposal_3.pdf
│   │   │   ├── 1_6_nsf_proposal_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_6_nsf_proposal_3_1.png
│   │   │           └── 1_6_nsf_proposal_3_1.txt
│   │   ├── 4
│   │   │   ├── 1_6_nsf_proposal_4.pdf
│   │   │   ├── 1_6_nsf_proposal_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_6_nsf_proposal_4_1.png
│   │   │           └── 1_6_nsf_proposal_4_1.txt
│   │   ├── 5
│   │   │   ├── 1_6_nsf_proposal_5.pdf
│   │   │   ├── 1_6_nsf_proposal_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_6_nsf_proposal_5_1.png
│   │   │           └── 1_6_nsf_proposal_5_1.txt
│   │   ├── 6
│   │   │   ├── 1_6_nsf_proposal_6.pdf
│   │   │   ├── 1_6_nsf_proposal_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_6_nsf_proposal_6_1.png
│   │   │           └── 1_6_nsf_proposal_6_1.txt
│   │   └── 7
│   │       ├── 1_6_nsf_proposal_7.pdf
│   │       ├── 1_6_nsf_proposal_7.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_6_nsf_proposal_7_1.png
│   │               └── 1_6_nsf_proposal_7_1.txt
│   └── raw_pdf
│       └── 1_6_nsf_proposal_raw.pdf
├── 1_7_nsf_cor
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_7_nsf_cor_1.pdf
│   │   │   ├── 1_7_nsf_cor_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_7_nsf_cor_1_1.png
│   │   │           └── 1_7_nsf_cor_1_1.txt
│   │   ├── 10
│   │   │   ├── 1_7_nsf_cor_10.pdf
│   │   │   ├── 1_7_nsf_cor_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_10_1.png
│   │   │       │   └── 1_7_nsf_cor_10_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_10_2.png
│   │   │       │   └── 1_7_nsf_cor_10_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_7_nsf_cor_10_3.png
│   │   │       │   └── 1_7_nsf_cor_10_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_7_nsf_cor_10_4.png
│   │   │       │   └── 1_7_nsf_cor_10_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_7_nsf_cor_10_5.png
│   │   │       │   └── 1_7_nsf_cor_10_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_7_nsf_cor_10_6.png
│   │   │       │   └── 1_7_nsf_cor_10_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_7_nsf_cor_10_7.png
│   │   │       │   └── 1_7_nsf_cor_10_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_7_nsf_cor_10_8.png
│   │   │       │   └── 1_7_nsf_cor_10_8.txt
│   │   │       └── 9
│   │   │           ├── 1_7_nsf_cor_10_9.png
│   │   │           └── 1_7_nsf_cor_10_9.txt
│   │   ├── 11
│   │   │   ├── 1_7_nsf_cor_11.pdf
│   │   │   ├── 1_7_nsf_cor_11.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_11_1.png
│   │   │       │   └── 1_7_nsf_cor_11_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_11_2.png
│   │   │       │   └── 1_7_nsf_cor_11_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_7_nsf_cor_11_3.png
│   │   │       │   └── 1_7_nsf_cor_11_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_7_nsf_cor_11_4.png
│   │   │       │   └── 1_7_nsf_cor_11_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_7_nsf_cor_11_5.png
│   │   │       │   └── 1_7_nsf_cor_11_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_7_nsf_cor_11_6.png
│   │   │       │   └── 1_7_nsf_cor_11_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_7_nsf_cor_11_7.png
│   │   │       │   └── 1_7_nsf_cor_11_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_7_nsf_cor_11_8.png
│   │   │       │   └── 1_7_nsf_cor_11_8.txt
│   │   │       └── 9
│   │   │           ├── 1_7_nsf_cor_11_9.png
│   │   │           └── 1_7_nsf_cor_11_9.txt
│   │   ├── 12
│   │   │   ├── 1_7_nsf_cor_12.pdf
│   │   │   ├── 1_7_nsf_cor_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_7_nsf_cor_12_1.png
│   │   │           └── 1_7_nsf_cor_12_1.txt
│   │   ├── 13
│   │   │   ├── 1_7_nsf_cor_13.pdf
│   │   │   ├── 1_7_nsf_cor_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_7_nsf_cor_13_1.png
│   │   │           └── 1_7_nsf_cor_13_1.txt
│   │   ├── 14
│   │   │   ├── 1_7_nsf_cor_14.pdf
│   │   │   ├── 1_7_nsf_cor_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_7_nsf_cor_14_1.png
│   │   │           └── 1_7_nsf_cor_14_1.txt
│   │   ├── 15
│   │   │   ├── 1_7_nsf_cor_15.pdf
│   │   │   ├── 1_7_nsf_cor_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_7_nsf_cor_15_1.png
│   │   │           └── 1_7_nsf_cor_15_1.txt
│   │   ├── 16
│   │   │   ├── 1_7_nsf_cor_16.pdf
│   │   │   ├── 1_7_nsf_cor_16.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_16_1.png
│   │   │       │   └── 1_7_nsf_cor_16_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_16_2.png
│   │   │       │   └── 1_7_nsf_cor_16_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_7_nsf_cor_16_3.png
│   │   │       │   └── 1_7_nsf_cor_16_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_7_nsf_cor_16_4.png
│   │   │       │   └── 1_7_nsf_cor_16_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_7_nsf_cor_16_5.png
│   │   │       │   └── 1_7_nsf_cor_16_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_7_nsf_cor_16_6.png
│   │   │       │   └── 1_7_nsf_cor_16_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_7_nsf_cor_16_7.png
│   │   │       │   └── 1_7_nsf_cor_16_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_7_nsf_cor_16_8.png
│   │   │       │   └── 1_7_nsf_cor_16_8.txt
│   │   │       └── 9
│   │   │           ├── 1_7_nsf_cor_16_9.png
│   │   │           └── 1_7_nsf_cor_16_9.txt
│   │   ├── 17
│   │   │   ├── 1_7_nsf_cor_17.pdf
│   │   │   ├── 1_7_nsf_cor_17.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_17_1.png
│   │   │       │   └── 1_7_nsf_cor_17_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_17_2.png
│   │   │       │   └── 1_7_nsf_cor_17_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_7_nsf_cor_17_3.png
│   │   │       │   └── 1_7_nsf_cor_17_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_7_nsf_cor_17_4.png
│   │   │       │   └── 1_7_nsf_cor_17_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_7_nsf_cor_17_5.png
│   │   │       │   └── 1_7_nsf_cor_17_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_7_nsf_cor_17_6.png
│   │   │       │   └── 1_7_nsf_cor_17_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_7_nsf_cor_17_7.png
│   │   │       │   └── 1_7_nsf_cor_17_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_7_nsf_cor_17_8.png
│   │   │       │   └── 1_7_nsf_cor_17_8.txt
│   │   │       └── 9
│   │   │           ├── 1_7_nsf_cor_17_9.png
│   │   │           └── 1_7_nsf_cor_17_9.txt
│   │   ├── 18
│   │   │   ├── 1_7_nsf_cor_18.pdf
│   │   │   ├── 1_7_nsf_cor_18.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_18_1.png
│   │   │       │   └── 1_7_nsf_cor_18_1.txt
│   │   │       └── 2
│   │   │           ├── 1_7_nsf_cor_18_2.png
│   │   │           └── 1_7_nsf_cor_18_2.txt
│   │   ├── 19
│   │   │   ├── 1_7_nsf_cor_19.pdf
│   │   │   ├── 1_7_nsf_cor_19.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_19_1.png
│   │   │       │   └── 1_7_nsf_cor_19_1.txt
│   │   │       └── 2
│   │   │           ├── 1_7_nsf_cor_19_2.png
│   │   │           └── 1_7_nsf_cor_19_2.txt
│   │   ├── 2
│   │   │   ├── 1_7_nsf_cor_2.pdf
│   │   │   ├── 1_7_nsf_cor_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_2_1.png
│   │   │       │   └── 1_7_nsf_cor_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_2_2.png
│   │   │       │   └── 1_7_nsf_cor_2_2.txt
│   │   │       └── 3
│   │   │           ├── 1_7_nsf_cor_2_3.png
│   │   │           └── 1_7_nsf_cor_2_3.txt
│   │   ├── 20
│   │   │   ├── 1_7_nsf_cor_20.pdf
│   │   │   ├── 1_7_nsf_cor_20.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_20_1.png
│   │   │       │   └── 1_7_nsf_cor_20_1.txt
│   │   │       └── 2
│   │   │           ├── 1_7_nsf_cor_20_2.png
│   │   │           └── 1_7_nsf_cor_20_2.txt
│   │   ├── 21
│   │   │   ├── 1_7_nsf_cor_21.pdf
│   │   │   ├── 1_7_nsf_cor_21.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_21_1.png
│   │   │       │   └── 1_7_nsf_cor_21_1.txt
│   │   │       └── 2
│   │   │           ├── 1_7_nsf_cor_21_2.png
│   │   │           └── 1_7_nsf_cor_21_2.txt
│   │   ├── 3
│   │   │   ├── 1_7_nsf_cor_3.pdf
│   │   │   ├── 1_7_nsf_cor_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_3_1.png
│   │   │       │   └── 1_7_nsf_cor_3_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_3_2.png
│   │   │       │   └── 1_7_nsf_cor_3_2.txt
│   │   │       └── 3
│   │   │           ├── 1_7_nsf_cor_3_3.png
│   │   │           └── 1_7_nsf_cor_3_3.txt
│   │   ├── 4
│   │   │   ├── 1_7_nsf_cor_4.pdf
│   │   │   ├── 1_7_nsf_cor_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_4_1.png
│   │   │       │   └── 1_7_nsf_cor_4_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_4_2.png
│   │   │       │   └── 1_7_nsf_cor_4_2.txt
│   │   │       └── 3
│   │   │           ├── 1_7_nsf_cor_4_3.png
│   │   │           └── 1_7_nsf_cor_4_3.txt
│   │   ├── 5
│   │   │   ├── 1_7_nsf_cor_5.pdf
│   │   │   ├── 1_7_nsf_cor_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_5_1.png
│   │   │       │   └── 1_7_nsf_cor_5_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_5_2.png
│   │   │       │   └── 1_7_nsf_cor_5_2.txt
│   │   │       └── 3
│   │   │           ├── 1_7_nsf_cor_5_3.png
│   │   │           └── 1_7_nsf_cor_5_3.txt
│   │   ├── 6
│   │   │   ├── 1_7_nsf_cor_6.pdf
│   │   │   ├── 1_7_nsf_cor_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_6_1.png
│   │   │       │   └── 1_7_nsf_cor_6_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_6_2.png
│   │   │       │   └── 1_7_nsf_cor_6_2.txt
│   │   │       └── 3
│   │   │           ├── 1_7_nsf_cor_6_3.png
│   │   │           └── 1_7_nsf_cor_6_3.txt
│   │   ├── 7
│   │   │   ├── 1_7_nsf_cor_7.pdf
│   │   │   ├── 1_7_nsf_cor_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_7_1.png
│   │   │       │   └── 1_7_nsf_cor_7_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_7_2.png
│   │   │       │   └── 1_7_nsf_cor_7_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_7_nsf_cor_7_3.png
│   │   │       │   └── 1_7_nsf_cor_7_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_7_nsf_cor_7_4.png
│   │   │       │   └── 1_7_nsf_cor_7_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_7_nsf_cor_7_5.png
│   │   │       │   └── 1_7_nsf_cor_7_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_7_nsf_cor_7_6.png
│   │   │       │   └── 1_7_nsf_cor_7_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_7_nsf_cor_7_7.png
│   │   │       │   └── 1_7_nsf_cor_7_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_7_nsf_cor_7_8.png
│   │   │       │   └── 1_7_nsf_cor_7_8.txt
│   │   │       └── 9
│   │   │           ├── 1_7_nsf_cor_7_9.png
│   │   │           └── 1_7_nsf_cor_7_9.txt
│   │   ├── 8
│   │   │   ├── 1_7_nsf_cor_8.pdf
│   │   │   ├── 1_7_nsf_cor_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_7_nsf_cor_8_1.png
│   │   │       │   └── 1_7_nsf_cor_8_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_7_nsf_cor_8_2.png
│   │   │       │   └── 1_7_nsf_cor_8_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_7_nsf_cor_8_3.png
│   │   │       │   └── 1_7_nsf_cor_8_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_7_nsf_cor_8_4.png
│   │   │       │   └── 1_7_nsf_cor_8_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_7_nsf_cor_8_5.png
│   │   │       │   └── 1_7_nsf_cor_8_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_7_nsf_cor_8_6.png
│   │   │       │   └── 1_7_nsf_cor_8_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_7_nsf_cor_8_7.png
│   │   │       │   └── 1_7_nsf_cor_8_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_7_nsf_cor_8_8.png
│   │   │       │   └── 1_7_nsf_cor_8_8.txt
│   │   │       └── 9
│   │   │           ├── 1_7_nsf_cor_8_9.png
│   │   │           └── 1_7_nsf_cor_8_9.txt
│   │   └── 9
│   │       ├── 1_7_nsf_cor_9.pdf
│   │       ├── 1_7_nsf_cor_9.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 1_7_nsf_cor_9_1.png
│   │           │   └── 1_7_nsf_cor_9_1.txt
│   │           ├── 2
│   │           │   ├── 1_7_nsf_cor_9_2.png
│   │           │   └── 1_7_nsf_cor_9_2.txt
│   │           ├── 3
│   │           │   ├── 1_7_nsf_cor_9_3.png
│   │           │   └── 1_7_nsf_cor_9_3.txt
│   │           ├── 4
│   │           │   ├── 1_7_nsf_cor_9_4.png
│   │           │   └── 1_7_nsf_cor_9_4.txt
│   │           ├── 5
│   │           │   ├── 1_7_nsf_cor_9_5.png
│   │           │   └── 1_7_nsf_cor_9_5.txt
│   │           ├── 6
│   │           │   ├── 1_7_nsf_cor_9_6.png
│   │           │   └── 1_7_nsf_cor_9_6.txt
│   │           ├── 7
│   │           │   ├── 1_7_nsf_cor_9_7.png
│   │           │   └── 1_7_nsf_cor_9_7.txt
│   │           ├── 8
│   │           │   ├── 1_7_nsf_cor_9_8.png
│   │           │   └── 1_7_nsf_cor_9_8.txt
│   │           └── 9
│   │               ├── 1_7_nsf_cor_9_9.png
│   │               └── 1_7_nsf_cor_9_9.txt
│   └── raw_pdf
│       └── 1_7_nsf_cor_raw.pdf
├── 1_8_rockefeller
│   ├── docs
│   │   ├── 1
│   │   │   ├── 1_8_rockefeller_1.pdf
│   │   │   ├── 1_8_rockefeller_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_1_1.png
│   │   │           └── 1_8_rockefeller_1_1.txt
│   │   ├── 10
│   │   │   ├── 1_8_rockefeller_10.pdf
│   │   │   ├── 1_8_rockefeller_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_8_rockefeller_10_1.png
│   │   │       │   └── 1_8_rockefeller_10_1.txt
│   │   │       └── 2
│   │   │           ├── 1_8_rockefeller_10_2.png
│   │   │           └── 1_8_rockefeller_10_2.txt
│   │   ├── 11
│   │   │   ├── 1_8_rockefeller_11.pdf
│   │   │   ├── 1_8_rockefeller_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_11_1.png
│   │   │           └── 1_8_rockefeller_11_1.txt
│   │   ├── 12
│   │   │   ├── 1_8_rockefeller_12.pdf
│   │   │   ├── 1_8_rockefeller_12.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_8_rockefeller_12_1.png
│   │   │       │   └── 1_8_rockefeller_12_1.txt
│   │   │       └── 2
│   │   │           ├── 1_8_rockefeller_12_2.png
│   │   │           └── 1_8_rockefeller_12_2.txt
│   │   ├── 13
│   │   │   ├── 1_8_rockefeller_13.pdf
│   │   │   ├── 1_8_rockefeller_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_13_1.png
│   │   │           └── 1_8_rockefeller_13_1.txt
│   │   ├── 14
│   │   │   ├── 1_8_rockefeller_14.pdf
│   │   │   ├── 1_8_rockefeller_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_14_1.png
│   │   │           └── 1_8_rockefeller_14_1.txt
│   │   ├── 15
│   │   │   ├── 1_8_rockefeller_15.pdf
│   │   │   ├── 1_8_rockefeller_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_15_1.png
│   │   │           └── 1_8_rockefeller_15_1.txt
│   │   ├── 16
│   │   │   ├── 1_8_rockefeller_16.pdf
│   │   │   ├── 1_8_rockefeller_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_16_1.png
│   │   │           └── 1_8_rockefeller_16_1.txt
│   │   ├── 17
│   │   │   ├── 1_8_rockefeller_17.pdf
│   │   │   ├── 1_8_rockefeller_17.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_17_1.png
│   │   │           └── 1_8_rockefeller_17_1.txt
│   │   ├── 18
│   │   │   ├── 1_8_rockefeller_18.pdf
│   │   │   ├── 1_8_rockefeller_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_18_1.png
│   │   │           └── 1_8_rockefeller_18_1.txt
│   │   ├── 19
│   │   │   ├── 1_8_rockefeller_19.pdf
│   │   │   ├── 1_8_rockefeller_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_19_1.png
│   │   │           └── 1_8_rockefeller_19_1.txt
│   │   ├── 2
│   │   │   ├── 1_8_rockefeller_2.pdf
│   │   │   ├── 1_8_rockefeller_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_2_1.png
│   │   │           └── 1_8_rockefeller_2_1.txt
│   │   ├── 20
│   │   │   ├── 1_8_rockefeller_20.pdf
│   │   │   ├── 1_8_rockefeller_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_20_1.png
│   │   │           └── 1_8_rockefeller_20_1.txt
│   │   ├── 21
│   │   │   ├── 1_8_rockefeller_21.pdf
│   │   │   ├── 1_8_rockefeller_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_21_1.png
│   │   │           └── 1_8_rockefeller_21_1.txt
│   │   ├── 22
│   │   │   ├── 1_8_rockefeller_22.pdf
│   │   │   ├── 1_8_rockefeller_22.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_22_1.png
│   │   │           └── 1_8_rockefeller_22_1.txt
│   │   ├── 23
│   │   │   ├── 1_8_rockefeller_23.pdf
│   │   │   ├── 1_8_rockefeller_23.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_23_1.png
│   │   │           └── 1_8_rockefeller_23_1.txt
│   │   ├── 24
│   │   │   ├── 1_8_rockefeller_24.pdf
│   │   │   ├── 1_8_rockefeller_24.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_24_1.png
│   │   │           └── 1_8_rockefeller_24_1.txt
│   │   ├── 25
│   │   │   ├── 1_8_rockefeller_25.pdf
│   │   │   ├── 1_8_rockefeller_25.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_25_1.png
│   │   │           └── 1_8_rockefeller_25_1.txt
│   │   ├── 26
│   │   │   ├── 1_8_rockefeller_26.pdf
│   │   │   ├── 1_8_rockefeller_26.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_26_1.png
│   │   │           └── 1_8_rockefeller_26_1.txt
│   │   ├── 27
│   │   │   ├── 1_8_rockefeller_27.pdf
│   │   │   ├── 1_8_rockefeller_27.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_27_1.png
│   │   │           └── 1_8_rockefeller_27_1.txt
│   │   ├── 28
│   │   │   ├── 1_8_rockefeller_28.pdf
│   │   │   ├── 1_8_rockefeller_28.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_8_rockefeller_28_1.png
│   │   │       │   └── 1_8_rockefeller_28_1.txt
│   │   │       ├── 10
│   │   │       │   ├── 1_8_rockefeller_28_10.png
│   │   │       │   └── 1_8_rockefeller_28_10.txt
│   │   │       ├── 11
│   │   │       │   ├── 1_8_rockefeller_28_11.png
│   │   │       │   └── 1_8_rockefeller_28_11.txt
│   │   │       ├── 12
│   │   │       │   ├── 1_8_rockefeller_28_12.png
│   │   │       │   └── 1_8_rockefeller_28_12.txt
│   │   │       ├── 13
│   │   │       │   ├── 1_8_rockefeller_28_13.png
│   │   │       │   └── 1_8_rockefeller_28_13.txt
│   │   │       ├── 14
│   │   │       │   ├── 1_8_rockefeller_28_14.png
│   │   │       │   └── 1_8_rockefeller_28_14.txt
│   │   │       ├── 15
│   │   │       │   ├── 1_8_rockefeller_28_15.png
│   │   │       │   └── 1_8_rockefeller_28_15.txt
│   │   │       ├── 16
│   │   │       │   ├── 1_8_rockefeller_28_16.png
│   │   │       │   └── 1_8_rockefeller_28_16.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_8_rockefeller_28_2.png
│   │   │       │   └── 1_8_rockefeller_28_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_8_rockefeller_28_3.png
│   │   │       │   └── 1_8_rockefeller_28_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_8_rockefeller_28_4.png
│   │   │       │   └── 1_8_rockefeller_28_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 1_8_rockefeller_28_5.png
│   │   │       │   └── 1_8_rockefeller_28_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 1_8_rockefeller_28_6.png
│   │   │       │   └── 1_8_rockefeller_28_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 1_8_rockefeller_28_7.png
│   │   │       │   └── 1_8_rockefeller_28_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 1_8_rockefeller_28_8.png
│   │   │       │   └── 1_8_rockefeller_28_8.txt
│   │   │       └── 9
│   │   │           ├── 1_8_rockefeller_28_9.png
│   │   │           └── 1_8_rockefeller_28_9.txt
│   │   ├── 29
│   │   │   ├── 1_8_rockefeller_29.pdf
│   │   │   ├── 1_8_rockefeller_29.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_29_1.png
│   │   │           └── 1_8_rockefeller_29_1.txt
│   │   ├── 3
│   │   │   ├── 1_8_rockefeller_3.pdf
│   │   │   ├── 1_8_rockefeller_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_3_1.png
│   │   │           └── 1_8_rockefeller_3_1.txt
│   │   ├── 30
│   │   │   ├── 1_8_rockefeller_30.pdf
│   │   │   ├── 1_8_rockefeller_30.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_8_rockefeller_30_1.png
│   │   │       │   └── 1_8_rockefeller_30_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_8_rockefeller_30_2.png
│   │   │       │   └── 1_8_rockefeller_30_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_8_rockefeller_30_3.png
│   │   │       │   └── 1_8_rockefeller_30_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_8_rockefeller_30_4.png
│   │   │       │   └── 1_8_rockefeller_30_4.txt
│   │   │       └── 5
│   │   │           ├── 1_8_rockefeller_30_5.png
│   │   │           └── 1_8_rockefeller_30_5.txt
│   │   ├── 31
│   │   │   ├── 1_8_rockefeller_31.pdf
│   │   │   ├── 1_8_rockefeller_31.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 1_8_rockefeller_31_1.png
│   │   │       │   └── 1_8_rockefeller_31_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 1_8_rockefeller_31_2.png
│   │   │       │   └── 1_8_rockefeller_31_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 1_8_rockefeller_31_3.png
│   │   │       │   └── 1_8_rockefeller_31_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 1_8_rockefeller_31_4.png
│   │   │       │   └── 1_8_rockefeller_31_4.txt
│   │   │       └── 5
│   │   │           ├── 1_8_rockefeller_31_5.png
│   │   │           └── 1_8_rockefeller_31_5.txt
│   │   ├── 4
│   │   │   ├── 1_8_rockefeller_4.pdf
│   │   │   ├── 1_8_rockefeller_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_4_1.png
│   │   │           └── 1_8_rockefeller_4_1.txt
│   │   ├── 5
│   │   │   ├── 1_8_rockefeller_5.pdf
│   │   │   ├── 1_8_rockefeller_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_5_1.png
│   │   │           └── 1_8_rockefeller_5_1.txt
│   │   ├── 6
│   │   │   ├── 1_8_rockefeller_6.pdf
│   │   │   ├── 1_8_rockefeller_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_6_1.png
│   │   │           └── 1_8_rockefeller_6_1.txt
│   │   ├── 7
│   │   │   ├── 1_8_rockefeller_7.pdf
│   │   │   ├── 1_8_rockefeller_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_7_1.png
│   │   │           └── 1_8_rockefeller_7_1.txt
│   │   ├── 8
│   │   │   ├── 1_8_rockefeller_8.pdf
│   │   │   ├── 1_8_rockefeller_8.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 1_8_rockefeller_8_1.png
│   │   │           └── 1_8_rockefeller_8_1.txt
│   │   └── 9
│   │       ├── 1_8_rockefeller_9.pdf
│   │       ├── 1_8_rockefeller_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 1_8_rockefeller_9_1.png
│   │               └── 1_8_rockefeller_9_1.txt
│   └── raw_pdf
│       └── 1_8_rockefeller_raw.pdf
├── 2_11_c
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_11_c_1.pdf
│   │   │   ├── 2_11_c_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_1_1.png
│   │   │           └── 2_11_c_1_1.txt
│   │   ├── 10
│   │   │   ├── 2_11_c_10.pdf
│   │   │   ├── 2_11_c_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_11_c_10_1.png
│   │   │       │   └── 2_11_c_10_1.txt
│   │   │       └── 2
│   │   │           ├── 2_11_c_10_2.png
│   │   │           └── 2_11_c_10_2.txt
│   │   ├── 11
│   │   │   ├── 2_11_c_11.pdf
│   │   │   ├── 2_11_c_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_11_1.png
│   │   │           └── 2_11_c_11_1.txt
│   │   ├── 12
│   │   │   ├── 2_11_c_12.pdf
│   │   │   ├── 2_11_c_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_12_1.png
│   │   │           └── 2_11_c_12_1.txt
│   │   ├── 13
│   │   │   ├── 2_11_c_13.pdf
│   │   │   ├── 2_11_c_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_13_1.png
│   │   │           └── 2_11_c_13_1.txt
│   │   ├── 14
│   │   │   ├── 2_11_c_14.pdf
│   │   │   ├── 2_11_c_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_14_1.png
│   │   │           └── 2_11_c_14_1.txt
│   │   ├── 15
│   │   │   ├── 2_11_c_15.pdf
│   │   │   ├── 2_11_c_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_15_1.png
│   │   │           └── 2_11_c_15_1.txt
│   │   ├── 16
│   │   │   ├── 2_11_c_16.pdf
│   │   │   ├── 2_11_c_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_16_1.png
│   │   │           └── 2_11_c_16_1.txt
│   │   ├── 17
│   │   │   ├── 2_11_c_17.pdf
│   │   │   ├── 2_11_c_17.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_17_1.png
│   │   │           └── 2_11_c_17_1.txt
│   │   ├── 18
│   │   │   ├── 2_11_c_18.pdf
│   │   │   ├── 2_11_c_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_18_1.png
│   │   │           └── 2_11_c_18_1.txt
│   │   ├── 19
│   │   │   ├── 2_11_c_19.pdf
│   │   │   ├── 2_11_c_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_19_1.png
│   │   │           └── 2_11_c_19_1.txt
│   │   ├── 2
│   │   │   ├── 2_11_c_2.pdf
│   │   │   ├── 2_11_c_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_2_1.png
│   │   │           └── 2_11_c_2_1.txt
│   │   ├── 20
│   │   │   ├── 2_11_c_20.pdf
│   │   │   ├── 2_11_c_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_20_1.png
│   │   │           └── 2_11_c_20_1.txt
│   │   ├── 21
│   │   │   ├── 2_11_c_21.pdf
│   │   │   ├── 2_11_c_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_21_1.png
│   │   │           └── 2_11_c_21_1.txt
│   │   ├── 3
│   │   │   ├── 2_11_c_3.pdf
│   │   │   ├── 2_11_c_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_3_1.png
│   │   │           └── 2_11_c_3_1.txt
│   │   ├── 4
│   │   │   ├── 2_11_c_4.pdf
│   │   │   ├── 2_11_c_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_4_1.png
│   │   │           └── 2_11_c_4_1.txt
│   │   ├── 5
│   │   │   ├── 2_11_c_5.pdf
│   │   │   ├── 2_11_c_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_11_c_5_1.png
│   │   │       │   └── 2_11_c_5_1.txt
│   │   │       └── 2
│   │   │           ├── 2_11_c_5_2.png
│   │   │           └── 2_11_c_5_2.txt
│   │   ├── 6
│   │   │   ├── 2_11_c_6.pdf
│   │   │   ├── 2_11_c_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_6_1.png
│   │   │           └── 2_11_c_6_1.txt
│   │   ├── 7
│   │   │   ├── 2_11_c_7.pdf
│   │   │   ├── 2_11_c_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_7_1.png
│   │   │           └── 2_11_c_7_1.txt
│   │   ├── 8
│   │   │   ├── 2_11_c_8.pdf
│   │   │   ├── 2_11_c_8.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_11_c_8_1.png
│   │   │           └── 2_11_c_8_1.txt
│   │   └── 9
│   │       ├── 2_11_c_9.pdf
│   │       ├── 2_11_c_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_11_c_9_1.png
│   │               └── 2_11_c_9_1.txt
│   └── raw_pdf
│       └── 2_11_c_raw.pdf
├── 2_12_cc_ceremonies
│   ├── docs
│   │   └── 1
│   │       ├── 2_12_cc_ceremonies_1.pdf
│   │       ├── 2_12_cc_ceremonies_1.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 2_12_cc_ceremonies_1_1.png
│   │           │   └── 2_12_cc_ceremonies_1_1.txt
│   │           └── 2
│   │               ├── 2_12_cc_ceremonies_1_2.png
│   │               └── 2_12_cc_ceremonies_1_2.txt
│   └── raw_pdf
│       └── 2_12_cc_ceremonies_raw.pdf
├── 2_13_cc_memoranda
│   ├── docs
│   │   └── 1
│   │       ├── 2_13_cc_memoranda_1.pdf
│   │       ├── 2_13_cc_memoranda_1.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 2_13_cc_memoranda_1_1.png
│   │           │   └── 2_13_cc_memoranda_1_1.txt
│   │           └── 2
│   │               ├── 2_13_cc_memoranda_1_2.png
│   │               └── 2_13_cc_memoranda_1_2.txt
│   └── raw_pdf
│       └── 2_13_cc_memoranda_raw.pdf
├── 2_15_cc_teaching_activities
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_15_cc_teaching_activities_1.pdf
│   │   │   ├── 2_15_cc_teaching_activities_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_15_cc_teaching_activities_1_1.png
│   │   │           └── 2_15_cc_teaching_activities_1_1.txt
│   │   ├── 2
│   │   │   ├── 2_15_cc_teaching_activities_2.pdf
│   │   │   ├── 2_15_cc_teaching_activities_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_15_cc_teaching_activities_2_1.png
│   │   │       │   └── 2_15_cc_teaching_activities_2_1.txt
│   │   │       └── 2
│   │   │           ├── 2_15_cc_teaching_activities_2_2.png
│   │   │           └── 2_15_cc_teaching_activities_2_2.txt
│   │   ├── 3
│   │   │   ├── 2_15_cc_teaching_activities_3.pdf
│   │   │   ├── 2_15_cc_teaching_activities_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_15_cc_teaching_activities_3_1.png
│   │   │           └── 2_15_cc_teaching_activities_3_1.txt
│   │   ├── 4
│   │   │   ├── 2_15_cc_teaching_activities_4.pdf
│   │   │   ├── 2_15_cc_teaching_activities_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_15_cc_teaching_activities_4_1.png
│   │   │       │   └── 2_15_cc_teaching_activities_4_1.txt
│   │   │       └── 2
│   │   │           ├── 2_15_cc_teaching_activities_4_2.png
│   │   │           └── 2_15_cc_teaching_activities_4_2.txt
│   │   ├── 5
│   │   │   ├── 2_15_cc_teaching_activities_5.pdf
│   │   │   ├── 2_15_cc_teaching_activities_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_15_cc_teaching_activities_5_1.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_1.txt
│   │   │       ├── 10
│   │   │       │   ├── 2_15_cc_teaching_activities_5_10.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_10.txt
│   │   │       ├── 11
│   │   │       │   ├── 2_15_cc_teaching_activities_5_11.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_11.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_15_cc_teaching_activities_5_2.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 2_15_cc_teaching_activities_5_3.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 2_15_cc_teaching_activities_5_4.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 2_15_cc_teaching_activities_5_5.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 2_15_cc_teaching_activities_5_6.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 2_15_cc_teaching_activities_5_7.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 2_15_cc_teaching_activities_5_8.png
│   │   │       │   └── 2_15_cc_teaching_activities_5_8.txt
│   │   │       └── 9
│   │   │           ├── 2_15_cc_teaching_activities_5_9.png
│   │   │           └── 2_15_cc_teaching_activities_5_9.txt
│   │   └── 6
│   │       ├── 2_15_cc_teaching_activities_6.pdf
│   │       ├── 2_15_cc_teaching_activities_6.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_15_cc_teaching_activities_6_1.png
│   │               └── 2_15_cc_teaching_activities_6_1.txt
│   └── raw_pdf
│       └── 2_15_cc_teaching_activities_raw.pdf
├── 2_16_f_j_corbato
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_16_f_j_corbato_1.pdf
│   │   │   ├── 2_16_f_j_corbato_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_16_f_j_corbato_1_1.png
│   │   │           └── 2_16_f_j_corbato_1_1.txt
│   │   ├── 2
│   │   │   ├── 2_16_f_j_corbato_2.pdf
│   │   │   ├── 2_16_f_j_corbato_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_16_f_j_corbato_2_1.png
│   │   │           └── 2_16_f_j_corbato_2_1.txt
│   │   ├── 3
│   │   │   ├── 2_16_f_j_corbato_3.pdf
│   │   │   ├── 2_16_f_j_corbato_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_16_f_j_corbato_3_1.png
│   │   │           └── 2_16_f_j_corbato_3_1.txt
│   │   └── 4
│   │       ├── 2_16_f_j_corbato_4.pdf
│   │       ├── 2_16_f_j_corbato_4.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_16_f_j_corbato_4_1.png
│   │               └── 2_16_f_j_corbato_4_1.txt
│   └── raw_pdf
│       └── 2_16_f_j_corbato_raw.pdf
├── 2_17_d
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_17_d_1.pdf
│   │   │   ├── 2_17_d_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_17_d_1_1.png
│   │   │           └── 2_17_d_1_1.txt
│   │   ├── 2
│   │   │   ├── 2_17_d_2.pdf
│   │   │   ├── 2_17_d_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_17_d_2_1.png
│   │   │           └── 2_17_d_2_1.txt
│   │   ├── 3
│   │   │   ├── 2_17_d_3.pdf
│   │   │   ├── 2_17_d_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_17_d_3_1.png
│   │   │           └── 2_17_d_3_1.txt
│   │   ├── 4
│   │   │   ├── 2_17_d_4.pdf
│   │   │   ├── 2_17_d_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_17_d_4_1.png
│   │   │           └── 2_17_d_4_1.txt
│   │   ├── 5
│   │   │   ├── 2_17_d_5.pdf
│   │   │   ├── 2_17_d_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_17_d_5_1.png
│   │   │           └── 2_17_d_5_1.txt
│   │   ├── 6
│   │   │   ├── 2_17_d_6.pdf
│   │   │   ├── 2_17_d_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_17_d_6_1.png
│   │   │       │   └── 2_17_d_6_1.txt
│   │   │       └── 2
│   │   │           ├── 2_17_d_6_2.png
│   │   │           └── 2_17_d_6_2.txt
│   │   └── 7
│   │       ├── 2_17_d_7.pdf
│   │       ├── 2_17_d_7.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 2_17_d_7_1.png
│   │           │   └── 2_17_d_7_1.txt
│   │           └── 2
│   │               ├── 2_17_d_7_2.png
│   │               └── 2_17_d_7_2.txt
│   └── raw_pdf
│       └── 2_17_d_raw.pdf
├── 2_18_d_s_r
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_18_d_s_r_1.pdf
│   │   │   ├── 2_18_d_s_r_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_18_d_s_r_1_1.png
│   │   │           └── 2_18_d_s_r_1_1.txt
│   │   └── 2
│   │       ├── 2_18_d_s_r_2.pdf
│   │       ├── 2_18_d_s_r_2.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_18_d_s_r_2_1.png
│   │               └── 2_18_d_s_r_2_1.txt
│   └── raw_pdf
│       └── 2_18_d_s_r_raw.pdf
├── 2_19_e
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_19_e_1.pdf
│   │   │   ├── 2_19_e_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_19_e_1_1.png
│   │   │           └── 2_19_e_1_1.txt
│   │   ├── 2
│   │   │   ├── 2_19_e_2.pdf
│   │   │   ├── 2_19_e_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_19_e_2_1.png
│   │   │           └── 2_19_e_2_1.txt
│   │   ├── 3
│   │   │   ├── 2_19_e_3.pdf
│   │   │   ├── 2_19_e_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_19_e_3_1.png
│   │   │           └── 2_19_e_3_1.txt
│   │   ├── 4
│   │   │   ├── 2_19_e_4.pdf
│   │   │   ├── 2_19_e_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_19_e_4_1.png
│   │   │           └── 2_19_e_4_1.txt
│   │   └── 5
│   │       ├── 2_19_e_5.pdf
│   │       ├── 2_19_e_5.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_19_e_5_1.png
│   │               └── 2_19_e_5_1.txt
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
├── 2_21_f
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_21_f_1.pdf
│   │   │   ├── 2_21_f_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_21_f_1_1.png
│   │   │           └── 2_21_f_1_1.txt
│   │   ├── 2
│   │   │   ├── 2_21_f_2.pdf
│   │   │   ├── 2_21_f_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_21_f_2_1.png
│   │   │           └── 2_21_f_2_1.txt
│   │   ├── 3
│   │   │   ├── 2_21_f_3.pdf
│   │   │   ├── 2_21_f_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_21_f_3_1.png
│   │   │           └── 2_21_f_3_1.txt
│   │   ├── 4
│   │   │   ├── 2_21_f_4.pdf
│   │   │   ├── 2_21_f_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_21_f_4_1.png
│   │   │       │   └── 2_21_f_4_1.txt
│   │   │       └── 2
│   │   │           ├── 2_21_f_4_2.png
│   │   │           └── 2_21_f_4_2.txt
│   │   ├── 5
│   │   │   ├── 2_21_f_5.pdf
│   │   │   ├── 2_21_f_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_21_f_5_1.png
│   │   │           └── 2_21_f_5_1.txt
│   │   ├── 6
│   │   │   ├── 2_21_f_6.pdf
│   │   │   ├── 2_21_f_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_21_f_6_1.png
│   │   │           └── 2_21_f_6_1.txt
│   │   ├── 7
│   │   │   ├── 2_21_f_7.pdf
│   │   │   ├── 2_21_f_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_21_f_7_1.png
│   │   │           └── 2_21_f_7_1.txt
│   │   ├── 8
│   │   │   ├── 2_21_f_8.pdf
│   │   │   ├── 2_21_f_8.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_21_f_8_1.png
│   │   │           └── 2_21_f_8_1.txt
│   │   └── 9
│   │       ├── 2_21_f_9.pdf
│   │       ├── 2_21_f_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_21_f_9_1.png
│   │               └── 2_21_f_9_1.txt
│   └── raw_pdf
│       └── 2_21_f_raw.pdf
├── 2_22_forrester_j_w
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_22_forrester_j_w_1.pdf
│   │   │   ├── 2_22_forrester_j_w_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_22_forrester_j_w_1_1.png
│   │   │       │   └── 2_22_forrester_j_w_1_1.txt
│   │   │       └── 2
│   │   │           ├── 2_22_forrester_j_w_1_2.png
│   │   │           └── 2_22_forrester_j_w_1_2.txt
│   │   ├── 2
│   │   │   ├── 2_22_forrester_j_w_2.pdf
│   │   │   ├── 2_22_forrester_j_w_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_22_forrester_j_w_2_1.png
│   │   │       │   └── 2_22_forrester_j_w_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_22_forrester_j_w_2_2.png
│   │   │       │   └── 2_22_forrester_j_w_2_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 2_22_forrester_j_w_2_3.png
│   │   │       │   └── 2_22_forrester_j_w_2_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 2_22_forrester_j_w_2_4.png
│   │   │       │   └── 2_22_forrester_j_w_2_4.txt
│   │   │       └── 5
│   │   │           ├── 2_22_forrester_j_w_2_5.png
│   │   │           └── 2_22_forrester_j_w_2_5.txt
│   │   ├── 3
│   │   │   ├── 2_22_forrester_j_w_3.pdf
│   │   │   ├── 2_22_forrester_j_w_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_22_forrester_j_w_3_1.png
│   │   │           └── 2_22_forrester_j_w_3_1.txt
│   │   ├── 4
│   │   │   ├── 2_22_forrester_j_w_4.pdf
│   │   │   ├── 2_22_forrester_j_w_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_22_forrester_j_w_4_1.png
│   │   │           └── 2_22_forrester_j_w_4_1.txt
│   │   ├── 5
│   │   │   ├── 2_22_forrester_j_w_5.pdf
│   │   │   ├── 2_22_forrester_j_w_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_22_forrester_j_w_5_1.png
│   │   │           └── 2_22_forrester_j_w_5_1.txt
│   │   └── 6
│   │       ├── 2_22_forrester_j_w_6.pdf
│   │       ├── 2_22_forrester_j_w_6.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_22_forrester_j_w_6_1.png
│   │               └── 2_22_forrester_j_w_6_1.txt
│   └── raw_pdf
│       └── 2_22_forrester_j_w_raw.pdf
├── 2_23_h
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_23_h_1.pdf
│   │   │   ├── 2_23_h_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_23_h_1_1.png
│   │   │           └── 2_23_h_1_1.txt
│   │   ├── 2
│   │   │   ├── 2_23_h_2.pdf
│   │   │   ├── 2_23_h_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_23_h_2_1.png
│   │   │       │   └── 2_23_h_2_1.txt
│   │   │       └── 2
│   │   │           ├── 2_23_h_2_2.png
│   │   │           └── 2_23_h_2_2.txt
│   │   └── 3
│   │       ├── 2_23_h_3.pdf
│   │       ├── 2_23_h_3.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_23_h_3_1.png
│   │               └── 2_23_h_3_1.txt
│   └── raw_pdf
│       └── 2_23_h_raw.pdf
├── 2_24_hildebrand_f_b
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_24_hildebrand_f_b_1.pdf
│   │   │   ├── 2_24_hildebrand_f_b_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_24_hildebrand_f_b_1_1.png
│   │   │       │   └── 2_24_hildebrand_f_b_1_1.txt
│   │   │       └── 2
│   │   │           ├── 2_24_hildebrand_f_b_1_2.png
│   │   │           └── 2_24_hildebrand_f_b_1_2.txt
│   │   ├── 2
│   │   │   ├── 2_24_hildebrand_f_b_2.pdf
│   │   │   ├── 2_24_hildebrand_f_b_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_24_hildebrand_f_b_2_1.png
│   │   │       │   └── 2_24_hildebrand_f_b_2_1.txt
│   │   │       └── 2
│   │   │           ├── 2_24_hildebrand_f_b_2_2.png
│   │   │           └── 2_24_hildebrand_f_b_2_2.txt
│   │   └── 3
│   │       ├── 2_24_hildebrand_f_b_3.pdf
│   │       ├── 2_24_hildebrand_f_b_3.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_24_hildebrand_f_b_3_1.png
│   │               └── 2_24_hildebrand_f_b_3_1.txt
│   └── raw_pdf
│       └── 2_24_hildebrand_f_b_raw.pdf
├── 2_26_i
│   ├── docs
│   │   ├── 3
│   │   │   ├── 2_26_i_3.pdf
│   │   │   ├── 2_26_i_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_26_i_3_1.png
│   │   │       │   └── 2_26_i_3_1.txt
│   │   │       └── 2
│   │   │           ├── 2_26_i_3_2.png
│   │   │           └── 2_26_i_3_2.txt
│   │   ├── 5
│   │   │   ├── 2_26_i_5.pdf
│   │   │   ├── 2_26_i_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_26_i_5_1.png
│   │   │           └── 2_26_i_5_1.txt
│   │   └── 6
│   │       ├── 2_26_i_6.pdf
│   │       ├── 2_26_i_6.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 2_26_i_6_1.png
│   │           │   └── 2_26_i_6_1.txt
│   │           └── 2
│   │               ├── 2_26_i_6_2.png
│   │               └── 2_26_i_6_2.txt
│   └── raw_pdf
│       └── 2_26_i_raw.pdf
├── 2_27_ibm_correspondence
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_27_ibm_correspondence_1.pdf
│   │   │   ├── 2_27_ibm_correspondence_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_1_1.png
│   │   │           └── 2_27_ibm_correspondence_1_1.txt
│   │   ├── 10
│   │   │   ├── 2_27_ibm_correspondence_10.pdf
│   │   │   ├── 2_27_ibm_correspondence_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_10_1.png
│   │   │           └── 2_27_ibm_correspondence_10_1.txt
│   │   ├── 11
│   │   │   ├── 2_27_ibm_correspondence_11.pdf
│   │   │   ├── 2_27_ibm_correspondence_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_11_1.png
│   │   │           └── 2_27_ibm_correspondence_11_1.txt
│   │   ├── 12
│   │   │   ├── 2_27_ibm_correspondence_12.pdf
│   │   │   ├── 2_27_ibm_correspondence_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_12_1.png
│   │   │           └── 2_27_ibm_correspondence_12_1.txt
│   │   ├── 13
│   │   │   ├── 2_27_ibm_correspondence_13.pdf
│   │   │   ├── 2_27_ibm_correspondence_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_13_1.png
│   │   │           └── 2_27_ibm_correspondence_13_1.txt
│   │   ├── 14
│   │   │   ├── 2_27_ibm_correspondence_14.pdf
│   │   │   ├── 2_27_ibm_correspondence_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_14_1.png
│   │   │           └── 2_27_ibm_correspondence_14_1.txt
│   │   ├── 15
│   │   │   ├── 2_27_ibm_correspondence_15.pdf
│   │   │   ├── 2_27_ibm_correspondence_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_15_1.png
│   │   │           └── 2_27_ibm_correspondence_15_1.txt
│   │   ├── 16
│   │   │   ├── 2_27_ibm_correspondence_16.pdf
│   │   │   ├── 2_27_ibm_correspondence_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_16_1.png
│   │   │           └── 2_27_ibm_correspondence_16_1.txt
│   │   ├── 17
│   │   │   ├── 2_27_ibm_correspondence_17.pdf
│   │   │   ├── 2_27_ibm_correspondence_17.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_27_ibm_correspondence_17_1.png
│   │   │       │   └── 2_27_ibm_correspondence_17_1.txt
│   │   │       └── 2
│   │   │           ├── 2_27_ibm_correspondence_17_2.png
│   │   │           └── 2_27_ibm_correspondence_17_2.txt
│   │   ├── 18
│   │   │   ├── 2_27_ibm_correspondence_18.pdf
│   │   │   ├── 2_27_ibm_correspondence_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_18_1.png
│   │   │           └── 2_27_ibm_correspondence_18_1.txt
│   │   ├── 19
│   │   │   ├── 2_27_ibm_correspondence_19.pdf
│   │   │   ├── 2_27_ibm_correspondence_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_19_1.png
│   │   │           └── 2_27_ibm_correspondence_19_1.txt
│   │   ├── 2
│   │   │   ├── 2_27_ibm_correspondence_2.pdf
│   │   │   ├── 2_27_ibm_correspondence_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_2_1.png
│   │   │           └── 2_27_ibm_correspondence_2_1.txt
│   │   ├── 20
│   │   │   ├── 2_27_ibm_correspondence_20.pdf
│   │   │   ├── 2_27_ibm_correspondence_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_20_1.png
│   │   │           └── 2_27_ibm_correspondence_20_1.txt
│   │   ├── 21
│   │   │   ├── 2_27_ibm_correspondence_21.pdf
│   │   │   ├── 2_27_ibm_correspondence_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_21_1.png
│   │   │           └── 2_27_ibm_correspondence_21_1.txt
│   │   ├── 22
│   │   │   ├── 2_27_ibm_correspondence_22.pdf
│   │   │   ├── 2_27_ibm_correspondence_22.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_22_1.png
│   │   │           └── 2_27_ibm_correspondence_22_1.txt
│   │   ├── 3
│   │   │   ├── 2_27_ibm_correspondence_3.pdf
│   │   │   ├── 2_27_ibm_correspondence_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_3_1.png
│   │   │           └── 2_27_ibm_correspondence_3_1.txt
│   │   ├── 4
│   │   │   ├── 2_27_ibm_correspondence_4.pdf
│   │   │   ├── 2_27_ibm_correspondence_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_4_1.png
│   │   │           └── 2_27_ibm_correspondence_4_1.txt
│   │   ├── 5
│   │   │   ├── 2_27_ibm_correspondence_5.pdf
│   │   │   ├── 2_27_ibm_correspondence_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_5_1.png
│   │   │           └── 2_27_ibm_correspondence_5_1.txt
│   │   ├── 6
│   │   │   ├── 2_27_ibm_correspondence_6.pdf
│   │   │   ├── 2_27_ibm_correspondence_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_6_1.png
│   │   │           └── 2_27_ibm_correspondence_6_1.txt
│   │   ├── 7
│   │   │   ├── 2_27_ibm_correspondence_7.pdf
│   │   │   ├── 2_27_ibm_correspondence_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_7_1.png
│   │   │           └── 2_27_ibm_correspondence_7_1.txt
│   │   ├── 8
│   │   │   ├── 2_27_ibm_correspondence_8.pdf
│   │   │   ├── 2_27_ibm_correspondence_8.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_27_ibm_correspondence_8_1.png
│   │   │           └── 2_27_ibm_correspondence_8_1.txt
│   │   └── 9
│   │       ├── 2_27_ibm_correspondence_9.pdf
│   │       ├── 2_27_ibm_correspondence_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_27_ibm_correspondence_9_1.png
│   │               └── 2_27_ibm_correspondence_9_1.txt
│   └── raw_pdf
│       └── 2_27_ibm_correspondence_raw.pdf
├── 2_29_j
│   ├── docs
│   │   ├── 2
│   │   │   ├── 2_29_j_2.pdf
│   │   │   ├── 2_29_j_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_29_j_2_1.png
│   │   │           └── 2_29_j_2_1.txt
│   │   ├── 3
│   │   │   ├── 2_29_j_3.pdf
│   │   │   ├── 2_29_j_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_29_j_3_1.png
│   │   │           └── 2_29_j_3_1.txt
│   │   ├── 4
│   │   │   ├── 2_29_j_4.pdf
│   │   │   ├── 2_29_j_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_29_j_4_1.png
│   │   │           └── 2_29_j_4_1.txt
│   │   └── 5
│   │       ├── 2_29_j_5.pdf
│   │       ├── 2_29_j_5.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_29_j_5_1.png
│   │               └── 2_29_j_5_1.txt
│   └── raw_pdf
│       └── 2_29_j_raw.pdf
├── 2_3_morse_correspondence_m_z
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_3_morse_correspondence_m_z_1.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_1_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_1_1.txt
│   │   ├── 10
│   │   │   ├── 2_3_morse_correspondence_m_z_10.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_10_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_10_1.txt
│   │   ├── 11
│   │   │   ├── 2_3_morse_correspondence_m_z_11.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_11.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_3_morse_correspondence_m_z_11_1.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_11_1.txt
│   │   │       └── 2
│   │   │           ├── 2_3_morse_correspondence_m_z_11_2.png
│   │   │           └── 2_3_morse_correspondence_m_z_11_2.txt
│   │   ├── 12
│   │   │   ├── 2_3_morse_correspondence_m_z_12.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_12_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_12_1.txt
│   │   ├── 13
│   │   │   ├── 2_3_morse_correspondence_m_z_13.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_13.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_3_morse_correspondence_m_z_13_1.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_13_1.txt
│   │   │       └── 2
│   │   │           ├── 2_3_morse_correspondence_m_z_13_2.png
│   │   │           └── 2_3_morse_correspondence_m_z_13_2.txt
│   │   ├── 14
│   │   │   ├── 2_3_morse_correspondence_m_z_14.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_14_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_14_1.txt
│   │   ├── 15
│   │   │   ├── 2_3_morse_correspondence_m_z_15.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_15_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_15_1.txt
│   │   ├── 16
│   │   │   ├── 2_3_morse_correspondence_m_z_16.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_16.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_16_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_16_1.txt
│   │   ├── 17
│   │   │   ├── 2_3_morse_correspondence_m_z_17.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_17.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_17_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_17_1.txt
│   │   ├── 18
│   │   │   ├── 2_3_morse_correspondence_m_z_18.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_18_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_18_1.txt
│   │   ├── 19
│   │   │   ├── 2_3_morse_correspondence_m_z_19.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_19_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_19_1.txt
│   │   ├── 2
│   │   │   ├── 2_3_morse_correspondence_m_z_2.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_2_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_2_1.txt
│   │   ├── 20
│   │   │   ├── 2_3_morse_correspondence_m_z_20.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_20_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_20_1.txt
│   │   ├── 21
│   │   │   ├── 2_3_morse_correspondence_m_z_21.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_21_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_21_1.txt
│   │   ├── 22
│   │   │   ├── 2_3_morse_correspondence_m_z_22.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_22.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_22_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_22_1.txt
│   │   ├── 23
│   │   │   ├── 2_3_morse_correspondence_m_z_23.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_23.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_23_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_23_1.txt
│   │   ├── 24
│   │   │   ├── 2_3_morse_correspondence_m_z_24.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_24.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_24_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_24_1.txt
│   │   ├── 25
│   │   │   ├── 2_3_morse_correspondence_m_z_25.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_25.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_25_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_25_1.txt
│   │   ├── 26
│   │   │   ├── 2_3_morse_correspondence_m_z_26.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_26.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_26_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_26_1.txt
│   │   ├── 27
│   │   │   ├── 2_3_morse_correspondence_m_z_27.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_27.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_3_morse_correspondence_m_z_27_1.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_27_1.txt
│   │   │       └── 2
│   │   │           ├── 2_3_morse_correspondence_m_z_27_2.png
│   │   │           └── 2_3_morse_correspondence_m_z_27_2.txt
│   │   ├── 28
│   │   │   ├── 2_3_morse_correspondence_m_z_28.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_28.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_28_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_28_1.txt
│   │   ├── 29
│   │   │   ├── 2_3_morse_correspondence_m_z_29.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_29.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_29_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_29_1.txt
│   │   ├── 3
│   │   │   ├── 2_3_morse_correspondence_m_z_3.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_3_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_3_1.txt
│   │   ├── 30
│   │   │   ├── 2_3_morse_correspondence_m_z_30.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_30.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_3_morse_correspondence_m_z_30_1.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_30_1.txt
│   │   │       └── 2
│   │   │           ├── 2_3_morse_correspondence_m_z_30_2.png
│   │   │           └── 2_3_morse_correspondence_m_z_30_2.txt
│   │   ├── 31
│   │   │   ├── 2_3_morse_correspondence_m_z_31.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_31.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_31_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_31_1.txt
│   │   ├── 32
│   │   │   ├── 2_3_morse_correspondence_m_z_32.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_32.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_32_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_32_1.txt
│   │   ├── 33
│   │   │   ├── 2_3_morse_correspondence_m_z_33.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_33.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_33_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_33_1.txt
│   │   ├── 34
│   │   │   ├── 2_3_morse_correspondence_m_z_34.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_34.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_34_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_34_1.txt
│   │   ├── 35
│   │   │   ├── 2_3_morse_correspondence_m_z_35.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_35.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_35_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_35_1.txt
│   │   ├── 37
│   │   │   ├── 2_3_morse_correspondence_m_z_37.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_37.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_37_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_37_1.txt
│   │   ├── 38
│   │   │   ├── 2_3_morse_correspondence_m_z_38.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_38.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_38_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_38_1.txt
│   │   ├── 39
│   │   │   ├── 2_3_morse_correspondence_m_z_39.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_39.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_39_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_39_1.txt
│   │   ├── 4
│   │   │   ├── 2_3_morse_correspondence_m_z_4.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_4.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_3_morse_correspondence_m_z_4_1.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_4_1.txt
│   │   │       └── 2
│   │   │           ├── 2_3_morse_correspondence_m_z_4_2.png
│   │   │           └── 2_3_morse_correspondence_m_z_4_2.txt
│   │   ├── 40
│   │   │   ├── 2_3_morse_correspondence_m_z_40.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_40.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_40_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_40_1.txt
│   │   ├── 41
│   │   │   ├── 2_3_morse_correspondence_m_z_41.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_41.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_41_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_41_1.txt
│   │   ├── 42
│   │   │   ├── 2_3_morse_correspondence_m_z_42.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_42.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_42_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_42_1.txt
│   │   ├── 43
│   │   │   ├── 2_3_morse_correspondence_m_z_43.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_43.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_43_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_43_1.txt
│   │   ├── 44
│   │   │   ├── 2_3_morse_correspondence_m_z_44.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_44.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_3_morse_correspondence_m_z_44_1.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_44_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_3_morse_correspondence_m_z_44_2.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_44_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 2_3_morse_correspondence_m_z_44_3.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_44_3.txt
│   │   │       └── 4
│   │   │           ├── 2_3_morse_correspondence_m_z_44_4.png
│   │   │           └── 2_3_morse_correspondence_m_z_44_4.txt
│   │   ├── 45
│   │   │   ├── 2_3_morse_correspondence_m_z_45.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_45.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_45_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_45_1.txt
│   │   ├── 46
│   │   │   ├── 2_3_morse_correspondence_m_z_46.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_46.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_46_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_46_1.txt
│   │   ├── 47
│   │   │   ├── 2_3_morse_correspondence_m_z_47.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_47.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_47_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_47_1.txt
│   │   ├── 48
│   │   │   ├── 2_3_morse_correspondence_m_z_48.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_48.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_48_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_48_1.txt
│   │   ├── 49
│   │   │   ├── 2_3_morse_correspondence_m_z_49.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_49.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_49_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_49_1.txt
│   │   ├── 5
│   │   │   ├── 2_3_morse_correspondence_m_z_5.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_5_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_5_1.txt
│   │   ├── 50
│   │   │   ├── 2_3_morse_correspondence_m_z_50.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_50.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_50_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_50_1.txt
│   │   ├── 51
│   │   │   ├── 2_3_morse_correspondence_m_z_51.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_51.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_51_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_51_1.txt
│   │   ├── 52
│   │   │   ├── 2_3_morse_correspondence_m_z_52.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_52.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_52_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_52_1.txt
│   │   ├── 53
│   │   │   ├── 2_3_morse_correspondence_m_z_53.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_53.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_53_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_53_1.txt
│   │   ├── 54
│   │   │   ├── 2_3_morse_correspondence_m_z_54.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_54.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_54_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_54_1.txt
│   │   ├── 55
│   │   │   ├── 2_3_morse_correspondence_m_z_55.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_55.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_55_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_55_1.txt
│   │   ├── 56
│   │   │   ├── 2_3_morse_correspondence_m_z_56.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_56.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_56_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_56_1.txt
│   │   ├── 57
│   │   │   ├── 2_3_morse_correspondence_m_z_57.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_57.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_57_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_57_1.txt
│   │   ├── 58
│   │   │   ├── 2_3_morse_correspondence_m_z_58.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_58.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_58_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_58_1.txt
│   │   ├── 59
│   │   │   ├── 2_3_morse_correspondence_m_z_59.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_59.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_59_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_59_1.txt
│   │   ├── 6
│   │   │   ├── 2_3_morse_correspondence_m_z_6.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_6_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_6_1.txt
│   │   ├── 7
│   │   │   ├── 2_3_morse_correspondence_m_z_7.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_3_morse_correspondence_m_z_7_1.png
│   │   │           └── 2_3_morse_correspondence_m_z_7_1.txt
│   │   ├── 8
│   │   │   ├── 2_3_morse_correspondence_m_z_8.pdf
│   │   │   ├── 2_3_morse_correspondence_m_z_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_3_morse_correspondence_m_z_8_1.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_8_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_3_morse_correspondence_m_z_8_2.png
│   │   │       │   └── 2_3_morse_correspondence_m_z_8_2.txt
│   │   │       └── 3
│   │   │           ├── 2_3_morse_correspondence_m_z_8_3.png
│   │   │           └── 2_3_morse_correspondence_m_z_8_3.txt
│   │   └── 9
│   │       ├── 2_3_morse_correspondence_m_z_9.pdf
│   │       ├── 2_3_morse_correspondence_m_z_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_3_morse_correspondence_m_z_9_1.png
│   │               └── 2_3_morse_correspondence_m_z_9_1.txt
│   └── raw_pdf
│       └── 2_3_morse_correspondence_m_z_raw.pdf
├── 2_5_morse_correspondence_a_g
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_5_morse_correspondence_a_g_1.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_1_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_1_1.txt
│   │   ├── 10
│   │   │   ├── 2_5_morse_correspondence_a_g_10.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_10_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_10_1.txt
│   │   ├── 11
│   │   │   ├── 2_5_morse_correspondence_a_g_11.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_11_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_11_1.txt
│   │   ├── 12
│   │   │   ├── 2_5_morse_correspondence_a_g_12.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_12_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_12_1.txt
│   │   ├── 13
│   │   │   ├── 2_5_morse_correspondence_a_g_13.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_13.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_13_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_13_1.txt
│   │   │       └── 2
│   │   │           ├── 2_5_morse_correspondence_a_g_13_2.png
│   │   │           └── 2_5_morse_correspondence_a_g_13_2.txt
│   │   ├── 14
│   │   │   ├── 2_5_morse_correspondence_a_g_14.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_14.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_14_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_14_1.txt
│   │   ├── 15
│   │   │   ├── 2_5_morse_correspondence_a_g_15.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_15_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_15_1.txt
│   │   ├── 16
│   │   │   ├── 2_5_morse_correspondence_a_g_16.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_16.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_16_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_16_1.txt
│   │   │       └── 2
│   │   │           ├── 2_5_morse_correspondence_a_g_16_2.png
│   │   │           └── 2_5_morse_correspondence_a_g_16_2.txt
│   │   ├── 17
│   │   │   ├── 2_5_morse_correspondence_a_g_17.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_17.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_17_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_17_1.txt
│   │   ├── 18
│   │   │   ├── 2_5_morse_correspondence_a_g_18.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_18_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_18_1.txt
│   │   ├── 19
│   │   │   ├── 2_5_morse_correspondence_a_g_19.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_19_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_19_1.txt
│   │   ├── 2
│   │   │   ├── 2_5_morse_correspondence_a_g_2.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_2_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_5_morse_correspondence_a_g_2_2.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_2_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 2_5_morse_correspondence_a_g_2_3.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_2_3.txt
│   │   │       └── 4
│   │   │           ├── 2_5_morse_correspondence_a_g_2_4.png
│   │   │           └── 2_5_morse_correspondence_a_g_2_4.txt
│   │   ├── 21
│   │   │   ├── 2_5_morse_correspondence_a_g_21.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_21_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_21_1.txt
│   │   ├── 22
│   │   │   ├── 2_5_morse_correspondence_a_g_22.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_22.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_22_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_22_1.txt
│   │   ├── 23
│   │   │   ├── 2_5_morse_correspondence_a_g_23.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_23.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_23_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_23_1.txt
│   │   ├── 24
│   │   │   ├── 2_5_morse_correspondence_a_g_24.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_24.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_24_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_24_1.txt
│   │   ├── 25
│   │   │   ├── 2_5_morse_correspondence_a_g_25.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_25.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_25_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_25_1.txt
│   │   │       └── 2
│   │   │           ├── 2_5_morse_correspondence_a_g_25_2.png
│   │   │           └── 2_5_morse_correspondence_a_g_25_2.txt
│   │   ├── 26
│   │   │   ├── 2_5_morse_correspondence_a_g_26.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_26.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_26_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_26_1.txt
│   │   ├── 27
│   │   │   ├── 2_5_morse_correspondence_a_g_27.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_27.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_27_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_27_1.txt
│   │   │       └── 2
│   │   │           ├── 2_5_morse_correspondence_a_g_27_2.png
│   │   │           └── 2_5_morse_correspondence_a_g_27_2.txt
│   │   ├── 28
│   │   │   ├── 2_5_morse_correspondence_a_g_28.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_28.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_28_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_28_1.txt
│   │   │       └── 2
│   │   │           ├── 2_5_morse_correspondence_a_g_28_2.png
│   │   │           └── 2_5_morse_correspondence_a_g_28_2.txt
│   │   ├── 29
│   │   │   ├── 2_5_morse_correspondence_a_g_29.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_29.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_29_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_29_1.txt
│   │   ├── 3
│   │   │   ├── 2_5_morse_correspondence_a_g_3.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_3_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_3_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_5_morse_correspondence_a_g_3_2.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_3_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 2_5_morse_correspondence_a_g_3_3.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_3_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 2_5_morse_correspondence_a_g_3_4.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_3_4.txt
│   │   │       └── 5
│   │   │           ├── 2_5_morse_correspondence_a_g_3_5.png
│   │   │           └── 2_5_morse_correspondence_a_g_3_5.txt
│   │   ├── 30
│   │   │   ├── 2_5_morse_correspondence_a_g_30.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_30.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_30_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_30_1.txt
│   │   ├── 31
│   │   │   ├── 2_5_morse_correspondence_a_g_31.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_31.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_31_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_31_1.txt
│   │   ├── 32
│   │   │   ├── 2_5_morse_correspondence_a_g_32.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_32.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_32_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_32_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_5_morse_correspondence_a_g_32_2.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_32_2.txt
│   │   │       └── 3
│   │   │           ├── 2_5_morse_correspondence_a_g_32_3.png
│   │   │           └── 2_5_morse_correspondence_a_g_32_3.txt
│   │   ├── 33
│   │   │   ├── 2_5_morse_correspondence_a_g_33.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_33.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_33_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_33_1.txt
│   │   ├── 4
│   │   │   ├── 2_5_morse_correspondence_a_g_4.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_4_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_4_1.txt
│   │   ├── 5
│   │   │   ├── 2_5_morse_correspondence_a_g_5.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_5_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_5_1.txt
│   │   ├── 6
│   │   │   ├── 2_5_morse_correspondence_a_g_6.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_5_morse_correspondence_a_g_6_1.png
│   │   │           └── 2_5_morse_correspondence_a_g_6_1.txt
│   │   ├── 7
│   │   │   ├── 2_5_morse_correspondence_a_g_7.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_7_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_7_1.txt
│   │   │       └── 2
│   │   │           ├── 2_5_morse_correspondence_a_g_7_2.png
│   │   │           └── 2_5_morse_correspondence_a_g_7_2.txt
│   │   ├── 8
│   │   │   ├── 2_5_morse_correspondence_a_g_8.pdf
│   │   │   ├── 2_5_morse_correspondence_a_g_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_5_morse_correspondence_a_g_8_1.png
│   │   │       │   └── 2_5_morse_correspondence_a_g_8_1.txt
│   │   │       └── 2
│   │   │           ├── 2_5_morse_correspondence_a_g_8_2.png
│   │   │           └── 2_5_morse_correspondence_a_g_8_2.txt
│   │   └── 9
│   │       ├── 2_5_morse_correspondence_a_g_9.pdf
│   │       ├── 2_5_morse_correspondence_a_g_9.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 2_5_morse_correspondence_a_g_9_1.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_1.txt
│   │           ├── 10
│   │           │   ├── 2_5_morse_correspondence_a_g_9_10.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_10.txt
│   │           ├── 11
│   │           │   ├── 2_5_morse_correspondence_a_g_9_11.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_11.txt
│   │           ├── 12
│   │           │   ├── 2_5_morse_correspondence_a_g_9_12.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_12.txt
│   │           ├── 13
│   │           │   ├── 2_5_morse_correspondence_a_g_9_13.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_13.txt
│   │           ├── 14
│   │           │   ├── 2_5_morse_correspondence_a_g_9_14.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_14.txt
│   │           ├── 15
│   │           │   ├── 2_5_morse_correspondence_a_g_9_15.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_15.txt
│   │           ├── 16
│   │           │   ├── 2_5_morse_correspondence_a_g_9_16.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_16.txt
│   │           ├── 17
│   │           │   ├── 2_5_morse_correspondence_a_g_9_17.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_17.txt
│   │           ├── 2
│   │           │   ├── 2_5_morse_correspondence_a_g_9_2.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_2.txt
│   │           ├── 3
│   │           │   ├── 2_5_morse_correspondence_a_g_9_3.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_3.txt
│   │           ├── 4
│   │           │   ├── 2_5_morse_correspondence_a_g_9_4.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_4.txt
│   │           ├── 5
│   │           │   ├── 2_5_morse_correspondence_a_g_9_5.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_5.txt
│   │           ├── 6
│   │           │   ├── 2_5_morse_correspondence_a_g_9_6.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_6.txt
│   │           ├── 7
│   │           │   ├── 2_5_morse_correspondence_a_g_9_7.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_7.txt
│   │           ├── 8
│   │           │   ├── 2_5_morse_correspondence_a_g_9_8.png
│   │           │   └── 2_5_morse_correspondence_a_g_9_8.txt
│   │           └── 9
│   │               ├── 2_5_morse_correspondence_a_g_9_9.png
│   │               └── 2_5_morse_correspondence_a_g_9_9.txt
│   └── raw_pdf
│       └── 2_5_morse_correspondence_a_g_raw.pdf
├── 2_7_association_for_computing_machinery
│   ├── docs
│   │   ├── 1
│   │   │   ├── 2_7_association_for_computing_machinery_1.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_1_1.png
│   │   │           └── 2_7_association_for_computing_machinery_1_1.txt
│   │   ├── 10
│   │   │   ├── 2_7_association_for_computing_machinery_10.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_10_1.png
│   │   │           └── 2_7_association_for_computing_machinery_10_1.txt
│   │   ├── 11
│   │   │   ├── 2_7_association_for_computing_machinery_11.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_11_1.png
│   │   │           └── 2_7_association_for_computing_machinery_11_1.txt
│   │   ├── 12
│   │   │   ├── 2_7_association_for_computing_machinery_12.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_12_1.png
│   │   │           └── 2_7_association_for_computing_machinery_12_1.txt
│   │   ├── 13
│   │   │   ├── 2_7_association_for_computing_machinery_13.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_13.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_13_1.png
│   │   │           └── 2_7_association_for_computing_machinery_13_1.txt
│   │   ├── 14
│   │   │   ├── 2_7_association_for_computing_machinery_14.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_14.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_7_association_for_computing_machinery_14_1.png
│   │   │       │   └── 2_7_association_for_computing_machinery_14_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_7_association_for_computing_machinery_14_2.png
│   │   │       │   └── 2_7_association_for_computing_machinery_14_2.txt
│   │   │       └── 3
│   │   │           ├── 2_7_association_for_computing_machinery_14_3.png
│   │   │           └── 2_7_association_for_computing_machinery_14_3.txt
│   │   ├── 15
│   │   │   ├── 2_7_association_for_computing_machinery_15.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_15_1.png
│   │   │           └── 2_7_association_for_computing_machinery_15_1.txt
│   │   ├── 2
│   │   │   ├── 2_7_association_for_computing_machinery_2.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_7_association_for_computing_machinery_2_1.png
│   │   │       │   └── 2_7_association_for_computing_machinery_2_1.txt
│   │   │       └── 2
│   │   │           ├── 2_7_association_for_computing_machinery_2_2.png
│   │   │           └── 2_7_association_for_computing_machinery_2_2.txt
│   │   ├── 3
│   │   │   ├── 2_7_association_for_computing_machinery_3.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_3_1.png
│   │   │           └── 2_7_association_for_computing_machinery_3_1.txt
│   │   ├── 4
│   │   │   ├── 2_7_association_for_computing_machinery_4.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_4_1.png
│   │   │           └── 2_7_association_for_computing_machinery_4_1.txt
│   │   ├── 5
│   │   │   ├── 2_7_association_for_computing_machinery_5.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_5_1.png
│   │   │           └── 2_7_association_for_computing_machinery_5_1.txt
│   │   ├── 6
│   │   │   ├── 2_7_association_for_computing_machinery_6.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_7_association_for_computing_machinery_6_1.png
│   │   │       │   └── 2_7_association_for_computing_machinery_6_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 2_7_association_for_computing_machinery_6_2.png
│   │   │       │   └── 2_7_association_for_computing_machinery_6_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 2_7_association_for_computing_machinery_6_3.png
│   │   │       │   └── 2_7_association_for_computing_machinery_6_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 2_7_association_for_computing_machinery_6_4.png
│   │   │       │   └── 2_7_association_for_computing_machinery_6_4.txt
│   │   │       └── 5
│   │   │           ├── 2_7_association_for_computing_machinery_6_5.png
│   │   │           └── 2_7_association_for_computing_machinery_6_5.txt
│   │   ├── 7
│   │   │   ├── 2_7_association_for_computing_machinery_7.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 2_7_association_for_computing_machinery_7_1.png
│   │   │           └── 2_7_association_for_computing_machinery_7_1.txt
│   │   ├── 8
│   │   │   ├── 2_7_association_for_computing_machinery_8.pdf
│   │   │   ├── 2_7_association_for_computing_machinery_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 2_7_association_for_computing_machinery_8_1.png
│   │   │       │   └── 2_7_association_for_computing_machinery_8_1.txt
│   │   │       └── 2
│   │   │           ├── 2_7_association_for_computing_machinery_8_2.png
│   │   │           └── 2_7_association_for_computing_machinery_8_2.txt
│   │   └── 9
│   │       ├── 2_7_association_for_computing_machinery_9.pdf
│   │       ├── 2_7_association_for_computing_machinery_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 2_7_association_for_computing_machinery_9_1.png
│   │               └── 2_7_association_for_computing_machinery_9_1.txt
│   └── raw_pdf
│       └── 2_7_association_for_computing_machinery_raw.pdf
├── 3_1_k
│   ├── docs
│   │   ├── 1
│   │   │   ├── 3_1_k_1.pdf
│   │   │   ├── 3_1_k_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_1_k_1_1.png
│   │   │           └── 3_1_k_1_1.txt
│   │   ├── 2
│   │   │   ├── 3_1_k_2.pdf
│   │   │   ├── 3_1_k_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_1_k_2_1.png
│   │   │           └── 3_1_k_2_1.txt
│   │   ├── 3
│   │   │   ├── 3_1_k_3.pdf
│   │   │   ├── 3_1_k_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_1_k_3_1.png
│   │   │           └── 3_1_k_3_1.txt
│   │   ├── 4
│   │   │   ├── 3_1_k_4.pdf
│   │   │   ├── 3_1_k_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_1_k_4_1.png
│   │   │           └── 3_1_k_4_1.txt
│   │   ├── 5
│   │   │   ├── 3_1_k_5.pdf
│   │   │   ├── 3_1_k_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_1_k_5_1.png
│   │   │           └── 3_1_k_5_1.txt
│   │   ├── 6
│   │   │   ├── 3_1_k_6.pdf
│   │   │   ├── 3_1_k_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_1_k_6_1.png
│   │   │           └── 3_1_k_6_1.txt
│   │   ├── 7
│   │   │   ├── 3_1_k_7.pdf
│   │   │   ├── 3_1_k_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_1_k_7_1.png
│   │   │           └── 3_1_k_7_1.txt
│   │   └── 8
│   │       ├── 3_1_k_8.pdf
│   │       ├── 3_1_k_8.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 3_1_k_8_1.png
│   │               └── 3_1_k_8_1.txt
│   └── raw_pdf
│       └── 3_1_k_raw.pdf
├── 3_2_korbel_j
│   ├── docs
│   │   ├── 1
│   │   │   ├── 3_2_korbel_j_1.pdf
│   │   │   ├── 3_2_korbel_j_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_2_korbel_j_1_1.png
│   │   │           └── 3_2_korbel_j_1_1.txt
│   │   ├── 2
│   │   │   ├── 3_2_korbel_j_2.pdf
│   │   │   ├── 3_2_korbel_j_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_2_korbel_j_2_1.png
│   │   │           └── 3_2_korbel_j_2_1.txt
│   │   └── 3
│   │       ├── 3_2_korbel_j_3.pdf
│   │       ├── 3_2_korbel_j_3.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 3_2_korbel_j_3_1.png
│   │           │   └── 3_2_korbel_j_3_1.txt
│   │           ├── 2
│   │           │   ├── 3_2_korbel_j_3_2.png
│   │           │   └── 3_2_korbel_j_3_2.txt
│   │           ├── 3
│   │           │   ├── 3_2_korbel_j_3_3.png
│   │           │   └── 3_2_korbel_j_3_3.txt
│   │           ├── 4
│   │           │   ├── 3_2_korbel_j_3_4.png
│   │           │   └── 3_2_korbel_j_3_4.txt
│   │           ├── 5
│   │           │   ├── 3_2_korbel_j_3_5.png
│   │           │   └── 3_2_korbel_j_3_5.txt
│   │           ├── 6
│   │           │   ├── 3_2_korbel_j_3_6.png
│   │           │   └── 3_2_korbel_j_3_6.txt
│   │           ├── 7
│   │           │   ├── 3_2_korbel_j_3_7.png
│   │           │   └── 3_2_korbel_j_3_7.txt
│   │           └── 8
│   │               ├── 3_2_korbel_j_3_8.png
│   │               └── 3_2_korbel_j_3_8.txt
│   └── raw_pdf
│       └── 3_2_korbel_j_raw.pdf
├── 3_32_verzuh
│   ├── docs
│   │   ├── 10
│   │   │   ├── 3_32_verzuh_10.pdf
│   │   │   ├── 3_32_verzuh_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_32_verzuh_10_1.png
│   │   │       │   └── 3_32_verzuh_10_1.txt
│   │   │       ├── 10
│   │   │       │   ├── 3_32_verzuh_10_10.png
│   │   │       │   └── 3_32_verzuh_10_10.txt
│   │   │       ├── 11
│   │   │       │   ├── 3_32_verzuh_10_11.png
│   │   │       │   └── 3_32_verzuh_10_11.txt
│   │   │       ├── 12
│   │   │       │   ├── 3_32_verzuh_10_12.png
│   │   │       │   └── 3_32_verzuh_10_12.txt
│   │   │       ├── 13
│   │   │       │   ├── 3_32_verzuh_10_13.png
│   │   │       │   └── 3_32_verzuh_10_13.txt
│   │   │       ├── 14
│   │   │       │   ├── 3_32_verzuh_10_14.png
│   │   │       │   └── 3_32_verzuh_10_14.txt
│   │   │       ├── 15
│   │   │       │   ├── 3_32_verzuh_10_15.png
│   │   │       │   └── 3_32_verzuh_10_15.txt
│   │   │       ├── 16
│   │   │       │   ├── 3_32_verzuh_10_16.png
│   │   │       │   └── 3_32_verzuh_10_16.txt
│   │   │       ├── 17
│   │   │       │   ├── 3_32_verzuh_10_17.png
│   │   │       │   └── 3_32_verzuh_10_17.txt
│   │   │       ├── 18
│   │   │       │   ├── 3_32_verzuh_10_18.png
│   │   │       │   └── 3_32_verzuh_10_18.txt
│   │   │       ├── 19
│   │   │       │   ├── 3_32_verzuh_10_19.png
│   │   │       │   └── 3_32_verzuh_10_19.txt
│   │   │       ├── 2
│   │   │       │   ├── 3_32_verzuh_10_2.png
│   │   │       │   └── 3_32_verzuh_10_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 3_32_verzuh_10_3.png
│   │   │       │   └── 3_32_verzuh_10_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 3_32_verzuh_10_4.png
│   │   │       │   └── 3_32_verzuh_10_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 3_32_verzuh_10_5.png
│   │   │       │   └── 3_32_verzuh_10_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 3_32_verzuh_10_6.png
│   │   │       │   └── 3_32_verzuh_10_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 3_32_verzuh_10_7.png
│   │   │       │   └── 3_32_verzuh_10_7.txt
│   │   │       ├── 8
│   │   │       │   ├── 3_32_verzuh_10_8.png
│   │   │       │   └── 3_32_verzuh_10_8.txt
│   │   │       └── 9
│   │   │           ├── 3_32_verzuh_10_9.png
│   │   │           └── 3_32_verzuh_10_9.txt
│   │   ├── 11
│   │   │   ├── 3_32_verzuh_11.pdf
│   │   │   ├── 3_32_verzuh_11.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_32_verzuh_11_1.png
│   │   │       │   └── 3_32_verzuh_11_1.txt
│   │   │       └── 2
│   │   │           ├── 3_32_verzuh_11_2.png
│   │   │           └── 3_32_verzuh_11_2.txt
│   │   ├── 3
│   │   │   ├── 3_32_verzuh_3.pdf
│   │   │   ├── 3_32_verzuh_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_32_verzuh_3_1.png
│   │   │           └── 3_32_verzuh_3_1.txt
│   │   ├── 4
│   │   │   ├── 3_32_verzuh_4.pdf
│   │   │   ├── 3_32_verzuh_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_32_verzuh_4_1.png
│   │   │           └── 3_32_verzuh_4_1.txt
│   │   ├── 5
│   │   │   ├── 3_32_verzuh_5.pdf
│   │   │   ├── 3_32_verzuh_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_32_verzuh_5_1.png
│   │   │           └── 3_32_verzuh_5_1.txt
│   │   ├── 6
│   │   │   ├── 3_32_verzuh_6.pdf
│   │   │   ├── 3_32_verzuh_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_32_verzuh_6_1.png
│   │   │           └── 3_32_verzuh_6_1.txt
│   │   ├── 7
│   │   │   ├── 3_32_verzuh_7.pdf
│   │   │   ├── 3_32_verzuh_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_32_verzuh_7_1.png
│   │   │       │   └── 3_32_verzuh_7_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 3_32_verzuh_7_2.png
│   │   │       │   └── 3_32_verzuh_7_2.txt
│   │   │       └── 3
│   │   │           ├── 3_32_verzuh_7_3.png
│   │   │           └── 3_32_verzuh_7_3.txt
│   │   ├── 8
│   │   │   ├── 3_32_verzuh_8.pdf
│   │   │   ├── 3_32_verzuh_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_32_verzuh_8_1.png
│   │   │       │   └── 3_32_verzuh_8_1.txt
│   │   │       └── 2
│   │   │           ├── 3_32_verzuh_8_2.png
│   │   │           └── 3_32_verzuh_8_2.txt
│   │   └── 9
│   │       ├── 3_32_verzuh_9.pdf
│   │       ├── 3_32_verzuh_9.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 3_32_verzuh_9_1.png
│   │           │   └── 3_32_verzuh_9_1.txt
│   │           └── 2
│   │               ├── 3_32_verzuh_9_2.png
│   │               └── 3_32_verzuh_9_2.txt
│   └── raw_pdf
│       └── 3_32_verzuh_raw.pdf
├── 3_3_l
│   ├── docs
│   │   ├── 1
│   │   │   ├── 3_3_l_1.pdf
│   │   │   ├── 3_3_l_1.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_3_l_1_1.png
│   │   │       │   └── 3_3_l_1_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 3_3_l_1_2.png
│   │   │       │   └── 3_3_l_1_2.txt
│   │   │       └── 3
│   │   │           ├── 3_3_l_1_3.png
│   │   │           └── 3_3_l_1_3.txt
│   │   ├── 2
│   │   │   ├── 3_3_l_2.pdf
│   │   │   ├── 3_3_l_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_3_l_2_1.png
│   │   │           └── 3_3_l_2_1.txt
│   │   └── 3
│   │       ├── 3_3_l_3.pdf
│   │       ├── 3_3_l_3.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 3_3_l_3_1.png
│   │               └── 3_3_l_3_1.txt
│   └── raw_pdf
│       └── 3_3_l_raw.pdf
├── 3_4_long_range_comp_study
│   ├── docs
│   │   ├── 1
│   │   │   ├── 3_4_long_range_comp_study_1.pdf
│   │   │   ├── 3_4_long_range_comp_study_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_4_long_range_comp_study_1_1.png
│   │   │           └── 3_4_long_range_comp_study_1_1.txt
│   │   ├── 2
│   │   │   ├── 3_4_long_range_comp_study_2.pdf
│   │   │   ├── 3_4_long_range_comp_study_2.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_4_long_range_comp_study_2_1.png
│   │   │       │   └── 3_4_long_range_comp_study_2_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 3_4_long_range_comp_study_2_2.png
│   │   │       │   └── 3_4_long_range_comp_study_2_2.txt
│   │   │       └── 3
│   │   │           ├── 3_4_long_range_comp_study_2_3.png
│   │   │           └── 3_4_long_range_comp_study_2_3.txt
│   │   └── 3
│   │       ├── 3_4_long_range_comp_study_3.pdf
│   │       ├── 3_4_long_range_comp_study_3.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 3_4_long_range_comp_study_3_1.png
│   │           │   └── 3_4_long_range_comp_study_3_1.txt
│   │           ├── 2
│   │           │   ├── 3_4_long_range_comp_study_3_2.png
│   │           │   └── 3_4_long_range_comp_study_3_2.txt
│   │           ├── 3
│   │           │   ├── 3_4_long_range_comp_study_3_3.png
│   │           │   └── 3_4_long_range_comp_study_3_3.txt
│   │           └── 4
│   │               ├── 3_4_long_range_comp_study_3_4.png
│   │               └── 3_4_long_range_comp_study_3_4.txt
│   └── raw_pdf
│       └── 3_4_long_range_comp_study_raw.pdf
├── 3_5_m
│   ├── docs
│   │   ├── 1
│   │   │   ├── 3_5_m_1.pdf
│   │   │   ├── 3_5_m_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_5_m_1_1.png
│   │   │           └── 3_5_m_1_1.txt
│   │   ├── 2
│   │   │   ├── 3_5_m_2.pdf
│   │   │   ├── 3_5_m_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_5_m_2_1.png
│   │   │           └── 3_5_m_2_1.txt
│   │   ├── 3
│   │   │   ├── 3_5_m_3.pdf
│   │   │   ├── 3_5_m_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_5_m_3_1.png
│   │   │       │   └── 3_5_m_3_1.txt
│   │   │       └── 2
│   │   │           ├── 3_5_m_3_2.png
│   │   │           └── 3_5_m_3_2.txt
│   │   ├── 4
│   │   │   ├── 3_5_m_4.pdf
│   │   │   ├── 3_5_m_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_5_m_4_1.png
│   │   │           └── 3_5_m_4_1.txt
│   │   ├── 5
│   │   │   ├── 3_5_m_5.pdf
│   │   │   ├── 3_5_m_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_5_m_5_1.png
│   │   │           └── 3_5_m_5_1.txt
│   │   └── 6
│   │       ├── 3_5_m_6.pdf
│   │       ├── 3_5_m_6.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 3_5_m_6_1.png
│   │               └── 3_5_m_6_1.txt
│   └── raw_pdf
│       └── 3_5_m_raw.pdf
├── 3_6_maine_med_center
│   ├── docs
│   │   ├── 1
│   │   │   ├── 3_6_maine_med_center_1.pdf
│   │   │   ├── 3_6_maine_med_center_1.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_6_maine_med_center_1_1.png
│   │   │           └── 3_6_maine_med_center_1_1.txt
│   │   ├── 10
│   │   │   ├── 3_6_maine_med_center_10.pdf
│   │   │   ├── 3_6_maine_med_center_10.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_6_maine_med_center_10_1.png
│   │   │       │   └── 3_6_maine_med_center_10_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 3_6_maine_med_center_10_2.png
│   │   │       │   └── 3_6_maine_med_center_10_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 3_6_maine_med_center_10_3.png
│   │   │       │   └── 3_6_maine_med_center_10_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 3_6_maine_med_center_10_4.png
│   │   │       │   └── 3_6_maine_med_center_10_4.txt
│   │   │       ├── 5
│   │   │       │   ├── 3_6_maine_med_center_10_5.png
│   │   │       │   └── 3_6_maine_med_center_10_5.txt
│   │   │       ├── 6
│   │   │       │   ├── 3_6_maine_med_center_10_6.png
│   │   │       │   └── 3_6_maine_med_center_10_6.txt
│   │   │       ├── 7
│   │   │       │   ├── 3_6_maine_med_center_10_7.png
│   │   │       │   └── 3_6_maine_med_center_10_7.txt
│   │   │       └── 8
│   │   │           ├── 3_6_maine_med_center_10_8.png
│   │   │           └── 3_6_maine_med_center_10_8.txt
│   │   ├── 2
│   │   │   ├── 3_6_maine_med_center_2.pdf
│   │   │   ├── 3_6_maine_med_center_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_6_maine_med_center_2_1.png
│   │   │           └── 3_6_maine_med_center_2_1.txt
│   │   ├── 3
│   │   │   ├── 3_6_maine_med_center_3.pdf
│   │   │   ├── 3_6_maine_med_center_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_6_maine_med_center_3_1.png
│   │   │       │   └── 3_6_maine_med_center_3_1.txt
│   │   │       └── 2
│   │   │           ├── 3_6_maine_med_center_3_2.png
│   │   │           └── 3_6_maine_med_center_3_2.txt
│   │   ├── 5
│   │   │   ├── 3_6_maine_med_center_5.pdf
│   │   │   ├── 3_6_maine_med_center_5.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_6_maine_med_center_5_1.png
│   │   │       │   └── 3_6_maine_med_center_5_1.txt
│   │   │       └── 2
│   │   │           ├── 3_6_maine_med_center_5_2.png
│   │   │           └── 3_6_maine_med_center_5_2.txt
│   │   ├── 6
│   │   │   ├── 3_6_maine_med_center_6.pdf
│   │   │   ├── 3_6_maine_med_center_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_6_maine_med_center_6_1.png
│   │   │       │   └── 3_6_maine_med_center_6_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 3_6_maine_med_center_6_2.png
│   │   │       │   └── 3_6_maine_med_center_6_2.txt
│   │   │       ├── 3
│   │   │       │   ├── 3_6_maine_med_center_6_3.png
│   │   │       │   └── 3_6_maine_med_center_6_3.txt
│   │   │       ├── 4
│   │   │       │   ├── 3_6_maine_med_center_6_4.png
│   │   │       │   └── 3_6_maine_med_center_6_4.txt
│   │   │       └── 5
│   │   │           ├── 3_6_maine_med_center_6_5.png
│   │   │           └── 3_6_maine_med_center_6_5.txt
│   │   ├── 7
│   │   │   ├── 3_6_maine_med_center_7.pdf
│   │   │   ├── 3_6_maine_med_center_7.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_6_maine_med_center_7_1.png
│   │   │       │   └── 3_6_maine_med_center_7_1.txt
│   │   │       └── 2
│   │   │           ├── 3_6_maine_med_center_7_2.png
│   │   │           └── 3_6_maine_med_center_7_2.txt
│   │   ├── 8
│   │   │   ├── 3_6_maine_med_center_8.pdf
│   │   │   ├── 3_6_maine_med_center_8.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_6_maine_med_center_8_1.png
│   │   │       │   └── 3_6_maine_med_center_8_1.txt
│   │   │       └── 2
│   │   │           ├── 3_6_maine_med_center_8_2.png
│   │   │           └── 3_6_maine_med_center_8_2.txt
│   │   └── 9
│   │       ├── 3_6_maine_med_center_9.pdf
│   │       ├── 3_6_maine_med_center_9.txt
│   │       └── pages
│   │           ├── 1
│   │           │   ├── 3_6_maine_med_center_9_1.png
│   │           │   └── 3_6_maine_med_center_9_1.txt
│   │           ├── 2
│   │           │   ├── 3_6_maine_med_center_9_2.png
│   │           │   └── 3_6_maine_med_center_9_2.txt
│   │           └── 3
│   │               ├── 3_6_maine_med_center_9_3.png
│   │               └── 3_6_maine_med_center_9_3.txt
│   └── raw_pdf
│       └── 3_6_maine_med_center_raw.pdf
├── 3_7_matill_j_i
│   ├── docs
│   │   ├── 2
│   │   │   ├── 3_7_matill_j_i_2.pdf
│   │   │   ├── 3_7_matill_j_i_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_7_matill_j_i_2_1.png
│   │   │           └── 3_7_matill_j_i_2_1.txt
│   │   ├── 3
│   │   │   ├── 3_7_matill_j_i_3.pdf
│   │   │   ├── 3_7_matill_j_i_3.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_7_matill_j_i_3_1.png
│   │   │       │   └── 3_7_matill_j_i_3_1.txt
│   │   │       ├── 2
│   │   │       │   ├── 3_7_matill_j_i_3_2.png
│   │   │       │   └── 3_7_matill_j_i_3_2.txt
│   │   │       └── 3
│   │   │           ├── 3_7_matill_j_i_3_3.png
│   │   │           └── 3_7_matill_j_i_3_3.txt
│   │   ├── 6
│   │   │   ├── 3_7_matill_j_i_6.pdf
│   │   │   ├── 3_7_matill_j_i_6.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_7_matill_j_i_6_1.png
│   │   │           └── 3_7_matill_j_i_6_1.txt
│   │   ├── 7
│   │   │   ├── 3_7_matill_j_i_7.pdf
│   │   │   ├── 3_7_matill_j_i_7.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_7_matill_j_i_7_1.png
│   │   │           └── 3_7_matill_j_i_7_1.txt
│   │   └── 8
│   │       ├── 3_7_matill_j_i_8.pdf
│   │       ├── 3_7_matill_j_i_8.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 3_7_matill_j_i_8_1.png
│   │               └── 3_7_matill_j_i_8_1.txt
│   └── raw_pdf
│       └── 3_7_matill_j_i_raw.pdf
├── 3_9_morse_1950_1955
│   ├── docs
│   │   ├── 10
│   │   │   ├── 3_9_morse_1950_1955_10.pdf
│   │   │   ├── 3_9_morse_1950_1955_10.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_10_1.png
│   │   │           └── 3_9_morse_1950_1955_10_1.txt
│   │   ├── 11
│   │   │   ├── 3_9_morse_1950_1955_11.pdf
│   │   │   ├── 3_9_morse_1950_1955_11.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_11_1.png
│   │   │           └── 3_9_morse_1950_1955_11_1.txt
│   │   ├── 12
│   │   │   ├── 3_9_morse_1950_1955_12.pdf
│   │   │   ├── 3_9_morse_1950_1955_12.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_12_1.png
│   │   │           └── 3_9_morse_1950_1955_12_1.txt
│   │   ├── 13
│   │   │   ├── 3_9_morse_1950_1955_13.pdf
│   │   │   ├── 3_9_morse_1950_1955_13.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_9_morse_1950_1955_13_1.png
│   │   │       │   └── 3_9_morse_1950_1955_13_1.txt
│   │   │       └── 2
│   │   │           ├── 3_9_morse_1950_1955_13_2.png
│   │   │           └── 3_9_morse_1950_1955_13_2.txt
│   │   ├── 15
│   │   │   ├── 3_9_morse_1950_1955_15.pdf
│   │   │   ├── 3_9_morse_1950_1955_15.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_15_1.png
│   │   │           └── 3_9_morse_1950_1955_15_1.txt
│   │   ├── 16
│   │   │   ├── 3_9_morse_1950_1955_16.pdf
│   │   │   ├── 3_9_morse_1950_1955_16.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_9_morse_1950_1955_16_1.png
│   │   │       │   └── 3_9_morse_1950_1955_16_1.txt
│   │   │       └── 2
│   │   │           ├── 3_9_morse_1950_1955_16_2.png
│   │   │           └── 3_9_morse_1950_1955_16_2.txt
│   │   ├── 18
│   │   │   ├── 3_9_morse_1950_1955_18.pdf
│   │   │   ├── 3_9_morse_1950_1955_18.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_18_1.png
│   │   │           └── 3_9_morse_1950_1955_18_1.txt
│   │   ├── 19
│   │   │   ├── 3_9_morse_1950_1955_19.pdf
│   │   │   ├── 3_9_morse_1950_1955_19.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_19_1.png
│   │   │           └── 3_9_morse_1950_1955_19_1.txt
│   │   ├── 2
│   │   │   ├── 3_9_morse_1950_1955_2.pdf
│   │   │   ├── 3_9_morse_1950_1955_2.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_2_1.png
│   │   │           └── 3_9_morse_1950_1955_2_1.txt
│   │   ├── 20
│   │   │   ├── 3_9_morse_1950_1955_20.pdf
│   │   │   ├── 3_9_morse_1950_1955_20.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_20_1.png
│   │   │           └── 3_9_morse_1950_1955_20_1.txt
│   │   ├── 21
│   │   │   ├── 3_9_morse_1950_1955_21.pdf
│   │   │   ├── 3_9_morse_1950_1955_21.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_21_1.png
│   │   │           └── 3_9_morse_1950_1955_21_1.txt
│   │   ├── 22
│   │   │   ├── 3_9_morse_1950_1955_22.pdf
│   │   │   ├── 3_9_morse_1950_1955_22.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_22_1.png
│   │   │           └── 3_9_morse_1950_1955_22_1.txt
│   │   ├── 23
│   │   │   ├── 3_9_morse_1950_1955_23.pdf
│   │   │   ├── 3_9_morse_1950_1955_23.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_23_1.png
│   │   │           └── 3_9_morse_1950_1955_23_1.txt
│   │   ├── 24
│   │   │   ├── 3_9_morse_1950_1955_24.pdf
│   │   │   ├── 3_9_morse_1950_1955_24.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_24_1.png
│   │   │           └── 3_9_morse_1950_1955_24_1.txt
│   │   ├── 25
│   │   │   ├── 3_9_morse_1950_1955_25.pdf
│   │   │   ├── 3_9_morse_1950_1955_25.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_25_1.png
│   │   │           └── 3_9_morse_1950_1955_25_1.txt
│   │   ├── 26
│   │   │   ├── 3_9_morse_1950_1955_26.pdf
│   │   │   ├── 3_9_morse_1950_1955_26.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_26_1.png
│   │   │           └── 3_9_morse_1950_1955_26_1.txt
│   │   ├── 27
│   │   │   ├── 3_9_morse_1950_1955_27.pdf
│   │   │   ├── 3_9_morse_1950_1955_27.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_27_1.png
│   │   │           └── 3_9_morse_1950_1955_27_1.txt
│   │   ├── 28
│   │   │   ├── 3_9_morse_1950_1955_28.pdf
│   │   │   ├── 3_9_morse_1950_1955_28.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_28_1.png
│   │   │           └── 3_9_morse_1950_1955_28_1.txt
│   │   ├── 29
│   │   │   ├── 3_9_morse_1950_1955_29.pdf
│   │   │   ├── 3_9_morse_1950_1955_29.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_29_1.png
│   │   │           └── 3_9_morse_1950_1955_29_1.txt
│   │   ├── 3
│   │   │   ├── 3_9_morse_1950_1955_3.pdf
│   │   │   ├── 3_9_morse_1950_1955_3.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_3_1.png
│   │   │           └── 3_9_morse_1950_1955_3_1.txt
│   │   ├── 30
│   │   │   ├── 3_9_morse_1950_1955_30.pdf
│   │   │   ├── 3_9_morse_1950_1955_30.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_30_1.png
│   │   │           └── 3_9_morse_1950_1955_30_1.txt
│   │   ├── 31
│   │   │   ├── 3_9_morse_1950_1955_31.pdf
│   │   │   ├── 3_9_morse_1950_1955_31.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_31_1.png
│   │   │           └── 3_9_morse_1950_1955_31_1.txt
│   │   ├── 32
│   │   │   ├── 3_9_morse_1950_1955_32.pdf
│   │   │   ├── 3_9_morse_1950_1955_32.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_32_1.png
│   │   │           └── 3_9_morse_1950_1955_32_1.txt
│   │   ├── 33
│   │   │   ├── 3_9_morse_1950_1955_33.pdf
│   │   │   ├── 3_9_morse_1950_1955_33.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_33_1.png
│   │   │           └── 3_9_morse_1950_1955_33_1.txt
│   │   ├── 34
│   │   │   ├── 3_9_morse_1950_1955_34.pdf
│   │   │   ├── 3_9_morse_1950_1955_34.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_34_1.png
│   │   │           └── 3_9_morse_1950_1955_34_1.txt
│   │   ├── 35
│   │   │   ├── 3_9_morse_1950_1955_35.pdf
│   │   │   ├── 3_9_morse_1950_1955_35.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_9_morse_1950_1955_35_1.png
│   │   │       │   └── 3_9_morse_1950_1955_35_1.txt
│   │   │       └── 2
│   │   │           ├── 3_9_morse_1950_1955_35_2.png
│   │   │           └── 3_9_morse_1950_1955_35_2.txt
│   │   ├── 37
│   │   │   ├── 3_9_morse_1950_1955_37.pdf
│   │   │   ├── 3_9_morse_1950_1955_37.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_37_1.png
│   │   │           └── 3_9_morse_1950_1955_37_1.txt
│   │   ├── 38
│   │   │   ├── 3_9_morse_1950_1955_38.pdf
│   │   │   ├── 3_9_morse_1950_1955_38.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_9_morse_1950_1955_38_1.png
│   │   │       │   └── 3_9_morse_1950_1955_38_1.txt
│   │   │       └── 2
│   │   │           ├── 3_9_morse_1950_1955_38_2.png
│   │   │           └── 3_9_morse_1950_1955_38_2.txt
│   │   ├── 4
│   │   │   ├── 3_9_morse_1950_1955_4.pdf
│   │   │   ├── 3_9_morse_1950_1955_4.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_4_1.png
│   │   │           └── 3_9_morse_1950_1955_4_1.txt
│   │   ├── 40
│   │   │   ├── 3_9_morse_1950_1955_40.pdf
│   │   │   ├── 3_9_morse_1950_1955_40.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_9_morse_1950_1955_40_1.png
│   │   │       │   └── 3_9_morse_1950_1955_40_1.txt
│   │   │       └── 2
│   │   │           ├── 3_9_morse_1950_1955_40_2.png
│   │   │           └── 3_9_morse_1950_1955_40_2.txt
│   │   ├── 42
│   │   │   ├── 3_9_morse_1950_1955_42.pdf
│   │   │   ├── 3_9_morse_1950_1955_42.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_42_1.png
│   │   │           └── 3_9_morse_1950_1955_42_1.txt
│   │   ├── 43
│   │   │   ├── 3_9_morse_1950_1955_43.pdf
│   │   │   ├── 3_9_morse_1950_1955_43.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_43_1.png
│   │   │           └── 3_9_morse_1950_1955_43_1.txt
│   │   ├── 44
│   │   │   ├── 3_9_morse_1950_1955_44.pdf
│   │   │   ├── 3_9_morse_1950_1955_44.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_44_1.png
│   │   │           └── 3_9_morse_1950_1955_44_1.txt
│   │   ├── 45
│   │   │   ├── 3_9_morse_1950_1955_45.pdf
│   │   │   ├── 3_9_morse_1950_1955_45.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_45_1.png
│   │   │           └── 3_9_morse_1950_1955_45_1.txt
│   │   ├── 46
│   │   │   ├── 3_9_morse_1950_1955_46.pdf
│   │   │   ├── 3_9_morse_1950_1955_46.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_9_morse_1950_1955_46_1.png
│   │   │       │   └── 3_9_morse_1950_1955_46_1.txt
│   │   │       └── 2
│   │   │           ├── 3_9_morse_1950_1955_46_2.png
│   │   │           └── 3_9_morse_1950_1955_46_2.txt
│   │   ├── 48
│   │   │   ├── 3_9_morse_1950_1955_48.pdf
│   │   │   ├── 3_9_morse_1950_1955_48.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_9_morse_1950_1955_48_1.png
│   │   │       │   └── 3_9_morse_1950_1955_48_1.txt
│   │   │       └── 2
│   │   │           ├── 3_9_morse_1950_1955_48_2.png
│   │   │           └── 3_9_morse_1950_1955_48_2.txt
│   │   ├── 5
│   │   │   ├── 3_9_morse_1950_1955_5.pdf
│   │   │   ├── 3_9_morse_1950_1955_5.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_5_1.png
│   │   │           └── 3_9_morse_1950_1955_5_1.txt
│   │   ├── 50
│   │   │   ├── 3_9_morse_1950_1955_50.pdf
│   │   │   ├── 3_9_morse_1950_1955_50.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_9_morse_1950_1955_50_1.png
│   │   │       │   └── 3_9_morse_1950_1955_50_1.txt
│   │   │       └── 2
│   │   │           ├── 3_9_morse_1950_1955_50_2.png
│   │   │           └── 3_9_morse_1950_1955_50_2.txt
│   │   ├── 6
│   │   │   ├── 3_9_morse_1950_1955_6.pdf
│   │   │   ├── 3_9_morse_1950_1955_6.txt
│   │   │   └── pages
│   │   │       ├── 1
│   │   │       │   ├── 3_9_morse_1950_1955_6_1.png
│   │   │       │   └── 3_9_morse_1950_1955_6_1.txt
│   │   │       └── 2
│   │   │           ├── 3_9_morse_1950_1955_6_2.png
│   │   │           └── 3_9_morse_1950_1955_6_2.txt
│   │   ├── 8
│   │   │   ├── 3_9_morse_1950_1955_8.pdf
│   │   │   ├── 3_9_morse_1950_1955_8.txt
│   │   │   └── pages
│   │   │       └── 1
│   │   │           ├── 3_9_morse_1950_1955_8_1.png
│   │   │           └── 3_9_morse_1950_1955_8_1.txt
│   │   └── 9
│   │       ├── 3_9_morse_1950_1955_9.pdf
│   │       ├── 3_9_morse_1950_1955_9.txt
│   │       └── pages
│   │           └── 1
│   │               ├── 3_9_morse_1950_1955_9_1.png
│   │               └── 3_9_morse_1950_1955_9_1.txt
│   └── raw_pdf
│       └── 3_9_morse_1950_1955_raw.pdf
├── aws_docs.txt
└── tree.txt

3187 directories, 4533 files


```
