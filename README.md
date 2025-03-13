# GridWorld Algorithms

This project demonstrates two important algorithms for solving Markov Decision Processes (MDPs) in a GridWorld environment:

1. **Policy Evaluation**
2. **Policy Iteration**

Both algorithms are crucial in reinforcement learning for finding optimal policies and estimating the value of each state.

---

## 1. Policy Evaluation

### Description
Policy Evaluation calculates the state values for a given policy using iterative updates until convergence. This algorithm helps in estimating the expected reward for each state under the current policy.

### Key Concepts
- **State Values (V):** The expected cumulative reward for each state.
- **Actions:** Movement directions (Up, Down, Left, Right).
- **Rewards:** A penalty of `-1` for each step to encourage shorter paths.

### Output Example
```
After 1 Steps:
  0.00 -1.00 -2.00 -3.00
 -1.00 -2.00 -3.00 -2.00
 -2.00 -3.00 -2.00 -1.00
 -3.00 -2.00 -1.00  0.00

Final Policy Directions:
 X ↓ ↓ ↓
↓ ↓ ← →
↓ ← → →
↓ → →  X
```

---

## 2. Policy Iteration

### Description
Policy Iteration improves upon Policy Evaluation by iteratively evaluating the policy and improving it until convergence to the optimal policy.

### Key Concepts
- **Policy Evaluation:** Estimate the value of each state under the current policy.
- **Policy Improvement:** Update the policy by choosing the best action in each state.
- **Optimal Policy:** The best possible set of actions that maximizes the cumulative reward.

### Output Example
```
Final State Values (V):
  0.00 -1.00 -2.00 -3.00
 -1.00 -2.00 -3.00 -2.00
 -2.00 -3.00 -2.00 -1.00
 -3.00 -2.00 -1.00  0.00

Optimal Policy Directions:
  ⬜    ↓    ↓    ↓
  ↓    ↓    ←    →
  ↓    ←    →    →
  ↓    →    →   ⬜
```

---

## Prerequisites
- Python 3.6 or higher

### Libraries Required
```
numpy
```

---

## Installation
1. Clone the repository

2. Install the dependencies:
   ```bash
   pip install numpy
   ```

---

## Usage
1. **Run Policy Evaluation:**
   ```bash
   python policy_eval.py
   ```

2. **Run Policy Iteration:**
   ```bash
   python policy_iteration.py
   ```

---

## File Structure
- **`policy_eval.py`**: Code for Policy Evaluation.
- **`policy_iteration.py`**: Code for Policy Iteration.
- **`requirements.txt`**: Dependencies for the project.
