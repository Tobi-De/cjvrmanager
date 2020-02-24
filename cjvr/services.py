from .models import Testimony, Plaintiff, Victim


def plaintiff_create(p_form):
    plaintiff = Plaintiff.objects.create(first_name=p_form.cleaned_data['first_name'],
                                         last_name=p_form.cleaned_data['last_name'],
                                         age=p_form.cleaned_data['age'],
                                         sex=p_form.cleaned_data['sex'],
                                         religion=p_form.cleaned_data['religion'],
                                         address=p_form.cleaned_data['address'],
                                         aggressions=p_form.cleaned_data['contact'])
    return plaintiff


def victim_create(v_form):
    victim = Victim.objects.create(first_name=v_form.cleaned_data['first_name'],
                                   last_name=v_form.cleaned_data['last_name'],
                                   age=v_form.cleaned_data['age'],
                                   sex=v_form.cleaned_data['sex'],
                                   religion=v_form.cleaned_data['religion'],
                                   address=v_form.cleaned_data['address'],
                                   aggression_place=v_form.cleaned_data['aggression_place'],
                                   status=v_form.cleaned_data['status'],
                                   aggressions=v_form.cleaned_data['aggressions'])
    return victim


def testimony_create(plaintiff, victim, description):
    return Testimony.objects.create(victim=victim, plaintiff=plaintiff, description=description)
