def resolucion():
    import pulp
    import numpy as np

    ingreso=True
    depositos = []
    oferta = {}
    destinos = []
    demanda = {}
    costos = []
    control=True

    print("RESOLUCION DE PROBLEMAS DE TRANSPORTE" + "\n")
    while control:
        while ingreso:
            revis="control"
            add = input("Ingrese el nombre del deposito. Ingrese FIN para finalizar. ")
            if add == "FIN":
                ingreso = False
            else:
                if add not in depositos:
                    depositos.append(add)
        while revis!="S" and revis!="N":
            print("Los depositos son: ", depositos)
            revis=input("Los datos ingresados, son correctos? S/N: ")
            if revis=="S":
                control=False
            elif revis=="N":
                ingreso=True
                depositos=[]
                print("Ingrese los datos nuevamente.")
            else:
                print("Debe ingresar S o N.")

    control=True
    ingreso=True
    while control:
        while ingreso:
            revis="control"
            for p in depositos:
                add = int(input("Ingrese la oferta disponible en el deposito " + p.upper() + ". "))
                oferta [p] = add
            ingreso=False
        while revis!="S" and revis!="N":
            for key in oferta:
                print(key, ": ", oferta[key])               
            revis=input("Los datos ingresados, son correctos? S/N: ")
            if revis=="S":
                ingreso=False
                control=False
            elif revis=="N":
                ingreso=True
                oferta={}
                print("Ingrese los datos nuevamente.")
            else:
                print("Debe ingresar S o N.")

    control=True
    ingreso=True
    while control:
        while ingreso:
            revis="control"
            add = input("Ingrese el nombre del destino. Ingrese FIN para finalizar. ")
            if add == "FIN":
                ingreso = False
            else:
                if add not in destinos:
                    destinos.append(add)
        while revis!="S" and revis!="N":
            print("Los destinos son: ", destinos)
            revis=input("Los datos ingresados, son correctos? S/N: ")
            if revis=="S":
                control=False
            elif revis=="N":
                ingreso=True
                destinos=[]
                print("Ingrese los datos nuevamente.")
            else:
                print("Debe ingresar S o N.")

    control=True
    ingreso=True
    while control:
        while ingreso:
            revis="control"
            for d in destinos:
                add = int(input("Ingrese la demanda en el destino " + d.upper() + ". "))
                demanda [d] = add
            ingreso=False
        while revis!="S" and revis!="N":
            for key in demanda:
                print(key, ": ", demanda[key])               
            revis=input("Los datos ingresados, son correctos? S/N: ")
            if revis=="S":
                ingreso=False
                control=False
            elif revis=="N":
                ingreso=True
                demanda:{}
                print("Ingrese los datos nuevamente.")
            else:
                print("Debe ingresar S o N.")

    control=True
    ingreso=True
    while control:
        revis="control"
        for p in depositos:
            a=[] 
            for d in destinos:
                a.append(int(input("Ingrese los costos de transporte desde el deposito " + p.upper() + " al destino " + d.upper() + ". ")))
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

    costos = pulp.makeDict([depositos, destinos], costos, 0)
    
    prob = pulp.LpProblem("Material_Supply_Problem", pulp.LpMinimize)
    
    Rutas = [(w, b) for w in depositos for b in destinos]
    
    vars = pulp.LpVariable.dicts("Ruta", (depositos, destinos), 0, None, pulp.LpInteger)
    
    prob += (
        pulp.lpSum([vars[w][b] * costos[w][b] for (w, b) in Rutas]),
        "Sum_of_Transporting_Costs",
    )
    
    for w in depositos:
        prob += (
            pulp.lpSum([vars[w][b] for b in destinos]) <= oferta[w],
            "Sum_of_Products_out_of_warehouses_%s" % w,
        )
    
    for b in destinos:
        prob += (
            pulp.lpSum([vars[w][b] for w in depositos]) >= demanda[b],
            "Sum_of_Products_into_projects%s" % b,
        )
    
    solver=pulp.CPLEX_PY(msg=False)
    #status=prob.solve(solver)
    """
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
        print("\n")"""
    prob.solve(solver)
    #print("Estado: ", pulp.LpStatus[prob.status], "\n")        
    print("La distribucion mas optima es la siguiente:", "\n")
    for v in prob.variables():
        print(v.name, "=", v.varValue)
        
    print("\n" + "Costo total del transporte =", pulp.value(prob.objective), "\n")
    fin=input("Presione cualquier tecla para continuar..." + "\n")