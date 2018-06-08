# Movie Recommender

**Overview**
---
The purpose of this project is to create a movie recommender system that makes recommendations based on a movie's plot.  The recommender will consist of the following functionality:

1) Input : Movie Title  
Output : Movies with plots similar to that of the input movie

2) Input : Brief description of a movie plot  
Output : Movies with plots similar to input plot

The project code consists of the following:

* [data_scraper.py](https://github.com/jrobischon/movie_plots/blob/master/data_scraper.py) (scrapes movie data from Wikipedia)
* [tests/tests.py](https://github.com/jrobischon/movie_plots/blob/master/tests/tests.py) (unit tests for get_data.py)
* [notebooks/data_exploration.ipynb](https://github.com/jrobischon/movie_plots/blob/master/notebooks/Data%20Exploration.ipynb) (TODO: create notebook to explore dataset)
* notebooks/recommender.ipynb (TODO: create notebook w/ recommender)

**Data**
---
The dataset used in this project was compiled by scraping data from movie pages on Wikipedia.  The dataset has been made publicly available and can be found at the following link: **<TODO: insert link>**

The dataset describes 40,179 movies from around the world, including a long-form summary of each movie's plot (WARNING: May contain spoilers!!).   All columns are listed below:

* Title
* Director
* Cast
* Plot
* Origin


**Potential Next Steps**
---
* Embed recommender in a web app

