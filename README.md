[![Format](https://github.com/nogibjj/Meron_Gedrago_individual1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_individual1/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/Meron_Gedrago_individual1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_individual1/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/Meron_Gedrago_individual1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_individual1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/Meron_Gedrago_individual1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_individual1/actions/workflows/test.yml)


# Meron_Gedrago_Individual_project1 

Welcome to the first individual project for Data Engineering!

## Structure for this project 

This project aims to build on top of the the second mini project (Meron_Gedrago_miniproject2) where we worked on reading csv files using pandas and visualizing a dataset. In this project, we will create a library of function which will serve a source of functions for the python script and jupyter notebook we will create. Additionally, we will be creating separate badges for different CI actions and lint using rust. Find below the structure of the project

```
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       ├── test.yml
├── mylib/
│   └── lib.py
├── .gitignore
├── Requirements.txt
├── Makefile
├── README.md
├── main.py
├── main.ipynb
├── Data_visual.png
├── test.csv
├── test_lib.csv
└── test_main.py

```

## Purpose of this project and findings 

Source of the dataset: https://catalog.data.gov/dataset/drug-overdose-death-rates-by-drug-type-sex-age-race-and-hispanic-origin-united-states-3f72f/resource/e8eca080-11f4-4ff6-85f6-5476093f5361 

The dataset looks at the death in the United States over the years due to drugs. The data has multiple columns and breaks down where the death rates are coming from. For this project, 
I will just be focusing on looking at the trend of death rates over the year. Therefore, I had to filter the dataset in *MG_main.py*. 
From the analysis, there is an average of 12-13 per 100,000 people losing their lives due to drugs and that the number was at its low when this rate was 6 in 1999 and has been steadily increasing since then with a small decrease in 2017. 

```
The mean is 12.45; the median is 12.05; the standard deviation is 4.507012080606934
The max is 21.6 and the min is 6.0

```


<img src="Data_visual.png" alt="alt text" width="1000">



## References 
**Previous projects**
- ([Meron Gedrago Data Engineering mini project 1](https://github.com/nogibjj/Meron_Gedrago_miniproject1))
- [Meron Gedrago Data Engineering mini project 2](https://github.com/nogibjj/Meron_Gedrago_miniprojt2)