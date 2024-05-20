from prefect import flow, task

@task
def task_one():
    print("Executing Task One")


@task
def task_two():
    print("Executing Task Two")


@flow(name="main", log_prints=True)
def flow():
    task_one()
    task_two()

if __name__ == "__main__":
    flow()
