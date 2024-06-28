import click
import crontab as cron

@click.command(help="view active jobs")
def view():
    cron_user = cron.CronTab(user="oncex")
    for jobs in cron_user:
        click.echo(jobs)


@click.command(help="stop specified job or all jobs")
@click.argument("user", type=click.STRING)
@click.argument("name", type=click.STRING)
def stop(user, name):
    cron_user = cron.CronTab(user=user)
    res = cron_user.remove_all(comment=name)
    cron_user.write()

@click.command(help="stop all jobs")
def stopall():
    cron_user = cron.CronTab(user="oncex")
    cron_user.remove_all()
    cron_user.write()
        

@click.command(help="start a job")
@click.argument("user", type=click.STRING)
@click.argument('name', type=click.STRING)
@click.argument("scriptpath", type=click.STRING)
@click.argument("time", type=click.STRING)
def start(user, name, scriptpath, time):
    cron_user = cron.CronTab(user=user)
    link = "python3 " + scriptpath
    li_job = cron_user.new(
        command=link,
        comment=name)
    li_job.setall(time)
    cron_user.write()