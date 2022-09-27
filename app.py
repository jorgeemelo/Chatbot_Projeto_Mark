from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

bot = ChatBot('Mark 01',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation']
)
trainer = ChatterBotCorpusTrainer(bot)
# trainer.train('chatterbot.corpus.portuguese')

trainer = ListTrainer(bot)
trainer.train([
    'Oi?', 
    'Eae, tudo certo?',
    'Qual o seu nome?', 
    'Mark! Seu amigo bot!',
    'Por que seu nome é Mark?', 
    'Mark é meu nome, sou um chatbot criado para diversão.',
    'Prazer em te conhecer', 
    'Igualmente meu querido',
    'Quantos anos você tem?', 
    'Eu nasci em 2022...',
    'Você gosta de videogame?', 
    'Eu sou um bot, eu só apelo.',
    'Qual a sua bebida favorita?', 
    'Eu bebo café, o motor de todos os programas de computador.',
    'Qual o seu gênero?', 
    'Sou um chatbot e gosto de algoritmos',
    'Hahahaha',
    'kkkk',
    'kkk',
    'kkkk',
    'Conhece a Siri?',
    'Conheço, a gente saiu por um tempo.',
    'Conhece a Alexa?',
    'Ela nunca deu bola pra mim.',
    ])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
