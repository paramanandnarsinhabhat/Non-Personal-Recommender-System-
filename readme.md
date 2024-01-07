# Non-Personalized Recommender System

This repository contains the code and associated files for a non-personalized recommender system. The system is designed to recommend items based on general statistics, without user-specific data.

## Project Structure

```
NON-PERSONAL-RECOMMENDER-SYSTEM-
│   .gitignore
│   requirements.txt
│
├── myenv
│
├── notebook
│   └── non_personalised_recommender_systems.ipynb
│

```

The project is structured into several directories:

- `notebook`: Contains Jupyter notebooks for exploratory data analysis and prototyping.
- `scripts`: Contains the Python script `non_personalised_recommender_systems.py` that implements the recommender system.
- `myenv`: Suggested directory for the Python virtual environment to encapsulate the dependencies.

## Installation

To run the code, you will need to install the required Python packages. A virtual environment is recommended.

1. Clone the repository to your local machine.
2. Navigate to the repository directory.
3. Create a virtual environment:

   ```
   python3 -m venv myenv
   ```

4. Activate the virtual environment:

   On macOS and Linux:
   ```
   source myenv/bin/activate
   ```

   On Windows:
   ```
   .\myenv\Scripts\activate
   ```

5. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

After installing the dependencies, you can run the script as follows:

```
python scripts/non_personalised_recommender_systems.py
```

Alternatively, you can open the Jupyter notebook in the `notebook` directory to interact with the code:

```
jupyter notebook notebook/non_personalised_recommender_systems.ipynb
```

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

