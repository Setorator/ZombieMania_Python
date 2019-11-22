# Zombie Mania Python Edition

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The first thing you will need is an editior(duh). We recommend [PyCharm](https://www.jetbrains.com/pycharm/?fromMenu) the Community edition is free and suits our needs perfectly.

You will also need to set up an virtual environment and install some packages in this virtual enviroment. For details on how to do this see the Installing chapter. 

The packages required are currently
* PyGame

Please note that this list may change with further updates.


### Installing

A step by step series of examples that tell you how to get a development env running inside PyCharm. If you are using another IDE you are on your own.

1. Open PyCharm and create a new project with a virtual environment
![New_Proj](https://user-images.githubusercontent.com/18465126/66916419-750bc680-f01b-11e9-8b67-d695f13b38b6.PNG)

2. Right-click on the new project folder and select "New"->"Python Package" and name it "zombiemania" (remove the __init__.py file)

3. Click on VCS (Version Control System) in the menu bar and select "Check out from version control"->"Git"

4. Enter the projects URL and select the "zombiemania" project you created in step 2 as the target location and press clone.

```
https://github.com/Setorator/ZombieMania_Python.git
```

![clone](https://user-images.githubusercontent.com/18465126/66916426-763cf380-f01b-11e9-8e52-08d37dc7095d.png)


5. After the clone process is done you have all the code but you still need to install the rerequisite packages. Open settings ```Ctrl+Alt+S ```. Navigate to Project: zombiemania -> "Project Interpeter and click the "+" sign.
![settings](https://user-images.githubusercontent.com/18465126/66916423-75a45d00-f01b-11e9-88ba-224c21de8166.png)

6. Search for the package you want to install and press "Install Package"
![pygame](https://user-images.githubusercontent.com/18465126/66916421-75a45d00-f01b-11e9-98c7-255f369b887c.png)

Finally try to run the game from the file ``` src/game.py ``` and then get hacking and cracking!

## Built With

* [Pygame](https://www.pygame.org) - A cross-platform set of Python modules designed for writing video games
* [Tiled](https://www.mapeditor.org/) - A map editor for creating tiled maps in the TMX-format.
* [PyTMX](https://github.com/bitcraft/pytmx) - A library for reading TMX maps created in the Tiled map editor.
* [pyscroll](https://github.com/bitcraft/pyscroll) - A module for creating animated scrolling maps.

## Contributing

Please read [CONTRIBUTING.md](TODO) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Todo

## Authors

* **Kim Askling** - *Creator* - [Setorator](https://github.com/Setorator)
* **Linus Sjölinder** - *Initial Work* - [Sjoelinder](https://github.com/sjoelinder)
* **Alexander Andreasson** - *Something* - [TBD]()
* **Elias Fredin** - *Initial Work* - [Bravos123](https://github.com/Bravos123)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* No
