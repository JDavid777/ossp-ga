
'''
Clase que representa la maquina. Se realiz� una abstracci�n de lo que representan las maquinas
en el problema: cada maquina cuenta con un identificador, una lista operaciones asignadas
y el tiempo m�ximo que lleva la maquina "makespan"
'''

class Machine:

    def __init__(self, machine_id):
        self.id = machine_id
        self.operation_list = list()
        self.makespan = 0


    def add_operation(self, operation):
        self.operation_list.append(operation)


    ''' Funcion principal de la maquina. Realiza la "ejecucion de una operacion asignada
    :param jobs_times: representa los tiempos acumulados de las operaciones 
    :param2 op_id: representa el id de la operacion a ejecutar por la maquina
    '''
    def run(self, jobs_times, op_id):
        # Obetenemos la operacion con el id proporcionado
        operation = self.operation_list[self.get_operation(op_id)]

        # se valida si el tiempo acumulado de la tarea supera al tiempo acumulado de la maquina
        if jobs_times[operation.job] >= self.makespan:

            # Actualiza el tiempo de la tarea sumandole el tiempo de la operacion a ejecutar
            jobs_times[operation.job] += operation.time
            # Se actualiza el makespan de la maquina
            self.makespan += operation.time
        else:
            # Se suma el tiempo de la operacion y el tiempo acumulado de la tarea al tiempo acumulado de la maquina
            self.makespan += jobs_times[operation.job] + operation.time

            # Se actualia el tiempo acumulado de la tarea a la que pertenece la operacion
            jobs_times[operation.job]=self.makespan

    '''Metodo que devuelve la operacion con el id proporcionado'''
    def get_operation(self,op_id):
        for i in range(len(self.operation_list)):
            if op_id == self.operation_list[i].op_id:
                return i






