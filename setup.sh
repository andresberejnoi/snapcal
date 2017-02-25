# Source this.
# Setup virtualenv
mkdir -p data

if [ ! -d venv ]
then
  virtualenv venv
fi

. venv/bin/activate

pip install pyyaml
pip install requests

# To deactivate the venv, use
#
# $ deactivate
#
# as a command on the command line.
# To set up the venv again, then type
#
# $ source setup.sh
