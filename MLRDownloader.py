import requests
import re
volume = input("Volume:")
cont = requests.get('http://proceedings.mlr.press/v' + volume + '/').text
paper_list = re.findall(
    r'(http://proceedings\.mlr\.press/v' + volume + r'/.*?\.pdf)', cont)
paperlist = list(set(paper_list))
for item in paperlist:
    cont = requests.get(item).content
    print('Download ' + item)
    f = open(re.findall(r'http://proceedings\.mlr\.press/v' +
                        volume + r'/.*?/(.*?\.pdf)', item)[0], 'wb+')
    f.write(cont)
    f.close()
