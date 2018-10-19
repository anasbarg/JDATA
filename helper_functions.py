import xml.etree.ElementTree as ET
def xml_to_dict(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    dict_ = {
        "charts":[]
    }
    for chart in root:
        chart_dict = chart.attrib
        for child in chart:
            if child.tag == "options":
                child_dict = child.attrib
                for grandchild in child:
                    child_dict[grandchild.tag] = grandchild.attrib
            else:
                child_dict = []
                for grandchild in child:
                    child_dict.append(grandchild.attrib)
            chart_dict[child.tag] = child_dict
        dict_["charts"].append(chart_dict)

    for chart in dict_["charts"]:
        for dataset in chart["datasets"]:
            if dataset["fill"] == "true":
                dataset["fill"] = True
            else:
                dataset["fill"] = False
    return dict_



