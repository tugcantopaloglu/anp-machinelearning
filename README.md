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

# Model Zoo
| Algorithm | Key Params | Overfitting? | Notes |
|-----------|------------|--------------|-------|
| Naïve Bayes | GaussianNB | **Low** | Best overall generalisation. |
| MLP | 2 × 128 neurons, *early‑stopping* | Low‑Medium | 93 % F1 live. |
| Logistic Reg. | C ∈ {1,10} | Medium | 76 % F1 live – borderline. |
| Random Forest | 300 trees | **High** | Severe overfit; rejected. |
| Decision Tree | depth = None | High | Rejected. |
| SVM | RBF, C = 1 | High | Rejected. |
| KNN | k = 2 | High | Rejected. |
| Gradient Boost | 200 estimators | High | Rejected. |
| LightGBM | default params | High | Rejected. |
| AdaBoost | 200 estimators | High | Rejected. |

## Training & Evaluation
Run **all** experiments:

```bash
python src/train.py --config configs/all_models.yaml
python src/evaluate.py --checkpoint results/model_weights/<model>.pkl
```

Metrics computed:
- **Accuracy**, **Precision**, **Recall**, **F1**, **ROC‑AUC**
- K‑fold (k = 5) cross‑validation to gauge variance.

Detailed confusion matrices and ROC curves are saved in `results/` for every model.

## Results
| Model | CV Mean | Test Accuracy | Live Accuracy | Live F1 |
|-------|---------|---------------|-----------------------|---------|
| **Naïve Bayes** | 0.903 | 0.906 | **0.82** | **0.87** |
| **MLP** | 0.967 | 0.957 | **0.91** | **0.93** |
| Logistic Reg. | 0.957 | 0.954 | 0.74 | 0.76 |
| Others | > 0.97 | > 0.98 | ≈ 0.20 | ≈ 0.22 |

**Interpretation**  
Low‑complexity generative models (NB) and moderately sized neural nets (MLP) balance bias/variance best on heterogeneous traffic, whereas tree‑based ensembles memorise training flows and collapse on unseen subnets.

## Usage
### 1. Batch Scoring
```bash
python src/api.py batch --input data/processed/new_capture.csv                         --model checkpoints/naive_bayes.pkl                         --output predictions.csv
```

### 2. Real‑time API (FastAPI)
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8080
# POST /predict {"features": [...]}  → {"anomaly": true, "score": 0.92}
```

### 3. SIEM Integration
`api.py` returns JSON for direct ingestion by Splunk/ELK.  
A webhook example is provided in `integrations/`.

## Future Work
- **Attack Type Classification** (e.g., DoS vs. Probe) with deep architectures (CNN‑1D, GRU, Transformer).  
- **Online Learning** to adapt to concept drift in evolving traffic.  
- **Adversarial Robustness** testing (evasion & poisoning).  
- **Edge Deployment** on programmable NIC / FPGA for wire‑speed inference.

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
