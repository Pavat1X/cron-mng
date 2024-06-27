import click 
import app.sub as sub

@click.group()
def main():
    pass

main.add_command(sub.view)
main.add_command(sub.stop)
main.add_command(sub.stopall)
main.add_command(sub.start)
