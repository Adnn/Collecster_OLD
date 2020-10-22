from concept_specifics_table import concept_specifics_table

specific_code_template = "specific = {specific_class}.objects.create({related_field}={related_instance}, **{fields})"

specifics_fields = {
    "ConceptSpecific.Remote": {"battery_type": None, },
    "ConceptSpecific.RemoteAccessory": {"wireless": False, },
}

def specific_code(specific_classname):
    return specific_code_template.format(specific_class=specific_classname, related_field="concept",
                                         related_instance="concept", fields=specifics_fields[specific_classname])

def concept_specifics_code_for(nature):
    code = [] 
    for specific_classname in concept_specifics_table[nature]:
        code.append(specific_code(specific_classname))
    return "\n".join(code)

