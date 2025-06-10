from graphviz import Digraph

er = Digraph('ER', filename='er_diagram', format='png')
er.attr(rankdir='LR', size='10')

entities = {
    "Client": ["telegram_id (PK)", "full_name", "phone"],
    "Service": ["title", "description", "price", "duration"],
    "Appointment": ["id (PK)", "client_id (FK)", "service_id (FK)", "date_time", "status", "comment"],
    "ActionLog": ["id (PK)", "user_id (FK)", "action", "model", "timestamp", "description"],
    "User": ["id (PK)", "username", "password", "role"]
}

for entity, attributes in entities.items():
    label = f"{{{entity}|{'|'.join(attributes)}}}"
    er.node(entity, label=label, shape='record')

relationships = [
    ("Appointment", "Client", "client_id"),
    ("Appointment", "Service", "service_id"),
    ("ActionLog", "User", "user_id")
]

for src, dst, label in relationships:
    er.edge(src, dst, label=label)

er.render('er_diagram', cleanup=False)