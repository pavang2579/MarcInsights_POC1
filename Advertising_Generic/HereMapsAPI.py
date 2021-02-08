import folium
from folium import plugins
import ipywidgets
import geocoder
import geopy
import pandas as pd
import numpy as np

# Create df
data = pd.read_csv('/Users/shivaneeprajapati/PycharmProjects/Download/datasetfiles/df_final.csv',index_col=None)
data = data.to_dict('list')
print(data)
df = pd.DataFrame(data,columns=["Countrycode","latitude","longitude","Country_name","Instagram","Facebook","Twitter","LinkedIn"])




def _plot_dot(point,radius=4, weight=1,color='black'):
    place = None
    folium.CircleMarker(location=[point["latitude"], point["longitude"]], radius=radius, weight=weight,
                        color=color, fill=True,
                        fill_color="red",
                        fill_opacity=0.9,
                        tooltip=f'<b>Country_name: </b>{str(point["Country_name"])}'
                                f'<br></br>'f'<b>Countrycode: </b>{str(point["Countrycode"])}'
                                f'<br></br>'f'<b>Instagram: </b>{str(point["Instagram"])}'
                                f'<br></br>'f'<b>Facebook: </b>{str(point["Facebook"])}'
                                f'<br></br>'f'<b>Twitter: </b>{str(point["Twitter"])}'
                                f'<br></br>'f'<b>LinkedIn: </b>{str(point["LinkedIn"])}'
                        ).add_to(place)


def generate_map(data, filename=None):
    map_element = folium.Map(tiles='Social Media stats:countrywise',attr='XXX Mapbox Attribution')


    data.apply(_plot_dot, axis=1,)
    folium.LayerControl().add_to(map_element)
    map_element.save(filename, close_file=True)

    return map_element


if __name__ == "__main__":
    map_1 = generate_map(df, 'test_maps.html')