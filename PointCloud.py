import open3d as o3d

def load_point_cloud(path):
    return o3d.io.read_point_cloud(path)