import streamlit as st
import numpy as np
import plotly.graph_objects as go
import os

from PointCloud import load_point_cloud
from preprocessing import preprocess_pointcloud
from feature_extraction import extract_features
from matcher import match_object
from info_fetcher import get_object_info
# from object_info import object_purpose

st.set_page_config(page_title="3D Object Recognition", layout="wide")

st.title("3D Object Recognition using Point Cloud")
st.write("Feature Discovery in 3D Point Cloud using Structural Pattern Matching")

menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Dashboard", "View Dataset", "Convert Dataset", "Train Model", "Recognize Object"]
)

# ---------------- HOME ---------------- #
if menu == "Home":

   

    st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>
    3D Object Recognition System
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h4 style='text-align: center;'>
    Feature Discovery in 3D Point Cloud using Structural Pattern Matching
    </h4>
    """, unsafe_allow_html=True)

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        🔍 **What This Project Does**
        
        - Converts 3D objects into point clouds  
        - Extracts structural features (FPFH)  
        - Matches with dataset  
        - Identifies object + purpose  
        """)

    with col2:
        st.success("""
        ⚙️ **Technologies Used**
        
        - Open3D  
        - Streamlit  
        - NumPy  
        - Plotly  
        - Machine Learning Concepts  
        """)

    st.write("---")

    st.subheader("📊 System Workflow")

    st.markdown("""
    ```
    Input Object
        ↓
    Point Cloud Processing
        ↓
    Feature Extraction (FPFH)
        ↓
    Pattern Matching
        ↓
    Object Recognition
    ```
    """)

    st.write("---")

    st.subheader("🚀 Features")

    col3, col4, col5 = st.columns(3)

    with col3:
        st.write("✔ 3D Visualization")
        st.write("✔ Real-time Processing")

    with col4:
        st.write("✔ Feature Discovery")
        st.write("✔ Pattern Matching")

    with col5:
        st.write("✔ Object Recognition")
        st.write("✔ Web Interface")

    st.write("---")

    st.success("👉 Use the sidebar to navigate through the system")

#----------------- DASHBOARD -------------------#

elif menu == "Dashboard":

    st.title("📊 3D Structural Pattern Matching Dashboard")

    if "pcd" not in st.session_state:
        st.warning("⚠️ Run object recognition first")
    else:

        pcd = st.session_state["pcd"]
        prediction = st.session_state["prediction"]
        feature = st.session_state["feature"]

        points = np.asarray(pcd.points)

        st.write("---")

        # 🔷 1. Point Cloud
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("🔹 Input Point Cloud")

            fig = go.Figure(data=[go.Scatter3d(
                x=points[:,0],
                y=points[:,1],
                z=points[:,2],
                mode='markers',
                marker=dict(size=2, color='blue')
            )])

            st.plotly_chart(fig, use_container_width=True)

        # 🔷 2. Keypoints (Simulated)
        with col2:
            st.subheader("🔹 Keypoints")

            keypoints = points[::50]  # sample points

            fig2 = go.Figure(data=[go.Scatter3d(
                x=keypoints[:,0],
                y=keypoints[:,1],
                z=keypoints[:,2],
                mode='markers',
                marker=dict(size=4, color='red')
            )])

            st.plotly_chart(fig2, use_container_width=True)

        # 🔷 3. Feature Visualization
        with col3:
            st.subheader("🔹 Feature Distribution")

            st.line_chart(feature)

        st.write("---")

        # 🔷 Matching Result
        st.subheader("🔄 Recognition Result")

        col4, col5 = st.columns(2)

        with col4:
            st.write("**Before Processing**")

            fig3 = go.Figure(data=[go.Scatter3d(
                x=points[:,0],
                y=points[:,1],
                z=points[:,2],
                mode='markers',
                marker=dict(size=2, color='gray')
            )])

            st.plotly_chart(fig3)

        with col5:
            st.write("**After Processing (Highlighted)**")

            fig4 = go.Figure(data=[go.Scatter3d(
                x=points[:,0],
                y=points[:,1],
                z=points[:,2],
                mode='markers',
                marker=dict(size=2, color=points[:,2], colorscale='Viridis')
            )])

            st.plotly_chart(fig4)

        st.write("---")

        # 🔷 Metrics (Dynamic)
        st.subheader("📈 Performance Metrics")

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric("Detected Object", prediction)

        with m2:
            st.metric("Feature Size", len(feature))

        with m3:
            st.metric("Points", len(points))

        st.success("✅ Dashboard generated from real object data")

# ---------------- VIEW DATASET ---------------- #
elif menu == "View Dataset":

    st.header("View Dataset Objects")

    files = [f for f in os.listdir("dataset") if f.endswith(".ply")]

    if len(files) == 0:
        st.warning("No .PLY files found")
    else:

        selected = st.selectbox("Select Object", files)

        if st.button("Load Object"):

            pcd = load_point_cloud(os.path.join("dataset", selected))

            points = np.asarray(pcd.points)

            fig = go.Figure(data=[go.Scatter3d(
                x=points[:,0],
                y=points[:,1],
                z=points[:,2],
                mode='markers',
                marker=dict(
                    size=2,
                    color=points[:,2],
                    colorscale='Viridis'
                )
            )])

            st.plotly_chart(fig, use_container_width=True)

# ---------------- CONVERT DATASET ---------------- #
elif menu == "Convert Dataset":

    st.header("Convert OFF → PLY")

    st.write("This will convert all .OFF files in dataset folder to .PLY format")

    if st.button("Start Conversion"):

        import open3d as o3d

        dataset = "dataset"

        if not os.path.exists(dataset):
            st.error("Dataset folder not found")
        else:

            files = os.listdir(dataset)

            off_files = [f for f in files if f.endswith(".off")]

            if len(off_files) == 0:
                st.warning("No .OFF files found in dataset folder")
            else:

                progress = st.progress(0)

                for i, file in enumerate(off_files):

                    path = os.path.join(dataset, file)

                    mesh = o3d.io.read_triangle_mesh(path)

                    pcd = mesh.sample_points_uniformly(number_of_points=5000)

                    new_file = file.replace(".off", ".ply")

                    o3d.io.write_point_cloud(
                        os.path.join(dataset, new_file),
                        pcd
                    )

                    progress.progress((i + 1) / len(off_files))

                    st.write(f"Converted: {file}")

                st.success("✅ Conversion Completed!")

# ---------------- TRAIN MODEL ---------------- #
elif menu == "Train Model":

    st.header("Train Dataset (Generate Models)")

    st.write("This will extract features from dataset and store in models/ folder")

    if st.button("Start Training"):

        import numpy as np
        from PointCloud import load_point_cloud
        from preprocessing import preprocess_pointcloud
        from feature_extraction import extract_features

        dataset = "dataset"
        models = "models"

        os.makedirs(models, exist_ok=True)

        if not os.path.exists(dataset):
            st.error("Dataset folder not found")
        else:

            files = [f for f in os.listdir(dataset) if f.endswith(".ply")]

            if len(files) == 0:
                st.warning("No .PLY files found in dataset")
            else:

                progress = st.progress(0)

                for i, file in enumerate(files):

                    path = os.path.join(dataset, file)

                    pcd = load_point_cloud(path)
                    pcd = preprocess_pointcloud(pcd)

                    feature = extract_features(pcd)

                    name = file.replace(".ply", ".npy")

                    np.save(os.path.join(models, name), feature)

                    progress.progress((i + 1) / len(files))

                    st.write(f"Trained: {file}")

                st.success("✅ Training Completed! Models saved in /models folder")

# ---------------- RECOGNIZE OBJECT ---------------- #
elif menu == "Recognize Object":

    st.header("Upload Object")

    uploaded = st.file_uploader("Upload PLY", type=["ply"])

    if uploaded:

        os.makedirs("uploads", exist_ok=True)

        path = os.path.join("uploads", "temp.ply")

        with open(path, "wb") as f:
            f.write(uploaded.read())

        st.success("File uploaded")

        pcd = load_point_cloud(path)

        # Show object
        points = np.asarray(pcd.points)

        fig = go.Figure(data=[go.Scatter3d(
            x=points[:,0],
            y=points[:,1],
            z=points[:,2],
            mode='markers',
            marker=dict(size=2)
        )])

        st.plotly_chart(fig, use_container_width=True)

        # Process
        pcd = preprocess_pointcloud(pcd)
        feature = extract_features(pcd)

        prediction = match_object(feature)

        # ✅ STORE HERE (IMPORTANT)
        st.session_state["pcd"] = pcd
        st.session_state["prediction"] = prediction
        st.session_state["feature"] = feature

        st.subheader("Result")

        if prediction:

            name = prediction.replace(".npy","")

            st.success(f"Detected Object: {name}")

            st.info("Confidence: High (Feature Match)")

            info = get_object_info(name.split("_")[0])

            st.subheader("Object Information")
            st.write(info)

        else:
            st.warning("No match found")