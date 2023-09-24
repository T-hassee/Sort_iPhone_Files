from pathlib import Path


users_directory = input("Введите путь к папке: ")
path_directory = Path(fr"{users_directory}")

only_photo_folder = Path(path_directory.parent) / "photo"
only_photo_folder.mkdir(exist_ok=True)

only_video_folder = Path(path_directory.parent) / "video"
only_video_folder.mkdir(exist_ok=True)


for file in path_directory.glob("**/*.*"):
     if file.suffix in [".JPG", ".HEIC", ".JPEG", ".PNG"]:
        file.replace(only_photo_folder / file.name)

     elif file.suffix in [".MOV", ".MP4"]:
         file.replace(only_video_folder / file.name)
print(f"Ваши фото и видео перенесены в папки для Фото - {only_photo_folder} и Видео - {only_video_folder} ")
