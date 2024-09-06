from django.shortcuts import render, HttpResponse
# Create your views here.
mathOperations = {
    "+" : lambda n1, n2: n1 + n2,
    "-" : lambda n1, n2: n1 - n2,
    "*" : lambda n1, n2: n1 * n2,
    "/" : lambda n1, n2: n1 / n2,
    "^" : lambda n1, n2: pow(n1, n2)
}

def viewInput(request):
    selectMathOperation = request.GET.get("operation", "")
    fullResult = ""
    operation = request.GET.get("operation", "")

    try:
        num1 = float(request.GET.get("num1", 0))
        num2 = float(request.GET.get("num2", 0))
    except:
        return HttpResponse("<h1>Ошибка: Вы некорректно ввели не число</")

    calc = mathOperations.get(selectMathOperation, "")
    print(calc)
    
    if calc != "":
        if operation == "/" and num2 == 0:
            return HttpResponse("<h1>Ошибка деления на ноль</")
        fullResult = f"{num1} {selectMathOperation} {num2} = {calc(num1, num2)}"

    context = {
        "action" : fullResult,
    }

    return render(request, "input.html", context)