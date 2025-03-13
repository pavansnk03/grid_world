import numpy as np

ACTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
ARROWS = {(1, 0): '↓', (-1, 0): '↑', (0, -1): '←', (0, 1): '→'}

class GridWorld:
    def __init__(self, size=4, gamma=1, theta=1e-6):
        self.size, self.gamma, self.theta = size, gamma, theta
        self.state_value = np.zeros((size, size))
        self.policy = np.full((size, size, len(ACTIONS)), 1 / len(ACTIONS))

    def step(self, state, action):
        if state in [(0, 0), (self.size - 1, self.size - 1)]:
            return state, 0
        return tuple(np.clip(np.add(state, action), 0, self.size - 1)), -1

    def policy_evaluation(self):
        while True:
            delta, new_values = 0, np.copy(self.state_value)
            for i in range(self.size):
                for j in range(self.size):
                    if (i, j) in [(0, 0), (self.size - 1, self.size - 1)]:
                        continue
                    new_values[i, j] = sum(
                        self.policy[i, j, idx] * (r + self.gamma * self.state_value[n])
                        for idx, act in enumerate(ACTIONS)
                        for n, r in [self.step((i, j), act)]
                    )
                    delta = max(delta, abs(new_values[i, j] - self.state_value[i, j]))
            self.state_value = new_values
            if delta < self.theta:
                break

    def policy_improvement(self):
        new_policy = np.zeros_like(self.policy)
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in [(0, 0), (self.size - 1, self.size - 1)]:
                    continue
                q_values = [sum(r + self.gamma * self.state_value[n] for n, r in [self.step((i, j), a)]) for a in ACTIONS]
                best_action = np.argmax(q_values)
                new_policy[i, j, best_action] = 1.0
        if np.array_equal(new_policy, self.policy):
            return False
        self.policy = new_policy
        return True

    def iterate_policy(self):
        while True:
            self.policy_evaluation()
            if not self.policy_improvement():
                break

    def print_results(self):
        print("\nFinal State Values (V):\n")
        for row in self.state_value:
            print(" ".join(f"{v:6.2f}" for v in row))
        
        print("\nOptimal Policy Directions:\n")
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in [(0, 0), (self.size - 1, self.size - 1)]:
                    print("  ⬜  ", end=" ")
                    continue
                best_move = np.argmax(self.policy[i, j])
                print(f"  {ARROWS[ACTIONS[best_move]]}  ", end=" ")
            print()

if __name__ == "__main__":
    env = GridWorld(4)
    env.iterate_policy()
    env.print_results()
