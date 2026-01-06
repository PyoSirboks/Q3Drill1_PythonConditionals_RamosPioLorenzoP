from pyscript import document

def compute_average(event):
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)

    average = (score1 + score2) / 2

    if average >= 75:
        result = "👍"
    else:
        result = "👎"

    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result