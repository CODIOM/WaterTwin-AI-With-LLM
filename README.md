<div id="top">

<div align="center">

<img src="codiom.jpeg" width="180px" alt="" style="margin-bottom: 10px;"/>

# <code>WATERTWIN AI: LLM-DRIVEN DIGITAL TWIN</code>
<div align="center">
  <img src="https://github.com/user-attachments/assets/51fd7451-e708-4fd2-a70e-caac8746781a" width="300" height="300" alt="WaterTwin AI Dashboard">
</div>

**CODIOM**



<em>Technologies to be Used:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Google_Gemini_2.0-4285F4.svg?style=for-the-badge&logo=Google-Gemini&logoColor=white" alt="Gemini">
<img src="https://img.shields.io/badge/scikit--learn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=for-the-badge&logo=Plotly&logoColor=white" alt="Plotly">
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="NumPy">

</div>
<br>

---

##  Table of Contents
- [ Overview](#️-overview)
- [ Team](#-team)
- [ Problem](#-problem)
- [ Solution](#-solution)
- [AI & LLM Integration](#-ai--llm-integration)
- [ Key Features](#-key-features)
- [ Installation & Usage](#️-installation--usage)
- [ Tech Stack](#-tech-stack)
- [ System Architecture](#️-system-architecture)
- [ Data Sources](#-data-sources)
- [ Roadmap](#️-roadmap)
---

##  Overview
**WaterTwin AI** is a high-fidelity **Digital Twin** platform designed for urban rainwater harvesting without the need for physical sensors or hardware dependency. By utilizing **mathematical simulations**, **Machine Learning forecasting**, and **Generative AI (LLM)**, it creates a virtual representation of water systems to predict risks and provide strategic management advice.
##  Team

| Role | Member | LinkedIn |
|------|--------|-----------|
| **AI Strategy & Data Modeling** | Berat Erol Çelik | [![LinkedIn](https://img.shields.io/badge/-Berat_Erol_Çelik-0077B5?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/berat-erol-%C3%A7elik-513915258/) |
| **Backend & System Architecture** | Emre Aldemir | [![LinkedIn](https://img.shields.io/badge/-Emre_Aldemir-0077B5?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/emre-aldemir-1b2301293/) |
| **Frontend & UI/UX Dashboard** | Umut Odabaş | [![LinkedIn](https://img.shields.io/badge/-Umut_Odabaş-0077B5?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/umut-odaba%C5%9F-8a26142a2/) |
| **Machine Learning Forecasting** | Ömer Altıntaş | [![LinkedIn](https://img.shields.io/badge/-Ömer_Altıntaş-0077B5?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/%C3%B6mer-alt%C4%B1nta%C5%9F-44773730b/) |

---

##  Problem
Rainwater management in urban areas often suffers from a lack of proactive intelligence:
- **High Hardware Costs:** Installing physical sensors for every tank is expensive and hard to maintain.
- **Reactive Management:** Decisions are often made only after a tank is empty or has already overflowed.
- **Data Interpretation Gap:** Raw numerical data (rainfall mm, tank liters) is difficult for non-engineers to translate into actionable strategy.

---

##  Solution
**WaterTwin AI** solves these challenges through a **purely software-based** approach:
- **Virtual Simulation:** Calculates water inflow using vectorized math based on roof area and runoff coefficients.
- **Predictive Demand:** Forecasts water usage using a **Scikit-Learn** model that adapts to ambient temperature.
- **Generative Strategy:** Employs **Gemini 2.0 Flash** to act as a "Senior Water Engineer," interpreting simulation results into clear strategic reports.

---
## AI & LLM Integration
### 1. Generative Strategic Advisor (LLM)
* **Model:** Google Gemini 2.0 Flash.
* **Function:** The LLM processes simulation telemetry (overflow volume, fill rates, inflow) and provides 3-sentence, action-oriented engineering reports.
* **Persona:** It operates with a technical, water-conservation-focused persona to ensure professional decision support.

### 2. Predictive Usage Forecasting (ML)
* **Model:** Linear Regression (Scikit-Learn).
* **Function:** Analyzes ambient temperature to predict water demand. This allows the Digital Twin to dynamically simulate increased consumption during hot weather scenarios.


##  Key Features

| Feature | Description | Status |
|---------|-------------|---------|
| **Digital Twin Logic** | High-fidelity NumPy-based water balance simulation | ✅ Done |
| **LLM Reasoning** | Gemini 2.0 Flash interpreting telemetry into reports | ✅ Done |
| **ML Usage Forecast** | Temperature-driven water demand prediction model | ✅ Done |
| **Safety Thresholds** | Real-time monitoring for Overflow and Critical Low (%15) levels | ✅ Done |
| **Industrial UI** | Dark-themed Plotly Gauge charts and metric dashboards | ✅ Done |
---

## Installation & Usage

To run **WaterTwin AI** locally, follow these steps.

### 1. Clone the Repository
```bash
git clone https://github.com/CODIOM/WaterTwin-AI-With-LLM
cd WaterTwin-AI-With-LLM
```
### 2. Environment Setup
Create a virtual environment (optional but recommended) and install dependencies.

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```
### 3. Configure API Keys
This project uses Google Gemini 2.0 Flash. You need to set up your API key.
- Create a .env file in the root directory.
- Add your Google API key as shown below:
  
```bash
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```
### 4. Run the Dashboard
Launch the Streamlit application:
```bash
streamlit run app.py
```
### A Small Detail You Should Pay Attention To:
To ensure these instructions work correctly, you must have a **`requirements.txt`** file in your project folder. If you haven't created one yet, you can create it by typing the following code into your terminal:

```bash
pip freeze > requirements.txt
```

---
##  Tech Stack
### AI & Machine Learning
<img src="https://img.shields.io/badge/Gemini_2.0_Flash-4285F4.svg?style=for-the-badge&logo=Google-Gemini&logoColor=white" alt="Gemini"> <img src="https://img.shields.io/badge/scikit--learn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn"> <img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="NumPy">

### Backend & Simulation Core
<img src="https://img.shields.io/badge/Python_3.11-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Joblib-000000.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Joblib"> <img src="https://img.shields.io/badge/Dotenv-ECD53F.svg?style=for-the-badge&logo=dotenv&logoColor=white" alt="Dotenv">

### Frontend & Data Visualization
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit"> <img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=for-the-badge&logo=Plotly&logoColor=white" alt="Plotly"> <img src="https://img.shields.io/badge/HTML5/CSS3-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML/CSS">


---

## System Architecture

The system utilizes a modular **Model-Service-App** architecture to ensure separation of concerns.
```sh
└── /
    ├── ai_models
    │   └── usage_forecaster.py  # ML Model Training script
    ├── backend
    │   ├── ai
    │   │   └── advisor.py       # LLM (Gemini) Integration layer
    │   └── services
    │       └── engine.py        # Core Digital Twin Logic
    ├── data
    │   └── system_params
    │       └── config.json      # Dynamic Thresholds (e.g., %15 Low)
    ├── models
    │   ├── usage_forecaster.joblib
    │   └── watertwin_engine.joblib
    └── app.py                   # Streamlit Frontend & Entry Point
```

### API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/predict/rain` | GET | Returns an ML-based rainfall forecast for the specified location. |
| `/api/simulate/tank` | POST | Calculates the expected tank level based on forecasted rainfall. |
| `/api/simulate/scenario` | POST | Runs a "What-if" scenario (e.g., heavy storm or drought simulation). |
| `/api/report/capacity` | GET | Returns predicted water availability and sustainability reports for the upcoming week. |

### Data Flow
1. **Input**: System receives environmental inputs (Rainfall mm, Temperature °C) and infrastructure parameters ($m^2$, L) from the Dashboard.
2. **ML Prediction**: The Scikit-Learn model calculates expected daily usage based on ambient temperature.
3. **Calculation**: Total Inflow is processed with formula.
4. **Digital Twin**: Virtual tank levels are updated, and boundary constraints (0 to Capacity) are applied via NumPy.
5. **AI Synthesis**: Simulation results are sent to Gemini 2.0 Flash for strategic reasoning.

---

##  Roadmap
-  **`Task 1`**: High-Fidelity Mathematical Algorithm Design (Rainfall-to-Volume Vectorization).
-  **`Task 2`**: Development of LLM-Driven Strategic Advisor & Reasoning Layer (Gemini 2.0 Flash).
-  **`Task 3`**: Core Digital Twin Simulation Engine Development (NumPy-based).
-  **`Task 4`**: Implementation of Generative AI for Actionable Engineering Reports.
-  **`Task 5`**: Industrial Dashboard Design & Plotly Visualization Integration.
-  **`Task 6`**: Automation with Live Meteorological Forecast APIs (e.g., Istanbul Weather Data).



---

### Example Data Flow

1. Scenario: A user inputs a 30mm rainfall forecast and an ambient temperature of 35°C.
2. System Setup: The Digital Twin is configured with a 500$m^2$ roof and a 15,000L tank (starting at 40% full).
3. ML Prediction: At 35°C, the ML model predicts a high usage of 700L due to heat.
4. Calculation: 30mm $\times$ 500$m^2$ $\times$ 0.9 (efficiency) = 13,500L Inflow.
5. Simulation: Start (6,000L) + Inflow (13,500L) - Usage (700L) = 18,800L.
6. Outcome: Final level clips to 15,000L, resulting in a 3,800L Predicted Overflow.
7. AI Advice: "High overflow risk detected. Prioritize water-intensive tasks today to maximize storage space before the rainfall event."

---


[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
















