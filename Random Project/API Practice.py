import requests
import json


class UserSummoner(object):
    def __init__(self, summoner_name):
        self.summoner_name = summoner_name

    def summoner_name(self):
        return self.summoner_name
# define some initial variables needed for the API request
api_key = ''  # 'x'  #whatever my api key
by_name_url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'  # {summoner name}?api_key={api key}

# request input for Summoner Name + API Key to utilize
new_summoner = UserSummoner(input('What is your Summoner Name: '))
api_key = input('What is your API key: ')

# create the URL to pass to Riot's API through a get request
by_name_url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + str(new_summoner.summoner_name) + '?api_key=' + str(api_key)

# make a GET request to find for the Summoner Name utilizing by_name_url
by_name_response = requests.get(by_name_url)

# test print API call status code and pretty print the JSON response
print(by_name_response.status_code)
print(json.dumps((by_name_response.json()), sort_keys=True, indent=4, separators=(',', ': ')))  # pretty printing the json response

# structure the API response to be a dictionary
by_name_response_json_list = json.loads(by_name_response.content.decode('utf-8'))    # assign a variable to the json list of response

# set variable summoner_id to be the id value returned by the JSON response
summoner_id = by_name_response_json_list[str(new_summoner.summoner_name)]['id']
print(summoner_id)

##### NEXT STEPS
# send a new API call to the  stats-v1.3
stats_url = 'https://na.api.pvp.net/api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/ranked' + str(summoner_id) + '?api_key=' + str(api_key)

# make a GET request to the
stats_response = requests.get(stats_url)

# structure the response and provide it back
stats_response_json_list = json.loads(stats_response.content.decode('utf-8'))
print(stats_response_json_list)     # diagnostic print run of the JSON response

# set variable sona_record to be only the ranked values for sona games
## maxNumDeaths, totalDeathsPerSession
sona_record = (by_name_response_json_list['37']['maxNumDeaths'], by_name_response_json_list['37']['totalDeathsPerSession'])
print('Max deaths %s | Total deaths per session %s' % sona_record)

# diagnostics - not sure why it's not matching on 'id' for the key in the dictionary - BECAUSE OF NESTED STRUCTURE
# print('DIAGNOSTIC')
# for key in response_json_list.keys():
#   print(key)  # diagnostic print of value in kvp


####################### EXAMPLE API call to summoner-v1.4 ####################
##  /api/lol/{region}/v1.4/summoner/by-name/{summonerNames} <-- diesel message #
# {"dieselmessage": {
#   "id": 21799384,
#   "name": "DieselMessage",
#   "profileIconId": 780,
#   "revisionDate": 1487479565000,
#   "summonerLevel": 30
# }}

#       "Sona": {
#        "id": 37,
#         "title": "Maven of the Strings",
#         "name": "Sona",
#         "key": "Sona"
#      },