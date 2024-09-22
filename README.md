[![Format](https://github.com/nogibjj/Meron_Gedrago_miniprjt3/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_miniprjt3/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/Meron_Gedrago_miniprjt3/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_miniprjt3/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/Meron_Gedrago_miniprjt3/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_miniprjt3/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/Meron_Gedrago_miniprjt3/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Meron_Gedrago_miniprjt3/actions/workflows/test.yml)

# Meron_Gedrago_Individual_project1 

Welcome to the third mini project for Data Engineering!

## Structure for this project 

This project serves as an introduction to polars, this project is a recreation of my [Individual Project 1](https://github.com/nogibjj/Meron_Gedrago_individual1) with polars. Similarly to the individual project, we use polars to read and describe the data, as well as use matplotlib to visualize the data. Find below the structure of the project

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

Source of the data: [the National Vital Statistics System](https://catalog.data.gov/dataset/drug-overdose-death-rates-by-drug-type-sex-age-race-and-hispanic-origin-united-states-3f72f/resource/e8eca080-11f4-4ff6-85f6-5476093f5361)

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
- [Individual Project 1](https://github.com/nogibjj/Meron_Gedrago_individual1)
- [Meron Gedrago Data Engineering mini project 2](https://github.com/nogibjj/Meron_Gedrago_miniprojt2)
- [Meron Gedrago Data Engineering mini project 1](https://github.com/nogibjj/Meron_Gedrago_miniproject1)

