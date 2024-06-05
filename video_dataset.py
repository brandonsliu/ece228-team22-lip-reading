import os
import cv2
import torch
import numpy as np
from torch.utils.data import Dataset
from PIL import Image

class VideoDataset(Dataset):
    def __init__(self, root_dir, mode='train', transform=None, target_size=(64,64), max_frames=29):
        self.root_dir = root_dir
        self.transform = transform
        self.target_size = target_size
        self.mode = mode

        self.max_frames = max_frames
        self.classes = sorted([d for d in os.listdir(root_dir) if not d.startswith('.')])
        self.file_paths = []
        self.labels = []
        
        for label, class_name in enumerate(self.classes):
            class_dir = os.path.join(root_dir, class_name, mode)
            for file_name in os.listdir(class_dir):
                if file_name.endswith(".mp4"):
                    self.file_paths.append(os.path.join(class_dir, file_name))
                    self.labels.append(label)

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        video_path = self.file_paths[idx]
        label = self.labels[idx]

        cap = cv2.VideoCapture(video_path)
        frames = []
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
            frames.append(frame)
            if len(frames) == self.max_frames:
                break
        cap.release()

        if len(frames) < self.max_frames:
            # Pad the video to the required number of frames with black frames
            padding = [np.zeros(self.target_size, dtype=np.uint8) for _ in range(self.max_frames - len(frames))]
            frames.extend(padding)

        frames = np.array(frames)
        frames = torch.tensor(frames, dtype=torch.float32) / 255.0
        frames = frames.unsqueeze(1)  # Add channel dimension (29, 1, 64, 64)
        label = torch.tensor(label, dtype=torch.long)

        return frames, label