def importe_total_carro(request):
    total = 0

    if request.user.is_authenticated:
        carro = request.session.get("carro", {})

        for key, value in carro.items():
            precio = float(value.get("precio", 0))
            cantidad = int(value.get("cantidad", 0))
            subtotal = precio * cantidad

            # Apply a 5% discount if the subtotal is greater than 40 euros
            if subtotal > 40:
                descuento = subtotal * 0.05
                subtotal -= descuento

            total += subtotal

    else:
        total = 'Debe iniciar sesión'

    return {"importe_total_carro": total}