# Change Log
All notable changes to this project will be documented in this file.\
The version format given as following.

> # [vX.Y.Z.W] - YYYY-MM-DD
> ### **_Additions_**
> - Any new features about the project.
> ### **_Changes_**
> - Any changes about project.
> ### **_Fixes_**
> - Any bug fixes about the project.
> ### **_Deletions_**
> - Any deleted features about the project.
>
> ## **_Version Increment & Time Format_**
> #### - X: Major Change.
> #### - Y: New Feature.
> #### - Z: Bug Fix.
> #### - W: No Change in the Project
> #### - YYYY-MM-DD: Date of release (Year - Month - Day)

# **_Latest Version: [v1.0.0.0] - 2023-07-07_**

<br>

# **_Change Log History_**

# [v1.0.0.0] - 2023-07-07
- First release of the project.
- Includes the necessary checking tools for the project to determine whether the project is ready to be used or not.

### **_Additions_**
- **_Project Files_**
  - **_check_steps.py:_**
    - Main start point of the project. Handles the input, shows the menu on the console, calls the 
    corresponding functions to check status of the necessary steps depending on the user's input.
  
  - **_detect_camera.py:_**
    - Includes function to both detect and capture the camera. This function also shows the captured 
      camera screen to a window.
  
  - **_process_images.py_**
    - Includes same processes in `detect_camera.py`. Also, includes functions that processes images 
      with different methods (graying, equalizing and normalizing) which also can be shown to the screen.
  
  - **_read_dataset_csv_file.py_**
    - Includes functions that reads CSV file, prints the data as pandas object and as an array list.
  
  - **_read_dataset_folders.py_**
    - Includes folder reading operations and counters for the images. Also, prints the information 
      about the count of the images in the folders.
  
  - **_create_graphs_**
    - Includes same processes in `read_dataset_folders.py` and `read_dataset_folder.py`. Also, function 
      creates graphs using the data inside these processes.

  - **_'DatasetFiles' Compressed '.rar' File_**
    - Includes the dataset files (dataset images and label file) used in this project.


- **_Documentations_**
  - **_README.md_**
    - This file will be used to give information about the project and also includes quick explanations 
      about installation and run.
  
  - **_CHANGELOG.md_**
    - This file will be used to keep track of changes. Currently, includes **_[v1.0.0.0]_** version changes.
  
  - **_LICENSE.txt_**
    - This project is licenced with MIT License. The project is free to use everyone. When used, 
      referencing the project & author (as "Görkem 'Go4Real34' Sarıkaya") is enough for any reason.
  
  - **_.gitignore_**
    - This file includes the excluded folders and files from the project. It is used to prevent
    unnecessary files to be uploaded to the repository. Currently includes multiple folders (6).


- **_Resources_**
  - **_'images(.png)' Folder_**
    - Added images (7) that are used in the [README.md](README.md) file in the `Project Media` section.

### **_Changes_**
- No changes were made.

### **_Fixes_**
 - No fixes were made.

### **_Deletions_**
- No deletions were made.