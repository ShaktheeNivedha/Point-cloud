import numpy as np
import os

# Normalize feature vector
def normalize(vec):
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec
    return vec / norm


def match_object(feature):

    models_path = "models"

    # Check if models folder exists
    if not os.path.exists(models_path):
        print("❌ Models folder not found")
        return None

    files = os.listdir(models_path)

    if len(files) == 0:
        print("⚠️ Models folder is empty")
        return None

    # Normalize input feature
    feature = normalize(feature)

    scores = {}

    for file in files:

        if file.endswith(".npy"):

            path = os.path.join(models_path, file)

            stored = np.load(path)

            # Skip mismatched features
            if feature.shape != stored.shape:
                print(f"Skipping {file} (shape mismatch)")
                continue

            stored = normalize(stored)

            # Compute distance
            score = np.linalg.norm(feature - stored)

            # Extract class name (chair_0001 → chair)
            class_name = file.split("_")[0]

            if class_name not in scores:
                scores[class_name] = []

            scores[class_name].append(score)

    # If no valid comparisons
    if len(scores) == 0:
        print("❌ No valid feature matches")
        return None

    # Find best class
    best_class = None
    best_score = float("inf")

    for cls in scores:
        avg_score = np.mean(scores[cls])

        print(f"{cls} → Score: {avg_score}")  # Debug

        if avg_score < best_score:
            best_score = avg_score
            best_class = cls

    print("Best Score:", best_score)

    # Threshold check (IMPORTANT)
    THRESHOLD = 0.6   # you can tune this

    if best_score < THRESHOLD:
        return best_class
    else:
        return None