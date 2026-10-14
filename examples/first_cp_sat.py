from ortools.sat.python import cp_model


def main():
    model = cp_model.CpModel()

    # 1. Définir x, y, z
    lower_bd = 0
    upper_bd = 10
    x = model.new_int_var(lower_bd, upper_bd, "x")
    y = model.new_int_var(lower_bd, upper_bd, "y")
    z = model.new_int_var(lower_bd, upper_bd, "z")

    # 2. Ajouter les contraintes
    model.add(2*x + y + z <= 15)
    model.add(x + 2*y <= 12)
    model.add(z <= 4)

    # 3. Définir la fonction objectif
    model.maximize(3*x + 2*y + z)

    # 4. Créer le solveur et résoudre
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # 5. Afficher le statut et la solution
    print(f"Status: {solver.status_name(status)}")
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        print(f"x = {solver.value(x)}")
        print(f"y = {solver.value(y)}")
        print(f"z = {solver.value(z)}")
        print(f"Objective value: {solver.objective_value}")
    else:
        print("No solution found.")
    print(f"Solving time: {solver.wall_time}")


if __name__ == "__main__":
    main()