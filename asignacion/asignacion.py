def minimizacion():

    import pulp
    import numpy as np

    operarios=[]
    puestos=[]
    costos=[]
    revis="control"
    control=True
    ingreso=True

    print("RESOLUCION DE PROBLEMAS DE ASIGNACION - MINIMIZACION")

    while control:
        while ingreso:
            revis="control"
            add = input("Ingrese los operarios. Ingrese FIN para finalizar. ")
            if add == "FIN":
                ingreso = False
            else:
                if add not in operarios:
                    operarios.append(add)
        while revis!="S" and revis!="N":
            print("Los operarios son: ", operarios)
            revis=input("Los datos ingresados, son correctos? S/N: ")
            if revis=="S":
                control=False
            elif revis=="N":
                ingreso=True
                operarios=[]
                print("Ingrese los datos nuevamente.")
            else:
                print("Debe ingresar S o N.")

    ingreso=True
    control=True
    revis="control"
    while control:
        while ingreso:
            revis="control"
            add = input("Ingrese el puesto de trabajo. Ingrese FIN para finalizar. ")
            if add == "FIN":
                ingreso = False
            else:
                if add not in puestos:
                    puestos.append(add)
        while revis!="S" and revis!="N":
            print("Los puestos de trabajo son: ", puestos)
            revis=input("Los datos ingresados, son correctos? S/N: ")
            if revis=="S":
                control=False
            elif revis=="N":
                ingreso=True
                puestos=[]
                print("Ingrese los datos nuevamente.")
            else:
                print("Debe ingresar S o N.")

    control=True
    ingreso=True
    revis="control"
    while control:
        revis="control"
        for p in operarios:
            a=[] 
            for d in puestos:
                a.append(int(input("Ingrese las horas/coste del operario " + p.upper() + " en el puesto de trabajo " + d.upper() + ". ")))
            costos.append(a)
            control=False
    while revis!="S" and revis!="N":
        print(np.matrix(costos))
        revis=input("Los datos ingresados, son correctos? S/N: ")
        if revis=="S":
            ingreso=False
            control=False
        elif revis=="N":
            ingreso=True
            control=True
            costos=[]
            print("Ingrese los datos nuevamente.")
        else:
            print("Debe ingresar S o N.")

    prob = pulp.LpProblem("Assignment_Problem", pulp.LpMinimize) 
    
    costos=pulp.makeDict([operarios, puestos], costos, 0)

    assign = [(w, j) for w in operarios for j in puestos]

    vars = pulp.LpVariable.dicts("Asignar", (operarios, puestos), 0, None, pulp.LpBinary)

    prob += (
        pulp.lpSum([vars[w][j] * costos[w][j] for (w, j) in assign]),
        "Sum_of_Assignment_Costs",
    )

    for j in puestos:
        prob+= pulp.lpSum(vars[w][j] for w in operarios) == 1

    for w in operarios:
        prob+= pulp.lpSum(vars[w][j] for j in puestos) == 1

    solver=pulp.CPLEX_PY(msg=False)
    status=prob.solve(solver)
    prob.solverModel.parameters.mip.pool.absgap.set(0.0)
    prob.solverModel.parameters.mip.pool.intensity.set(4)
    prob.solverModel.parameters.mip.limits.populate.set(3000000)
    prob.solverModel.populate_solution_pool()
    numSol=prob.solverModel.solution.pool.get_num()
    meanobjval = prob.solverModel.solution.pool.get_mean_objective_value()
    sol_pool = []
    for i in range(numSol):
        objval_i = prob.solverModel.solution.pool.get_objective_value(i)
        x_i = prob.solverModel.solution.pool.get_values(i)
        nb_vars=len(x_i)
        sol = []
        for k in range(nb_vars):
            sol.append([prob.solverModel.variables.get_names(k),x_i[k]])
        sol_pool.append(sol)
    print("Hay",numSol, "soluciones", "\n")
    print("Soluciones posibles:")#,sol_pool, "\n")
    for l in sol_pool:
        for n in l:
            if (n[1]>0):
                print(n[0])
        print("\n")
    prob.solve()
    #print("Estado: ", pulp.LpStatus[prob.status], "\n")
    #print("La distribucion mas optima es la siguiente:", "\n")
    #for v in prob.variables():
    #    print(v.name, "=", v.varValue)
    print("Costo total de la distribucion = ", pulp.value(prob.objective), "\n")
    resultado=int(pulp.value(prob.objective))
    revis="S"
    revis=input("Desea multiplicar el valor por horas/costo? S/N: ")
    if revis=="S":
        revis="control"
        while revis!="S":
            factor=int(input("Ingrese el multiplo: "))
            revis=input("Es " + str(factor) + " correcto? S/N: ")
        print("El costo total es = " + str(resultado*factor))
    fin=input("Presione cualquier tecla para continuar..." + "\n")

def maximizacion():

    import pulp
    import numpy as np

    operarios=[]
    puestos=[]
    costos=[]
    revis="control"
    control=True
    ingreso=True

    print("RESOLUCION DE PROBLEMAS DE ASIGNACION - MAXIMIZACION")

    while control:
        while ingreso:
            revis="control"
            add = input("Ingrese los operarios. Ingrese FIN para finalizar. ")
            if add == "FIN":
                ingreso = False
            else:
                if add not in operarios:
                    operarios.append(add)
        while revis!="S" and revis!="N":
            print("Los operarios son: ", operarios)
            revis=input("Los datos ingresados, son correctos? S/N: ")
            if revis=="S":
                control=False
            elif revis=="N":
                ingreso=True
                operarios=[]
                print("Ingrese los datos nuevamente.")
            else:
                print("Debe ingresar S o N.")

    ingreso=True
    control=True
    revis="control"
    while control:
        while ingreso:
            revis="control"
            add = input("Ingrese el puesto de trabajo. Ingrese FIN para finalizar. ")
            if add == "FIN":
                ingreso = False
            else:
                if add not in puestos:
                    puestos.append(add)
        while revis!="S" and revis!="N":
            print("Los puestos de trabajo son: ", puestos)
            revis=input("Los datos ingresados, son correctos? S/N: ")
            if revis=="S":
                control=False
            elif revis=="N":
                ingreso=True
                puestos=[]
                print("Ingrese los datos nuevamente.")
            else:
                print("Debe ingresar S o N.")

    control=True
    ingreso=True
    revis="control"
    while control:
        revis="control"
        for p in operarios:
            a=[] 
            for d in puestos:
                a.append(int(input("Ingrese la eficiencia del operario " + p.upper() + " en el puesto de trabajo " + d.upper() + ". ")))
            costos.append(a)
            control=False
        while revis!="S" and revis!="N":
            print(np.matrix(costos))
            revis=input("Los datos ingresados, son correctos? S/N: ")
            if revis=="S":
                ingreso=False
                control=False
            elif revis=="N":
                ingreso=True
                control=True
                costos=[]
                print("Ingrese los datos nuevamente.")
            else:
                print("Debe ingresar S o N.")
           
    """
    matriz_inv=[]
    
    for row in costos:
        costos_row=[]
        for col in row:
            costos_row +=[np.amax(costos)-col]
        matriz_inv +=[costos_row]
    """

    prob = pulp.LpProblem("Assignment_Problem", pulp.LpMaximize) 
    
    costos=pulp.makeDict([operarios, puestos], costos, 0)

    assign = [(w, j) for w in operarios for j in puestos]

    vars = pulp.LpVariable.dicts("Asignar", (operarios, puestos), 0, None, pulp.LpBinary)

    prob += (
        pulp.lpSum([vars[w][j] * costos[w][j] for (w, j) in assign]),
        "Sum_of_Assignment_Costs",
    )

    for j in puestos:
        prob+= pulp.lpSum(vars[w][j] for w in operarios) == 1

    for w in operarios:
        prob+= pulp.lpSum(vars[w][j] for j in puestos) == 1

    solver=pulp.CPLEX_PY(msg=False)
    status=prob.solve(solver)
    prob.solverModel.parameters.mip.pool.absgap.set(0.0)
    prob.solverModel.parameters.mip.pool.intensity.set(4)
    prob.solverModel.parameters.mip.limits.populate.set(3000000)
    prob.solverModel.populate_solution_pool()
    numSol=prob.solverModel.solution.pool.get_num()
    meanobjval = prob.solverModel.solution.pool.get_mean_objective_value()
    sol_pool = []
    for i in range(numSol):
        objval_i = prob.solverModel.solution.pool.get_objective_value(i)
        x_i = prob.solverModel.solution.pool.get_values(i)
        nb_vars=len(x_i)
        sol = []
        for k in range(nb_vars):
            sol.append([prob.solverModel.variables.get_names(k),x_i[k]])
        sol_pool.append(sol)
    print("Hay",numSol, "soluciones", "\n")
    print("Soluciones posibles:")#,sol_pool, "\n")
    for l in sol_pool:
        for n in l:
            if (n[1]>0):
                print(n[0])
        print("\n")
    prob.solve()
    #print("Estado: ", pulp.LpStatus[prob.status], "\n")
    #print("La distribucion mas optima es la siguiente:", "\n")
    #for v in prob.variables():
    #    print(v.name, "=", v.varValue)
    print("Eficiencia total de la distribucion = ", pulp.value(prob.objective), "\n")
    resultado=int(pulp.value(prob.objective))
    revis="S"
    revis=input("Desea multiplicar el valor por horas/costo? S/N: ")
    if revis=="S":
        revis="control"
        while revis!="S":
            factor=int(input("Ingrese el multiplo: "))
            revis=input("Es " + str(factor) + " correcto? S/N: ")
        print("El costo total es = " + str(resultado*factor))
    fin=input("Presione cualquier tecla para continuar..." + "\n")