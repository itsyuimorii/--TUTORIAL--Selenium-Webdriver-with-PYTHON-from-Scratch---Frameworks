from lxml import etree 
 
tree= etree.parse("./fundamentals/src/web_page.html", etree.HTMLParser())
print(etree.tostring(tree))
 
 
# pip install pipenv
# pipenv install pylint autopep8 --dev
# pip install lxml
