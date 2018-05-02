import requests
from bs4 import BeautifulSoup
import logging
import numpy as np
import pandas as pd
import time
from tqdm import tqdm

def get_html(url):
    """
    Return html content for url

    Params:
    -------
    url : Webpage input url

    Returns:
    --------
    String containing html content
    """
    try:
        p = requests.get(url)
    except Exception:
        logging.debug("HTML not returned (Invalid url): '%s'" %url)
        return None
    else:
        if p.status_code == 200:
            return p.content
        else:
            return None

def make_soup(url):
    """
    Return BeautifulSoup object for input url

    Params:
    -------
    url : Webpage url

    Returns:
    --------
    BeautifulSoup object
    """

    r = get_html(url)

    try:
        return BeautifulSoup(r, 'html.parser')
    except TypeError:
        return None


def get_plot(url, sleep_time=0):
    """
    Return wikipedia plot description for input url

    Params:
    -------
    url : Webpage url
    sleep_time : Time to sleep (seconds)

    Returns:
    --------
    Plot description (str)
    """

    soup = make_soup(url)

    # Find Plot section header
    try:
        plot = soup.find(id="Plot").parent
    except AttributeError:
        logging.debug("Plot header not found: '%s'" % url)
    else:
        out = []

        # Extract all text content until next header
        while True:
            plot = plot.findNextSibling()
            if plot.name == 'h2':
                break
            elif plot.name == 'p':
                out.append(plot.get_text())
            else:
                break

        time.sleep(sleep_time)
        return " ".join(out)

def normalize_headers(x):
    """
    Different years may have differing columns names for the same data (i.e. 'Cast', 'Cast and crew', etc).
    Returns a normalized column name

    Params:
    -------
    x : String containing column name

    Returns:
    --------
    Normalized column name

    """
    if "Cast" in x:
        return "Cast"
    else:
        return x.replace("\n", "")

def get_header(table):
    """
    Return the column headers for an input html table

    Params:
    -------
    table : bs4 element with table tag

    Returns:
    --------
    list of header names
    """
    cols = []
    try:
        for x in table.find_all('tr')[0].find_all('th'):
            cols.append(x.get_text())
    except AttributeError:
        pass

    return [normalize_headers(x) for x in cols]



def get_movie_table(year):
    """
    Return a dataframe containing info for all American movies released during input year

    Params:
    ------
    year: Release year

    Returns:
    --------
    Dataframe containing movie info
    """

    url = "https://en.wikipedia.org/wiki/List_of_American_films_of_" + str(year)
    soup = make_soup(url)

    tables = soup.find_all("table")

    df_out = pd.DataFrame()

    # Iterate over all tables on page
    for t in tables:

        # Get table headers and column count
        cols = get_header(t)
        n_cols = len(cols)

        # Check that table header contains 'Title' and 'Cast'
        if {"Title", "Cast"}.issubset(set(cols)):

            # Iterate over table rows (excluding header)
            for row in t.find_all('tr')[1:]:
                vals = []
                for v in row.find_all('td'):
                    vals.append(v.get_text())

                # "Opening" column is not present for all rows, replace with np.nan where missing
                if len(vals) < n_cols:
                    n_pad = n_cols - len(vals)
                    vals = [np.nan]*n_pad + vals
                elif len(vals) > n_cols:
                    n = len(vals) - n_cols
                    vals = vals[n:]
                else:
                    pass

                # Get link to movie Wiki page, if exists
                try:
                    link_post = row.find('a').get_attribute_list('href')[0]
                    link = 'https://en.wikipedia.org' + link_post
                except AttributeError:
                    link = np.nan

                cols.extend(["Wiki Page", "Release Year"])

                vals.extend([link, year])

                # Append row to output dataframe
                df_out = df_out.append(dict(zip(cols, vals)), ignore_index=True)
        else:
            pass

    return df_out

def get_all_tables(min_year, max_year, sleep_time=0):
    """
    Return a dataframe containing all American movies released between min_year and max_year

    Params:
    ------
    min_year : minimum year
    max_year : maximum year

    Returns:
    --------
    Dataframe containing movie info
    """

    df_out = pd.DataFrame()

    for year in range(min_year, max_year+1):
        df = get_movie_table(year)

        if df.shape[0] > 0:
            df_out = pd.concat([df_out, df], axis=0)
        else:
            logging.debug("No movies found for year %i" %year)

        print("Year %i Complete: %i rows added" %(year, df.shape[0]))
        time.sleep(sleep_time)

    return df_out


if __name__ == "__main__":
    logging.basicConfig(filename="get_data.log", level=logging.DEBUG)

    # Get movie info
    df_movies = get_all_tables(1900, 2017, sleep_time=1)

    print("Total Rows: %i\n" %df_movies.shape[0])

    # Append plot description from each movie Wiki page
    print("Appending Plots")
    t0 = time.time()

    plots = []
    for i in tqdm(range(df_movies.shape[0])):
        url = df_movies.iloc[i]["Wiki Page"]
        plots.append(get_plot(url, sleep_time=0.2))

    df_movies["Plot"] = plots
    print("Completed in %0.3f sec" %(time.time() - t0))

    # Keep columns that are consistent across most years
    keep_cols = ["Release Year", "Title", "Director", "Cast", "Genre", "Wiki Page", "Plot"]
    df_movies = df_movies[keep_cols]

    # Convert 'Release Year' to type int
    df_movies["Release Year"] = df_movies["Release Year"].astype(int)

    print("Saving CSV")
    df_movies.to_csv("data/wiki_movies.csv", index=False)
