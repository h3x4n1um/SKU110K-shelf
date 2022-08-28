import os
import numpy as np

LABELS_DIR = "shelf_labels"
IMAGES_DIR = "images"
TRAIN_SIZE = 0.8

def write_set(files: np.ndarray, set_name: str) -> None:
    with open("{}.txt".format(set_name), 'w') as f:
        for file in files:
            file_name = file.split('.')[-2]
            f.write("./{}/{}.jpg\n".format(IMAGES_DIR, file_name))

def main() -> None:
    for root, dirs, files in os.walk(LABELS_DIR):
        try:
            files.remove("classes.txt")
        except ValueError:
            pass
        files = np.array(files)
        np.random.shuffle(files)

        split_pos = round(files.size*TRAIN_SIZE)
        print(split_pos)

        train_files = files[:split_pos]
        val_files = files[split_pos:]

        print(train_files)
        print(val_files)
        print(train_files.size + val_files.size)

        write_set(train_files, "train")
        write_set(val_files, "val")

if __name__ == "__main__":
    main()
