import xml.etree.ElementTree as ET
def xml_to_dict(xml_path):
    default_yearSlider_labels = [1992, 2002, 2006, 2008, 2010, 2013]
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

        # converting "true" and "false" strings to Python boolean objects
        for dataset in chart["datasets"]:
            if dataset["fill"] == "true":
                dataset["fill"] = True
            else:
                dataset["fill"] = False
        if chart["options"]["legendDisplay"] == "true":
            chart["options"]["legendDisplay"] = True
        else:
            chart["options"]["legendDisplay"] = False
        
        # converting stringified lists "[...]" to Python list objects
        for slider in chart["sliders"]:
            if "labels" in slider and slider["type"] is "yearSlider":
                slider["labels"] = eval(slider["labels"])
            if "labels" not in slider and slider["type"] is "yearSlider":
                slider["labels"] = default_yearSlider_labels

    return dict_



