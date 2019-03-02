if 'cached' not in os.listdir('./'):
        os.system('mkdir cached')
    listdir = os.listdir("./cached")
    path = './cached/'
    
def download(index, url, listdir, path):
    target_file = "{}.html".format(index)
    target_url = url.format(index * 25)
    if target_file not in listdir:
        html = requests.get(target_url, headers=headers)
        html.encoding = 'utf-8'
        with open(path + target_file, 'w+') as file:
            file.write(html.text)
        html = html.text
    else:
        with open(path + target_file, 'r') as file:
            html = file.read()
    return html
