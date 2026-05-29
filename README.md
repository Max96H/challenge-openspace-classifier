# challenge-openspace-classifier
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

Your company moved to a new office at CEVI Ghent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.

![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)

## 📦 Repo structure

```
.
├── utils/
│   ├── file_utils.py
│   ├── openspace.py
│   └── table.py
├── .gitignore
├── main.py
├── new_colleagues.txt
├── output.txt
└── README.md
```

### For more features -> Go check the branch "Nice-to-have-ft"


## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

```
   python main.py
```

3. The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.txt" file in your root directory. 

```python
def main():
    """
    Main function of this project
    -Reads and takes in names from a text file 
    -Make use of an openspace
    -Organize the people(names) in the openspace by assigning one person per seat and randomly filling the tables
    -Write in an output text file the names of the people who found a seat in the openspace
    -Prints out the state of the openspace, one table at a time
    """
    input_filepath = "new_colleagues.txt"
    output_filename = "output.txt"

    names = make_list_from_txt(input_filepath)

    open_space = Openspace()

    open_space.organize(names)

    open_space.store(output_filename)

    open_space.display()

if __name__ == "__main__":
    main()
```
## ⏱️ Timeline

This project took one day for completion.

28/05/2026

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/max-h-540881409/).

