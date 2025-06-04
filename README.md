# Map of Power Plants Worldwide

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python project that visualizes power plants across the globe on an interactive map using data from the Global Power Plant Database.

<!--
    RECOMMENDATION:
    1. Run your `main.py` script.
    2. Open the generated `output.html` file.
    3. Take a compelling screenshot of the map.
    4. Save it in the repository (e.g., in a `docs/images/` folder or directly in root as `map_screenshot.png`).
    5. Uncomment and update the line below:
-->

![Screenshot of the Interactive Map](./Example%20of%20the%20map%20-%20Screenshot.jpg)

## 🗺️ Overview

This project reads data from the `global_power_plant_database.csv` file, processes it, and then uses the Folium library to generate an interactive HTML map (`output.html`). Each power plant is represented by a marker, and clicking on a marker displays information about that plant.

## ✨ Features

*   Interactive map visualization of global power plants.
*   Data sourced from the comprehensive [Global Power Plant Database](https://datasets.wri.org/dataset/globalpowerplantdatabase).
*   Markers for each power plant with pop-up information (e.g., name, capacity, primary fuel).
*   Generates a standalone HTML file that can be opened in any web browser.

## 📊 Data Source

The project utilizes the **Global Power Plant Database** by the World Resources Institute (WRI).
*   **Link:** [https://datasets.wri.org/dataset/globalpowerplantdatabase](https://datasets.wri.org/dataset/globalpowerplantdatabase)
*   The specific CSV file used is `global_power_plant_database.csv` included in this repository. It contains information on approximately 35,000 power plants worldwide.

## 🛠️ Technology Stack

*   **Python 3.x**
*   **Pandas:** For data manipulation and reading the CSV file.
*   **Folium:** For creating the interactive map.

## 🚀 Getting Started

### Prerequisites

*   Python 3.6 or higher
*   Pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Theotime66/Map_of_power_factories_worldwide.git
    cd Map_of_power_factories_worldwide
    ```

2.  **(Recommended) Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    (The `requirements.txt` file includes `pandas` and `folium`.)

### Usage

1.  Ensure you have completed the installation steps and activated your virtual environment (if used).
2.  Run the main script from the project's root directory:
    ```bash
    python main.py
    ```
3.  This will process the `global_power_plant_database.csv` file and generate an `output.html` file in the same directory.
4.  Open `output.html` in your preferred web browser to view and interact with the map.

## 📄 Output

The script generates an HTML file (default: `output.html`) containing an interactive map. Each power plant is represented by a marker. Clicking on a marker will display a popup with details such as:
*   Name of the power plant
*   Capacity (MW)
*   Primary fuel type
*   Country

## 💡 Potential Enhancements / Future Work

*   **Filter by fuel type:** Add controls to filter power plants by their primary fuel (e.g., Coal, Gas, Hydro, Solar, Wind).
*   **Filter by country/region:** Allow users to focus on specific geographical areas.
*   **Marker Clustering:** For areas with a high density of power plants, use marker clustering to improve performance and readability.
*   **Advanced Styling:** Customize marker icons based on fuel type or capacity.
*   **Different Base Maps:** Explore and offer options for different Folium tile layers (map styles).
*   **Data Summaries:** Display summary statistics (e.g., total capacity by fuel type for the visible map area).
*   **Web Application:** Turn this into a simple web application using Flask or Django for easier online access.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or find any issues, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourAmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/YourAmazingFeature`).
6.  Open a Pull Request.

Please ensure your code follows the existing style and that your changes are well-documented.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

*   The **World Resources Institute (WRI)** for providing and maintaining the [Global Power Plant Database](https://datasets.wri.org/dataset/globalpowerplantdatabase).
*   The developers of **Folium** and **Pandas** for their excellent libraries.
