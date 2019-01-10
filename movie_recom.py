import argparse
import json
import numpy as np

from compute_scores import pearson_score
from collaborative_filtering import find_similar_users

#Define function to parse

def build_arg_parser():
  parser = argparse.ArgumentParser(description = 'Find the movie recommendation for the given user')
  parser.add_argument('--user',dest='user',required=True,help='Input user')
  return parser
  
#Movie recommendation for the user

def get_recommendations(dataset,input_user):
  if input_user is not in dataset:
    raise TypeError('cannot find'+ imput_user +'in the dataset')
    
#Track the scores
  overall_scores = {}
  similarity_scores = {}

#similarity scores between input user and the other users
  for user in [x for x in  dataset if x != input_user]:
    similarity_score = pearson_score(dataset,input_user,user)
    if similarity_score <= 0:
      continue
  
#Extract list of movies
  filtered_list = [x for x in dataset[user] if x not in \ dataset[input_user] or dataset[input_user][x] == 0]
      
#Rating of movies
    for item in filtered_list:
      overall_scores.update({item: dataset[user][item] * similarity_score})
      similarity_scores.update({item: similarity_score})
      
  if len(overall_scores) == 0:
    return['No recommendation possible']

  movie_scores = np.array([score/similarity_scores[item], item] for item, score in overall_scores.items()])
  
#Sort movie recommendations
  movie_scores = movie_scores[np.argsort(movie_scores[:, 0])[: :-1]]
  movie_recommendations = [movie for _, movie in movie_scores]
  
  return movie_recommendations

#Extract the name of input user
if _name_=='_main_':
  args = build_arg_parser().parse_args()
  user = args.user
  
#Load rating from movie_ratings.json
  ratings_file = 'movie_ratings.json'
  with open(ratingss_file,'r') as f:
    data = json.loads(f.read())
    
  print("\nMovie Recommendations for "+ user +":")
  movies = get_recommendations(data, user)
  for i, movie in enumerate(movies):
    print(str(i+1) + '.' + movie)
    
##The Movie Recommendation is ready ##
    

  
  
      
      
      
      
      
