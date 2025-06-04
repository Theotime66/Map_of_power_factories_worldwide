import folium
import requests
import pandas as pd
import numpy as np

# Étape 1: Récupérer les données des centrales électriques
url = "https://wri-rw.carto.com/api/v2/sql?q=SELECT%20*%20FROM%20powerwatch_data_20180102"
response = requests.get(url)
data = response.json()

# Convertir les données en DataFrame
plants = pd.DataFrame(data['rows'])

# Étape 2: Définir les couleurs par type d'énergie
fuel_colors = {
    'Coal': '#000000',
    'Oil': '#B15928',
    'Gas': '#BC80BD',
    'Hydro': '#1F78B4',
    'Nuclear': '#E31A1C',
    'Solar': '#FF7F00',
    'Waste': '#6A3D9A',
    'Wind': '#5CA2D1',
    'Geothermal': '#FDBF6F',
    'Biomass': '#229A00',
    'Others': '#B2DF8A'
}

# Étape 3: Créer une carte
m = folium.Map(location=[20, 0], zoom_start=2)

# Étape 4: Ajouter les points des centrales électriques avec des couleurs et des tailles variables
for index, row in plants.iterrows():
    # Texte à afficher au survol
    popup_text = f"Plant: {row['name']}<br>Estimated Generation (2017): {row['estimated_generation_gwh_2017']} GWh<br>Fuel Type: {row['primary_fuel']}<br>Operator: {row['owner']}"
    
    # Déterminer la couleur en fonction du type de combustible
    fuel_type = row['primary_fuel']
    color = fuel_colors.get(fuel_type, '#B2DF8A')  # Si le type n'est pas dans le dictionnaire, utiliser une couleur par défaut
    
    # Déterminer la taille du cercle en fonction de la capacité et du niveau de zoom
    capacity = row['estimated_generation_gwh_2017']
    
    # Calculer la taille initiale en fonction de la capacité (petite taille de base pour les petites usines)
    if capacity > 0:
        base_radius = np.log(capacity + 1)  # Échelle logarithmique pour les grandes capacités
    else:
        base_radius = 1  # Taille par défaut pour les petites capacités
    
    # Ajustement dynamique : ici, les cercles grossissent à mesure qu'on zoome
    # L'idée est de multiplier par un facteur dépendant du niveau de zoom (plus grand cercle à plus grand zoom)
    dynamic_radius = base_radius * 0.9  # Vous pouvez ajuster ce facteur selon l'effet souhaité
    
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=dynamic_radius,  # Taille ajustée avec un facteur fixe
        popup=folium.Popup(popup_text, max_width=200),
        color=color,  # Bordure du cercle
        fill=True,
        fill_color=color,  # Couleur de remplissage
        fill_opacity=0.7
    ).add_to(m)

# Étape 5: Ajouter la légende des couleurs pour chaque type d'énergie
legend_html = '''
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 200px; height: 250px; 
            border:2px solid grey; z-index:9999; font-size:14px;
            background-color:white; padding: 10px;">
    <b>Fuel Type Legend</b><br>
    <i style="background: #000000; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Coal<br>
    <i style="background: #B15928; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Oil<br>
    <i style="background: #BC80BD; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Gas<br>
    <i style="background: #1F78B4; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Hydro<br>
    <i style="background: #E31A1C; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Nuclear<br>
    <i style="background: #FF7F00; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Solar<br>
    <i style="background: #6A3D9A; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Waste<br>
    <i style="background: #5CA2D1; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Wind<br>
    <i style="background: #FDBF6F; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Geothermal<br>
    <i style="background: #229A00; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Biomass<br>
    <i style="background: #B2DF8A; width: 20px; height: 20px; float: left; margin-right: 8px;"></i>Others<br>
</div>
'''

# Ajouter la légende à la carte
m.get_root().html.add_child(folium.Element(legend_html))

# Étape 6: Afficher la carte
m.save('power_plants_map_with_Estimated_Generation_GWh_2017.html')
