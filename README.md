<div align="center">
  <p align="center">
    <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/Go4Real34/TrafficSense/total?style=flat&logo=GitHub&label=Downloads" style="margin-right: 5px;">
    <img alt="GitHub last commit (by committer)" src="https://img.shields.io/github/last-commit/Go4Real34/TrafficSense?display_timestamp=committer" style="margin-right: 5px;">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Go4Real34/TrafficSense" style="margin-right: 5px;">
    <img alt="GitHub" src="https://img.shields.io/github/license/Go4Real34/TrafficSense">
  </p>
</div>

# TrafficSense
**_Traffic Sign Recognition with CNN (Convolutional Neural Network) Machine Learning \
by Görkem Sarıkaya for Computer Engineering II, Engineering Project II Course,
2nd Year Project at Beykoz University._**

# Needed Installations for Windows 11
- **Python Version:** [3.11.3 for Windows 11](https://www.python.org/downloads/release/python-3113/).


* If any NVIDIA CUDA supported GPU(s) exist on your system and want to use it for training;
  - **NVIDIA GPU Driver Version:** [450.80.02 or higher for Windows 11](https://www.nvidia.com/download/index.aspx?lang=en-us).
  - **NVIDIA CUDA Toolkit Version:** [11.8.0 for Windows 11](https://developer.nvidia.com/cuda-toolkit-archive).
  - **WinRAR Version:** [6.2.2 for Windows 11](https://www.win-rar.com/download.html?&L=0).
  - **cuDNN SDK Version:** [8.6.0 for Windows 11](https://developer.nvidia.com/cudnn). 
  - **Zlib Version:** [1.2.3 for Windows 11](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-zlib-windows)


# Installations
# Installations
  ## Python Installation for Windows 11
  - Download the Python with `version '3.11.3'`.
  - Run the downloaded file.
  - Follow the instructions on the installation screen and complete installation.
    - Adding Python Path to the environment variables in the installation may be needed.
    - Not tested but can result in some errors especially for background processes and callbacks.

  ## CUDA Installation
  - Download the CUDA Toolkit with `version '11.8.0'`.
  - Run the downloaded file.
  - Follow the instructions on the installation screen and complete installation.
  
  ## Graphic Card Driver Installation
  - Download the Graphic Card Driver of your GPU with the last version.
  - Run the downloaded file.
  - Follow the instructions on the installation screen and complete installation.
    - **Note:** While installing it, your screen can go black for a few seconds. Do not panic, it is normal and 
      will be gone after 5-10 seconds depending on your computer's speed.
  
  ## WinRAR Installation for Windows 11
  - Download the WinRAR with `version '6.22'`.
  - Run the downloaded file.
  - Follow the instructions on the installation screen and complete installation.

  ## cuDNN Installation
  - Download the cuDNN SDK with `version '8.6.0'`.
  - Extract the ZIP file with using WinRAR.
    - Install WinRAR using the steps above if you did not.
    - After installing;
      - Right-click to the file.
      - Hover over `Show More Options`.
      - Hover over `WinRAR`.
      - Click to `Extract to "cudnn-windows-x86_64-8.6.0.163_cuda11-archive\"`.
      - You have successfully extracted the file.
  - After extracting the files to the folder;
    - Navigate into the folder you extract them to and `cudnn-windows-x86_64-8.6.0.163_cuda11-archive` folder inside it.
    - Copy the files you see (`bin`, `include`, `lib` and `LICENSE`).
  - Navigate to the NVIDIA CUDA Toolkit installation folder: `C:\Program Files\NVIDIA GPU Computing Toolkit`.
    - Navigate into the `CUDA` and `v11.8` folders.
      - Paste the files here and;
        - If any `Do you want to merge these folders?` question appears, select `Yes`,
        - If any `Do you want to overwrite or keep both files?` question appears, select `Overwrite` option.
  
  ## Zlib Installation
  - Download the Zlib with `version '1.2.3'` or go to the location.
  - Extract the ZIP file with using WinRAR.
    - Install WinRAR using the steps above if you did not.
    - After installing;
      - Right-click to the file.
      - Hover over `Show More Options`.
      - Hover over `WinRAR`.
      - Click to `Extract to "zlib123dllx64\"`.
      - You have successfully extracted the file.
  - After extracting the files to the folder;
    - Copy the folder you extract them to.
  - Navigate to the NVIDIA CUDA Toolkit installation folder: `C:\Program Files\NVIDIA GPU Computing Toolkit`.
    - Navigate into the `CUDA` and `v11.8` folders.
      You should not be getting any merge or overwrite questions but if you got, select same options as you did above.
  

- After doing installation operations;
  - Open your Windows Search Bar and type `Environment Variables`.
  - Click on the `Environment Variables` button that is bottom right of the opened window.
  - In System Variables tab (bottom one),
    - Check `CUDA_PATH` and `CUDA_PATH_V11_8` entries exists and having the `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8` path as value.
      - If they are exists and having the correct path as value, you can continue to the next step.
      - If they are not exists or having some other path as value, there is something wrong with the CUDA installation.
    - Find `Path` entry and open its properties by selecting it and clicking `Edit` or double-clicking on it.
      - Check that Python paths are there successfully. You should confirm that the following two entries exists in the following order;
        - `C:\{path_to_python}\Python311\Scripts`
        - `C:\{path_to_python}\Python311`
      - Find every entry that includes `NVIDIA` in it and delete them and add them in the following order;
        - `C:\Program Files\NVIDIA Corporation\Nsight Compute 2022.3.0`
        - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin`
        - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp`
        - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\include`
        - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\lib\x64`
        - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\extras\CUPTI\include`
        - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\extras\CUPTI\lib64`
        - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\zlib123dllx64\dll_x64`
    - After adding them, hit Enter on your keyboard and click 'OK' to every window you opened to close them.
  - After closing all windows, restart your computers for all these things to take effect.
  - After your computer opened again;
    - Open a command prompt (cmd).
    - Type `python --version`.
      - If you see the version number on the console output, that means you have successfully installed Python.
    - Type `nvcc --version`.
      - If you see the version number on the console output, that means you have successfully installed CUDA & cuDNN.
    - Type `where zlibwapi.dll`
      - If you see the absolute path of the DLL file, that means you have successfully installed Zlib.


  - If you couldn't get right console output for any of them, try revert your changes back (delete files, uninstall, remove 
    variables from `Path`) and do the steps again or follow the instruction on the official websites of 
    [Python](https://www.python.org/downloads/), [Tensorflow](https://www.tensorflow.org/install/pip) and 
    [NVIDIA](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-windows).

> Since the project is done in Windows 11, I don't specifically know how to install Python, CUDA, cuDNN & Zlib for the older version 
  of Windows, Linux, macOS or other operating systems. I did my best to make it easy for you to install it at least for 
  Windows 11.\
> If you have any problems with the installation, just to be sure, check official website for problems.\
> Thank you for your understanding again.


# Preparation, Usage & Deletion
- Install Python & NVIDIA CUDA Supported GPU Support if you have any NVIDIA GPU with the steps above if you don't have it or haven't done the steps.


- Download the project from `Code -> Download ZIP` and extract files or clone it in command the prompt.\
  ```git clone https://github.com/Go4Real34/TrafficSense.git```


- If you are using an IDE;
  - Create a virtual environment using your IDE.

  - Then, activate it and install the required packages with the following command via console or go and find them in your 
    IDE tabs if any exists.\
    ```.\venv\Scripts\activate```\
    ```pip install -r requirements.txt```
  
  - Finally, you can run the file using your IDE;
    - `TrafficSense.py`, to start the program and navigate through the menu.


- If you are using command prompt;
  - Go to the location of the project.\
  ```cd TrafficSense```
  
  - Run the following commands to create a virtual environment and activate it;
    - Create a virtual environment.\
      ```python -m venv venv```
    
    - Activate the virtual environment.\
      ```.\venv\Scripts\activate```
  
  - After activating it, you should see a `(venv)` text at the start of the command line or if you changed its name
    (2nd 'venv' in command above), you should see that name.
  
  - Then, install the required packages with the following command via console.\
    ```pip install -r requirements.txt```
  
  - Finally, run the following commands;
    - ```python TrafficSense.py``` to start the program and navigate through the menu.

And you should be good to go.

- After your work is done with the project you can directly close the command prompt or; if you want to delete something, 
  right-clicking on it and deleting will be enough for the process.


- But if you want to clean it from the console, do the following steps.
  - First, deactivate the virtual environment.\
  ```deactivate```
  
  - Then, decide what you are going to delete.
    - If you are going to delete the virtual environment only for some problem use the following command.\
      ```rmdir /s /q venv``` (for 'venv', put your virtual environment's name if you have changed it.)
    
    - But if you want to completely get rid of the project itself, you can go back one directory and delete the project 
      folder completely by executing the following commands:
        - First go back one directory.\
          ```cd ..```
        
        - Then remove the project folder completely.\
          ```rmdir /s /q TrafficSense```


# Quick Explanation About How The Tools Work
## **_Start_**
  - Firstly, you can select what mode you want to use.

## **_Step Checking Tools_**
  - In step checking mode, you can check if these tool are working properly or not.
  - For the project, we need 5 critical tools to work. They are;
    - **detect_camera:** Detects the camera and shows the camera capture to the screen. (If your camera is not captured correctly or,
      you want to another camera to be captured; try changing the camera index in the code from 0 to 1, 2, 3... until you found the camera you want to capture.)
    - **process_images:** Processes camera capture with 3 different methods (graying, equalizing and normalizing) and shows them to the screen.
      By pressing 1, 2, 3 or 4 on your keyboard (not numpad keys), you can navigate between different processed images of your camera capture.
    - **read_dataset_csv_file:** Reads the dataset CSV file and prints the data to the console with 2 different methods (as pandas object and as an array list).
    - **read_dataset_folders:** Reads the dataset folders and prints the information about the dataset.
    - **create_graphs:** Reads both dataset CSV file and folders, separates dataset to 3 different groups (train, validate and test), 
      counts the images in each folder and creates 2 different graphs. One graph is created by combining traffic sign names from CSV file and 
      5 example of traffic signs from each group, another graph is created by combining traffic sign class IDs by counting from 0 to 42 (43 classes) and 
      traffic sign image count for training for each group.

## **_Model Training_**
- In model training, you can train the model with the dataset & labels and save it to the `ProjectFiles/DatasetFiles` folder.
  - In this part, the dataset and label file are read and seperated into 3 different groups named train, validation and test, 
    which will be used for the following parts. Then, the dataset is checked for the compatibility for any issues. If it passes, 
    some examples for each group will be shown as a graph. After closing this window, a graph will be shown that shows the distribution 
    of the dataset for each class. After closing this window, the images will be processed to a version that computer can understand 
    while training. After the processing is complete, one of the images that selected randomly will be shown to screen. After closing this window, 
    a depth of 1 will be added to images, and they become ready for augmentation. In augmentation, all the images will be randomly 
    shifted to left, right, up and down, zoomed in and out, sheared and rotated. After augmentation one batch example of images will be shown 
    to screen and after closing this window, the class IDs will be categorized. After the categorization, model will be created and compiled for training. 
    After compiling; if you have any NVIDIA GPU and, it is suitable for training, you will select one GPU; if you have not, it will automatically 
    select your CPU and training starts. You will be seeing your training progress as `epochs`. After all of them done, two graphs will be shown 
    to the screen where one of them is being the graph of accuracy of the model and other is being the graph of loss of the model. After closing these windows, 
    model will be scored and score will be printed on console. Finally, both model and training type will be saved and save paths will be printed to console.

## **Application Testing_**
- In application testing, the trained model is used to analyze traffic signs and show the results on the screen.
  - In this part, your selected camera frames are captured and processed to a version that computer can understand. Meanwhile;
    - If `Begin Analyzing` button is clicked, analysis become activated. Trained model is used for analyzing the images and if one of the predictions that contains a higher number than 
    the `detection threshold`, that means a traffic sign detected. So, the corresponding information about traffic sign is acquired and this information 
    put to the screen.
    - If the `Stop Analyzing` button is clicked, analysis is deactivated. Just the captured screen is shown to the screen along with the `detection deactivated` text.
    - If the `Take Photo` button is clicked, the current information put to a different image in the background simultaneously and the image is saved to 
    `Photos` folder so that user can access it later.
    - If the `Clear Photos` button is clicked, all the photos in the `Photos` folder will be deleted and results tab will be cleared.
    - If the `Clear Results Tab` button is clicked, only the results tab will be cleared.
    - If the `Close` button or the `X` button on the top right corner of the window is clicked, the user will be asked about being sure and if `Yes` is 
      clicked, the application will be closed.


# Project Media

# Full Menu
![Full Menu](Resources/images(.png)/full_menu.png)

## Menu, Show Current Check Status and Exit Console Outputs of "check_steps.py"
![check_steps.py Menu, Show Current Check Status and Exit Console Outputs](Resources/images(.png)/check_steps_menu_show_current_check_status_and_exit_console_output.png)

## Console Output of "detect_camera.py" and "process_images.py"
![detect_camera.py and process_images.py Console Outputs](Resources/images(.png)/detect_camera_and_process_images_console_outputs.png)

## Camera Screens of "detect_camera.py" and "process_images.py"
![detect_camera.py and process_images.py Camera Screens](Resources/images(.png)/detect_camera_and_process_images_camera_screens.png)

## Console Output of "read_dataset_csv_file.py"
![read_dataset_csv_file.py Console Output](Resources/images(.png)/read_dataset_csv_file_console_output.png)

## Console Outputs of "read_dataset_folders.py" and "create_graphs.py"
![read_dataset_folders.py and create_graphs.py Console Outputs](Resources/images(.png)/read_dataset_folders_and_create_graphs_console_outputs.png)

## Figures of "create_graphs.py" 
### Traffic Signs with Names
![create_graphs.py Graph of Traffic Signs with Names](Resources/images(.png)/create_graphs_figure_1_traffic_signs_with_names.png)
### Traffic Signs with Image Counts
![create_graphs.py Graph of Traffic Signs with Count](Resources/images(.png)/create_graphs_figure_2_traffic_signs_with_counts.png)

# Dataset Compatibility Checks
![Dataset Compatability Checks](Resources/images(.png)/dataset_compatability_checks.png)

## Example of a Processed Image
![Example of a Processed Image](Resources/images(.png)/example_of_a_processed_image.png)

## Example of a Batch of Augmented Images
![Example of a Batch of Augmented Images](Resources/images(.png)/example_of_a_batch_of_augmented_images.png)

# Model Summary
![Model Summary](Resources/images(.png)/model_summary.png)

# Supported NVIDIA GPU Not Detected Information
![Supported NVIDIA GPU Not Detected Information](Resources/images(.png)/supported_nvidia_gpu_not_detected_information.png)

# Supported NVIDIA GPU Detected Information
![Supported NVIDIA GPU Detected Information](Resources/images(.png)/supported_nvidia_gpu_detected_information.png)

# CPU Trained Model Results
  ## CPU Training Epoch Statuses
  ![CPU Training Epoch Statuses](Resources/images(.png)/cpu_training_epoch_statuses.png)

  ## CPU Trained Model Accuracy and Loss Graphs
  ![CPU Trained Model Accuracy and Loss Graphs](Resources/images(.png)/cpu_trained_model_accuracy_and_loss_graphs.png)

  ## CPU Trained Model Test Score
  ![CPU Trained Model Test Score](Resources/images(.png)/cpu_trained_model_test_score.png)

# GPU Trained Model Results
  ## GPU Training Epoch Statuses
  ![GPU Training Epoch Statuses](Resources/images(.png)/gpu_training_epoch_statuses.png)

  ## GPU Trained Model Accuracy and Loss Graphs
  ![GPU Trained Model Accuracy and Loss Graphs](Resources/images(.png)/gpu_trained_model_accuracy_and_loss_graphs.png)

  ## GPU Trained Model Test Score
  ![GPU Trained Model Test Score](Resources/images(.png)/gpu_trained_model_test_score.png)

# Camera Detection Check before Analysis
![Camera Detection Check before Analysis](Resources/images(.png)/camera_detection_check_before_analysis.png)

# All Command Completed Texts
![All Command Completed Texts](Resources/images(.png)/all_command_completed_texts.png)

# Detection Deactivated UI
![Detection Deactivated UI](Resources/images(.png)/detection_deactivated_ui.png)

# Detection Activated but Traffic Sign Not Detected UI
![Detection Activated but Traffic Sign Not Detected UI](Resources/images(.png)/detection_activated_but_traffic_sign_not_detected_ui.png)

# Detection Activated and Traffic Sign Detected UI
![Detection Activated and Traffic Sign Detected UI](Resources/images(.png)/detection_activated_and_traffic_sign_detected_ui.png)


# Known Issues
- This section will be updated whenever a bug is discovered or fixed.

### **_Training_**
> 1. If you have a supported NVIDIA GPU but not want to use it for training, you cannot select CPU and forced to do it with GPU.


# License
 - The project is licensed under MIT License. If you want to use it, please check the [LICENSE](LICENSE.txt) file. 
 - Referencing to the project & author (as "Görkem 'Go4Real34' Sarıkaya") is enough for any reason.


### Feel free to use the project, make suggestions if you have any or report bugs maybe with their fixes if you found any.

# Thank you for using my TrafficSense Tool.