import numpy as np
def sigmoid(yin):
    # Standard formula is 1/(1+exp), not 1-exp
    return 1 / (1 + np.exp(-yin))
def tanh(yin):
    return np.tanh(yin)
def activation(activation_type, yin, theta, off_state):
    if activation_type == 1:
        return 1 if yin > theta else off_state
    elif activation_type == 2:
        return 1 if sigmoid(yin) > theta else off_state
    elif activation_type == 3:
        return 1 if tanh(yin) > theta else off_state
def train(data, n, w, ch_w, b, ch_b, alpha, activation_type, theta, 
max_epochs=5):
    dataset = np.array(data)
    X = dataset[:, :-1]
    T = dataset[:, -1]
    # STOPPING CRITERIA HELPER: Determine if targets use 0 or -1
    off_state = -1 if -1 in np.unique(T) else 0
    for epoch in range(1, max_epochs + 1):
        print(f"\n===== Epoch {epoch} =====")
        print(f"{'Inputs':<12} {'t':<3} {'yin':<7} {'y':<4} {'chg_W':<12} 
{'chg_b':<6} {'W':<12} {'b':<5}")
        print("-" * 75)
        error_occurred = False
        for i in range(len(X)):
            x_i = X[i]
            t_i = T[i]
            yin = np.dot(x_i, w) + b
            y = activation(activation_type, yin, theta, off_state)
            # Reset changes for this step (display only)
            ch_w = np.zeros(n)
            ch_b = 0.0
            if y != t_i:
                ch_w = alpha * t_i * x_i
                w = w + ch_w
                ch_b = alpha * t_i
                b = b + ch_b
                error_occurred = True
            print(f"{str(x_i):<12} {t_i:<3} {yin:<7.2f} {y:<4} {str(ch_w):<12} 
{ch_b:<6.1f} {str(w):<12} {b:<5.1f}")
        if not error_occurred:
            print(f"\nCONVERGED at Epoch {epoch}")
            return w, b
    return w, b
# --- Execution --
try:
    data = np.loadtxt(r"\\172.16.16.220\CSE-Student\UG\23BCS\A\19805\SEM6\
exercises\EX_7\data.txt", dtype=int)
    n = int(input("Enter number of inputs (n): "))
    print("Enter initial weights:")
    w = np.array([float(input(f"w{i+1}: ")) for i in range(n)])
    ch_w = np.zeros(n)
    b = float(input("Enter bias (b): "))
    ch_b = 0.0
    alpha = float(input("Enter learning rate (alpha): "))
    print("\nSelect Activation Function:\n1. Threshold\n2. Sigmoid\n3. Tanh")
    activation_type = int(input("Enter choice (1-3): "))
    theta = float(input("Enter threshold: ")) 
    final_w, final_b = train(data, n, w, ch_w, b, ch_b, alpha, activation_type, 
theta)
    print(f"\nFinal Answer:\nWeights: {final_w}\nBias: {final_b}")
except Exception as e:
    print(f"Error: {e}")
