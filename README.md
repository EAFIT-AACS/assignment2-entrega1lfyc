#  **PDA for the CFG: S → aSb | ε**

## 👥 **Team Members**
- **Laura Indabur García**
- **Daniela Salazar Amaya**

## 💻 **Development Environment**
- **Operating System:** Windows 11
- **Programming Language:** Python 3
- **IDE Used:** PyCharm

---

##  **Description**
This project implements a **Pushdown Automaton (PDA)** for the following **Context-Free Grammar (CFG):**

```
S → aSb | ε
```

The PDA is defined as:

```
M = {Q, Σ, Γ, δ, Z0, F}
```
Where:
- **Q = {q0, q1}** (Set of states)
- **Σ = {a, b}** (Input alphabet)
- **Γ = {Z0, P}** (Stack alphabet)
- **F = ∅** (Accepts by empty stack)
- **δ (Transition function):**

```
δ = {
    ('q0', ε, ε) -> ('q0', 'Z0'),
    ('q0', 'a', 'Z0') -> ('q0', 'PZ0'),
    ('q0', 'a', 'P') -> ('q0', 'PP'),
    ('q0', 'b', 'PP') -> ('q1', 'P'),
    ('q0', 'b', 'P') -> ('q1', 'Z0'),
    ('q1', 'b', 'PP') -> ('q1', 'P'),
    ('q1', 'b', 'P') -> ('q1', 'Z0')
}
```

---

## 🔹 **Implemented Algorithms**
### 🔹 **Algoritmo1**
Generates **five random strings** accepted by the CFG and **five that are not**. You can modify the number of generated strings in the `main` function of `algoritmo1.py`.

### 🔹 **Algoritmo2**
Takes the generated strings from **Algoritmo1** and determines **which ones are accepted** by the PDA and which are not.

### 🔹 **Algoritmo3**
*(Description pending)*

---

## **How to Run the Program**
### 🔹 **1️⃣ Open CMD as Administrator**
Navigate to the directory where the code is located:
```sh
cd C:/File/entrega2
```
### 🔹 *2️⃣ Install Dependencies**
Before running the program, install the required library:
```sh
pip install rich
```

### 🔹 **    3️⃣ Run the algorithms**
#### ➤ **To run Algoritmo1:**
```sh
python ALGORITHM_1_LFCO_2025_DSA_LIG.py
```

#### ➤ **To run Algoritmo2:**
```sh
python ALGORITHM_1_LFCO_2025_DSA_LIG.py | python ALGORITHM_2_LFCO_2025_DSA_LIG.py
```
*(Algoritmo2 takes the output from Algoritmo1, so they must be run together in this way.)*

#### ➤ **To run Algoritmo3:**
```sh
python ALGORITHM_1_LFCO_2025_DSA_LIG.py | python ALGORITHM_2_LFCO_2025_DSA_LIG.py | python ALGORITHM_3_LFCO_2025_DSA_LIG.py
```

---



