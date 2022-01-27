from .machine import Machine
from .operation import Operation

'''
Clase que representa el Open Shop Scheduling Problem 
'''
class OsspProblem:
    def __init__(self, problem, n):
        self.matrix = problem
        self.num_machines = n
        self.machine_list = []
        self.operation_list = []
        self.jobs_in_execution ={}
        self.setup()


    '''
    Funcion encargada de la configuracion de las maquinas; creacion de las n maquinas,
    inicializacion de las operaciones y asignaci�n de las mismas a las maquinas correspondientes
    '''
    def setup(self):
        for i in range(len(self.matrix[0])):
            op_id = self.matrix[0][i]
            job = self.matrix[1][i]
            machine = self.matrix[2][i]
            time = self.matrix[3][i]
            op = Operation(op_id=op_id, machine_id=machine, time= time, job=job)
            self.operation_list.append(op)
        self.create_machines()
        self.assign_operations()

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

    '''Metodo para limpiar las referencias en cada evauacion de un individuo'''
    def clearData(self):
        for operation in self.operation_list:
            self.jobs_in_execution[operation.job]=0
        for machine in self.machine_list:
            machine.makespan = 0;

    '''
    Funcion de evaluaci�n. Se encarga de ejecutar las operaciones representadas por los valores de el
    individio.
    :return: El makespan (resultado de la evaluacion) correspondiente al individio que se pada como parametro
    :param: individual: individio a evaluar 
    '''
    def evaluate(self, individual):
        for operation in individual:
            machine = self.get_machine(operation)
            machine.run(self.jobs_in_execution,operation)
        makespan = 0
        for value in self.jobs_in_execution:
            if self.jobs_in_execution[value] > makespan:
                makespan = self.jobs_in_execution[value]

        self.clearData();
        return makespan,

