import json
import pip

def install(pkg):        
        if pip.main(['install', pkg]):
            return True
        else:
            return False
        
def loadData():
    file=open('data.json','r')
    data=json.load(file)
    return data


def main():
    data=loadData()
    invalid_pkg=[]
    for i in data["Dependencies"]:
        check=install(i)
        if not check:
            invalid_pkg.append(i)
            
    print("NO OF INVALID PACKAGES:",end="")
    print(len(invalid_pkg))
    print("NAME OF PACKAGES:")
    for i in invalid_pkg:
        print(i)

main()

