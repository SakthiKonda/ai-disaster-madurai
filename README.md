# AI Flood Resource Allocation System (Madurai)

An AI-powered disaster response system that analyzes multiple areas in Madurai and intelligently allocates limited resources such as rescue teams and food supplies during flood situations.

---

## Problem

Floods in urban areas like Madurai create urgent challenges:
- Limited rescue resources
- Uneven distribution of aid
- Delays in identifying high-risk zones
- Vulnerable populations (elderly, women) not prioritized effectively

---

## Solution

This system uses a data-driven AI approach to:
- Analyze multiple regions simultaneously
- Evaluate key factors such as:
  - Population
  - Vulnerability
  - Severity
  - Accessibility
  - Demographics (women & elderly)
- Prioritize areas based on urgency
- Allocate limited resources efficiently

---

## Features

-  Area-level analysis (Madurai regions)
-  AI-based priority scoring
-  Rescue team allocation
-  Food supply distribution
-  Priority ranking of all areas
-  Real-time decision logic

---

## How It Works

1. The system collects data for each area
2. Calculates:
   - Rescue Priority Score
   - Food Supply Priority Score
3. Sorts all areas based on priority
4. Allocates limited resources:
   - 1 Rescue Team → Highest rescue priority area
   - 1 Food Unit → Highest food priority area
5. Displays ranked results and decisions

---

## Tech Stack

- Python
- Streamlit

---

## How to Run Locally

```bash
pip install streamlit
streamlit run app.py
