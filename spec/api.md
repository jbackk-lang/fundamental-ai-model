# API — Public Interface for Libraries, Models and Simulations  
*Fundamental AI Model*

## 1. Overview
This document defines the **public API** for interacting with the  
Fundamental AI Model.

The API is designed to be:
- minimal  
- stable  
- composable  
- language‑agnostic  
- implementation‑independent  

It exposes:
- orientation operations  
- collapse mechanics  
- residue tracking  
- horizon state  
- chain evolution  
- carrier simulation  
- FFT projection  

---

# 2. Core API Structure

Each module exposes a clean, minimal interface.

---

# 3. Orientation API

### 3.1 Get Orientation

### 3.2 Flip Orientation

### 3.3 Validate Orientation

---

# 4. Collapse API

### 4.1 Trigger Collapse

### 4.2 Collapse Probability

### 4.3 Collapse History

---

# 5. Residue API

### 5.1 Get Total Residue

### 5.2 Get Residue for Structure

### 5.3 Add Residue (internal)

---

# 6. Horizon API

### 6.1 Get Horizon State

### 6.2 Horizon Growth Rate

### 6.3 Horizon Crossing Check

---

# 7. Eye API

### 7.1 Get Eye State

### 7.2 Trigger Eye Event

### 7.3 Eye Activity History

---

# 8. Chain API

### 8.1 Get Chain Length

### 8.2 Get Link by Index

### 8.3 Append Link (internal)

---

# 9. Carrier API

### 9.1 Create Carrier

### 9.2 Step Carrier

### 9.3 Get Carrier State

---

# 10. FFT API

### 10.1 Compute FFT from Residue Sequence

### 10.2 Get FFT of Chain Residue

### 10.3 Get FFT Metadata

---

# 11. Simulation API

### 11.1 Run Simulation Step

### 11.2 Run N Steps

### 11.3 Reset Simulation

---

# 12. API Summary

The API exposes:
- orientation operations  
- collapse mechanics  
- residue tracking  
- horizon state  
- Eye events  
- chain evolution  
- carrier simulation  
- FFT projection  
- full simulation control  

The API is:
- modular  
- deterministic in structure  
- stochastic in collapse  
- scalable  
- universal  

This is the **official public interface** of the Fundamental AI Model.

The API is divided into modules:

