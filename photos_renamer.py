import os
import datetime

directory = os.path.dirname(os.path.abspath(__file__))
extensions = ['.jpg', '.jpeg', '.png']
filelist = os.listdir(directory)
newfilesDictionary = {}
count = 0

for file in filelist:
    filename, extension = os.path.splitext(file)
    if extension in extensions:
        create_time = os.path.getmtime(os.path.join(directory, file))
        format_time = datetime.datetime.fromtimestamp(create_time)
        format_time_string = format_time.strftime("%Y-%m-%d_%H-%M-%S")
        newfile = format_time_string + '_' + str(count) + extension
        os.rename(os.path.join(directory, file), os.path.join(directory, newfile))
        count += 1

print(f"All done. {count} files are renamed.")
