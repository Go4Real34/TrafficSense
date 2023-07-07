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

# **_Latest Version: [v1.3.0.1] - 2023-07-07_**

<br>

# **_Change Log History_**

# [v1.3.0.1] - 2023-07-07
- Updated README.md file.

### **_Additions_**
- No additions were made.

### **_Changes_**
- **_Documentations_**
  - **_README.md_**
    - Added necessary 'shields.io' badges (4) about the project.

  - **_CHANGELOG.md_**
    - Added new changes about **_[v1.3.0.1]_**.

### **_Fixes_**
 - No fixes were made.

### **_Deletions_**
- No deletions were made.

<br>

# [v1.3.0.0] - 2023-07-07
- Created test application for the model and added an option to test in the menu.

### **_Additions_**
- **_Project Files_**
  - **_test_model.py_**
    - Main start point of the testing application. Functions are called to get images, do analysis and set the 
      results to the screen.
  
  - **_test_step_functions.py_**
    - Includes all steps of the model testing. Each function definition is representing one step.
  
  - **_test_settings.py_**
    - Includes settings for the testing. These settings can be changed by the user but be aware that changing 
      these settings may cause problems.
  
  - **_test_extra_functions.py_**
    - Includes other necessary functions that is called multiple times to used by main functions to prevent code repetition.
  
  - **_background_functions.py_**
    - Includes functions that is called by 'tkinter' window asynchronously.


- **_Resources_**
  - **_'images(.png)' Folder_**
      - Added images (5) that are used in the [README.md](README.md) file in the `Project Media` section.

### **_Changes_**
- **_Project Files_**
  - **_TrafficSense.py_**
    - Added new option to the menu to execute application testing.


- **_Documentation_**
  - **_README.md_**
    - Added more explanations to `Quick Explanation About How The Tools Work` and `Project Media` section.
  
  - **_CHANGELOG.md_**
    - Added new changes about **_[v1.3.0.0]_**.

  - **_.gitignore_**
    - Added multiple folders (2) to ignore. 


- **_Resources_**
  - **_'images(.png)' Folder_**
    - `full_menu.png` is updated according to the new menu on the console.

### **_Fixes_**
 - No fixes were made.

### **_Deletions_**
- No deletions were made.

<br>

# [v1.2.0.0] - 2023-07-07
- Created menu for the project to navigate between functionalities.

### **_Additions_**
- **_Project Files_**
  - **_TrafficSense.py_**
    - Main start point of the menu version of project. Handles the input, shows the menu on the console and calls the corresponding 
      feature depending on the entered input.


- **_Resources_**
  - **_'images(.png) Folder_**
    - Added an image (1) that is used in the [README.md](README.md) file in the `Project Media` section.

### **_Changes_**
- **_Documentation_**
  - **_README.md_**
    - Added more explanations to `Preparation, Usage & Deletion` and `Quick Explanation About How The Tools Work` sections.
  
  - **_CHANGELOG.md_**
    - Added new changes about **_[v1.2.0.0]_**.


- **_Documentation_**
  - **_.gitignore_**
    - Added a folder (1) to ignore.

### **_Fixes_**
 - No fixes were made.

### **_Deletions_**
- No deletions were made.


# [v1.1.0.0] - 2023-07-07
- Added training phase with CPU & GPU using Tensorflow & Keras.

### **_Additions_**
- **_Project Files_**
  - **_train_model.py_**
    - Main start point of the training. Uses all the other functions to train the model step by step.
  
  - **_training_step_functions.py_**
    - Includes all steps of the model training. Each function definition is representing one step.

  - **_training_settings.py_**
    - Includes settings for the training. These settings can be changed by the user but be aware that changing 
      these settings may cause problems. 

  - **_training_extra_functions.py_**
    - Includes other necessary functions that is called multiple times to used by main functions to prevent code repetition.


- **_Resources_**
  - **_'images(.png)' Folder_**
    - Added images (12) that are used in the [README.md](README.md) file in the `Project Media` section.

### **_Changes_**
- **_Project Files_**
  **_'DatasetFiles' Compressed '.rar' File_**
    - Now, includes pre-trained CPU & GPU models.


- **_Documentations_**
  - **_README.md_**
    - Added more explanations to `Needed Installation for Windows 11`, `Preparation, Usage & Deletion`, 
    `Quick Explanation About How the Tool Works` and `Project Media` sections.
  
  - **_CHANGELOG.md_**
    - Added new changes about **_[v1.1.0.0]_**.

  - **_requirements.txt_**
    - Added new packages that are needed for the training phase.

  - **_.gitignore_**
    - Added multiple folders (2) to ignore.

### **_Fixes_**
 - No fixes were made.

### **_Deletions_**
- No deletions were made.

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