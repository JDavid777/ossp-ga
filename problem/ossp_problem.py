from .machine import Machine
from .operation import Operation


class OsspProblem:
    def __init__(self, problem, n):
        self.matrix = problem
        self.num_machines = n
        self.machine_list = []
        self.operation_list = []
        self.jobs_in_execution ={}
        self.setup()
        self.create_machines()
        self.assign_operations()

    def setup(self):
        for i in range(len(self.matrix[0])):
            op_id = self.matrix[0][i]
            job = self.matrix[1][i]
            machine = self.matrix[2][i]
            time = self.matrix[3][i]
            op = Operation(op_id=op_id, machine_id=machine, time= time, job=job)
            self.operation_list.append(op)

    def create_machines(self):
        for i in range(self.num_machines ):
            mc = Machine(i+1)
            self.machine_list.insert(i,mc)

    def assign_operations(self):
        for operation in self.operation_list:
            machine = self.machine_list[operation.machine_id-1]
            machine.add_operation(operation)
            self.jobs_in_execution[operation.job] = 0

    def get_machine(self,operation):
        for machine in self.machine_list:
            if any(op.op_id == operation for op in machine.operation_list):
                return machine

    def validate(self,individual):
        if 0 in individual:
            return False
        aux = dict(enumerate(set(individual)))
        if len(aux) == len(individual):
            return True
        return False

    def evaluate(self, individual):
        if self.validate(individual):
            for operation in individual:
                machine = self.get_machine(operation)
                machine.run(self.jobs_in_execution,operation)
            makespan = 0
            for value in self.jobs_in_execution:
                if self.jobs_in_execution[value] > makespan:
                    makespan = self.jobs_in_execution[value]
            return makespan,
        else:
            return 10000,

'''
    op1 = Operation(op_id=1, machine_id=3, job=1, time=2)
    op2 = Operation(op_id=2, machine_id=1, job=1, time=3)
    op3 = Operation(op_id=3, machine_id=2, job=1, time=5)
    op4 = Operation(op_id=4, machine_id=1, job=2, time=5)
    op5 = Operation(op_id=5, machine_id=3, job=2, time=7)
    op6 = Operation(op_id=6, machine_id=2, job=2, time=1)
    op7 = Operation(op_id=7, machine_id=1, job=3, time=4)
    op8 = Operation(op_id=8, machine_id=2, job=3, time=5)
    op9 = Operation(op_id=9, machine_id=3, job=3, time=1)

    ops = list()
    ops.append(op1)
    ops.append(op2)
    ops.append(op3)
    ops.append(op4)
    ops.append(op5)
    ops.append(op6)
    ops.append(op7)
    ops.append(op8)
    ops.append(op9)

    ossp = OsspProblem(3, ops)
    # inv = [7,5,3,2,9,1,6,4,8]
    inv = [1,3,6,5,7,4,2,9,8]
    ossp.evaluate(inv)
'''


if __name__ == '__main__':
    MATRIX = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [1, 1, 1, 2, 2, 2, 3, 3, 3],
              [3, 1, 2, 1, 3, 2, 1, 2, 3],
              [2, 3, 5, 5, 7, 1, 4, 5, 1]]

    ossp = OsspProblem(MATRIX, 3)
    inv = [1, 3, 6, 5, 7, 4, 2, 9, 9]
    ossp.evaluate(inv)
