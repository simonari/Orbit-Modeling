import os


def create_folder(image_resolution, cycle_number):
    folder = os.getcwd()
    folder = os.path.join(folder, f"../data",
                          f"{image_resolution[0]}x{image_resolution[1]}",
                          f"{cycle_number}")

    if not os.path.exists(folder):
        os.makedirs(folder)

    return folder
