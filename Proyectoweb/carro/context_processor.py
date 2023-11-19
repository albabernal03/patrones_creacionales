# En tu context_processor.py modificado
def importe_total_carro(request):
    carro = request.session.get("carro", {})  # Usa get() para evitar KeyError
    total = sum(item['precio_total'] for item in carro.values())
    return {'importe_total_carro': total}
