import getpass
import os

from fabric import Connection, Config

from dotenv import load_dotenv

load_dotenv()
# password = input("enter password: ")
password =  getpass.getpass("enter the password: ")
config = Config(overrides={'sudo': {'password': password}})
connection = Connection(
    host=os.environ.get("HOST"),
    user=os.environ.get("USER"),
    config=config,
    connect_kwargs={
        "key_filename": "/home/pelino/.ssh/id_rsa",
        "passphrase": os.environ.get("PASSPHRASE"),
    },
)
connection.sudo('whoami', hide='stderr')
connection.run("pwd")
connection.sudo("apt install nginx")

