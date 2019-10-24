import yaml
class Read():
    def read(self):
        with open('./data/write.yml','r',encoding='utf-8')as f:
            print(yaml.load(f))