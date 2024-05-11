import requests
url="https://maps.googleapis.com/maps/api/place/textsearch/json"
json_data = requests.get(url).json
json_status = json_data()["status"]

print(json_status)

print('\nAPI Status :' + json_status)

if json_status == 'OK':

    location_details = {
        'name_of_place':
        json_data()['results'][0]['name'],
        'formatted_address':
        json_data()['results'][0]['formatted_address'],
        'location':
        json_data()['results'][0]['geometry']['location'],
        'upper_left':
        (json_data()['results'][0]['geometry']['viewport']['northeast']['lat'],
         json_data()['results'][0]['geometry']['viewport']['southwest']['lng']
         ),
        'lower_right':
        (json_data()['results'][0]['geometry']['viewport']['southwest']['lat'],
         json_data()['results'][0]['geometry']['viewport']['northeast']['lng']
         ),
    }

    print(location_details) 