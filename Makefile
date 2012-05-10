PYTHON = python
JAVA = java -classpath /opt/local/share/java/xalan.jar

#BASEURL = http://nltk.googlecode.com/svn/trunk/nltk_data/packages
BASEURL = https://raw.github.com/nltk/nltk_data/master/packages

pkg_index:
	$(PYTHON) tools/build_pkg_index.py . $(BASEURL) index.xml
	$(JAVA) org.apache.xalan.xslt.Process -IN index.xml -XSL index.xsl -OUT index.html
	git add index.xml index.html
	git commit -m "updated data index" index.xml index.html


