# Pearson ActiveLearn Downloader
Downloads `.jpg` images of the pages of your registered ebook on [Pearson ActiveLearn](https://www.pearsonactivelearn.com/app/home).  
I have created this for the sole moral that it is right for the owner of the book to have an unlimited and local version of the textbook, given that you paid for your book and is the legal owner.

## Author's notes
- This repository doesn't condone piracy, commercial use, copying or printing of copyrighted material, as this should be used for only personal use.
- **Only has been tested only on IGCSE and IAL books.**

Code is provided under the [**MIT License**](https://github.com/pepershukov/Pearson-ActiveLearn?tab=MIT-1-ov-file#MIT-1-ov-file).

## Requirements
- Active license to the ebook
- Chrome browser

## Usage
### Config file
`.env` file with variables can be used to automate the login process, and also include the path to the directory where the images will be stored.  
The file is optional, and the program will ask for that information if it wasn't provided.  

**`.env` has to be in the same directory as the executable.**  

**Example of `.env`**
```bash
SAVE_DIR=/absolute/path
USERNAME=user
PASSWORD=pass
```

### Running
- After logging in, you choose and load the ebook you want to download.
- When you load the book, wait for it to load fully the first page, and then press Enter in the console.