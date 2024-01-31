import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import messagebox
import csv

file_name = "../positions_data.txt"

def initialization_coordinates(PopSize, LB, UB):
    x_coords = np.random.uniform(LB[0], UB[0], PopSize)
    y_coords = np.random.uniform(LB[1], UB[1], PopSize)
    Positions = np.column_stack((x_coords, y_coords))
    print(Positions)
    return Positions

def nodes_initialization(alpha_count, beta_count, delta_count, LB, UB):
    # Generating Alpha nodes
    alpha_positions = initialization_coordinates(alpha_count, LB, UB)

    # Generating Beta nodes
    beta_positions = initialization_coordinates(beta_count, LB, UB)

    # Generating Delta nodes
    delta_positions = initialization_coordinates(delta_count, LB, UB)

    Positions = np.vstack((alpha_positions, beta_positions, delta_positions))

    return Positions

def get_positions():
    # Read the data from the file
    file_name = "positions_data.txt"  # Replace with your file name
    data = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.strip().split(',')
            data.append([float(val) for val in values])

    # Convert the read data into a NumPy array
    Positions = np.array(data)
    print(Positions)
    return Positions

# def get_ch_id(bestsol, Positions):



def GWO(PopSize, MaxT, LB, UB, D, Fobj):
    Alpha_Pos = np.zeros(D)
    Alpha_Fit = 1
    Beta_Pos = np.zeros(D)
    Beta_Fit = 0.75
    Delta_Pos = np.zeros(D)
    Delta_Fit = 0.5
        
    Convergence_curve = np.zeros(MaxT)

    alpha_count = 15
    beta_count = 30
    delta_count = PopSize - alpha_count - beta_count

    Positions = nodes_initialization(alpha_count, beta_count, delta_count, LB, UB)

    l = 0
    while l < MaxT:
        for i in range(Positions.shape[0]):
            BB_UB = Positions[i, :] > UB
            BB_LB = Positions[i, :] < LB
            Positions[i, :] = (Positions[i, :] * (~(BB_UB + BB_LB))) + UB * BB_UB + LB * BB_LB
            Fitness = Fobj(Positions[i, :])

            if Fitness < Alpha_Fit:
                Alpha_Fit = Fitness
                Alpha_Pos = Positions[i, :]

            if Fitness > Alpha_Fit and Fitness < Beta_Fit:
                Beta_Fit = Fitness
                Beta_Pos = Positions[i, :]

            if Fitness > Alpha_Fit and Fitness > Beta_Fit and Fitness < Delta_Fit:
                Delta_Fit = Fitness
                Delta_Pos = Positions[i, :]

        a = 2 - 1 * (2 / MaxT)
        for i in range(Positions.shape[0]):
            for j in range(Positions.shape[1]):
                r1 = np.random.random()
                r2 = np.random.random()

                A1 = 2 * a * r1 - a
                C1 = 2 * r2

                D_Alpha = abs(C1 * Alpha_Pos[j] - Positions[i, j])
                X1 = Alpha_Pos[j] - A1 * D_Alpha

                r1 = np.random.random()
                r2 = np.random.random()

                A2 = 2 * a * r1 - a
                C2 = 2 * r2

                D_Beta = abs(C2 * Beta_Pos[j] - Positions[i, j])
                X2 = Beta_Pos[j] - A2 * D_Beta

                r1 = np.random.random()
                r2 = np.random.random()

                A3 = 2 * a * r1 - a
                C3 = 2 * r2

                D_Delta = abs(C3 * Delta_Pos[j] - Positions[i, j])
                X3 = Delta_Pos[j] - A3 * D_Delta

                Positions[i, j] = (X1 + X2 + X3) / 3
        l += 1
        Convergence_curve[l - 1] = Alpha_Fit

    return Alpha_Fit, Alpha_Pos, Convergence_curve, Positions

if __name__ == "__main__":
    def F1(x):
        return np.sum(x ** 2)

    Fun_name = F1
    D = 2
    PopSize = 100
    LB = [-100, -100]
    UB = [100, 100]
    MaxT = 200

    bestfit, bestsol, convergence_curve, Positions = GWO(PopSize, MaxT, LB, UB, D, Fun_name)
    print("Best Fitness =", bestfit)
    print("Best Solution = ", bestsol)

    # Calculate fitness values for all positions
    fitness_values = np.array([Fun_name(pos) for pos in Positions])

    # Sort positions based on fitness values
    sorted_indices = np.argsort(fitness_values)

    # Display the indexes of all solutions
    for i in range(len(sorted_indices)):
        print(f"Solution {i + 1} Index:", sorted_indices[i])

    # Select top 4 positions and their fitness values
    top_4_positions = Positions[sorted_indices[:4]]
    top_4_fitness = fitness_values[sorted_indices[:4]]

    # Display top 4 solutions and their fitness values
    for i in range(len(top_4_positions)):
        print(f"\nTop 4 Solution {i + 1}:")
        print(f"Position: {top_4_positions[i]}")
        print(f"Fitness Value: {top_4_fitness[i]}")

    # alpha_count = 15
    # beta_count = 40
    # delta_count = PopSize - alpha_count - beta_count

    # alpha_nodes = Positions[:alpha_count]
    # beta_nodes = Positions[alpha_count:alpha_count + beta_count]
    # delta_nodes = Positions[alpha_count + beta_count:]

    # # Plotting
    # plt.figure(figsize=(8, 6))
    # plt.scatter(beta_nodes[:, 0], beta_nodes[:, 1], color='blue', label='Beta Nodes')
    # plt.scatter(delta_nodes[:, 0], delta_nodes[:, 1], color='red', label='Delta Nodes')
    # plt.scatter(alpha_nodes[:, 0], alpha_nodes[:, 1], color='green', label='Alpha Nodes (Best)')

    # # Highlighting the best alpha node
    # best_alpha_index = np.argmin([Fun_name(alpha) for alpha in alpha_nodes])
    # plt.scatter(alpha_nodes[best_alpha_index, 0], alpha_nodes[best_alpha_index, 1], color='gold', label='Best Alpha', s=100)

    # plt.title('Alpha Nodes vs Beta Nodes and Delta Nodes')
    # plt.xlabel('X-axis')
    # plt.ylabel('Y-axis')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

    with open(file_name, mode='w') as file:
        for position in Positions:
            file.write(f"{position[0]}, {position[1]}\n")