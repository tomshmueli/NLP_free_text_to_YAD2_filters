
# NLP Free Text to YAD2 Filters

This project provides a solution for parsing free-text input in Hebrew to extract parameters for searching cars on the Yad2 website. The extracted parameters are used to generate URLs with the relevant filters for car searches.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
```
Explain your project structure here. Example:
```
- `main.py` : The main script to run the application.
- `parser.py` : Contains functions to parse the free-text input.
- `url_generator.py` : Generates the URL based on extracted parameters.
- `requirements.txt` : Lists the dependencies required for the project.
```

## Installation

To run this project, you need to have Python 3.9 and the necessary libraries installed. Follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/tomshmueli/NLP_free_text_to_YAD2_filters.git
   cd NLP_free_text_to_YAD2_filters
   ```

2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To use the application, follow these steps:

1. Add your OpenAI API key securely:
   ```sh
   export OPENAI_API_KEY='your-api-key'
   ```

2. Run the main script:
   ```sh
   python main.py
   ```

3. Input your free-text search query in Hebrew, and the application will generate the relevant URL for car searches on Yad2.

## Features

- Parses free-text input in Hebrew to extract car search parameters.
- Generates URLs with filters for the Yad2 car search.
- Handles various car manufacturers and allows the user to choose up to 4 manufacturers.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

