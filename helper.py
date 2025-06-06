import os

def get_image_list(folder_path):
    try:
        return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    except Exception as e:
        print(f"Error: {e}")
        return []


# img_dir = r"microservices\components\images"
# files = get_image_list(img_dir)
# print(files[0].split('-')[1].split('.')[0])