import omdb
import sys
import requests

#print movie found in OMDB and corresponding Rotten Tomatoes rating value
def rt_rating(movie):

    try:
        result = omdb.get(title=movie, fullplot=True, tomatoes=True)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)

    if not bool(result):
        print('Movie not found')
        sys.exit(1)
            
    #get nested dict
    ratings = {item['source']: item['value'] for item in result['ratings']}
    rt_rate = ratings.get('Rotten Tomatoes')
    if rt_rate is not None:
        print('Movie: %s \tRotten Tomatoes rating: %s' % (result['title'], ratings['Rotten Tomatoes']))
    else:
        print('Movie: %s \tRotten Tomatoes rating: not found' % result['title'])
  

def main():

    if len (sys.argv) != 2 :
        sys.exit("Usage: python rtom_rating.py <movie title>")
    else :
        movie = sys.argv[1]

    try:
        import omdb_config
    except ImportError:
        print('ERROR: omdb config file not present')
        sys.exit(-1)

    if not omdb_config.api_key:
        print('ERROR: Add your OMDB API key to account file')
        sys.exit(-1)

    omdb.set_default('apikey', omdb_config.api_key)

    rt_rating(movie)



if __name__ == "__main__":
    main()
