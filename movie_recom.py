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
      
      
      
