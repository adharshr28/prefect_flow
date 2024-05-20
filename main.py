from prefect import Flow, task


@task
def task_one():
    print("Executing Task One")


@task
def task_two():
    print("Executing Task Two")


@Flow()
def flow():
    task_one()
    task_two()

if __name__ == "__main__":
    flow()
