from surname import SurnameList
from APIkey import APIkey

def main():
    app = SurnameList()
    app.start_application()

if __name__ == '__main__':
    main()




'''
# store API key
API_key = "27a3464607480ec1f54c0ddfac1f78c5105bf008"

#show all columns in display
pd.options.display.max_columns = None 

#read api keys file and assign variables
url = "https://api.census.gov/data/2010/surname?get=PCTAPI,PCTBLACK,PCTAIAN,PCTWHITE,COUNT,PCT2PRACE,PCTHISPANIC,NAME&RANK=1:100&key={0}".format(API_key)

response = requests.request("GET", url)
surname_data = json_to_dataframe(response)

#convert surname counts into int
surname_data['COUNT'] = surname_data['COUNT'].astype(int)

#top 10 surnames with largest counts
surname_data_sort = surname_data.sort_values(by=['COUNT'], ascending=False).head(10)
print(f'Top 10 surnames overall: \n{surname_data_sort}')


top_10_surname_list = surname_data_sort['NAME'].tolist()
#print(f'List of top 10 surnames: {top_10_surname_list}')

surname_str = ",".join(top_10_surname_list)
#print(f'List of top 10 surnames as one string: {surname_str}')


#top 10 surnames in non-Hispanic White
url = "https://api.census.gov/data/2010/surname?get=PCTWHITE,COUNT,NAME&RANK=1:100&key={0}".format(API_key)
response = requests.request("GET", url)
surname_data = json_to_dataframe(response)
surname_data_sort_white = surname_data.sort_values(by=['COUNT'], ascending=False).head(10)
print(f'Top 10 surnames in non-hispanic white: \n{surname_data_sort_white}')
'''