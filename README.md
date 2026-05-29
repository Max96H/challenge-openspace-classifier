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
│   ├── late_arrivals.py
│   ├── openspace.py
│   ├── preferances.py
│   ├── questions.py
│   └── table.py
├── .gitignore
├── config.json
├── main.py
├── new_colleagues+.txt
├── output.txt
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

```
   python main.py
```

3. The script reads your input file, and organizes your colleagues to random seat assignments. It takes into accound demands to seat with a specific person. It also alerts you if the room is full an ask your permission to add a table.

```
    Openspace is full! Do you want to add a table? (y/n) :
```

4. It will then check for late arrivals wich are to be input manually and subsequently assign them a seat.

```
    Did more people arrive late? (y/n) : y
    How many people needs a seats ? 10
    Name 1 : 
```

5. The resulting seating plan is displayed in your console and also saved to an "output.txt" file in your root directory.

6. It finally offers to answer a few questions you could have.

```
    If you want the answer to any of these questions, type their number :
    1 How many seats are in the room?
    2 How many people are in the room?
    3 How many empty seats are left?
    4 No more questions, thank you
    -->
```


```python
    def main():
        """
        Main function of this project
        """
        #Reads and takes in names from a text file
        input_filepath = "new_colleagues+.txt"
        names = make_list_from_txt(input_filepath)

        #Makes a 'whish list' in the form of a dictionnary
        wish_dict = make_relation_dict(names)

        output_filename = "output.txt"

        #Reads a json file containing the different configurations of openspaces
        with open("config.json") as jsfile:
            json_object = json.load(jsfile)

        #Offers a choice of configuration
        choice = input("Pick the size of your openspace between 'small', 'medium' and 'large' : ")
        config = json_object[choice]

        #Make use of an openspace
        open_space = Openspace(config["tables"], config["seats_per_table"])

        #Organize the people(names) in the openspace by assigning one person per seat and randomly filling the tables
        open_space.organize(names, wish_dict)

        #Write in an output text file the names of the people who found a seat in the openspace
        open_space.store(output_filename)

        #Prints out the state of the openspace, one table at a time
        open_space.display()

        #Check for late arrivals and eventually adds them
        checking_late_arrivals(open_space, output_filename)    

        #Answer some questions
        answering_qestions(open_space)

    if __name__ == "__main__":
        main()
```
## ⏱️ Timeline

This project took two days for completion.
29/05/2026

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/max-h-540881409/).

