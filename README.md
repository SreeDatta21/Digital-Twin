# Leveraging Digital Twin for Early Warning of Bridge Failure

A **Digital Twin** is a virtual replica or simulation of a physical object, system, or process. This project combines **3D modeling**, **IoT**, and **Machine Learning** to create a digital twin for a bridge to predict its health using data from sensors embedded in its pillars.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Components](#project-components)
  - [3D Modeling](#3d-modeling)
  - [Machine Learning](#machine-learning)
- [How It Works](#how-it-works)
- [Installation](#installation)


---

## Overview

The project provides early warnings about bridge health by analyzing sensor data from strain, temperature, and displacement. These properties are the most affected factors in determining bridge health. The results are displayed visually on a **3D model** of the bridge using a **Flask server**.

---

## Features

1. **3D Modeling:** Realistic virtual representation of a bridge and its pillars.
2. **IoT Simulation:** Strain, temperature, and displacement sensor data are embedded in each pillar.
3. **Machine Learning Integration:** A Decision Tree Classifier trained on sensor data to classify the bridge's condition as *Healthy* or *Unhealthy*.
4. **Real-time Updates:** Sensor data is analyzed and reflected on the 3D digital twin in real time.
5. **Interactive UI:** Buttons for each pillar display detailed results, with health data visualized clearly.

---

## Technology Stack

- **3D Modeling:** Blender
- **Web-based Viewer:** Model-Viewer
- **Machine Learning:** Decision Tree Classifier (Python)
- **Backend Server:** Flask
- **Languages:** Python, JavaScript, HTML, CSS

---

## Project Components

### 1. 3D Modeling

- **Tools:** Blender, Model-Viewer.
- **Bridge and Environment:** Created using Blender to simulate a realistic structure with a background.
- **Interactive Elements:** Buttons for each pillar using Model-Viewer.

### 2. Machine Learning

- **Dataset:** Contains values for strain, temperature, and displacement.
- **Model:** A Decision Tree Classifier trained to predict the bridge's health as *Healthy* or *Unhealthy*.
- **Real-time Testing:** Sensor values are sent to the model in real time, and predictions are displayed on the respective pillar of the 3D model.

---

## How It Works

1. **3D Model Creation:**  
   - A 3D representation of the bridge, pillars, and background is created using Blender.  
   - The environment and interactive buttons are set up using Model-Viewer to make the system user-friendly.  
![b1](https://github.com/user-attachments/assets/3de473fa-fae9-4224-a682-db40b49a231b)
2. **Sensor Data Collection:**  
   - The pillars of the bridge are simulated to include strain, temperature, and displacement sensors.  
   - These values are collected in real time and sent to a Flask server for processing.

3. **Machine Learning Prediction:**  
   - A Decision Tree Classifier, trained on the collected dataset, predicts the bridge's health status (*Healthy* or *Unhealthy*).  
   - Predictions are sent back to the Flask server.  

4. **Visualization on Digital Twin:**  
   - The health condition is displayed on the 3D digital twin of the bridge.  
   - Buttons attached to each pillar allow users to view detailed health reports interactively.  
![b2](https://github.com/user-attachments/assets/235a5648-4ee0-47a2-b854-287ee2e31903)
5. **Real-Time Updates:**  
   - Sensor values are continually monitored and the digital twin is updated dynamically.
![b3](https://github.com/user-attachments/assets/31736537-e0b0-4f91-9e7d-ec9fb58fc6bf)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SreeDatta21/Digital-Twin.git
2. Install Depemdencies:
   ```bash
   pip install flask scikit-learn
3. Start the Flask Server
   ```bash
   python app.py
 
