# CRUD Server

This project is a simple server that implements CRUD (Create, Read, Update,
Delete) operations to alter the `restaurantmenu` database. It utilizes `flask` to incorporate URL routing for different links in the app.

## Getting Started

My operating system is a Mac so the installation instructions reflect this system. The code editor used was Atom. Most of the files and configurations were provided by Udacity.

### Installing Git

Git is already installed on MacOS, but these instructions are to ensure we have the latest version:

1. go to [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. download the software for Mac
3. install Git choosing all the default options

Once everything is installed, you should be able to run `git` on the command line. If usage information is displayed, we're good to go!

### Configuring Mac's Terminal (OPTIONAL)

Git can be used without reconfiguring the terminal but doing so makes it easier to use.

To configure the terminal, perform the following:

1. download [udacity-terminal-config.zip](http://video.udacity-data.com.s3.amazonaws.com/topher/2017/March/58d31ce3_ud123-udacity-terminal-config/ud123-udacity-terminal-config.zip)
2. Move the `udacity-terminal-config` directory to the directory of your choice and name it `.udacity-terminal-config`(Note the dot in front)
3. Move the `bash-profile` to the same directory as in `step 2` and name it `.bash_profile`(Note the dot in front)
    * If you already have a `.bash_profile` file in your directory, transfer the content from the downloaded `bash_profile` to the existing `.bash_profile`

**Note:** It's considerably easier to just use
`mv bash_profile .bash_profile`
and `mv udacity-terminal-config .udacity-terminal-config`
when moving and renaming these files in order to avoid mac system errors

### First Time Git Configuration
Run each of the following lines on the command line to make sure everything is set up.
```
# sets up Git with your name
git config --global user.name "<Your-Full-Name>"

# sets up Git with your email
git config --global user.email "<your-email-address>"

# makes sure that Git output is colored
git config --global color.ui auto

# displays the original state in a conflict
git config --global merge.conflictstyle diff3

git config --list
```

### Git & Code Editor

The last step of configuration is to get Git working with your code editor. Below is the configuration for Atom. If you use a different editor, then do a quick search on Google for "associate X text editor with Git" (replace the X with the name of your code editor).
```
git config --global core.editor "atom --wait"
```

### Fetch the Source Code

#### Fork the starter repo
Log into your personal Github account, and fork the [crudserver](https://github.com/rtelles64/crudserver.git) so that you have a personal repo.

#### Clone the remote to your local machine
From the terminal, run the following command (be sure to replace <username> with your Github username):
`git clone http://github.com/<username>/crudserver crudserver`

This will give you a directory named `crudserver` that is a clone of your remote `crudserver` repository

## Version
This project uses `Python 3`

## Run crudserver2.py
With data loaded and with `crudserver2.py` in the `crudserver` directory, run:

```
python crudserver2.py
```

or, if this doesn't work:

```
python3 crudserver2.py
```

This will open the server listening on port `5000`

## Access localhost:5000
Once the server is listening, open your favorite web browser and go to:

`localhost:5000/restaurants/`

Here you will see a list of menu items in the restaurant with id 1 (id corresponding to the database).

> Note: Change the 1 to a different number to get the menu of a different restaurant (if an id isn't in the database, an error is returned)

## Closing (Quitting) the Server
To quit the program simply type `control + C` on the keyboard

## Author(s)

* **Roy Telles, Jr.** *(with the help of the Udacity team)*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* I would like to acknowledge and give big thanks to Udacity and team for this excellent resume-building experience
