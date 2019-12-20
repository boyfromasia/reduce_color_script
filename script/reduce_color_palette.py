import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans


class ReduceColor:
    def __init__(self, filename, n):
        print("Working...")
        self.data = cv2.imread(f"./images/{filename}")
        self.model = KMeans(n_clusters=n)
        self.shape = self.data.shape
        self.y_pred = 0

    def bgr_to_rgb(self, data):
        b, g, r = cv2.split(data)
        data = cv2.merge([r, g, b])
        return data

    def preprocess_in(self, data):
        data = data / 255.0
        data = data.reshape(self.shape[0] * self.shape[1], 3)
        return data

    def preprocess_out(self, data):
        data = data.reshape(self.shape)
        data = data * 255.0
        return data

    def fit(self):
        self.model.fit(self.data)

    def predict(self):
        new_colors = self.model.cluster_centers_[self.model.predict(self.data)]
        return new_colors

    def save(self):
        cv2.imwrite("output/recolored.png", self.y_pred)

    def draw_graph(self):
        colors = self.preprocess_in(self.bgr_to_rgb(self.y_pred))
        plt.rcParams["figure.figsize"] = (30, 30)
        plt.scatter(self.data[:, 0], self.data[:, 1], s=50, c=colors, cmap='viridis')
        plt.savefig("output/plot.png")

    def start(self):
        self.data = self.preprocess_in(self.data)
        self.fit()
        self.y_pred = self.predict()
        self.y_pred = self.preprocess_out(self.y_pred)
        self.draw_graph()
        self.save()
        print("DONE!")