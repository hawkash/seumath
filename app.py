from cmath import exp
from flask import Flask, render_template,url_for,request
from sympy import symbols, solve, Eq, solve_linear_system
from fractions import Fraction


app = Flask(__name__)

#question 1
def printer_question(black_price,color_price,total_cartridges_sold,total_cost):
    x = symbols('x')
    color_cartridge_sold = x
    black_cartridge_sold = total_cartridges_sold-x
    exper = Eq(color_price*x+black_price*black_cartridge_sold,total_cost)
    color_cartridge_sold = int(solve(exper)[0])
    black_cartridge_sold = total_cartridges_sold - color_cartridge_sold
    return {
        "black":black_cartridge_sold,
        "color":color_cartridge_sold
    }


#question 2
def convert_to_mixed_numeral(num):
    num = Fraction(str(num)) 
    n, d = (num.numerator, num.denominator)
    m, p = divmod(abs(n), d)
    if n < 0:
        m = -m
    return '{} {}/{}'.format(m, p, d) if m != 0 and p > 0 \
        else '{}'.format(m) if m != 0 \
        else '{}/{}'.format(n, d)

def polish_question(oil_amount_to_vinegar,furniture_polish):
    x,y = symbols('x y')
    amount_of_oil = Eq(y,oil_amount_to_vinegar*x)
    amount_of_vinegar = Eq(x+y,furniture_polish)
    ans = solve((amount_of_oil, amount_of_vinegar), (x, y))
    ans_x = float(ans[x])
    ans_y = float(ans[y])
    ans_x = convert_to_mixed_numeral(ans_x)
    ans_y = convert_to_mixed_numeral(ans_y)
    return {
        "vinegar":ans_x,
        "oil":ans_y
    }

def return_number(text_number):
    if text_number.lower().strip() == "one":
        return 1
    elif text_number.lower().strip() == "two":
        return 2
    elif text_number.lower().strip() == "three":
        return 3
    elif text_number.lower().strip() == "four":
        return 4
    elif text_number.lower().strip() == "five":
        return 5
    elif text_number.lower().strip() == "six":
        return 6
    elif text_number.lower().strip() == "seven":
        return 7
    elif text_number.lower().strip() == "eight":
        return 8
    elif text_number.lower().strip() == "nine":
        return 9
    elif text_number.lower().strip() == "ten":
        return 10

    

#quesiton 3
def soybean_question(soybean1,cornmeal1,total_mixture_lb,total_mixture_percent1):
    soybean = float(soybean1/100)
    cornmeal = float(cornmeal1/100)
    total_mixture_percent = float(total_mixture_percent1/100) 
    x,y = symbols('x y')
    amount1 = Eq(x+y,total_mixture_lb)
    amount2 = Eq(soybean*x+cornmeal*y,total_mixture_percent*(x+y))
    ans = solve((amount1, amount2), (x, y))
    ans_x = int(ans[x])
    ans_y = int(ans[y])
    return {
        "cornmeal":ans_y,
        "soybean":ans_x
    }

#question 4
def investment_question(total_investment,first_part,second_part,total_yield):
    x = symbols('x')
    amount = Eq(first_part*(total_investment-x)+second_part*x,total_yield)
    ans = int(solve((amount),x)[0])
    return {
        f"{int(first_part*100)}%":total_investment-ans,
        f"{int(second_part*100)}%":ans
    }

#question 5
def triangle_question(measure_angleB,second_measure_angleB,measure_angleC):
    a = symbols('a')
    measure = Eq(a+(second_measure_angleB*a+measure_angleB)+(measure_angleC+a),180)
    angleA = int(solve((measure),a)[0])
    angleB = second_measure_angleB*angleA+measure_angleB
    angleC = measure_angleC+angleA
    return {
        "angle A":angleA,
        "angle B":angleB,
        "angle C":angleC
    }

#question 6
def car_question(basic_2WD_sunroof,fourWD_sunroof,basic_4WD):
    x,y,z = symbols('x y z')
    cost1 = Eq(x+z,basic_2WD_sunroof)
    cost2 = Eq(x+y+z,fourWD_sunroof)
    cost3 = Eq(x+y,basic_4WD)
    ans = solve((cost1, cost2, cost3), (x, y, z))
    return {
        "basic":ans[x],
        "4WD":ans[y],
        "sunroof":ans[z]
    }

#question 7
def business_question(total_investment,first_part_interest,second_part_interest,third_part_interest,total_interest,interest_of_first_second):
    x,y,z = symbols('x y z')
    amount1 = Eq(x+y+z,total_investment)
    amount2 = Eq(first_part_interest*x + second_part_interest*y + third_part_interest*z,total_interest)
    amount3 = Eq(first_part_interest*x,interest_of_first_second*(second_part_interest*y))
    ans = solve((amount1, amount2, amount3), (x, y, z))
    return {
        f"{int(first_part_interest*100)}%"  : int(ans[x]),
        f"{int(second_part_interest*100)}%" : int(ans[y]),
        f"{int(third_part_interest*100)}%"  : int(ans[z])
    }

#question 8
def pump_question(all_pumps,A_B_pumps,A_C_pumps):
    a,b,c = symbols('a b c')
    pump1 = Eq(a+b+c,all_pumps)
    pump2 = Eq(a+b,A_B_pumps)
    pump3 = Eq(a+c,A_C_pumps)
    ans = solve((pump1, pump2, pump3), (a, b, c))
    return {
        "A": int(ans[a]),
        "B": int(ans[b]),
        "C": int(ans[c])
    }

# question 9
def summation_question(sum_of_all,difference,sum_of_smallers):
    x,y,z = symbols('x y z')
    eq1 = Eq(x+y+z,sum_of_all)
    eq2 = Eq(x-z,difference)
    eq3 = Eq(y+z,sum_of_smallers)
    ans = solve((eq1, eq2, eq3), (x, y, z))
    return [
        int(ans[x]),
        int(ans[y]),
        int(ans[z])
    ]

# question 10
def drink_question(first_can,second_can,required_liters,required_percentage):
    x = symbols('x')
    eq1 = Eq(first_can*x + second_can*(required_liters-x),required_percentage*required_liters)
    ans = solve(eq1, x)[0]
    first_can_ans = int(ans)
    second_can_ans = required_liters - first_can_ans
    return {
        f"{int(first_can*100)}%": first_can_ans,
        f"{int(second_can*100)}%": second_can_ans
    }

#question 11
def train_question(first_train_speed,hour_late,second_train_speed):
    s = symbols('s')
    eq1 = Eq(s,second_train_speed*(s/first_train_speed-hour_late))
    ans = solve(eq1, s)[0]
    return f"{ans}"

#question 12
def donut_question(oz10,oz14,oz20,served_cups,used_coffee,total_of_all_cups):
    a,b,c = symbols('a b c')
    eq1 = Eq(a+b+c,served_cups)
    eq2 = Eq(10*a+14*b+20*c,used_coffee)
    eq3 = Eq(oz10*a+oz14*b+oz20*c,total_of_all_cups)
    ans = solve((eq1, eq2, eq3), (a,b,c))
    return {
        "10oz": int(ans[a]),
        "14oz": int(ans[b]),
        "20oz": int(ans[c])
    }




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/printer", methods=('GET', 'POST'))
def printer():
    if request.method == 'POST':
        black_price = float(request.form['black_price'])
        color_price = float(request.form['color_price'])
        total_cartridges_sold = int(request.form['total_cartridges_sold'])
        total_cost = float(request.form['total_cost'])   
        answer = printer_question(black_price,color_price,total_cartridges_sold,total_cost)
        return render_template("printer_question.html",answer=answer.items())

    answer = ""
    return render_template("printer_question.html",answer=answer)

@app.route("/polish", methods=('GET', 'POST'))
def polish():
    if request.method == 'POST':
        try:
            oil_amount_to_vinegar = int(request.form['oil_amount_to_vinegar'])
        except:
            oil_amount_to_vinegar = return_number(request.form['oil_amount_to_vinegar'])
            
        furniture_polish = int(request.form['furniture_polish'])  
        answer = polish_question(oil_amount_to_vinegar,furniture_polish)
        return render_template("polish_question.html",answer=answer.items())

    answer = ""
    return render_template("polish_question.html",answer=answer)

@app.route("/soybean", methods=('GET', 'POST'))
def soybean():
    if request.method == 'POST':
        soybean1 = int(request.form['soybean1'])
        cornmeal1 = int(request.form['cornmeal1'])
        total_mixture_lb = int(request.form['total_mixture_lb'])
        total_mixture_percent1 = int(request.form['total_mixture_percent1'])
        answer = soybean_question(soybean1,cornmeal1,total_mixture_lb,total_mixture_percent1)
        return render_template("soybean_question.html",answer=answer.items())

    answer = ""
    return render_template("soybean_question.html",answer=answer)

@app.route("/investment", methods=('GET', 'POST'))
def investment():
    if request.method == 'POST':
        total_investment = int(request.form['total_investment'])
        first_part = int(request.form['first_part'])/100
        second_part = int(request.form['second_part'])/100
        try:
            total_yield = int(request.form['total_yield'])
        except:
            total_yield = int(float(request.form['total_yield']))
        answer = investment_question(total_investment,first_part,second_part,total_yield)
        return render_template("investment_question.html",answer=answer.items())

    answer = ""
    return render_template("investment_question.html",answer=answer)

@app.route("/triangle", methods=('GET', 'POST'))
def triangle():
    if request.method == 'POST':
        measure_angleB = int(request.form['measure_angleB'])
        try:
            second_measure_angleB = int(request.form['second_measure_angleB'])
        except:
            second_measure_angleB = return_number(request.form['second_measure_angleB'])
        measure_angleC = int(request.form['measure_angleC'])
        answer = triangle_question(measure_angleB,second_measure_angleB,measure_angleC)
        return render_template("triangle_question.html",answer=answer.items())

    answer = ""
    return render_template("triangle_question.html",answer=answer)



@app.route("/car", methods=('GET', 'POST'))
def car():
    if request.method == 'POST':
        try:
            basic_2WD_sunroof = int(request.form['basic_2WD_sunroof'].replace(',',"").strip())
        except:
            basic_2WD_sunroof = int(request.form['basic_2WD_sunroof'].strip())
        try:
            fourWD_sunroof = int(request.form['fourWD_sunroof'].replace(",","").strip())
        except:
            fourWD_sunroof = int(request.form['fourWD_sunroof'].strip())
        try:
            basic_4WD = int(request.form['basic_4WD'].replace(",","").strip())
        except:
            basic_4WD = int(request.form['basic_4WD'].strip())
        answer = car_question(basic_2WD_sunroof,fourWD_sunroof,basic_4WD)
        return render_template("car_question.html",answer=answer.items())

    answer = ""
    return render_template("car_question.html",answer=answer)

@app.route("/business", methods=('GET', 'POST'))
def business():
    if request.method == 'POST':
        try:
            total_investment = int(request.form['total_investment'].replace(",","").strip())
        except:
            total_investment = int(request.form['total_investment'].strip())

        first_part_interest = int(request.form['first_part_interest'])/100
        second_part_interest = int(request.form['second_part_interest'])/100
        third_part_interest = int(request.form['third_part_interest'])/100
        total_interest = int(request.form['total_interest'])
        try:
            interest_of_first_second = int(request.form['interest_of_first_second'])
        except:
            interest_of_first_second = return_number(request.form['interest_of_first_second'])

        answer = business_question(total_investment,first_part_interest,second_part_interest,third_part_interest,total_interest,interest_of_first_second)
        return render_template("business_question.html",answer=answer.items())

    answer = ""
    return render_template("business_question.html",answer=answer)

@app.route("/pump", methods=('GET', 'POST'))
def pump():
    if request.method == 'POST':
        all_pumps = int(request.form['all_pumps'])
        A_B_pumps = int(request.form['A_B_pumps'])
        A_C_pumps = int(request.form['A_C_pumps'])
        answer = pump_question(all_pumps,A_B_pumps,A_C_pumps)
        return render_template("pump_question.html",answer=answer.items())

    answer = ""
    return render_template("pump_question.html",answer=answer)

@app.route("/summation", methods=('GET', 'POST'))
def summation():
    if request.method == 'POST':
        sum_of_all = int(request.form['sum_of_all'])
        difference = int(request.form['difference'])
        sum_of_smallers = int(request.form['sum_of_smallers'])
        answer = summation_question(sum_of_all,difference,sum_of_smallers)
        return render_template("summation_question.html",answer=answer)

    answer = ""
    return render_template("summation_question.html",answer=answer)


@app.route("/drink", methods=('GET', 'POST'))
def drink():
    if request.method == 'POST':
        first_can = int(request.form['first_can'])/100
        second_can = int(request.form['second_can'])/100
        required_liters = int(request.form['required_liters'])
        required_percentage = int(request.form['required_percentage'])/100
        answer = drink_question(first_can,second_can,required_liters,required_percentage)
        return render_template("drink_question.html",answer=answer.items())

    answer = ""
    return render_template("drink_question.html",answer=answer)



@app.route("/train", methods=('GET', 'POST'))
def train():
    if request.method == 'POST':
        first_train_speed = int(request.form['first_train_speed'])
        try:
            hour_late = int(request.form['hour_late'].strip())
        except:
            hour_late = return_number(request.form['hour_late'].strip())
        second_train_speed = int(request.form['second_train_speed'])
        answer = train_question(first_train_speed,hour_late,second_train_speed)
        return render_template("train_question.html",answer=answer)

    answer = ""
    return render_template("train_question.html",answer=answer)



@app.route("/donut", methods=('GET', 'POST'))
def donut():
    if request.method == 'POST':
        oz10 = float(request.form['oz10'])/100
        oz14 = float(request.form['oz14'])
        oz20 = float(request.form['oz20'])
        served_cups = int(request.form['served_cups'])
        used_coffee = int(request.form['used_coffee'])
        total_of_all_cups = float(request.form['total_of_all_cups'])
        answer = donut_question(oz10,oz14,oz20,served_cups,used_coffee,total_of_all_cups)
        return render_template("donut_question.html",answer=answer.items())

    answer = ""
    return render_template("donut_question.html",answer=answer)

