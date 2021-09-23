# Searching for the Best Chopped Episodes to Rerun

## *Chopped* Recommendation Engine
Author: Mikhaela Martin

### Introduction

Chopped is one of my favorite television shows. I have yet to watch every episode, but I have watched the same episode multiple times. And not on purpose. Television networks rerun the same episodes because they know their audience enjoys them. 

### Business Objectives:

Based off this [article](https://screenrant.com/chopped-best-episodes-imdb/) which pinpoints the top 10 favorited Chopped episodes, I want to recommend 10 more episodes for The Food Network to rerun.

### Model Objective:

1. Visualize patterns across all episodes

![](https://github.com/mikhaelamartin/Chopped-Recommendations/blob/master/images/PCA%20Plot.png)

2. Interpret visualization pertaining to top 10 favorited episodes

A majority of the most popular shows emphasized either the judges, familiar faces, or family. The viewers love the judges' personalities and interactions with each other which is why "Judges' Face-Off' and 'Chopped All-Stars: Judges are part of the pack. The audience also loves cooking shows in general which is why "Crunch Time" and "Chopped All-Stars: Food Network vs. Cooking Channel" are also fan faves. Lastly, the viewers are very sentimental beings which is why the first aired episode, "Ocotpus, Duck, Animal Crackers" and "It's a Sibling Thing" are the top two episodes.

Our clusters somewhat capture this sentiment. Celebrity/Charity episodes 

![](https://github.com/mikhaelamartin/Chopped-Recommendations/blob/master/top10.png)

Four of the top 10 episodes were grouped in the Celebs/Charity cluster. Viewers tend to favor familiar faces and big personalities. 
Four of the top 10 episodes were grouped in the NY cluster. Viewers tend to favor 

Family-related episodes (Thanksgiving, Sibling Time)

3. Recommend episodes similar to the top 10 favorited episodes

Teen Tournament Series


4. Create a recommendation engine to recommend episodes based on user input

[Heroku website](https://choppedrecommendations.herokuapp.com/)

### Heroku Website

### Observations and Recommendations

### 

### Methods
- TFIDFVectorizor
- PCA
- KMeans

### Chopped Dataset Attributes and Descriptions 
[Kaggle Link](https://www.kaggle.com/jeffreybraun/chopped-10-years-of-episode-data)
There are 567 episodes total included in the dataset. Here are the attributes:

- `season`
- `season_episode`
- `series_episode`
- `episode_name`
- `episode_notes`
- `air_date`
- `judge1`
- `judge2`
- `judge3`
- `appetizer`
- `entree`
- `dessert`
- `contestant1`
- `contestant1_info`
- `contestant2`
- `contestant2_info`
- `contestant3`
- `contestant3_info`
- `contestant4`
- `contestant4_info`