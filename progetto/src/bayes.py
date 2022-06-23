from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController

# Costruizione Rete Bayesiana Percentuale Assunzione

#panico
panic = BbnNode(Variable(0, 'panic', ['si', 'no']), [0.60, 0.4])
#prendersela con se stessi
blamingYourself = BbnNode(Variable(1, 'blamingYourself', ['si', 'no']), [0.55, 0.45])

#sintoni medi
mediumSymptom = BbnNode(Variable(2, 'mediumSymptom', ['si', 'no']), [0.85, 0.15, 0.8, 0.2, 0.4, 0.6, 0.25, 0.75])

#nessuna speranza
hopelessness = BbnNode(Variable(3, 'hopelessness', ['si', 'no']), [0.70, 0.3])
#pensieri suicidi
suicidalThought = BbnNode(Variable(4, 'suicidalThought', ['si', 'no']), [0.8, 0.2])

#sintoni gravi
hardSymptom = BbnNode(Variable(5, 'hardSymptom', ['si', 'no']), [0.9, 0.1, 0.6, 0.4, 0.85, 0.15, 0.20, 0.80])

#predizione
prediction = BbnNode(Variable(6, 'prediction', ['si', 'no']), [0.99, 0.01, 0.55, 0.45, 0.9, 0.1, 0.05, 0.95])

bbn = Bbn() \
    .add_node(panic) \
    .add_node(hopelessness) \
    .add_node(blamingYourself) \
    .add_node(suicidalThought) \
    .add_node(mediumSymptom) \
    .add_node(hardSymptom) \
    .add_node(prediction) \
    .add_edge(Edge(panic, mediumSymptom, EdgeType.DIRECTED)) \
    .add_edge(Edge(blamingYourself, mediumSymptom, EdgeType.DIRECTED)) \
    .add_edge(Edge(hopelessness, hardSymptom, EdgeType.DIRECTED)) \
    .add_edge(Edge(suicidalThought, hardSymptom, EdgeType.DIRECTED)) \
    .add_edge(Edge(mediumSymptom, prediction, EdgeType.DIRECTED)) \
    .add_edge(Edge(hardSymptom, prediction, EdgeType.DIRECTED))

# Conversione da bbn ad albero
treeCopy = InferenceController.apply(bbn)

#Setta il valore scelto in base alla risposta data
def insertDefinedValue(tree, nodeName, optionName, value):
    ev = EvidenceBuilder() \
        .with_node(tree.get_bbn_node_by_name(nodeName)) \
        .with_evidence(optionName, value) \
        .build()
    tree.set_observation(ev)

#predizione: domande da fare all'utente
def prediction():
    tree = treeCopy.__copy__()

    while True:
        value = input(
            "Hai mai attacchi di panico?\n"
            "Risposte possibili: (si) (no) (info)\n").lower()
        if value in ["si" ,"no"]:
            insertDefinedValue(tree, "panic", value, 1.0)
            break
        elif value in ["info"]:
            info(0)

    while True:
        value = input(
            "Te la prendi mai con te stesso anche per fatti insignificanti?\n"
            "Risposte possibili: (si) (no) (info)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "blamingYourself", value, 1.0)
            break
        elif value in ["info"]:
            info(1)

    while True:
        value = input(
            "Pensi mai che non ci sia speranza per il mondo o per le cose in cui vorresti credere?\n"
            "Risposte possibili: (si) (no) (info)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "hopelessness", value, 1.0)
            break
        elif value in ["info"]:
            info(2)

    while True:
        value = input(
            "Ti è mai capitato di pensare al suicidio?\n"
            "Risposte possibili: (si) (no) (info)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "suicidalThought", value, 1.0)
            break
        elif value in ["info"]:
            info(3)


    print("Analisi delle tue risposte...")
    outputPrediction(tree)


#stampa la probabilità di essere assunti e,in base alla probabilità, stampa un messaggio/consiglio
def outputPrediction(tree):
    for node, posteriors in tree.get_posteriors().items():
        if node == 'prediction':
            max, min = posteriors.items()
            #print(f'[{node} : {max[1]*100:.0f}%]') visualizza la percentuale

            if max[1] < 0.39:
                print("Godi di una buona salute mentale!\n"
                      "Anche se potrebbe risultare non necessario, ti è consigliata una visita da un professionista, anche per prova. Potresti giovarne!\n")
            elif max[1] < 0.59:
                print("Potresti soffrire di sintomi di lieve-media entità che potrebbero causare problemi alla tua salute psicofisica.\n"
                      "Anche se non potrebbe risultare non necessario, ti è consigliata una visita da un professionista, anche per prova. Potresti giovarne!\n")
            elif max[1] < 0.79:
                print("Potresti soffrire di sintomi medio gravi legati alla tua salute mentale che potrebbero causarti malattie come: solitudine, stress o depressione.\n"
                      "E' consigliata una visita da uno professionista. \n")
            else:
                print("Potresti soffrire di sintomi gravi legati alla tua salute mentale che potrebbero causarti malattie come: solitudine, stress o depressione.\n"
                      "E' consigliata vivamente una visita da uno professionista. \n")


def info(number):
    if number == 0:
        print("L'attacco di panico è un evento caratterizzato da un'ansia molto intensa, tachicardia, fiato corto e paura di morire o di impazzire."
              "\nPuò presentarsi in qualsiasi momento e spesso è associato a periodi di forte stress e stanchezza. Se credi di esserti mai sentito cosi rispondi 'si' alla domanda, digita no altrimenti.\n")
    elif number == 1:
        print("I soggetti che tendono ad essere severi con se stessi non vogliono trasgressioni rispetto ai loro programmi e alle loro aspettative. "
              "\nDi solito sono quelle persone che restano irremovibili nei loro punti di vista e che non considerano nemmeno possibile che si possa agire o pensare diversamente. Se credi di esserti mai sentito cosi rispondi 'si' alla domanda, digita no altrimenti.\n")
    elif number == 2:
        print("Essere senza speranza significa restare apatici ed indifferenti davanti ad ogni cosa con la convinzione che nulla potrà mai andare diversamente. Se credi di esserti mai sentito cosi rispondi 'si' alla domanda, digita no altrimenti.\n")
    elif number == 3:
        print("I pensieri suicidi sono pensieri che esprimono il desiderio di morire, in persone depresse o con crisi di disperazione, senso di colpa, senso di impotenza rispetto a situazioni che le sopraffanno. Se credi di esserti mai sentito cosi rispondi 'si' alla domanda, digita no altrimenti.\n")



