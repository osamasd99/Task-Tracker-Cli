


import cmd
import json
import datetime
import os

class task:
    if os.path.exists("tasksStore.json"):
        with open('tasksStore.json') as tasksStore:
            data = json.load(tasksStore)
        if len(data)!=0:
            taskId=int(data[len(data)-1]["id"])
        else:
            taskId=0
    else:
        with open('tasksStore.json', 'w') as tasksStore:
            json.dump([], tasksStore)
        with open('tasksStore.json') as tasksStore:
            data = json.load(tasksStore)
        if len(data)!=0:
            taskId=int(data[len(data)-1]["id"])
        else:
            taskId=0
    #==========add new task func =========#    

    def do_add(self,line):
        "add task : use command add then write  description of task  ex: add description"
        date= datetime.datetime.now()
        if line:
            task.taskId+=1
            newTask ={"id":f"{task.taskId}","description":f"{line}","status":"todo","createdDate":f"{date}","updatedDate":"none"}
            tasks=task.data
            tasks.append(newTask)
            with open('tasksStore.json', 'w') as tasksStore:
                json.dump(tasks, tasksStore)
            print(f"Add new task success description:{newTask['description']} - id:{newTask['id']} - status:{newTask['status']} - createdDate:{newTask['createdDate']}")
        else:
            print("Erorr: write task name")

    # ============ update task name by id func =======#

    def do_update(self,line):
        "update task description by id of task : use command update  then id of task then the new description   ex: update 1 newDescription"
        date= datetime.datetime.now()
        done=False
        line= parse(line)
        if line[0] and line[1]:
            tasks=task.data
            for i in range(len(tasks)):
                if tasks[i]["id"]==f"{line[0]}":
                    tasks[i]["description"]=f"{line[1]}"
                    tasks[i]["updatedDate"]=f"{date}"
                    with open('tasksStore.json', 'w') as tasksStore:
                        json.dump(tasks, tasksStore)
                    done=f"Update success new task description is {tasks[i]['description']}"
                    break
            if done!=False:
                print(done)
            else:
                print("Erorr: Invalid id ")
        else:
            print("Erorr: write id of task then task new description ")     

    #============ delete task  by id func ==========#     

    def do_delete(self,line):
        "delete task by id  ex: delete 1 "
        done=False
        tasks=task.data
        for i in range(len(tasks)):
            if tasks[i]["id"]==f"{line}":
                tasks.remove(tasks[i])
                with open('tasksStore.json', 'w') as tasksStore:
                    json.dump(tasks, tasksStore)
                done=f"  Task is deleted"
                break
        if done!=False:
            print(done)
        else:
            print("Erorr: invalid id ")

    # ================= change task status to done  ===========#

    def do_markDone(self,id):
        "change task status to done by id ex: markDone 1 "
        date= datetime.datetime.now()
        tasks=task.data
        success=False
        if id:
            for i in range(len(tasks)):
                if tasks[i]["id"]==id:
                    tasks[i]["status"]="done"
                    tasks[i]["updatedDate"]=f"{date}"
                    with open('tasksStore.json', 'w') as tasksStore:
                        json.dump(tasks, tasksStore)
                    print( f" task :{tasks[i]['description']} -- is done ")
                    success=True
                    break
            if success==False:
                print("Erorr: Invalid id")
        else:
            print("Error: write id ")

    # ================= change task status to in-progress  ===========#

    def do_markInProgress(self,id):
        "change task status to in-progress by id ex: markInProgress 1 "
        date= datetime.datetime.now()
        tasks=task.data
        success=False
        if id:
            for i in range(len(tasks)):
                if tasks[i]["id"]==id:
                    tasks[i]["status"]="in-progress"
                    tasks[i]["updatedDate"]=f"{date}"
                    with open('tasksStore.json', 'w') as tasksStore:
                        json.dump(tasks, tasksStore)
                    print( f" task :{tasks[i]['description']}  --  is in-progress ")
                    success=True
                    break
            if success==False:
                print("Erorr: Invalid id")
        else:
            print("Error: write id ")

    # ================= change task status to todo  ===========#

    def do_markTodo(self,id):
        "change task status to todo by id ex: markTodo 1 "
        date= datetime.datetime.now()
        tasks=task.data
        success=False
        if id:
            for i in range(len(tasks)):
                if tasks[i]["id"]==id:
                    tasks[i]["status"]="todo"
                    tasks[i]["updatedDate"]=f"{date}"
                    with open('tasksStore.json', 'w') as tasksStore:
                        json.dump(tasks, tasksStore)
                    print( f" task :{tasks[i]['description']} -- is todo ")
                    success=True
                    break
            if success==False:
                print("Erorr: Invalid id")
        else:
            print("Error: write id ")

    #============ get tasks list  func ==========#   

    def do_list(self,line):
        "get tasks list and id of it by command  list  " 
        if len(task.data)!=0:
            for Task in task.data:
                print(f"-->> Task:{Task['description']}   id:{Task['id']}   status:{Task['status']}  createdDate:{Task['createdDate']}  updatedDate:{Task['updatedDate']}")
        else:
            print(" No tasks added ")

        #============ get tasks todo list  func ==========# 

    def do_listTodo(self,line):
        "get tasks todo list  it by command  listTodo  " 
        done=False
        if len(task.data)!=0:
            for Task in task.data:
                if Task["status"]=="todo":
                    print(f"-->> Task:{Task['description']}   id:{Task['id']}   status:{Task['status']}  createdDate:{Task['createdDate']}  updatedDate:{Task['updatedDate']}")
                    done=True
            if done==False:
                print("No Tasks status todo")

        else:
            print(" No tasks added ")

    #============ get tasks done list  func ==========# 

    def do_listDone(self,line):
        "get tasks done list  it by command  listTodo  " 
        done=False
        if len(task.data)!=0:
            for Task in task.data:
                if Task["status"]=="done":
                    print(f"-->> Task:{Task['description']}   id:{Task['id']}   status:{Task['status']}  createdDate:{Task['createdDate']}  updatedDate:{Task['updatedDate']}")
                    done=True
            if done==False:
                print("No Tasks status done")

        else:
            print(" No tasks added ")

    #============ get tasks in-progress list  func ==========#

    def do_listInProgress(self,line):
        "get tasks in-progress list  it by command  listTodo  " 
        done=False
        if len(task.data)!=0:
            for Task in task.data:
                if Task["status"]=="in-progress":
                    print(f"-->> Task:{Task['description']}   id:{Task['id']}   status:{Task['status']}  createdDate:{Task['createdDate']}  updatedDate:{Task['updatedDate']}")
                    done=True
            if done==False:
                print("No Tasks status in-progress")

        else:
            print(" No tasks added ")

    



class TaskMangerCLI(cmd.Cmd,task):
    prompt = 'taskMangerCli>> '
    intro = 'Welcome to TaskMangerCLI. Type "help" for available commands.'
    def __init__(self):
        super().__init__()
    def do_quit(self, line):
        """Exit the CLI."""
        return True
    def precmd(self, line):
        print("==============================")  # Add an empty line for better readability
        return line
    def postcmd(self, stop, line):
        print("==============================")  # Add an empty line for better readability
        return stop
def parse(arg):
    # spilt arg  
    arg= arg.split(" ",1)
    
    return arg
if __name__ == '__main__':
    TaskMangerCLI().cmdloop()




