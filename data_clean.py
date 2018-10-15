import pandas as pd


if __name__ == "__main__":

    # Import data
    df = pd.read_csv("data/wiki_movie_plots.csv")

    # Title is not Null
    df = df[df["Title"].notnull()]

    # Remove newlines from Title
    df["Title"] = df["Title"].apply(lambda x: x.replace("\n", " "))

    df["Genre"].fillna("Unknown", inplace=True)
    df["Genre"] = df["Genre"].apply(lambda x: x.lower().replace("\n", " "))

    df["Director"].fillna("Unknown", inplace=True)
    df["Director"] = df["Director"].apply(lambda x: x.replace("\n", " "))

    # Dedupe
    df = df.groupby(["Title", "Release Year", "Director"], as_index=False).head(1)

    # Save as csv
    df.to_csv("data/wiki_movie_plots_deduped.csv", index=False)
