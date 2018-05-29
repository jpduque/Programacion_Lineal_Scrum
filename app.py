from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from transaction import connection
from optimization import opt
import optimization


class app:
    seniorDevCost = ''
    techDevCost = ''
    juniorDevCost = ''
    internDevCost = ''
    seniorQACost = ''
    techQACost = ''
    juniorQACost = ''
    internQACost = ''
    seniorDevDeliver = ''
    techDevDeliver = ''
    juniorDevDeliver = ''
    internDevDeliver = ''
    seniorQADeliver = ''
    techQADeliver = ''
    juniorQADeliver = ''
    internQADeliver = ''
    sprintPoints = ''
    projectPoints = ''
    projectBudget = ''

    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/')
    def hello_world():
        # connection.queryData(2)

        # return 'Hello World!'
        return render_template('Home.html', data=connection.queryFullData())

    # Routing dev team costs
    @app.route('/DevTeamCost')
    def dev_team_build_up():
        return render_template('TeamCostDev.html')

    @app.route('/DevTeamCost', methods=['POST'])
    def dev_team_build_up_post():
        global seniorDevCost
        global techDevCost
        global juniorDevCost
        global internDevCost
        seniorDevCost = request.form['Dsenior']
        techDevCost = request.form['Dstandard']
        juniorDevCost = request.form['Djunior']
        internDevCost = request.form['Dintern']
        return redirect(url_for('qa_team_build_up'))

    # Routing qa team costs
    @app.route('/QATeamCost')
    def qa_team_build_up():
        return render_template('TeamCostQA.html')

    @app.route('/QATeamCost', methods=['POST'])
    def qa_team_build_up_post():
        global seniorQACost
        global techQACost
        global juniorQACost
        global internQACost
        seniorQACost = request.form['Qsenior']
        techQACost = request.form['Qstandard']
        juniorQACost = request.form['Qjunior']
        internQACost = request.form['Qintern']
        return redirect(url_for('dev_points_build_up'))

    # Routing dev team deliverable
    @app.route('/SprintPointsDev')
    def dev_points_build_up():
        return render_template('SprintPointsDev.html')

    @app.route('/SprintPointsDev', methods=['POST'])
    def dev_points_build_up_post():
        global seniorDevDeliver
        global techDevDeliver
        global juniorDevDeliver
        global internDevDeliver
        seniorDevDeliver = request.form['PDsenior']
        techDevDeliver = request.form['PDstandard']
        juniorDevDeliver = request.form['PDjunior']
        internDevDeliver = request.form['PDintern']
        return redirect(url_for('qa_points_build_up'))

    # Routing qa team deliverable
    @app.route('/SprintPointsQA')
    def qa_points_build_up():
        return render_template('SprintPointsQA.html')

    @app.route('/SprintPointsQA', methods=['POST'])
    def qa_points_build_up_post():
        global seniorQADeliver
        global techQADeliver
        global juniorQADeliver
        global internQADeliver
        seniorQADeliver = request.form['PQsenior']
        techQADeliver = request.form['PQstandard']
        juniorQADeliver = request.form['PQjunior']
        internQADeliver = request.form['PQintern']
        return redirect(url_for('project_points'))

    # Routing project deliverables
    @app.route('/ProjectPoints')
    def project_points():
        return render_template('ProjectPoints.html')

    @app.route('/ProjectPoints', methods=['POST'])
    def project_points_post():
        global sprintPoints
        global projectPoints
        global projectBudget
        sprintPoints = request.form['PSprint']
        projectPoints = request.form['PProject']
        projectBudget = request.form['ProjectBudget']
        return redirect(url_for('project_optimal'))

    # Routing Optimization
    @app.route('/OptimalProject')
    def project_optimal():
        opt.model(seniorDevCost, techDevCost, juniorDevCost, internDevCost, seniorQACost, techQACost, juniorQACost,
                  internQACost, seniorDevDeliver, techDevDeliver, juniorDevDeliver, internDevDeliver,
                  seniorQADeliver, techQADeliver, juniorQADeliver, internQADeliver, sprintPoints, projectPoints,
                  projectBudget)

        if optimization.lp1.status == 'optimal':

            connection.createData(seniorDevCost, techDevCost, juniorDevCost, internDevCost, seniorQACost, techQACost,
                                  juniorQACost
                                  , internQACost, seniorDevDeliver, techDevDeliver, juniorDevDeliver, internDevDeliver,
                                  seniorQADeliver
                                  , techQADeliver, juniorQADeliver, internQADeliver, round(optimization.x1.value[0]),
                                  round(optimization.x2.value[0]),
                                  round(optimization.x3.value[0]), round(optimization.x4.value[0]),
                                  round(optimization.x5.value[0]), round(optimization.x6.value[0]),
                                  round(optimization.x7.value[0]), round(optimization.x8.value[0])
                                  , projectPoints
                                  , sprintPoints)

            return render_template('Optimal.html', seniorDevCost=seniorDevCost, techDevCost=techDevCost,
                                   juniorDevCost=juniorDevCost, internDevCost=internDevCost, seniorQACost=seniorQACost,
                                   techQACost=techQACost, juniorQACost=juniorQACost, internQACost=internQACost,
                                   seniorDevDeliver=seniorDevDeliver, techDevDeliver=techDevDeliver,
                                   juniorDevDeliver=juniorDevDeliver, internDevDeliver=internDevDeliver,
                                   seniorQADeliver=seniorQADeliver, techQADeliver=techQADeliver,
                                   juniorQADeliver=juniorQADeliver, internQADeliver=internQADeliver,
                                   x1=round(optimization.x1.value[0]), x2=round(optimization.x2.value[0]),
                                   x3=round(optimization.x3.value[0]), x4=round(optimization.x4.value[0]),
                                   x5=round(optimization.x5.value[0]), x6=round(optimization.x6.value[0]),
                                   x7=round(optimization.x7.value[0]), x8=round(optimization.x8.value[0]),
                                   sprints=round(int(projectPoints) / int(sprintPoints)))

        return redirect(url_for('error'))

    @app.route('/OptimalHistoryProject/<id>')
    def project_optimal_history(id):
        connection.queryData(id)


        return render_template('Optimal.html', seniorDevCost=seniorDevCost, techDevCost=techDevCost,
                               juniorDevCost=juniorDevCost, internDevCost=internDevCost, seniorQACost=seniorQACost,
                               techQACost=techQACost, juniorQACost=juniorQACost, internQACost=internQACost,
                               seniorDevDeliver=seniorDevDeliver, techDevDeliver=techDevDeliver,
                               juniorDevDeliver=juniorDevDeliver, internDevDeliver=internDevDeliver,
                               seniorQADeliver=seniorQADeliver, techQADeliver=techQADeliver,
                               juniorQADeliver=juniorQADeliver, internQADeliver=internQADeliver,
                               x1=optimization.x1, x2=optimization.x2,
                               x3=optimization.x3, x4=optimization.x4,
                               x5=optimization.x5, x6=optimization.x6,
                               x7=optimization.x7, x8=optimization.x8,
                               sprints=round(int(projectPoints) / int(sprintPoints)))


    # Routing project deliverables
    @app.route('/Error')
    def error():
        return render_template('UnOptimal.html')
