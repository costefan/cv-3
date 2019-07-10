from task1.app import main as maint_task_1


def run_task(task_num):
    if task_num == 1:
        maint_task_1()


if __name__ == '__main__':
    task_number = int(input(
        """
        Which task do you want to run? \n
        1. MeanShift/CamShift \n
        """
    ))
    run_task(task_number)
