# Searching for the Best Chopped Episodes to Rerun

## *Chopped* Recommendation Engine
Author: Mikhaela Martin

### Introduction

Chopped is one of my favorite television shows. I have yet to watch every episode, but I have watched the same episode multiple times, unintentionally. Television networks rerun the same episodes because they know their audience enjoys them. 

### Business Objectives:

This [article](https://screenrant.com/chopped-best-episodes-imdb/) pinpoints the top 10 all-time favored Chopped episodes. I will use this article as a basis to suggest more episodes for The Food Network to rerun.

### Model Objective:

**1. Visualize and interpret patterns across all episodes**

![](https://github.com/mikhaelamartin/Chopped-Recommendations/blob/master/images/PCA%20Plot.png)

In order to suggest shows similar to the top 10, I needed to find patterns that occurred amongst them. Therefore, I used kmeans to cluster every episode into segments.

If the above figure were not colored, the number of optimal clusters would be unclear. This amount of overlap is expected because the shows themselves are inherently structured the same and the descriptions were fairly short.

But, I used kmeans to cluster them into seven groups. The shows that differed the most from each other were the celebrity/charity based episodes and NY Executive Chef episodes. This is probably because of the difference in skill level and intention between the competitors - NY Executive Chefs came to Chopped to showcase their skills and compete seriously in order to win whereas the Celebrities who competed for their charity were not trained and leaned more towards comedic than serious.

The top 10 episodes emphasized either the judges, familiar faces, or family. The viewers love the judges' personalities and interactions with each other which is why "Judges' Face-Off' and 'Chopped All-Stars: Judges are part of the pack. The audience also loves cooking shows in general which is why "Crunch Time" and "Chopped All-Stars: Food Network vs. Cooking Channel" are also fan faves. Lastly, the viewers are very sentimental beings which is why the first aired episode, "Ocotpus, Duck, Animal Crackers" and "It's a Sibling Thing" are the top two episodes.

![](https://github.com/mikhaelamartin/Chopped-Recommendations/blob/master/top10.png)


**2. Recommend episodes similar to the top 10 favorited episodes**

Almost half of the top 10 rated episodes centered around the judges challenging each other. Here are series similar to that sentiment:

1. All Stars (Episode 118-122). This series features Food Network show hosts competing for their charity of choice.
2. Chopped Tournament of Stars (Episodes 229-233). This series features athletes, comedians, actors, and experienced chefs competing for $50,000 towards their charity of choice.
3. All-Stars Tournament: Episode 71-75): This series features celebrity chefs competing for $50,000 towards thier charity of choice.


**3. Create a recommendation engine to recommend episodes based on user input**

[Heroku website](https://choppedrecommendations.herokuapp.com/)


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