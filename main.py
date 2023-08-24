import pandas as pd
import matplotlib.pyplot as plt

COLORS = {
    "I": "#FFFF00",
    "II": "#DEEBF7",
    "III": "#A9CE91",
    "IV": "#FFF2CC",
    "V": "#F4B183",
    "VI": "#E7E6E6",
}

if __name__ == "__main__":
    df = pd.read_csv("data.csv", sep="\t")
    data = sorted(
        sum([[{"value": x, "string": y} for x in df[y]] for y in df.columns], []),
        key=lambda x: x["value"],
    )

    x = range(len(data))
    y = [x["value"] for x in data]
    c = [COLORS[x["string"]] for x in data]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y, c=c, edgecolors="black")
    fig.savefig("harmonics.pdf")
