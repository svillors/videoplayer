import os
from livereload import Server


def reload():
    print("Файл обновлён")


server = Server()
index_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                          'index.html')
styles_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'styles.css')
server.watch(index_path, reload)
server.watch(styles_path, reload)
root_dir = os.path.abspath(os.path.dirname(__file__))
server.serve(root=root_dir,
             default_filename='index.html',
             port=8080,
             liveport=35729)
