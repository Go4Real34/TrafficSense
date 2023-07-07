# TrafficSense
**_Traffic Sign Recognition with CNN (Convolutional Neural Network) Machine Learning \
by Görkem Sarıkaya for Computer Engineering II, Engineering Project II Course,
2nd Year Project at Beykoz University._**

# Needed Installations for Windows 11
- **Python Version:** [3.11.3 for Windows 11](https://www.python.org/downloads/release/python-3113/).


# Installations
  ## Python Installation for Windows 11
  - Download the Python with `version '3.11.3'`.
  - Run the downloaded file.
  - Follow the instructions on the installation screen and complete installation.
    - Adding Python Path to the environment variables in the installation may be needed.
    - Not tested but can result in some errors especially for background processes and callbacks.


- After doing all installation operations;
  - Open your Windows Search Bar and type `Environment Variables`.
  - Click on the `Environment Variables` button that is bottom right of the opened window. 
  - For both User & System Variables tabs, find `Path` entry and open it by double-clicking on it or selecting it and clicking `Edit`.
  - Check that Python paths are there successfully. You should confirm that the following two entries exists in the following order;
    - `C:\{path_to_python}\Python311\Scripts`
    - `C:\{path_to_python}\Python311`
  - After closing all windows, restart your computers for all these things to take effect.
  - After your computer opened again;
    - Open a command prompt (cmd).
    - Type `python --version`.
      - If you see the version number on the console output, that means you have successfully installed Python.
    - If you couldn't get right console output for it, try revert your changes back (uninstall, remove variables from `Path`) 
      and do the steps again or follow the instruction on the official websites of [Python](https://www.python.org/downloads/).

> Since the project is done in Windows 11, I don't specifically know how to install both FFMPEG & Python for the older version 
  of Windows, Linux, macOS or other operating systems. I did my best to make it easy for you to install them at least for 
  Windows 11.\
> If you still have any problems with the installation, as I said, definitely check official websites for solutions.\
> Thank you for your understanding.



# Preparation, Usage & Deletion
- Install Python with the steps above if you don't have it or haven't done the steps.


- Download the project from `Code -> Download ZIP` and extract files or clone it in command the prompt.\
  ```git clone https://github.com/Go4Real34/TrafficSense.git```


- If you are using an IDE;
  - Create a virtual environment using your IDE.

  - Then, activate it and install the required packages with the following command via console or go and find them in your 
    IDE tabs if any exists.\
    ```.\venv\Scripts\activate```\
    ```pip install -r requirements.txt```
  
  - Finally, you can run the file `ProjectFiles/StepPreparations/check_steps.py` to check if they necessary functionalities for the project are working or not.`


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
  
  - Finally, run the following command to check if necessary functionalities for the project are working or not.\
  ```python ProjectFiles/StepPreparations/check_steps.py```

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
- In this version, these tools are not connected to each other but each of them consist of a critical part of the project.
- Just for this version, they are work just for checking if the necessary functionalities are working or not.
- For now, you just select the tool you want to use from the menu and check if it is working or not.


# Project Media

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


# Known Issues
- This section will be updated whenever a bug is discovered or fixed.

> There is no known issue encountered for now.


# License
 - The project is licensed under MIT License. If you want to use it, please check the [LICENSE](LICENSE.txt) file. 
 - Referencing to the project & author (as "Görkem 'Go4Real34' Sarıkaya") is enough for any reason.


### Feel free to use the project, make suggestions if you have any or report bugs maybe with their fixes if you found any.

# Thank you for using my TrafficSense Tool.