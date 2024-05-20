from prefect import flow, task

@task
def task_one():
    print("Executing Task One")


@task
def task_two():
    print("Executing Task Two")

@task
def task_three():
    print("Executing Task three")


@flow(name="main", log_prints=True)
def flow():
    task_one()
    task_two()
    task_three()

if __name__ == "__main__":
    flow()
