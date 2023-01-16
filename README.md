# Starlink QGIS Plugin

A QGIS plugin that allows users to select a specific geographical area on the QGIS map and displays the number of Starlink satellites currently orbiting over that area.

## Installation

1. Download the plugin from the release page<br />
2. In QGIS, go to Plugins > Manage and Install Plugins<br />
3. Select Install from ZIP and choose the downloaded file<br />
4. The plugin should now be installed and can be found in the Plugins menu<br />

## Usage

1. Open a new QGIS project or open an existing project<br />
2. Go to Plugins > Starlink QGIS Plugin<br />
3. Use the map tools to select a specific area on the map<br />
4. Click the Search button to initiate the search<br />
5. The plugin will display the number of Starlink satellites currently orbiting over the selected area<br />

## Data Source

The plugin uses TLE (Two-Line Elements) data as the primary data source. TLE data is a common format for representing the orbital elements of satellites and is publicly available from various sources. However, the use of TLE data does have some limitations.<br />

1. The TLE data used in the plugin is based on a snapshot of the satellite orbits at a specific point in time, rather than live data. Therefore, the plugin is only able to provide information on the location and density of satellites at the time the TLE data was collected, rather than in real-time.<br />

2. The TLE data used only contains information on the orbits of active satellites. The TLE data used in the plugin only includes information on satellites that are currently in orbit, and does not include information on inactive or decommissioned satellites.<br />

## Limitations

1. The plugin uses TLE data as the primary data source, which is not real-time data.<br />

2. The plugin only covers the active satellite orbits, and does not include information on inactive or decommissioned satellites.<br />

## Contributing

1. Fork the repository<br />
2. Create a new branch<br />
3. Make your changes<br />
4. Create a pull request<br />

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgements

The plugin uses the QGIS mapping software as the foundation.<br />
The plugin uses TLE data from various sources.

## Contact

Email: alperkara247@gmail.com<br />
LinkedIn: https://www.linkedin.com/in/alperkara/
