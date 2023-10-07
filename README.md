```
# Weather App - py3

Weather application that provides real-time weather information for a given city.

## Features

- Retrieve weather data using the OpenWeatherMap API.
- Display current temperature, weather description, and location.
- Dynamic weather icon based on the current weather conditions.
- User-friendly graphical interface.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/weather-app.git
   ```

2. Change directory:

   ```bash
   cd weather-app
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a `.env` file in the project directory and add your OpenWeatherMap API key as follows:

   ```
   API_KEY=your_api_key_here
   ```

7. Run the app:

   ```bash
   python app.py
   ```

## Usage

- Enter the name of a city in the input field and click the "Search" button to view the weather details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Icons provided by OpenWeatherMap.
- Built with Python, Tkinter, and requests.
