for i in range(1, 21):
    with open(f"tables 09_08/table of {i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i*j} \n")
