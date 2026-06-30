import open3d as o3d
import numpy as np

def extract_features(pcd):

    # Better preprocessing
    pcd = pcd.voxel_down_sample(0.02)

    pcd.estimate_normals(
        o3d.geometry.KDTreeSearchParamHybrid(
            radius=0.05,
            max_nn=30
        )
    )

    fpfh = o3d.pipelines.registration.compute_fpfh_feature(
        pcd,
        o3d.geometry.KDTreeSearchParamHybrid(
            radius=0.1,
            max_nn=100
        )
    )

    # Better aggregation
    feature = np.hstack([
        np.mean(fpfh.data, axis=1),
        np.std(fpfh.data, axis=1)
    ])

    return feature