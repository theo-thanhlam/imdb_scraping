import requests
from bs4 import BeautifulSoup
import pandas as pd

sites = ["boxoffice", "moviemeter", "top", "top-english-movies", "tvmeter", "toptv", "bottom"]

url = 'https://www.imdb.com/chart/' 
csv_name = "imdb_"


    
def get_years_list(year_tags):
    return [year.text.strip("()") for year in year_tags]

def get_actors_list(actor_tags):
    return [tag['title'] for tag in actor_tags]
    
def get_titles_list(actor_tags):
    return [tag.text for tag in actor_tags]

def get_rating_list(rating_tags):
    return [tag.text for tag in rating_tags]

def export_to_csv(df, title):
    return df.to_csv(title)   


def main():
    for site in sites :
       
        url_link = url + site +"/"

        file_name = csv_name + site +".csv"

        print(url_link +"\n"+file_name)
        #access URL and get html
        response = requests.get(url_link)
        html = response.text
            
            #get movies tag
        soup = BeautifulSoup(html, "html.parser")
            
            #Tags that get movie titles, actors, years
        movie_tag_for_title_actors = soup.select("td.titleColumn a")
        movie_tag_for_years = soup.select("td.titleColumn span")
            
            #Tags that get movie rating
        movie_rating_tags = soup.select("td.imdbRating strong")
        
        print("title:{}\tactor:{}\tyear:{}\trating:{}".format(len(get_titles_list(movie_tag_for_title_actors)), len(get_actors_list(movie_tag_for_title_actors)),
                                                                  len(get_years_list(movie_tag_for_years)), len(get_rating_list(movie_rating_tags))))
        
        # #Create dataframe with these value
        # df = pd.DataFrame({
        #     "title": get_titles_list(movie_tag_for_title_actors),
        #     "actor": get_actors_list(movie_tag_for_title_actors),
        #     "year":get_years_list(movie_tag_for_years),
        #     'rating':get_rating_list(movie_rating_tags)
        # })
        

    



if __name__ == '__main__':
    main()