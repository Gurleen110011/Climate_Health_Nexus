import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd

file_path = 'Final_data.csv'
data = pd.read_csv(file_path)

data_filtered = data[['Latitude', 'Longitude', 'Temp', 'preci', 'year']]

fig, ax = plt.subplots(1, 2, figsize=(20, 10), subplot_kw={'projection': ccrs.PlateCarree()})

for axis in ax:
    axis.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')
    axis.add_feature(cfeature.COASTLINE)
    axis.add_feature(cfeature.LAND, edgecolor='black', alpha=0.4)
    axis.add_feature(cfeature.OCEAN, alpha=0.1)
    axis.set_extent([68, 98, 6, 37], crs=ccrs.PlateCarree())
    axis.gridlines(draw_labels=True, color='gray', alpha=0.5, linestyle='--')

scatter_temp = ax[0].scatter(
    data_filtered['Longitude'],
    data_filtered['Latitude'],
    c=data_filtered['Temp'],
    cmap='coolwarm',
    s=data_filtered['Temp'] * 0.1,  
    alpha=0.6,
    edgecolors='k',
    linewidth=0.2
)
ax[0].set_title('Temperature Variation Across India', fontsize=16)
cb_temp = fig.colorbar(scatter_temp, ax=ax[0], orientation='vertical', shrink=0.7, label='Temperature (K)')

scatter_preci = ax[1].scatter(
    data_filtered['Longitude'],
    data_filtered['Latitude'],
    c=data_filtered['preci'],
    cmap='Blues',
    s=data_filtered['preci'] * 200, 
    alpha=0.6,
    edgecolors='k',
    linewidth=0.2
)
ax[1].set_title('Precipitation Variation Across India', fontsize=16)
cb_preci = fig.colorbar(scatter_preci, ax=ax[1], orientation='vertical', shrink=0.7, label='Precipitation (mm/day)')

plt.tight_layout()
plt.savefig("temperature_precipitation_side_by_side_maps.png", dpi=300, bbox_inches='tight')
plt.show()
