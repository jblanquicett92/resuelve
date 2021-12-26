# Check if the script is being sourced
if [ $_ == $0 ]; then 
    echo "Script should be sourced. Please run the following command:"
    printf "\nsource `basename "$0"`\n"
    exit 1
fi

# Check if python3 is installed
if [ -z "$(dpkg -l | grep python3-dev)" ]; then
    printf "\nInstalling Python3 dev package...\n"
    sudo apt-get update -y
    sudo apt-get install -y python3-dev
fi

# Check if python3 is installed
if [ -z "$(dpkg -l | grep python3-venv)" ]; then
    printf "\nInstalling Python3 venv package...\n"
    sudo apt-get update -y
    sudo apt-get install -y python3-venv
fi

# Check if libicu is installed
if [ -z "$(dpkg -l | grep libicu-dev)" ]; then
    printf "\nInstalling libicu-dev package...\n"
    sudo apt-get update -y
    sudo apt-get install -y libicu-dev
fi

# Create virtual environment
python3 -m venv env

# Install project dev requirements
pip3 install -r requirements/dev.txt

