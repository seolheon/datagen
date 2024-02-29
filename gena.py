import random
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkbootstrap import Style

def generate_dataset():
    with open("names.txt", "r") as file:
        cat_names = [name.strip() for name in file.readlines()]

    breeds_characteristics = {
        "Siamese": {"weight": (3, 6), "height": (20, 26), "life_expectancy": (12, 15),
                    "coat_length": (1, 2), "grooming_needs": 1, "energy_level": (7, 9),
                    "intelligence_level": (6, 8), "playfulness": (8, 10),
                    "vocalization": (8, 10), "adaptability": (8, 10)},
        "Persian": {"weight": (3, 7), "height": (25, 32), "life_expectancy": (10, 15),
                    "coat_length": (3, 3), "grooming_needs": 3, "energy_level": (3, 5),
                    "intelligence_level": (4, 6), "playfulness": (3, 5),
                    "vocalization": (2, 4), "adaptability": (4, 6)},
        "Munchkin": {"weight": (2, 4), "height": (15, 21), "life_expectancy": (12, 14),
                     "coat_length": (1, 2), "grooming_needs": 1, "energy_level": (5, 7),
                     "intelligence_level": (6, 8), "playfulness": (7, 9),
                     "vocalization": (4, 6), "adaptability": (7, 9)},
        "Ragdoll": {"weight": (4, 9), "height": (25, 32), "life_expectancy": (12, 17),
                    "coat_length": (3, 3), "grooming_needs": 2, "energy_level": (3, 5),
                    "intelligence_level": (5, 7), "playfulness": (4, 6),
                    "vocalization": (2, 4), "adaptability": (6, 8)},
        "Bengal": {"weight": (4, 8), "height": (25, 35), "life_expectancy": (12, 16),
                   "coat_length": (1, 2), "grooming_needs": 1, "energy_level": (8, 10),
                   "intelligence_level": (6, 8), "playfulness": (9, 10),
                   "vocalization": (6, 8), "adaptability": (7, 9)},
        "Sphynx": {"weight": (3, 5), "height": (20, 27), "life_expectancy": (12, 14),
                   "coat_length": (0, 0), "grooming_needs": 0, "energy_level": (6, 8),
                   "intelligence_level": (5, 7), "playfulness": (5, 7),
                   "vocalization": (7, 9), "adaptability": (7, 9)},
        "Scottish Fold": {"weight": (3, 6), "height": (20, 26), "life_expectancy": (12, 15),
                          "coat_length": (2, 3), "grooming_needs": 2, "energy_level": (4, 6),
                          "intelligence_level": (6, 8), "playfulness": (5, 7),
                          "vocalization": (3, 5), "adaptability": (7, 9)},
        "British Shorthair": {"weight": (4, 7), "height": (25, 30), "life_expectancy": (12, 17),
                              "coat_length": (1, 2), "grooming_needs": 1, "energy_level": (4, 6),
                              "intelligence_level": (5, 7), "playfulness": (3, 5),
                              "vocalization": (2, 4), "adaptability": (6, 8)},
        "Abyssinian": {"weight": (3, 5), "height": (20, 26), "life_expectancy": (10, 15),
                       "coat_length": (1, 2), "grooming_needs": 0, "energy_level": (7, 9),
                       "intelligence_level": (6, 8), "playfulness": (7, 9),
                       "vocalization": (5, 7), "adaptability": (8, 10)},
        "Khao Manee": {"weight": (3, 5), "height": (20, 26), "life_expectancy": (12, 16),
                       "coat_length": (1, 2), "grooming_needs": 1, "energy_level": (6, 8),
                       "intelligence_level": (6, 8), "playfulness": (7, 9),
                       "vocalization": (3, 5), "adaptability": (8, 10)}
    }

    total_samples = 1000
    num_samples = {breed: random.randint(1, total_samples // len(breeds_characteristics)) for breed in
                   breeds_characteristics.keys()}
    remainder = total_samples - sum(num_samples.values())

    breed_to_add_to = list(num_samples.keys())[0]
    num_samples[breed_to_add_to] += remainder

    df = pd.DataFrame(columns=["Name", "Breed", "Weight", "Height", "Life Expectancy",
                               "Coat Length", "Grooming Needs", "Energy Level",
                               "Intelligence Level", "Playfulness", "Vocalization", "Adaptability"])

    for breed, characteristics in breeds_characteristics.items():
        for _ in range(num_samples[breed]):
            name = random.choice(cat_names)
            weight = round(random.uniform(*characteristics["weight"]), 1)
            height = random.randint(*characteristics["height"])
            life_expectancy = random.randint(*characteristics["life_expectancy"])
            coat_length = random.randint(*characteristics["coat_length"])
            grooming_needs = characteristics["grooming_needs"]
            energy_level = random.randint(*characteristics["energy_level"])
            intelligence_level = random.randint(*characteristics["intelligence_level"])
            playfulness = random.randint(*characteristics["playfulness"])
            vocalization = random.randint(*characteristics["vocalization"])
            adaptability = random.randint(*characteristics["adaptability"])

            df = pd.concat([df, pd.DataFrame({"Name": [name], "Breed": [breed], "Weight": [weight], "Height": [height],
                                              "Life Expectancy": [life_expectancy], "Coat Length": [coat_length],
                                              "Grooming Needs": [grooming_needs], "Energy Level": [energy_level],
                                              "Intelligence Level": [intelligence_level], "Playfulness": [playfulness],
                                              "Vocalization": [vocalization], "Adaptability": [adaptability]})],
                           ignore_index=True)

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df_shuffled = df.sample(frac=1).reset_index(drop=True)
        df_shuffled.to_csv(file_path, index=False)
        print("Dataset saved to:", file_path)


root = tk.Tk()
root.title("Generate Cats Dataset")

# Применяем стили из темы darkly
style = Style(theme="darkly")

generate_button = ttk.Button(root, text="Generate Dataset", command=generate_dataset)
generate_button.pack(pady=10)

save_button = ttk.Button(root, text="Save Dataset As", command=generate_dataset)
save_button.pack(pady=10)

root.mainloop()
