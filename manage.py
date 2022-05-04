from app import create_app
from flask_script import manager,server 
  
app =create_app('development')

manager=manager(app)
 manager.add_command('server',server)
 if __name__ =='__main__':
     manager.run()