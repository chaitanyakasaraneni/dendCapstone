import configparser
from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import MetaData

config = configparser.ConfigParser()
config.read('dwh.cfg')
host = config['CLUSTER']['HOST']
user = config['CLUSTER']['DB_USER']
password = config['CLUSTER']['DB_PASSWORD']
db = config['CLUSTER']['DB_NAME']

def main():
    graph = create_schema_graph(metadata=MetaData('postgresql://'+user+':'+password+'@'+host+':5439/'+db))
    graph.write_png('imgs/data_model.png')

if __name__ == "__main__":
    main()