import click
import crontab as cron

@click.command(help="view active jobs")
def view():
    cron_user = cron.CronTab(user="your_username")
    for jobs in cron_user:
        click.echo(jobs)


@click.command(help="stop specified job or all jobs")
@click.argument("name", type=click.STRING)
def stop(name):
    cron_user = cron.CronTab(user="your_username")
    res = cron_user.remove_all(comment=name)
    cron_user.write()

@click.command(help="stop all jobs")
def stopall():
    cron_user = cron.CronTab(user="oncex")
    cron_user.remove_all()
    cron_user.write()
        

@click.command(help="start a job")
@click.argument('name', type=click.STRING)
@click.argument("scriptpath", type=click.STRING)
@click.argument("time", type=click.STRING)
def start(name, scriptpath, time):
    cron_user = cron.CronTab(user="your_username")
    link = "python3 " + scriptpath
    li_job = cron_user.new(
        command=link,
        comment=name)
    li_job.setall(time)
    cron_user.write()