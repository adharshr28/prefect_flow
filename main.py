from prefect import Flow, task

@task
def task_one():
    print("Executing Task One")

@task
def task_two():
    print("Executing Task Two")

with Flow("simple_flow") as flow:
    result_one = task_one()
    result_two = task_two()

if __name__ == "__main__":
    flow.run()
