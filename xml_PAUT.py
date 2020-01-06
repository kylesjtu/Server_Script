import xml.etree.ElementTree as ET


########################## 创建xml文件 ################################

a = ET.Element("root")       #创建根节点

b = ET.SubElement(a,"sub1")  #创建子节点，并添加属性
b.attrib = {"name":"name attribute"}

c = ET.SubElement(a,"sub2")  #创建子节点，并添加数据
c.text = "test"

tree = ET.ElementTree(a)    #创建elementtree对象，写文件
tree.write("test.xml")

########################## 修改XML ###################################

"""
    ElementTree.write()       将构建的XML文档写入文件。
    Element.text = ''         直接改变字段内容
    Element.append(Element)   为当前的Elment对象添加子对象
    Element.remove(Element)   删除Element节点
    Element.set(key, value)   添加和修改属性
    ElementTree.write('filename.xml')   写出（更新）XMl文件
"""

updateTree = ET.parse("test.xml")   # 读取待修改文件
root = updateTree.getroot()

newEle = ET.Element("NewElement")   # 创建新节点并添加为root的子节点
newEle.attrib = {"name":"NewElement","age":"20"}
newEle.text = "This is a new element"
root.append(newEle)                 # 更新xml

sub1 = root.find("sub1")            # 修改sub1的name属性
sub1.set("name","New Name")

sub2 = root.find("sub2")            # 修改sub2的数据值
sub2.text = "New Value"


updateTree.write("test.xml")        # 写回原文件
