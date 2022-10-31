from flask import flash, redirect, render_template, request, Blueprint, abort
from players import db
from players.api.models import Player, Team
from players.api.forms import PlayerForm, EditPlayerForm

player = Blueprint('player', __name__)


@player.route('/')
@player.route('/home')
def home():
    players = Player.query.all()
    print(players)
    return render_template('home.html', players = players)


@player.route('/add_players', methods = ['POST','GET'])
def add_players():
    form = PlayerForm()
    if request.method == 'GET':
        return render_template('add_player.html',form=form)
    if request.method == 'POST':
        if form.validate_on_submit:
            player = Player(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                city = form.city.data, 
                state =  form.state.data
                )
            db.session.add(player)
            db.session.commit()
            return redirect('/home')
        else:
            return render_template('add_player.html',form=form)

    
@player.route('/players')
def players():
    players = Player.query.all()
    print(players)
    return render_template('players.html', players = players)

@player.route('/teams')
def teams():
    
    teams = Team.query.all()
    print(teams)
    return render_template('teams.html', teams=teams)

    
@player.route('/edit_players/<int:id>', methods=['GET', 'POST'])
def edit_players(id):
    form = EditPlayerForm()
    player = Player.query.filter_by(id =id).first()
    if request.method == 'POST':
        player.first_name = form.first_name.data
        player.last_name = form.last_name.data
        player.city = form.city.data
        player.state = form.state.data
        db.session.commit()
        return redirect('/players')
    return render_template('edit_player.html',form=form, player = player)


@player.route('/delete_player/<int:id>', methods=['GET','POST'])
def delete_player(id):
    player = Player.query.filter_by(id =id).first()
    if request.method == 'POST':
        if player:
            db.session.delete(player)
            db.session.commit()
            return redirect('/players')
        abort(404)
 
    return render_template('delete_player.html')
