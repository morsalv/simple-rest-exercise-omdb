# Simple Rest exercise

Get Rotten Tomatoes movie ratings from OMDB (www.omdbapi.com).

## Prerequisite

- This application has been built under python3 environnment
- It uses a Python wrapper for OMDb API (https://pypi.org/project/omdb/)
- For containerized version, docker is required
- Please, get an apikey from OMDB API website and add it to the omdb_config.py.

```
sudo pip install omdb
sudo pip install requests
```

## Usage

CLI command
```
python omdb_rt_rating.py "movie title"
```
## Docker usage

- Build
```
sudo docker build -t movie_rt_rating .
```
- Run
```
sudo docker run movie_rt_rating "movie title"
```



