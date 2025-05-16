# Anti Network Pirate - Anomaly Detection Platform (Prototype)
[![Python Script Workflow](https://github.com/tugcantopaloglu/anp/actions/workflows/python-app.yml/badge.svg)](https://github.com/tugcantopaloglu/anp/actions/workflows/python-app.yml)  

This repository contains a prototype implementation of **AnP**, a simplified **Anomaly Detection Platform** developed for research and experimentation purposes. It allows the testing and demonstration of various anomaly detection methods, particularly for time series data such as system resource usage or application logs.

> ⚠️ **Disclaimer:** This is a prototype project. Several features, models, and modules are developed purely for testing purposes and may be incomplete or unstable.

---

## 🚀 Features

- 📊 Time series anomaly detection
- 🧠 Classical ML-based methods (Isolation Forest, One-Class SVM, etc.)
- 🧪 Test cases for memory, CPU, disk, and other system metrics
- 📈 Interactive result visualization using Matplotlib and Pandas
- 🧼 Synthetic anomaly generation for testing
- 📁 Modular structure for easy experimentation

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/tugcantopaloglu/anp.git
cd anp
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

> 💡 Note: It is recommended to use a virtual environment.

---

## 📂 Project Structure

```
anp/
├── data/                   # Input data files (e.g., system metrics)
├── models/                 # Custom anomaly detection implementations
├── utils/                  # Utility functions (data loading, metrics, etc.)
├── notebooks/              # Sample Jupyter notebooks for testing and visualization
├── main.py                 # Entry point for testing anomaly detection models
├── test_cases/             # Synthetic test case generators
└── requirements.txt        # Python package requirements
```

---

## 🧪 Usage

Run the main script to execute a test case:

```bash
python main.py --test memory
```

This will:
- Load the corresponding synthetic test data,
- Apply the selected anomaly detection algorithm,
- Visualize results and print anomaly statistics.

Available test types:
- `memory`
- `cpu`
- `disk`
- `multivariate`

---

## 🧠 Models

Current anomaly detection methods supported:

- Isolation Forest
- One-Class SVM
- Elliptic Envelope
- Custom thresholding logic

Planned additions:
- LSTM Autoencoders
- Facebook Prophet
- Statistical methods like STL

---

## 📊 Example Output

Output includes:
- Anomaly scores
- Anomaly flags (binary)
- Visualizations with anomaly points highlighted

You can find example plots and logs inside the `notebooks/` or `outputs/` folders (if enabled).

---

## 📌 TODOs & Notes

- Add advanced anomaly detection models (LSTM, Variational Autoencoders)
- Improve test data generation realism
- Refactor configuration into a YAML-based setup
- Add unit tests for model evaluation and metrics

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributions

Feel free to fork this repository and open pull requests for enhancements, bugfixes, or new models.

---

## 👨‍💻 Author

Developed by [Tuğcan Topaloğlu](https://github.com/tugcantopaloglu)  
For research and educational purposes.
