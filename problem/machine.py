

class Machine:

    def __init__(self, machine_id):
        self.id = machine_id
        self.operation_list = list()
        self.makespan = 0

    def add_operation(self, operation):
        self.operation_list.append(operation)

    def run(self, jobs_times, op_id):
        operation = self.operation_list[self.get_operation(op_id)]
        #print("operation",operation.op_id, "tiempo", operation.time)
        if jobs_times[operation.job] >= self.makespan:
            jobs_times[operation.job] += operation.time
            self.makespan += operation.time
        else:
            self.makespan += jobs_times[operation.job] + operation.time
            jobs_times[operation.job]=self.makespan
        #print(jobs_times, "t mchine",self.makespan)

    def get_operation(self,op_id):
        for i in range(len(self.operation_list)):
            if op_id == self.operation_list[i].op_id:
                return i






