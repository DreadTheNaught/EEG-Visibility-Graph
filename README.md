# EEG-Visibility-Graph

## Overview
This project explores the use of visibility graphs for EEG-based alcoholic classification. The method involves converting EEG time-series data into graphs and extracting relevant features for classification using statistical and graph-based approaches.

## Features
- **Graph-based classification** using EEG signals.
- **Feature selection** to optimize model performance.
- **Statistical analysis** of extracted features.
- **Data extraction and preprocessing** scripts.
- **Support for multiple datasets** including `.csv` and `.json` formats.

## Repository Structure
```
├── classification_graph_based.ipynb   # Graph-based classification notebook
├── classification_statistical.ipynb   # Statistical classification notebook
├── data_extraction.py                 # Script for EEG data preprocessing
├── feature_selection.ipynb            # Feature selection notebook
├── lda_data_test.csv                   # Test data for LDA
├── lda_data_train.csv                  # Training data for LDA
├── sensor_data.json                    # Raw sensor data
├── sensor_data_test.json               # Test sensor data
├── utility.py                           # Utility functions
├── .gitignore                          # Ignored files
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/EEG-Visibility-Graph.git
   cd EEG-Visibility-Graph
   ```

## Usage
1. **Preprocess Data**: Use `data_extraction.py` to process raw EEG data.
2. **Feature Selection**: Run `feature_selection.ipynb` to select the most relevant features.
3. **Train & Evaluate**:
   - `classification_graph_based.ipynb` for graph-based models.
   - `classification_statistical.ipynb` for statistical models.
4. **Test with New Data**: Load test datasets (`sensor_data_test.json` or `lda_data_test.csv`) and evaluate performance.

## Dependencies
- Python 3.x
- NumPy
- Pandas
- NetworkX (for graph-based processing)
- Scikit-learn
- Matplotlib

## Contributing
Feel free to submit pull requests or report issues.

## License
MIT License

## Acknowledgments
- Based on EEG visibility graph transformation techniques.
- Data sourced from https://archive.ics.uci.edu/dataset/121/eeg+database.

