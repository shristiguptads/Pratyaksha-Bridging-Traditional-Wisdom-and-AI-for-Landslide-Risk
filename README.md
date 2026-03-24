# 🌱 Pratyaksha – Bridging Traditional Wisdom and AI for Landslide Risk

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Pratyaksha** (Sanskrit for "observable") is a research‑driven platform that fuses centuries‑old soil knowledge (color, texture, smell) with modern machine learning to predict landslide risk. Built on two peer‑reviewed studies from IIT Mandi, it demonstrates how indigenous expertise can enhance scientific forecasting. The system collects field data via a Streamlit frontend and provides immediate risk insights through a FastAPI backend – a scalable prototype for data‑informed slope management in the Himalayas.

---

## 📖 Table of Contents
- [✨ Features](#-features)
- [🏗️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [🎯 Usage](#-usage)
- [🔮 Future Improvements](#-future-improvements)
- [📚 Research Papers](#-research-papers)
- [📄 License](#-license)
- [👏 Acknowledgements](#-acknowledgements)

---

## ✨ Features
- 📝 **Traditional Soil Indicators** – 32 features (color, texture, smell, etc.) rated on a 1‑5 scale.
- ⚖️ **Real‑time Risk Prediction** – Placeholder model (to be replaced with trained XGBoost/SFEL).
- 💾 **Data Storage** – Observations saved in SQLite database for future model training.
- 🖥️ **Interactive Frontend** – Built with Streamlit for easy data entry and risk visualisation.
- 🔗 **Modular API** – FastAPI endpoints ready to serve ML models and manage data.

---

## 🏗️ Tech Stack
| Component   | Technology                          |
|-------------|-------------------------------------|
| Backend     | FastAPI, SQLAlchemy, SQLite, Uvicorn |
| Frontend    | Streamlit, Requests                 |
| ML (future) | XGBoost, SHAP, scikit‑learn          |
| Deployment  | (Planned) Render / Streamlit Cloud  |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- (Optional) A virtual environment manager

### Backend Setup
1. Clone the repository and navigate to the backend folder:
   ```bash
   git clone https://github.com/yourusername/pratyaksha.git
   cd pratyaksha/backend
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Copy the example environment file:
   ```bash
   cp .env.example .env          # The default .env uses SQLite
5. Start the backend server:
   ```bash
   uvicorn app.main:app --reload

### Frontend Setup
1.In a new terminal, navigate to the frontend folder:
    ```bash
    cd ../frontend
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate      # On Windows: venv\Scripts\activate
3. Install dependencies
   ```bash
   pip install -r requirements.txt
4. Launch the Streamlit app:
   ```bash
   streamlit run app.py           #The app will open in your browser at http://localhost:8501.

## 🎯 Usage
1. Adjust the 32 soil feature ratings (each from 1 to 5).

2. Click Check Risk – the backend returns a risk level (Low/Moderate/High), a score, and the top‑three contributing features.

3. Click Save Observation – the data is stored in the SQLite database (test.db).

4. View saved observations by visiting http://localhost:8000/observations/ or using the Streamlit interface (planned).

## 🔮 Future Improvements
- Train a real ML model – Replace the placeholder risk logic with the XGBoost/SFEL ensemble from the research paper using the collected dataset.

- SHAP explanations – Show which features most influence the prediction.

- Satellite data integration – Pull ΔVV deformation proxies from Google Earth Engine.

- Deploy to cloud – Host the backend on Render/Railway and the frontend on Streamlit Cloud.

- Mobile‑friendly UI – Optimise for field use on smartphones.

## 📚 Research Papers
This project is directly inspired by two studies from IIT Mandi:

1. Sankhyan, S., Sharma, S., Pohal, S., Uday, K. V., & Dutt, V. (2026)
SFEL: A machine learning framework for forecasting radar backscatter based ground deformation.
Scientific Reports.
  [Link:https://www.researchgate.net/publication/400090592_SFEL_a_machine_learning_framework_for_forecasting_radar_backscatter_based_ground_deformation]

2. Sankhyan, S., Uday, K. V., & Dutt, V. (2026)
Bridging traditional and conventional knowledge for soil classification in landslide‑prone areas using exploratory factor analysis.
Frontiers in Environmental Science. 
[Link:https://www.researchgate.net/publication/389491805_Bridging_traditional_and_conventional_knowledge_for_soil_classification_in_landslide-prone_areas_using_exploratory_factor_analysis]

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

## 👏 Acknowledgements
- The authors of the two research papers for sharing their work.

- The Indian Institute of Technology Mandi for supporting the original research.

- All contributors and open‑source libraries that made this project possible.

Made with ❤️ for the Himalayas
