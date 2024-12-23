import os
import shutil

src_dir = "C:/Users/hdhiman/Downloads" #folder where sorting of files will happrn

# defining the folders for every extension type
extension_map = {
    'pdf': 'PDF',
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'txt': 'Text',
    'mp3': 'Audio',
    'docx': 'Documents',
    'xlsx': 'Spreadsheets',
    'pptx': 'Presentations',
    'csv': 'Spreadsheets',
    'zip': 'Archives',
    'rar': 'Archives',
    'html': 'Web Files',
    'css': 'Web Files',
    'js': 'Web Files',
    'exe' : 'Setup Files',
    'apk' : 'Applications'
}

# Function to organize files based on the extension list
def organization():
  for filename in os.listdir(src_dir):  # os.listdir returns a list of names of all files and directories in that directory.
    file_path = os.path.join(src_dir,filename)

    #Skip directories (we only want to process files)
    if os.path.isdir(file_path):  #os.path.isdir checking if the file path formed is matching with existing path. isdir returns true or false checking with dir.
        continue

    # Get the file extension (e.g., 'pdf', 'jpg', 'txt')
    file_extension = filename.split('.')[-1].lower() #spliting the extension from filename

    #putting file into folder
    if file_extension in extension_map:
            # Get the folder name for the current extension
            folder_name = extension_map[file_extension]

            #create the folder if it is not existed
            ext_folder = os.path.join(src_dir,folder_name)
            if not os.path.exists(ext_folder):
             os.makedirs(ext_folder)

            # Move the file into the corresponding folder
            shutil.move(file_path, os.path.join(ext_folder, filename)) # original shuti.move(src,dest)
            print(f"Moved: {filename} -> {folder_name} folder")

    else:
            print(f"Skipping: {filename} (unsupported file type)")


organization()
