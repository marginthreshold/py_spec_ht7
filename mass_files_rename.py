from pathlib import Path


def rename(wanted_name, count_nums, extension_old, extension_new, diapazon):
    directory = Path(".")
    files = list(directory.glob(f"*{extension_old}"))

    for indx, file_path in enumerate(files, start=1):
        base_name = file_path.stem
        original_name = base_name[diapazon[0]:diapazon[1]]
        new_name = original_name + wanted_name + str(indx).zfill(count_nums) + extension_new
        new_path = file_path.with_name(new_name)
        file_path.rename(new_path)


# Пример использования
rename(wanted_name="video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 9])
