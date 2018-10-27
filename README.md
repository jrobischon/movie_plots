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
* [notebooks/data_exploration.ipynb](https://github.com/jrobischon/movie_plots/blob/master/notebooks/Data%20Exploration.ipynb)
(exploration of dataset)
* [notebooks/Train Doc2Vec.ipynb](https://github.com/jrobischon/movie_plots/blob/master/notebooks/Train%20Doc2Vec.ipynb) (Train a Doc2Vec model)
* [notebooks/Keras Model.ipynb](https://github.com/jrobischon/movie_plots/blob/master/notebooks/Keras%20Model.ipynb) (Train a Keras model  **In Progress**)

**Data**
---
The dataset used in this project was compiled by scraping data from movie pages on Wikipedia.  The dataset has been made publicly available and can be found at the following [link](https://www.kaggle.com/jrobischon/wikipedia-movie-plots)

The dataset describes 34,886 movies from around the world, including a long-form summary of each movie's plot (WARNING: May contain spoilers!!).   Column descriptions are listed below:

* Release Year - Year in which the movie was released
* Title - Movie title
* Origin / Ethnicity - Origin of movie (i.e. American, Bollywood, Tamil, etc.)
* Director - Director(s)
* Plot - Main actor and actresses
* Genre - Movie Genre(s)
* Wiki Page - URL of the Wikipedia movie page from which the plot description was scraped
* Plot - Long form description of movie plot



