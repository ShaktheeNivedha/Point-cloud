import open3d as o3d

def preprocess_pointcloud(pcd):

    # Downsample
    pcd = pcd.voxel_down_sample(voxel_size=0.02)

    # Remove noise
    pcd, _ = pcd.remove_statistical_outlier(
        nb_neighbors=20,
        std_ratio=2.0
    )

    # Estimate normals
    pcd.estimate_normals()

    return pcd