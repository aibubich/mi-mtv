from familia.models import Familiar

Familiar(nombre="Agustina", direccion="Olazabal 6012", numero_pasaporte=356248967,fecha_nacimiento="1990-3-9").save()
Familiar(nombre="Rafael", direccion="Olazabal 6012", numero_pasaporte=28314967,fecha_nacimiento="1980-2-26").save()
Familiar(nombre="Delfina", direccion="Olazabal 6012", numero_pasaporte=57203369,fecha_nacimiento="2018-5-27").save()
Familiar(nombre="Santiago", direccion="Olazabal 6012", numero_pasaporte=58142367, fecha_nacimiento="2021-6-6").save()

print("Se cargo con éxito los usuarios de pruebas")
