import os
import numpy as np

from PointCloud import load_point_cloud
from preprocessing import preprocess_pointcloud
from feature_extraction import extract_features

dataset = "dataset"
models = "models"

os.makedirs(models, exist_ok=True)

for file in os.listdir(dataset):

    if file.endswith(".ply"):

        print("Processing:", file)

        pcd = load_point_cloud(os.path.join(dataset, file))

        pcd = preprocess_pointcloud(pcd)

        feature = extract_features(pcd)

        name = file.replace(".ply", ".npy")

        np.save(os.path.join(models, name), feature)

        print("Saved:", name)

print("Training completed")