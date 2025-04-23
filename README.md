## 🧼 System Updater & Cleaner (Linux Bash Automation)

A simple Python script that automates system updates, upgrades, and optionally clears the terminal—so you can keep your Linux system tidy and up-to-date with zero hassle.

## ⚙️ What It Does

Runs sudo apt update to fetch latest package lists

Runs sudo apt upgrade to install available updates

Prompts the user whether to clear the terminal screen

## 🛠️ Requirements

Linux system with apt package manager

Python 3.x

## 🚀 How to Use

Run the script:

python updater.py

Enter your sudo password when prompted.

After updates finish, you’ll see:

Would you like to 'clear' current terminal window? >>:

Enter yes to clear the screen or no to keep the output visible.

## 🧠 Why This Script?

Automates repetitive tasks

Great for beginners learning automation

Easily extendable (e.g., add autoremove, autoclean, logging, etc.)

##🔒 Important Notes

sudo is required for system updates/upgrades

Use responsibly—this script will apply all available updates

##📄 License

MIT License – Use it, fork it, modify it.

