#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from Datamanager.models import *

companies = {} 
for company in Company.objects.all():
    companies[company.pk] = {"name": company.name, "services": set()}

for concept in Concept.objects.all():
    if concept.company:
        if concept.category in ["CONSOLE", "ACCESSORY"]:
            companies[concept.company.pk]["services"].add(1)
        elif concept.category in ["APPLICATION", "DEMO", "GAME", "OS"]:
            companies[concept.company.pk]["services"].add(2)
        else:
            print("unhandled concept: {}, categeory {}, company {}".format(concept, concept.category, concept.company))

#for brand in [platform.brand for platform in Platform.objects.all()]:
for platform in Platform.objects.all():
    companies[platform.brand.pk]["services"].add(1)

for console in Console.objects.all():
    companies[console.constructor.pk]["services"].add(1)

for game in Game.objects.all():
    companies[game.publisher.pk]["services"].add(3)

for app in Application.objects.all():
    if app.publisher:
        companies[app.publisher.pk]["services"].add(3)

with open("import_companies.py", "w") as f :
    for key, company in companies.iteritems():
        line = "company = Company.objects.create(name=\"{}\")\n".format(company["name"])
        f.write(line)
        if company["services"]:
            lines = ["company.services.add({})\n".format(service) for service in company["services"]]
            f.write("".join(lines))
