import pandas as pd
import requests

#Pull in data from an API. Here's a list of public APIs that don't require Auth keys, though if you have another API you want to use feel free: https://apipheny.io/free-api/

# Define URL
url1= 'https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2022-01-01/2022-01-01'
  
# Pull JSON Data
data_CVD19 = requests.get(url1).json()

# List of main keys
#print(data_CVD19.keys())

# List of Countries
dfs=data_CVD19['data']['2022-01-01']
#print(dfs.keys())

# List of sub keys
df1=data_CVD19['data']['2022-01-01']['USA']
#print(df1.keys())

#Iterate and append sub-keys for each country code
country_list = []
for df in dfs:
    df1=data_CVD19['data']['2022-01-01'][df]
    country_list.append([df1['country_code'], df1['confirmed'], df1['deaths']])
country_df = pd.DataFrame(data=country_list, columns=['Country', 'Confirmed_Cases', 'Confirmed_Deaths'])
print(country_df.head(10))

#Find and print TWO descriptive statistics about your data. This can be absolutely anything, from the mean() or sum() of a column to the number of different categories, to the number of null values in a column. We just want to see two pieces of information.
print("Average: ", country_df['Confirmed_Deaths'].mean())
print("Total: ", country_df['Confirmed_Deaths'].sum())

#Write a query in Pandas to select a particular set of your data. You can use a mask or with .query(), but we want you to pull out a subset based on any parameter you like. This could be "show me every row where HTTPS=False" or anything else.
print(country_df.query('Confirmed_Deaths > 5000'))
#Select and print the SECOND AND THIRD columns of your data frame.
print(country_df[['Confirmed_Cases', 'Confirmed_Deaths']])

#Select and print the FIRST 4 rows of you data frame.
print(country_df[:4])