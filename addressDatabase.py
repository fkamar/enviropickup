import pandas as pd
import utm
import googlemaps
# apparently this returns the UML coordinates too. Consider converting and not use Google earth?
df = pd.read_csv('Addresses.csv')


df = df.filter(['UnitFullAddress', 'X', 'Y'])

df['Latitude'] = None
df['Longitude'] = None
print(len(df))
def toLatLong(df):
    for i in range(0, len(df), 1):

        x = df.iloc[i]['X']
        # print(x)
        y = df.iloc[i]['Y']
        # print(y)

        df.iat[i, df.columns.get_loc("Latitude")] = utm.to_latlon(x, y, 17, 'T')[0]
        df.iat[i, df.columns.get_loc("Longitude")] = utm.to_latlon(x, y, 17, 'T')[1]

    return df
df = toLatLong(df)
print(df)
export_csv = df.to_csv(r'/home/bq/Documents/Hackathon/LondonAddressesDatabase.csv', index=None, header=True)

"""
gmaps_key = googlemaps.Client(key="AIzaSyAuq9_wSiD_6SDc5-kpcuYDw4Uo9LOg230")

# create empty columns for coordinates
df["Latitude"] = None
df["Longitude"] = None

# iterate throughout dataframe to obtain coordinates for all addresses
for i in range(0, len(df), 1):
    result = gmaps_key.geocode(df.iat[i, 0])

    try:
        lat = result[0]["geometry"]["location"]["lat"]
        lng = result[0]["geometry"]["location"]["lng"]
        df.iat[i, df.columns.get_loc("Latitude")] = lat
        df.iat[i, df.columns.get_loc("Longitude")] = lng
    except:
        lat = None
        lng = None
"""
