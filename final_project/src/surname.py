import pandas as pd
import numpy as np
import requests
from dataframe import json_to_dataframe


class SurnameList():

    def __init__(self):
        self.OVERALL_COUNTS='1'
        self.WHITE='2'
        self.HISPANIC='3'
        self.BLACK='4'
        self.API='5' #Non-Hispanic Asian and Native Hawaiian and Other Pacific Islander Alone
        self.AIAN='6' #Non-Hispanic American Indian and Alaska Native Alone
        self.TWORACES='7' #Non-Hispanic American Indian and Alaska Native Alone
        self.EXIT='8'
        self.menu_choice = 1
        self.keep_going = True
    
    def display_menu(self):
        print('\t\t\tU.S. Census 2010 surname data')
        print()
        print('\t\t1. Top 10 surnames overall')
        print('\t\t2. Surname percentage: non-hispanic white')
        print('\t\t3. Surname percentage: hispanic')
        print('\t\t4. Surname percentage: non-hispanic black')
        print('\t\t5. Surname percentage: non-hispanic asian and native hawaiian and other pacific islander')
        print('\t\t6. Surname percentage: non-hispanic american indian and alaska native')
        print('\t\t7. Surname percentage: non-hispanic two or more races')
        print('\t\t8. Exit')
        print()
    

    def process_menu_choice(self):
        self.menu_choice = input('Please enter menu item number: ')
        print(f'User input: {self.menu_choice}')
    
        match self.menu_choice:
            case self.OVERALL_COUNTS:
                self.overall_counts() 
            case self.WHITE:
                self.white() 
            case self.HISPANIC:
                self.hispanic() 
            case self.BLACK:
                self.black() 
            case self.API:
                self.api() 
            case self.AIAN:
                self.aian() 
            case self.TWORACES:
                self.tworaces() 
            case self.EXIT:
                if __debug__:
                    print('Have a nice day!')
                self.keep_going = False
            case _:
                print("Invalid menu choice!")
    

    def overall_counts (self):
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

        top_10_surname_list = surname_data_sort['NAME'].tolist()
        print(f'List of top 10 surnames: {top_10_surname_list}')
        print()
        input('\n\nPress any key to return to menu')
        print()

    def white (self):
        API_key = "27a3464607480ec1f54c0ddfac1f78c5105bf008"
        url = "https://api.census.gov/data/2010/surname?get=PCTWHITE,COUNT,NAME&RANK=1:100&key={0}".format(API_key)
        response = requests.request("GET", url)
        surname_data = json_to_dataframe(response)
        surname_data_sort = surname_data.sort_values(by=['PCTWHITE'], ascending=False).head(10)
        print(f'Percentage of surnames ranking in non-hispanic white: \n{surname_data_sort}')
        print()
        input('\n\nPress any key to return to menu')
        print()
    
    def hispanic (self):
        API_key = "27a3464607480ec1f54c0ddfac1f78c5105bf008"
        url = "https://api.census.gov/data/2010/surname?get=PCTHISPANIC,COUNT,NAME&RANK=1:100&key={0}".format(API_key)
        response = requests.request("GET", url)
        surname_data = json_to_dataframe(response)
        surname_data_sort = surname_data.sort_values(by=['PCTHISPANIC'], ascending=False).head(10)
        print(f'Percentage of surnames ranking in hispanic: \n{surname_data_sort}')
        print()
        input('\n\nPress any key to return to menu')
        print()
        
    
    def black(self):
        API_key = "27a3464607480ec1f54c0ddfac1f78c5105bf008"
        url = "https://api.census.gov/data/2010/surname?get=PCTBLACK,COUNT,NAME&RANK=1:100&key={0}".format(API_key)
        response = requests.request("GET", url)
        surname_data = json_to_dataframe(response)
        surname_data_sort = surname_data.sort_values(by=['PCTBLACK'], ascending=False).head(10)
        print(f'Percentage of surnames ranking in black: \n{surname_data_sort}')
        print()
        input('\n\nPress any key to return to menu')
        print()

    def api(self):
        API_key = "27a3464607480ec1f54c0ddfac1f78c5105bf008"
        url = "https://api.census.gov/data/2010/surname?get=PCTAPI,COUNT,NAME&RANK=1:100&key={0}".format(API_key)
        response = requests.request("GET", url)
        surname_data = json_to_dataframe(response)
        surname_data_sort = surname_data.sort_values(by=['PCTAPI'], ascending=False).head(10)
        print(f'Percentage of surnames ranking in non-hispanic asian and native hawaiian and other pacific islander: \n{surname_data_sort}')
        print()
        input('\n\nPress any key to return to menu')
        print()

    def aian(self):
        API_key = "27a3464607480ec1f54c0ddfac1f78c5105bf008"
        url = "https://api.census.gov/data/2010/surname?get=PCTAIAN,COUNT,NAME&RANK=1:100&key={0}".format(API_key)
        response = requests.request("GET", url)
        surname_data = json_to_dataframe(response)
        surname_data_sort = surname_data.sort_values(by=['PCTAIAN'], ascending=False).head(10)
        print(f'Percentage of surnames ranking in non-hispanic american indian and alaska native: \n{surname_data_sort}')
        print()
        input('\n\nPress any key to return to menu')
        print()

    def tworaces(self):
        API_key = "27a3464607480ec1f54c0ddfac1f78c5105bf008"
        url = "https://api.census.gov/data/2010/surname?get=PCT2PRACE,COUNT,NAME&RANK=1:100&key={0}".format(API_key)
        response = requests.request("GET", url)
        surname_data = json_to_dataframe(response)
        surname_data_sort = surname_data.sort_values(by=['PCT2PRACE'], ascending=False).head(10)
        print(f'Percentage of surnames ranking in non-hispanic non-hispanic two or more races: \n{surname_data_sort}')
        print()
        input('\n\nPress any key to return to menu')
        print()

    def start_application(self):
        while self.keep_going:
            self.display_menu()
            self.process_menu_choice()
