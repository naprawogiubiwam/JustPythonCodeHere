import numpy as np
from sklearn.cluster import KMeans

# read the satellite velocities in km/s from a txt file containling the speed (7.58061039376213 example)
# velocities = np.array([7.8, 7.81, 7.82, 7.85, 7.9, 7.91, 7.92, 8.0, 8.1, 8.15])
velocities = np.loadtxt('km_satellites.txt')
print(velocities)
print(velocities.shape)

# Reshape data for clustering
velocities = velocities.reshape(-1, 1)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3)  # Adjust the number of clusters as needed
kmeans.fit(velocities)

# Get cluster labels
labels = kmeans.labels_

# Print grouped velocities
for i in range(3):  # Adjust the range based on the number of clusters
    group = velocities[labels == i]
    print(f"Group {i+1}: {group.flatten()}")
