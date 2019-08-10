import re
import os
import requests
import json

session = requests.session()

def fetch_url(url):
    return session.get(url).content.decode('gbk')

def get_doc_id(url):
    return re.findall("view/(.*).html", url)[0]

def parser_type(content):
    return re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]

def parser_title(content):
    return re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)[0]

def parser_txt(filename, doc_id):
    content_url = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=' + doc_id
    content = fetch_url(content_url)
    md5 = re.findall('"md5sum":"(.*?)"', content)[0]
    pn = re.findall('"totalPageNum":"(.*?)"', content)[0]
    rsign = re.findall('"rsign":"(.*?)"', content)[0]
    content_urls = 'https://wkretype.bdimg.com/retype/text/' + doc_id + '?rn=' + pn + '&type=txt' + \
                    md5 + '&rsign=' + rsign

    content = json.loads(fetch_url(content_urls))
    result = ''
    for item in content:
        for i in item['parags']:
            result += i['c'].replace('\\r', '\r').replace('\\n', '\n')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(result)
        print(f"Saved as {filename}")

def parser_ppt(filename, doc_id):
    content_url = 'https://wenku.baidu.com/browse/getbcsurl?doc_id=' + doc_id + \
                  '&pn=1&rn=99999&type=ppt'
    content = fetch_url(content_url)
    url_list = re.findall('"zoom":"(.*?)","page"', content)
    url_list = [item.replace("\\","") for item in url_list]

    if not os.path.exists(filename):
        os.mkdir(filename)
    for index, url in enumerate(url_list):
        content = session.get(url).content
        path = os.path.join(filename, filename + '_page_' + str(index) + '.jpg')
        with open(path, 'wb') as f:
            f.write(content)
    print(f"PPT saved in {filename} directory")

def main():
    url = input('input url: ')
    content = fetch_url(url)
    doc_id = get_doc_id(url)
    type = parser_type(content)
    title = parser_title(content).replace(".","")
    if type == 'txt':
        parser_txt(title, doc_id)
    elif type == 'ppt':
        parser_ppt(title, doc_id)

if __name__ == '__main__':
    main()
