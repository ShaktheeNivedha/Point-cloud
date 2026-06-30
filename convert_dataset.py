import open3d as o3d
import os

dataset = "dataset"

for file in os.listdir(dataset):

    if file.endswith(".off"):

        mesh = o3d.io.read_triangle_mesh(os.path.join(dataset, file))

        pcd = mesh.sample_points_uniformly(number_of_points=5000)

        new_file = file.replace(".off", ".ply")

        o3d.io.write_point_cloud(
            os.path.join(dataset, new_file),
            pcd
        )

        print(file, "converted")