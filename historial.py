# historial_tramites = {}

historial_tramites = {}

def registrar_tramite(ciudadano, tramite):
    
    if ciudadano not in historial_tramites:
        historial_tramites[ciudadano] = [] 
    historial_tramites[ciudadano].append(tramite)
    print(f"Trámite '{tramite}' registrado para {ciudadano}.")

def ver_historial(ciudadano):

    if ciudadano in historial_tramites and historial_tramites[ciudadano]:
        print(f"Historial de trámites de {ciudadano}:")
        for tramite in reversed(historial_tramites[ciudadano]):
            print(f"- {tramite}")
    else:
        print(f"No hay historial de trámites para {ciudadano}.")
