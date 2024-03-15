# photos_renamer

# Table of Contents

1. [Introduction](#1-introduction)
2. [Installation](#2-installation)
3. [Usage](#3-usage)
4. [What It Does](#4-what-it-does)
5. [Contribution](#5-contribution)
6. [License](#6-license)

---

## 1. Introduction

This program is designed to rename image files in a specified directory based on their creation timestamps. It utilises Python and its `os` and `datetime` modules to achieve this functionality.

## 2. Installation

There's no formal installation process for this program. You can simply download the script and run it using Python 3. Ensure that you have Python installed on your system.

## 3. Usage

1. **Clone the Repository**: Download the script or clone the repository to your local machine.

2. **Navigate to the Directory**: Using the command line or terminal, navigate to the directory where the script is located.

3. **Run the Script**: Execute the script by running the following command:
    ```bash
    python rename_images.py
    ```

4. **Check Renamed Files**: Once the script completes execution, check the specified directory. The image files should now be renamed based on their creation timestamps.

## 4. What It Does

This program performs the following steps:

- It scans the specified directory for image files (with extensions `.jpg`, `.jpeg`, and `.png`).
- For each image file found, it retrieves the creation timestamp.
- It formats the timestamp into a readable string format (`YYYY-MM-DD_HH-MM-SS`).
- It renames the image file by appending the formatted timestamp to the original filename.
- The program keeps track of the count of renamed files.
- Upon completion, it prints a message indicating the total number of files renamed.

## 5. Contribution

Contributions to this project are welcome! If you have any ideas for improvements or encounter any issues, feel free to open an issue or create a pull request on the GitHub repository.

## 6. License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.
