
import os
import sys
from glob import glob
from typing import List
from xml.etree import ElementTree
from nltk.downloader import _indent_xml

if len(sys.argv) != 2:
    print("Usage: ")
    print("build_collections.py <path-to-packages>")
    sys.exit(-1)

ROOT = sys.argv[1]

def write(file_name: str, coll_name: str, items: List[str]) -> None:
    """Write `collection/{file_name}.xml` with `file_name` as the collection `id`,
    `coll_name` as the collection `name`, and `items` as a list of collection items.

    :param file_name: The id of the collection, equivalent to the file name,
        e.g. `all-corpora`.
    :type file_name: str
    :param coll_name: The name of the collection, e.g. `"All corpora"`
    :type coll_name: str
    :param items: A list of names for the collection items, e.g. `["abc", "alpino", ...]`
    :type items: List[str]
    """
    et = ElementTree.Element("collection", id=file_name, name=coll_name)
    et.extend(ElementTree.Element("item", ref=item) for item in sorted(items))
    _indent_xml(et)
    with open(os.path.join(ROOT, "collections", file_name + ".xml"), "w", encoding="utf8") as f:
        f.write(ElementTree.tostring(et).decode("utf8"))

def get_id(xml_path: str) -> str:
    """Given a full path, extract only the filename (i.e. the nltk_data id)

    :param xml_path: A full path, e.g. "./packages/corpora/abc.xml"
    :type xml_path: str
    :return: The filename, without the extension, e.g. "abc"
    :rtype: str
    """
    return os.path.splitext(os.path.basename(xml_path))[0]

# Write `collection/all-corpora.xml` based on all files under /packages/corpora
corpora_items = [get_id(xml_path) for xml_path in glob(f"{ROOT}/packages/corpora/*.xml")]
write("all-corpora", "All the corpora", corpora_items)

# Write `collection/all-nltk.xml` and `collection/all.xml` based on all files under /packages
all_items = [get_id(xml_path) for xml_path in glob(f"{ROOT}/packages/**/*.xml")]
write("all-nltk", "All packages available on nltk_data gh-pages branch", all_items)
write("all", "All packages", all_items)