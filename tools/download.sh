#!/bin/bash
function usage() {
  echo
  echo "Usage: $(basename $0) <collection name>"
  echo
  echo "Copies nltk data to proper locations from local copy of repository."
  echo "Assumes script is in repo tools directory."
  echo
  echo "Clone the repo:"
  printf '\t%s\n' 'git clone git@github.com:<owner>/nltk_data.git'
  echo
  echo "Now switch branches to the one with the data on it (and this script):"
  printf '\t%s\n' 'git branch gh-pages remotes/origin/gh-pages'
  printf '\t%s\n' 'git checkout gh-pages'
  echo
  echo "Remember to use sudo if installing to /usr/share (default)"
  echo
  echo set NLTK_DATA_DIR to target directory if different than /usr/share, e.g.:
  printf '\t%s %s\n' 'NLTK_DATA_DIR=./local/dir' "$(basename $0) book"
  echo
}

[ $# -eq 0 ] && { usage; exit 1; }

collection=$1
data_dir=${NLTK_DATA_DIR:-/usr/share/nltk_data}
script_dir="$( cd "$( dirname "$0" )" && pwd )"
repo_dir=$(readlink -f "$script_dir/..")
package_dir=$repo_dir/packages
collections_dir=$repo_dir/collections

mkdir -p $data_dir
pushd $data_dir

python -c "import xml.etree.ElementTree as e
for item in e.parse('$collections_dir/$collection.xml').getroot().findall('item'): 
  print item.get('ref')" |
while read item 
do
  package=$(find $package_dir -name $item.zip -print)
  target_dir=$(basename $(dirname $package))
  target_file=$target_dir/$item.zip 
  mkdir -p $target_dir
  cp $package $target_file 
  unzip -u -d $target_dir $target_file
done

popd

