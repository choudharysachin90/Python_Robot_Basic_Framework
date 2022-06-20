import xml.etree.ElementTree as ET


class DataAccess:

    def getLoginDetails(self):
        Credentials = dict()
        Namelist = []
        ValueLIst = []

        tree = ET.parse('C:\\Users\\nidhi\\PycharmProjects\\Oct_SamplePythonProject\\TestData\\UserDetails.xml')
        root = tree.getroot()

        for child in root.iter():
            for key, value in child.items():
                if key == 'UserName':
                    Namelist.append(value)
                else:
                    ValueLIst.append(value)

        Credentials = dict(zip(Namelist, ValueLIst))
        return Credentials
