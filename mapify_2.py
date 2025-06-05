import pandas as pd
import folium

# Load the volcano data
us_volcano_data = pd.read_csv("us_volcano_data.txt")
world_volcano_data = pd.read_csv("world_volcano_data.txt")

# Strip any extra spaces from column names to prevent mismatches
us_volcano_data.columns = us_volcano_data.columns.str.strip()
world_volcano_data.columns = world_volcano_data.columns.str.strip()

# Check column names to ensure the correct ones are being used
print("US Volcano Data Columns:", us_volcano_data.columns)
print("World Volcano Data Columns:", world_volcano_data.columns)

# Create a base map centered on the US
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Define a function to create a popup for each volcano
def popup(volcano):
    return folium.Popup(f"Name: {volcano.get('NAME', 'N/A')}<br>"
                        f"Location: {volcano.get('LOCATION', 'N/A')}<br>"
                        f"Elevation: {volcano.get('ELEV', 'N/A')} m<br>"
                        f"Latitude: {volcano.get('LAT', 'N/A')}<br>"
                        f"Longitude: {volcano.get('LON', 'N/A')}")

# Add volcano markers to the map for US volcanoes
def add_us_volcano_markers():
    for _, volcano in us_volcano_data.iterrows():
        folium.Marker(
            location=[volcano['LAT'], volcano['LON']],  # Ensure 'LAT' and 'LON' exist
            popup=popup(volcano),
            icon=folium.Icon(color='blue', icon='cloud')
        ).add_to(m)

# Add volcano markers to the map for world volcanoes
def add_world_volcano_markers():
    for _, volcano in world_volcano_data.iterrows():
        folium.Marker(
            location=[volcano['LAT'], volcano['LON']],  # Ensure 'LAT' and 'LON' exist
            popup=popup(volcano),
            icon=folium.Icon(color='red', icon='cloud')
        ).add_to(m)

# Call functions to add markers
add_us_volcano_markers()
add_world_volcano_markers()

# Save the map as an HTML file
m.save("volcano_map.html")

# Output for confirmation
print("Map has been saved as 'volcano_map.html'")
