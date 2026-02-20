import matplotlib.pyplot as plt
import numpy as np

pulls, probs = [], []
with open("result.txt") as f:
    next(f)
    for line in f:
        p, prob = line.strip().split("\t")
        pulls.append(int(p))
        probs.append(float(prob))

pulls = np.array(pulls)
probs = np.array(probs)
cdf = np.cumsum(probs)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# PDF
axes[0][0].plot(pulls, probs)
axes[0][0].set_title("PDF")
axes[0][0].set_xlabel("Pulls")
axes[0][0].set_ylabel("Probability")
axes[0][0].grid(True, alpha=0.3)

# CDF
axes[0][1].plot(pulls, cdf)
axes[0][1].set_title("CDF")
axes[0][1].set_xlabel("Pulls")
axes[0][1].set_ylabel("Cumulative Probability")
axes[0][1].grid(True, alpha=0.3)

# Normalized PDF (log scale to see structure despite spikes)
axes[1][0].plot(pulls, probs)
axes[1][0].set_yscale("log")
axes[1][0].set_title("PDF (log scale)")
axes[1][0].set_xlabel("Pulls")
axes[1][0].set_ylabel("Probability (log)")
axes[1][0].grid(True, alpha=0.3)

# Normalized CDF (zoomed into 0.9–1.0 range)
axes[1][1].plot(pulls, cdf)
axes[1][1].set_ylim(0.9, 1.005)
axes[1][1].set_title("CDF (zoomed 0.9–1.0)")
axes[1][1].set_xlabel("Pulls")
axes[1][1].set_ylabel("Cumulative Probability")
axes[1][1].grid(True, alpha=0.3)

for ax in axes.flat:
    for x in [240, 480, 720, 960]:
        ax.axvline(x=x, color='r', linestyle='--', alpha=0.4, label=f'{x}' if ax == axes[0][0] else None)

axes[0][0].legend()
plt.suptitle("Distribution of pulls to get 6 rate-up copies", fontsize=14)
plt.tight_layout()
plt.savefig("distribution.png", dpi=150)
plt.show()
