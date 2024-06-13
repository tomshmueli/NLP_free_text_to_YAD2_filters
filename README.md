
# NLP Free Text to YAD2 Filters

This project provides a solution for parsing free-text input in Hebrew to extract parameters for searching cars on the Yad2 website. The extracted parameters are used to generate URLs with the relevant filters for car searches.

## Table of Contents
- [Key Takeaways](#key-takeaways)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Key Takeaways

Key Takeaways:

1. **Problem Understanding and Constraints**:
   - Parsing Hebrew text is challenging due to a lack of robust, up-to-date models.
   - Extracting relevant filters from the text.
   - Mapping text to its corresponding code on the Yad2 website.

2. **Research Phase**:
   - Various methods were considered: Rule-Based, Regex and Matching, NLP - NER, Pre-trained models, and Custom Transformer-Based models.
   - The chosen approach is a combination of methods 2 and 3 (Regex and Matching, NLP - NER).

3. **Solution Selection**:
   - Use NER to identify relevant entities.
   - Use fuzzy matching and regex for edge cases.

4. **Project Workflow**:
   - `main.py`: Translates text from Hebrew to English using Google Translate API.
   - `parse.py`: Uses NLP tools to extract filter arrays (date, price, car types, manufacturers).
   - `mapping.py`: Creates mappings between each filter's code on the Yad2 website and the corresponding value.
   - `construct_url.py`: Constructs the appropriate URL and returns it.

5. **Detailed Solution Description**:
   - The text is translated and sent to `parse_text` function.
   - Entities are checked for dates or prices and stored if found.
   - Tokens are processed to identify car types, numbers (handling numerical descriptions), and manufacturers.
   - Fuzzy matching is used for tokens not found in the predefined lists.
   - Edge cases are handled by looking for specific phrases to determine the upper or lower bounds for dates/prices.
   - URL construction is done manually due to the complexity of class structures on the Yad2 website.

6. **Solution Analysis**:
   - The accuracy of Google Translate API is assumed to be high but can have significant gaps.
   - Translation Accuracy: 85%.
   - Parsing Quality: 90%.
   - URL Construction: Successful in all tested cases.

7. **Conclusion**:
   - The solution is reasonably effective given the time constraints, though translation quality posed some challenges that were addressed satisfactorily.


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

1. Run the main script:
   ```sh
   python main.py
   ```

2. Input your free-text search query in Hebrew, and the application will generate the relevant URL for car searches on Yad2.

## Features

- Parses free-text input in Hebrew to extract car search parameters.
- Generates URLs with filters for the Yad2 car search.
- Handles various car manufacturers and allows the user to choose up to 4 manufacturers.
