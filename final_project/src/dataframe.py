import pandas as pd

def json_to_dataframe(response):
    #convert response to dataframe
    return pd.DataFrame(response.json()[1:], columns=response.json()[0])
